"""Signal-detection analysis for the SPARK / Airtable parent survey.

Usage:  python spark_signal_analysis.py export.csv
        python spark_signal_analysis.py --synthetic [--rr 3.0] [--n 1500]

Expects REDCap-style export columns (checkbox fields exported as name___k = 0/1)
with the codes from spark_survey_redcap_dictionary.csv.
"""
import sys, argparse
import numpy as np, pandas as pd
from scipy import stats

# vax_interval code -> (lag_start_day, n_days)
BINS = {3:(0,1),4:(1,1),5:(2,1),6:(3,1),7:(4,1),8:(5,1),9:(6,1),10:(7,6),11:(13,16),12:(29,30),13:(59,32)}
EARLY = [3,4,5]                       # days 0-2
REF   = [9,10,11,12,13]               # days 6-90 (per-day reference)  -- day 6 included to keep bins whole
REF_DAYS = sum(BINS[c][1] for c in REF)

def cb(df, field, k):
    col = f"{field}___{k}"
    return df[col].fillna(0).astype(int).eq(1) if col in df else pd.Series(False, index=df.index)

def day02_excess(codes):
    """RR of days 0-2 vs per-day rate over days 6-90, exact Poisson CI."""
    codes = pd.Series(codes).dropna().astype(int)
    obs = codes.isin(EARLY).sum()
    ref = codes.isin(REF).sum()
    n_vac = codes.between(3, 14).sum()
    exp = 3 * ref / REF_DAYS if ref else np.nan
    rr = obs / exp if exp else np.nan
    lo, hi = (stats.chi2.ppf(0.025, 2*obs)/2, stats.chi2.ppf(0.975, 2*(obs+1))/2) if exp else (np.nan, np.nan)
    p = stats.poisson.sf(obs-1, exp) if exp else np.nan
    return dict(n_vaccinated_120d=int(n_vac), obs_d02=int(obs), exp_d02=round(exp,2), RR=round(rr,2),
                CI=(round(lo/exp,2) if exp else None, round(hi/exp,2) if exp else None), p_one_sided=round(p,4))

def lag_hist(codes):
    codes = pd.Series(codes).dropna().astype(int)
    return {f"d{BINS[c][0]}-{BINS[c][0]+BINS[c][1]-1}": round(codes.eq(c).sum()/BINS[c][1], 2) for c in BINS}  # per-day rate

def dow_test(dow):
    d = pd.Series(dow).dropna().astype(int)
    days = d[d.between(2, 8)].value_counts().reindex(range(2, 9), fill_value=0)
    chi, p = stats.chisquare(days) if days.sum() else (np.nan, np.nan)
    wk = d.isin([2,3,4,5,6,9]).sum(); we = d.isin([7,8,10]).sum()
    return dict(counts=dict(zip("Mon Tue Wed Thu Fri Sat Sun".split(), days.tolist())), chi2=round(chi,2), p=round(p,4),
                weekday=int(wk), weekend=int(we), weekday_frac=round(wk/(wk+we),3) if wk+we else None)

def run(df):
    R = df[df.change_type.isin([1,2])].copy(); RS = R[R.change_type.eq(1)]
    C = df[df.change_type.isin([3,4])]
    conf = RS[~cb(RS,"attribution",5) & (sum(cb(RS,"date_evidence",k) for k in range(2,9)) > 0) & RS.vax_confidence.le(3)]
    out = {}
    out["primary_confirmatory_subgroup"] = day02_excess(conf.vax_interval)
    out["R_sudden_all"] = day02_excess(RS.vax_interval)
    out["R_all"] = day02_excess(R.vax_interval)
    out["control_nonvax_visit_R_sudden"] = day02_excess(RS.visit_novax_interval)
    out["comparison_arm_first_concern"] = day02_excess(C.vax_interval_c)
    out["lag_hist_per_day_R_sudden"] = lag_hist(RS.vax_interval)
    out["dow_R_sudden"] = dow_test(RS.onset_dow)
    out["dow_R_sudden_day02_only"] = dow_test(RS[RS.vax_interval.isin(EARLY)].onset_dow)
    # before3 exposure contrasts R-sudden vs C  (codes: 1 fever,4 visit no shots,5 visit shots,7 vaccination,10 new Rx)
    b3 = {}
    for k, name in {1:"fever",4:"visit_no_shots",5:"visit_with_shots",7:"vaccination",10:"new_rx"}.items():
        a, b = cb(RS,"before3",k).mean(), cb(C,"before3_c",k).mean()
        b3[name] = dict(R_sudden=round(a,3), C=round(b,3), OR=round((a/(1-a))/(b/(1-b)),2) if 0<b<1 and 0<a<1 else None)
    out["before3_contrasts"] = b3
    # subgroups
    sg = {}
    sg["vaccine_attributing"] = day02_excess(RS[cb(RS,"attribution",5)].vax_interval)
    sg["not_attributing"] = day02_excess(RS[~cb(RS,"attribution",5)].vax_interval)
    sg["memory_only"] = day02_excess(RS[cb(RS,"date_evidence",1) & (sum(cb(RS,"date_evidence",k) for k in range(2,9))==0)].vax_interval)
    sg["artifact_dated"] = day02_excess(RS[sum(cb(RS,"date_evidence",k) for k in range(2,9))>0].vax_interval)
    sg["hyp_before_onset"] = day02_excess(RS[RS.hypothesis_exposure.isin([1,2])].vax_interval)
    sg["hyp_after_or_never"] = day02_excess(RS[RS.hypothesis_exposure.isin([4,5])].vax_interval)
    sg["doc_80plus"] = day02_excess(RS[RS.documentation.le(2)].vax_interval)
    sg["recent_le2y"] = day02_excess(RS[RS.how_long_ago.le(4)].vax_interval)
    for lo_, hi_, nm in [(0,11,"age_lt12"),(12,17,"age_12_17"),(18,23,"age_18_23"),(24,99,"age_ge24")]:
        sg[nm] = day02_excess(RS[RS.age_onset_months.between(lo_,hi_)].vax_interval)
    out["subgroups"] = sg
    return out

def synthetic(n=1500, rr=3.0, seed=1):
    """Null-plus-signal generator for testing the pipeline: vaccinating visits every ~90 days, flat onset, Day 0-2 boosted by rr."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(index=range(n))
    df["change_type"] = rng.choice([1,2,3,4], n, p=[.4,.2,.3,.1])
    df["sex"] = rng.choice([1,2], n, p=[.8,.2])
    df["age_onset_months"] = rng.integers(9, 30, n)
    df["how_long_ago"] = rng.integers(1, 7, n)
    df["hypothesis_exposure"] = rng.integers(1, 7, n)
    df["documentation"] = rng.integers(1, 6, n)
    df["vax_confidence"] = rng.integers(1, 7, n)
    for k in range(1, 11): df[f"attribution___{k}"] = rng.random(n) < (0.25 if k == 5 else 0.2)
    for k in range(1, 9):  df[f"date_evidence___{k}"] = rng.random(n) < 0.3
    for k in range(1, 17): df[f"before3___{k}"] = rng.random(n) < 0.08; df[f"before3_c___{k}"] = rng.random(n) < 0.06
    def lags(m, boost):
        p_early = 3 * boost / (3 * boost + 88)             # flat per-day null, days 0-2 boosted by `boost`
        early = rng.random(m) < p_early
        lag = np.where(early, rng.integers(0, 3, m), rng.integers(3, 91, m))
        code = np.select([lag<=6, lag<=13, lag<=29, lag<=59, lag<=90], [lag+3, 10, 11, 12, 13], 14)
        code = np.where(rng.random(m) < 0.35, rng.choice([1,2,14], m), code)
        return code
    df["vax_interval"] = lags(n, rr); df["vax_interval_c"] = lags(n, 1.0)
    df["visit_novax_interval"] = lags(n, 1.0)
    dow = rng.integers(2, 9, n); df["onset_dow"] = np.where(rng.random(n) < .4, 1, dow)
    df.loc[df.change_type.ge(3), ["vax_interval","visit_novax_interval","onset_dow"]] = np.nan
    df.loc[df.change_type.le(2), "vax_interval_c"] = np.nan
    return df

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("csv", nargs="?"); ap.add_argument("--synthetic", action="store_true")
    ap.add_argument("--rr", type=float, default=3.0); ap.add_argument("--n", type=int, default=1500)
    a = ap.parse_args()
    df = synthetic(a.n, a.rr) if a.synthetic or not a.csv else pd.read_csv(a.csv)
    import json; print(json.dumps(run(df), indent=1, default=str))
