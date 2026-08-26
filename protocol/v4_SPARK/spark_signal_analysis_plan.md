# Signal-Detection Analysis Plan — SPARK Parent Survey v1

Pre-specify before the first invitation. Implemented in `spark_signal_analysis.py`, which runs unchanged on the Airtable export (same field names/codes) and on the SPARK export.

## 1. Analysis populations
- **R** (regression path): `change_type` ∈ {1, 2}.
- **R-sudden**: `change_type` = 1 (primary).
- **C** (comparison): `change_type` ∈ {3, 4}; interval items are relative to first concern.
- **Confirmatory subgroup**: R-sudden ∧ "A vaccine" *not* checked in `attribution` ∧ `date_evidence` includes at least one non-memory source ∧ `vax_confidence` ≤ "within 2 days".

## 2. Primary signal: lag-histogram excess at Day 0–2
Among R-sudden with a numeric `vax_interval` (codes 3–14, i.e. vaccinated within 120 days):

- Convert bins to per-day rates: single-day bins (codes 3–9 → days 0…6), then 8–13 (6 d), 14–29 (16 d), 30–59 (30 d), 60–90 (31 d).
- **Null (schedule-only):** onset is unrelated to vaccination timing, so within the 0–90 day window the per-day density is smooth in lag. Empirical null = per-day rate over days 7–90 (bins 7 through 60–90). This is the SORA v2 "flat-lag" null; it is conservative relative to a decreasing-hazard null because well-visit spacing makes short lags slightly *less* likely than mid lags for any given onset age.
- **Statistic:** observed count in days 0–2 (codes 3–5) vs expected = 3 × (per-day rate, days 7–90). Report RR, exact Poisson 95% CI, one-sided p.
- **Secondary contrast:** Day 0–2 vs Day 90–92 is not available at this resolution; use Day 0–2 vs Day 3–6 (per-day) as the near-field contrast, and Day 0–6 vs Day 7–29.
- **Decision rule (signal present):** RR ≥ 2 with lower CI > 1 in the confirmatory subgroup, *and* no comparable excess in the `visit_novax_interval` histogram (see §4).

## 3. Day-of-week test
`onset_dow` among R-sudden with a specific day (codes 2–8). Under the null, days are uniform (or, if parents date onset to memorable days, skewed toward weekends). If onset follows vaccinating visits by 0–2 days, onset should be depleted on Sunday/Monday and enriched Tue–Sat. Chi-square vs uniform; also report the weekday/weekend split including codes 9–10. Repeat within the Day 0–2 group only: those should be almost entirely weekdays.

## 4. Controls
1. **Non-vaccinating visit histogram:** same Day 0–2 excess statistic on `visit_novax_interval`. Visit-prompted noticing predicts an excess here too; a vaccine effect predicts it only in `vax_interval`. Report ratio of the two RRs with bootstrap CI.
2. **`before3` contrasts:** P(vaccination) vs P(visit-without-shots) vs P(fever) vs P(new Rx) in the 3 days before onset, R-sudden vs C. Each exposure's R:C odds ratio; vaccination should stand out from the other visit-linked exposures if the biological account is right.
3. **Comparison arm histogram:** `vax_interval_c` gives the Day 0–2 fraction for parents dating *first concern* without a sudden change. This is the empirical reconstruction/anchoring baseline.

## 5. Pre-specified subgroups (report all; none confirmatory)
attribution (vaccine checked / not) × date evidence (artifact / memory-only) × confidence (≤2 days / worse) × documentation (≥80% / less) × `hypothesis_exposure` (before onset / after or never) × `how_long_ago` (≤2 y / >2 y) × `change_type` (1 / 2) × age at onset (<12, 12–17, 18–23, ≥24 mo) × sex.

Predictions written in advance:
- **Biological:** Day 0–2 RR similar across attribution and evidence cells; present in confirmatory subgroup; absent for non-vaccinating visits; weekday-enriched.
- **Artifactual:** RR concentrated in vaccine-attributing, memory-only, hypothesis-before-onset cells; comparable RR for non-vaccinating visits; C-arm shows similar Day 0–2 fraction.

## 6. Narrative coding (`sequence`)
Blind coding of the (0)-anchored narrative: events mentioned and day offsets. Extract the parent-stated vaccination→first-change day offset where present and compare with `vax_interval` (internal consistency; discrepancies flagged, not corrected). Spontaneous-mention rate of vaccination in R vs C narratives.

## 7. Drift
`age_onset_months` − SPARK enrollment age-at-loss, regressed on years since enrollment, attribution, and `hypothesis_exposure`.

## 8. Power (planning)
If the true Day 0–2 per-day rate equals the days 7–90 rate, with N=300 vaccinated-within-120-day sudden-regression cases, expected Day 0–2 count ≈ 10; RR=2 is detectable at 80% power with ~250 such cases; RR=3 with ~100. Aim for ≥300 in R-sudden with a numeric interval, which at ~60% "vaccinated within 120 days" and ~50% sudden means ~1,000 R completes plus ~500 C completes.

## 9. Multiplicity
One primary test (§2 confirmatory subgroup). Everything else descriptive with CIs; no p-value thresholding on subgroups.
