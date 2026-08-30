# Pre-specified Predictions — SOA Survey v2.3 (version 1 archive)

**Archived:** 2026-08-30. This is the first explicitly versioned snapshot of `prespecified_predictions.md`, including its disclosed post-n=270 P11 amendment. It is preserved for auditability and is not to be silently edited.

**Purpose.** Written before the comparative data exist, so that every outcome has an agreed meaning in advance. Three hypotheses are in play and each row states what each predicts. A result matching one column and not the others is evidence for that column; a result all three columns predict carries no weight for any of them.

- **H-null** — onset timing is unrelated to vaccination, and reports are accurate (random onset, perfect recall).
- **H-vax** — vaccination causes the large majority (working figure: ≥80%) of sudden-onset regressions, concentrated at short lags (with a possible delayed window for live-virus vaccines). Not the sole cause: infections (strep, C. diff, encephalitides) and other insults supply the remainder, in vaccinated and never-vaccinated children alike.
- **H-artifact** — no causal effect; reported clustering is produced by memory anchoring to remembered visits plus recruitment through hypothesis-aware channels.

Exposure groups: **VAX** = vaccinated per schedule question; **NEVER** = "No vaccines were ever given"; **SHOT-VISIT** = last well visit included vaccination (type question authoritative); **NOSHOT-VISIT** = last well visit certain-none.

| # | Metric | H-null predicts | H-vax predicts | H-artifact predicts |
|---|--------|-----------------|----------------|---------------------|
| P1 | Onset-year distribution, VAX vs NEVER | Same shape | 2020 dip and 2021 rebound in VAX only; NEVER flat through the pandemic | Same shape in both, incl. a shared 2020 dip (fewer visits = fewer anchors) tracking well-visit volume |
| P2 | Day-of-week distribution (named days), VAX vs NEVER | Uniform in both | VAX weekday-shifted with Sun/Mon depletion; NEVER uniform or weekend-leaning | Same weekday shift in both groups (anchoring to weekday visits is exposure-blind) |
| P3 | Lag histogram, days 0–5 vs days 6–60 after last well visit | Days 0–5 ≈ 6/55 ≈ 11% of days 6–60 count (day 0 partial) | Days 0–5 strongly in excess at SHOT-VISITs | Days 0–5 in excess at both SHOT- and NOSHOT-VISITs |
| P4 | **Lag curve at NOSHOT-VISITs vs SHOT-VISITs** (key test) | Both flat | Early cliff at SHOT-VISITs only; NOSHOT flat | Same early cliff in both |
| P5 | Same-day onsets, BEFORE vs AFTER the doctor was seen | After ≈ 2–3× before (waking hours; visits mostly before noon) | After ≫ before at SHOT-VISITs; at NOSHOT-VISITs, ratio matches the null baseline | Same before/after ratio at SHOT- and NOSHOT-VISITs |
| P6 | Lag shape, MMR-containing vs MMR-free shot visits | Same | MMR-containing shifted later (day 5–12 window, live-virus replication); MMRV strongest in record-verified subset | Identical (memory doesn't know virology). Caution: MMR over-reporting expected among vaccine-attributing parents; weight the non-attributing and record-verified subsets |
| P7 | Age-at-onset distribution | Single peak, right-skewed (developmental floor ~12 mo; long upper tail) — same in VAX and NEVER | Peak sharpened around vaccinating-visit ages (12/15/18 mo) in VAX; NEVER broader/flatter | Same VAX sharpening (visits anchor ages too); NEVER group small and story-poor |
| P8 | Day 0–2 fraction by attribution (vaccine named in Cause? vs not) | Equal (no clustering in either) | Roughly equal across attribution (biology doesn't care what the parent believes) | Concentrated in the vaccine-attributing group |
| P9 | Record-verified interval vs reported interval (validation subset) | Match | Match (accurate recall of a real event) | Reported intervals shorter than documented; errors drift toward the shot |
| P10 | Digit pattern within week 1 (days 4/5/6/7) | Smooth | Smooth decline per risk window | Heaping on 5 and 7, troughs at 4 and 6 (already observed at n=230) |
| P11 | Fraction of sudden-onset cases in NEVER children | ≈ never-vaccinated share of the respondent population | ≈ 20% of that share (5-fold per-capita suppression: if ≥80% of cases are vaccine-caused and non-vaccine triggers hit both groups equally, NEVER children generate cases at ~1/5 the vaccinated rate). Not zero — infection-caused cases occur in NEVER children and their narratives should name infections, not visits | ≈ full population share; these parents simply lack a shot to anchor to, so more "don't remember" dates. Caution for all columns: interpretable only where the never-vaccinated share of the *invited* population is known (neutral channels); vaccine-aware channels over-sample never-vaccinating families by an unknown factor |
| P12 | Discordance rate (visit checklist Vaccination(s) vs type question) | Low, random | Low, random | Low, random — reported as a data-quality metric either way; sensitivity analyses on concordant subset |

## Decision rules (committed in advance)

1. **Primary:** P4 in a sample of ≥100 NOSHOT-VISIT cases. If the NOSHOT early-cliff (days 0–2 per-day rate ÷ days 6–60 per-day rate) is within a factor of 2 of the SHOT-VISIT cliff → anchoring accounts for the clustering; the timing evidence for H-vax fails. If the SHOT-VISIT cliff exceeds the NOSHOT cliff by ≥3× with a CI excluding 1 → the excess belongs to the injection, not the visit; H-artifact fails as a full explanation.
2. **Secondary:** P2 (day-of-week by exposure), P6 (MMR shift), P9 (verification). Each interpreted per its row; none overrides the primary alone, but concordant secondaries strengthen whichever verdict the primary gives.
3. P1, P3, P5, P7, P8, P10, P11 are reported descriptively against their three columns; no single row is treated as dispositive.
4. Known confounds stated now: deferral suppresses same-day-BEFORE counts at SHOT-VISITs (P5 asymmetry is expected under all hypotheses; only the SHOT/NOSHOT comparison of ratios is interpreted); the visit calendar mechanically thins lags >60 days (P3 reference window ends at 60 for this reason); recall interval correlates with onset era (P6/P7 era splits are descriptive only).
5. These predictions apply to each recruitment channel separately and to the pooled data; a result that holds in vaccine-aware channels but vanishes in neutral channels (clinic, TACA post-2020, SPARK) is attributed to recruitment, per the channel-gradient design.

*Both parties to any dispute over this survey's results are invited to add predictions to this table before the comparative cells fill in. Neither may add or reinterpret after.*

## Amendment log

- **2026-08-30 (P11, H-vax column and hypothesis statement).** Original column read "Near zero," which encoded vaccines-as-sole-cause — a strawman neither party holds. Replaced with the quantified ≥80%-of-cases version (NEVER share ≈ 20% of population share) at Steve's correction. Amended when the NEVER cell held n=3; recorded here so the change and its timing are auditable. The denominator caveat (never-vax share of the invited population unmeasured in vaccine-aware channels) was added at the same time and cuts against every column equally.
