# Prospective Predictions and Decision Rules — SOA Survey (version 2 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 exported responses.  
**Prospective confirmation cohort:** Airtable record number **319 and higher**. Records 46–318 form the exploratory n=270 cohort and must not be used to claim confirmation of predictions introduced or changed here.  
**Status:** Superseded draft. Preserved for the version history; its certain-NOSHOT primary design was rejected as infeasible before being frozen.

## Purpose and scope

The primary question is whether sudden-onset cases report an onset in the early post-visit window **more often after visits with vaccination than after comparable visits certain to have had no vaccination**.

This survey samples reported sudden-onset cases. Its internal SHOT/NOSHOT comparison can detect a vaccine-specific timing association within respondents. By itself, it cannot estimate population incidence, prove causation, or estimate what percentage of all sudden-onset autism is caused by vaccination, infection, or another exposure. Those stronger claims require known source-population denominators and protection against differential selection and recall.

## Mechanisms may coexist

These are not mutually exclusive explanations for every child:

- **M0 — no vaccine-specific timing association:** within eligible cases, the probability of an early reported onset is the same after SHOT and NOSHOT visits, after accounting for recruitment channel.
- **MV — vaccine-associated subgroup:** some eligible cases have an excess of early reported onset following a SHOT visit. This predicts an early-window excess in SHOT relative to NOSHOT; it does not predict that every case follows vaccination.
- **MI — infection-associated or other non-vaccine biological subgroup:** some cases follow prespecified non-vaccine acute exposures. The proposed approximate 10% share is a working hypothesis, not a result established by the current survey. It requires structured exposure definitions and an appropriate denominator before formal testing.
- **MA — measurement and selection mechanisms:** visit anchoring, digit heaping, exposure-aware recall, and recruitment selection can affect any of the groups above. Their presence does not automatically exclude a vaccine-associated component, and a vaccine association does not exclude their presence.

## Exposure and outcome definitions

### Exposure

- **SHOT:** the authoritative vaccine-type question says one or more vaccines were given at the last pediatrician visit before onset.
- **NOSHOT:** the authoritative vaccine-type question says, “None — I'm certain no vaccines were given at that visit.”
- **UNKNOWN:** “I don't remember whether,” missing, or internally unusable responses.
- **DISCORDANT:** the visit checklist and authoritative vaccine-type answer disagree. The vaccine-type answer remains authoritative, but discordant records are excluded from the primary analysis and included in sensitivity analysis.

Absence of `Vaccination(s)` from the older visit checklist is not sufficient to classify NOSHOT.

### Lag windows

- **Early post-visit window E:** onset on the same day **after** the doctor visit, or 1–5 days after the visit. This is six reported categories.
- **Reference window R:** onset 6–59 days after the visit. This window is exactly recoverable from the current response bins.
- **Same-day before visit:** a temporal negative-control category, reported separately and not counted in E because onset preceded anything administered at that visit.
- All other intervals, “don't remember,” and “never had a prior visit” are excluded from the primary E-versus-R comparison and reported in the flow table.

## Primary vaccine-specific test

Let:

- \(p_S = E_S/(E_S+R_S)\), the early fraction among eligible SHOT records;
- \(p_N = E_N/(E_N+R_N)\), the early fraction among eligible NOSHOT records;
- \(PD=p_S-p_N\), the difference in early proportions within this case sample;
- \(PR=p_S/p_N\), the ratio of early proportions, with an exact method used when a cell is zero.

The hypotheses are:

- **H0V:** \(p_S \le p_N\) — no vaccine-specific early excess.
- **H1V:** \(p_S > p_N\) — an early excess is present after SHOT visits.

The primary analysis uses a recruitment-channel-stratified comparison. Report the stratum-specific 2×2 tables and the pooled Mantel–Haenszel estimate. If sparse cells prevent the stratified test, use an exact SHOT-versus-NOSHOT 2×2 test and label it unadjusted.

**Statistical support for MV requires all of the following:**

1. the estimated direction is \(p_S>p_N\);
2. the prespecified two-sided test gives \(p<0.05\);
3. the 95% confidence interval for the SHOT/NOSHOT association excludes 1 (and the interval for PD excludes 0);
4. at least 100 eligible certain-NOSHOT and 100 eligible SHOT records are available; and
5. the direction is not confined to a single vaccine-aware recruitment channel.

No arbitrary threefold effect is required. Statistical significance and uncertainty determine whether a vaccine-specific deviation from the null is present; PD and PR show whether that deviation is small or large. A statistically significant but small difference must be described as small, not as proof of a large causal contribution.

### How extreme early clustering is interpreted

- **95% early in SHOT and 95% early in NOSHOT:** rejects a flat lag model but gives \(PD=0\) and \(PR=1\); it does **not** support a vaccine-specific effect.
- **95% early in SHOT and 10% early in NOSHOT:** strongly supports a vaccine-specific timing association if the eligibility, sample-size, channel, and uncertainty rules above are met.
- **95% early pooled, with too few valid NOSHOT records:** the vaccine-specific primary question is unanswered, regardless of how impressive the pooled clustering looks.
- **95% early in SHOT and 90% in NOSHOT:** may become statistically significant in a very large sample, but the five-percentage-point PD is small and must be reported as such.

The primary test concerns association. Causal language requires concordance in neutral recruitment channels and the validation analyses below.

## Secondary and diagnostic predictions

| # | Analysis | Prospective prediction and interpretation |
|---|---|---|
| S1 | Same-day BEFORE versus AFTER | A vaccine-associated effect cannot cause onset before the shot. Report BEFORE separately by SHOT/NOSHOT and audit contradictory narratives. AFTER enrichment is supportive only as part of the SHOT/NOSHOT contrast because visit timing and deferral can also produce asymmetry. |
| S2 | MMR-containing versus MMR-free SHOT visits | Exploratory until the form isolates the proposed day 5–12 window. Do not call the current 8–13 bin a confirmatory 5–12 test. A prospective form revision must be frozen before using this prediction. |
| S3 | Record validation | In a predefined validation subset, compare reported visit date, vaccination status, and onset date with contemporaneous records. Report direction and magnitude of errors separately for SHOT and NOSHOT. Differential shortening toward SHOT weakens causal interpretation. |
| S4 | Attribution | Freeze a blinded coding manual before coding post-318 Cause narratives. Compare the primary association among vaccine-attributing and non-attributing respondents. Persistence in the non-attributing group reduces, but does not eliminate, concern about attribution-driven recall. |
| S5 | Digit heaping | Report exact day 4/5/6/7 counts in the post-318 cohort. Because heaping was seen before v2, this is a replication/measurement diagnostic, not an original confirmatory prediction. |
| S6 | Recruitment channel | Report the primary 2×2 table in each adequately sized channel. Agreement in neutral channels strengthens interpretation; concentration in vaccine-aware channels indicates selection or differential recall may explain part or all of the pooled association. |
| S7 | VAX versus NEVER | Descriptive unless the vaccination distribution and response probabilities of the invited source population are known. Do not infer an etiologic fraction from the share of NEVER respondents in this outcome-selected survey. |
| S8 | Infection/other acute exposure | Exploratory until the survey collects a frozen structured exposure, evidence level, and lag window. Parent narrative alone may generate hypotheses but does not verify that an infection caused onset. |

## Missingness, exclusions, and sensitivity analyses

Before looking at outcomes in the confirmation cohort, publish a flow table containing every exclusion reason. Do not silently convert missing or unknown vaccine status to NOSHOT.

Primary exclusions are UNKNOWN exposure, invalid/unknown lag, same-day-before, lag outside E or R, and DISCORDANT exposure. Prespecified sensitivity analyses add discordant records using the authoritative type answer, restrict to high-confidence intervals, restrict to specialist-diagnosed autism, and restrict to record-verified exposure/intervals. Results that reverse across these analyses are reported as unstable.

## Multiplicity and reporting

The SHOT-versus-NOSHOT E-versus-R comparison is the single primary test at two-sided α=0.05. Secondary analyses are reported with effect sizes, 95% confidence intervals, exact denominators, and multiplicity-adjusted p-values where a family of related tests is performed. “No statistical support” is not evidence of no effect when intervals remain wide.

Always publish the four primary cell counts \(E_S, R_S, E_N, R_N\), missingness, PD, PR, the association estimate used by the stratified test, confidence intervals, and p-value. Report source-channel results even when they complicate the pooled conclusion.

## Version history

- **v1:** Original three-column H-null/H-vax/H-artifact table, later amended at n=270 to replace “near zero” NEVER cases with a ≥80% working hypothesis.
- **v2 draft:** Replaces mutually exclusive whole-sample stories with a vaccine-specific statistical contrast; defines exact exposure and lag windows; makes records 46–318 exploratory; and treats infection, recall, and recruitment as mechanisms that may coexist.
