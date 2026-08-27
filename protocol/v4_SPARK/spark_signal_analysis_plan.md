# Signal-Detection Analysis Plan — SPARK Parent Survey v1

Pre-specify before the first invitation. Implemented in `spark_signal_analysis.py`, which runs unchanged on the Airtable export (same field names/codes) and on the SPARK export.

## 1. Analysis populations
- **R** (regression path): `change_type` ∈ {1, 2}.
- **R-sudden**: `change_type` = 1 (primary).
- **C** (comparison): `change_type` ∈ {3, 4}; interval items are relative to first concern.
- **Derived vaccination interval** `vax_interval` = `visit_interval` if `visit_shots` ≥ 1; = `vax_prior_interval` if `visit_shots` = 0; missing if `visit_shots` is "don't remember". Same for the comparison arm.
- **Confirmatory subgroup**: R-sudden ∧ "A vaccine" *not* checked in `attribution` ∧ `date_evidence` includes at least one non-memory source ∧ `visit_confidence` ≤ "within 2 days".

## 2. Primary signal: lag-histogram excess at Day 0–2
Among R-sudden with a numeric `vax_interval` (codes 3–15, i.e. vaccinated within 120 days):

- Convert bins to per-day rates: single-day bins (codes 3–9 → days 0…6), then 8–13 (6 d), 14–29 (16 d), 30–59 (30 d), 60–83 (24 d), 84–97 (14 d), 98–120 (23 d).
- **Null (schedule-only):** onset is unrelated to vaccination timing, so within the 0–90 day window the per-day density is smooth in lag. Empirical null = per-day rate over days 6–120. This is the SORA v2 "flat-lag" null; it is conservative relative to a decreasing-hazard null because well-visit spacing makes short lags slightly *less* likely than mid lags for any given onset age.
- **Statistic:** observed count in days 0–2 (codes 3–5) vs expected = 3 × (per-day rate, days 6–120). Report RR, exact Poisson 95% CI, one-sided p.
- **Mirror contrast (SORA v2 Day 90 logic):** an onset a few days *before* the next scheduled visit shows up as a lag of roughly 90 days from the prior visit. Under an age-driven null the spike at Day 0–2 should have a counterpart hump around Day 84–97; under a vaccine effect it should not. Report per-day Day 0–2 ÷ per-day Day 84–97 with bootstrap CI. Note the mirror is smeared (combined 12/15-month visits, skipped or late 18-month visits, catch-up doses), so it is a hump, not a spike; with immunization records the per-child permutation null from v2 replaces this bin comparison.
- Near-field contrasts: Day 0–2 vs Day 3–6 (per-day); Day 0–6 vs Day 7–29.
- **Dose–response (co-primary descriptive):** Day 0–2 fraction of `visit_interval` by `visit_shots` = 0, 1, 2, 3, 4, 5+. Cochran–Armitage trend test. Visit-anchoring predicts a flat row; a vaccine effect predicts a rising row.
- **Decision rule (signal present):** RR ≥ 2 with lower CI > 1 in the confirmatory subgroup, *and* no comparable Day 0–2 excess among `visit_shots` = 0 visits (see §4).

## 3. Day-of-week test
`onset_dow` among R-sudden with a specific day (codes 2–8). Under the null, days are uniform (or, if parents date onset to memorable days, skewed toward weekends). If onset follows vaccinating visits by 0–2 days, onset should be depleted on Sunday/Monday and enriched Tue–Sat. Chi-square vs uniform; also report the weekday/weekend split including codes 9–10. Repeat within the Day 0–2 group only: those should be almost entirely weekdays.

## 4. Controls
1. **No-shot visit histogram:** same Day 0–2 excess statistic on `visit_interval` restricted to `visit_shots` = 0. Visit-prompted noticing predicts an excess here too; a vaccine effect predicts it only when `visit_shots` ≥ 1. Report ratio of the two RRs with bootstrap CI.
2. **`before3` contrasts:** P(vaccination) vs P(visit-without-shots) vs P(fever) vs P(new Rx) in the 3 days before onset, R-sudden vs C. Each exposure's R:C odds ratio; vaccination should stand out from the other visit-linked exposures if the biological account is right.
3. **Comparison arm histogram:** the derived comparison-arm `vax_interval` gives the Day 0–2 fraction for parents dating *first concern* without a sudden change. This is the empirical reconstruction/anchoring baseline.

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
If the true Day 0–2 per-day rate equals the days 6–120 rate, with N=300 vaccinated-within-120-day sudden-regression cases, expected Day 0–2 count ≈ 10; RR=2 is detectable at 80% power with ~250 such cases; RR=3 with ~100. Aim for ≥300 in R-sudden with a numeric interval, which at ~60% "vaccinated within 120 days" and ~50% sudden means ~1,000 R completes plus ~500 C completes.

## 9. Multiplicity
One primary test (§2 confirmatory subgroup). Everything else descriptive with CIs; no p-value thresholding on subgroups.

---

## Addendum — mapping to the live Airtable form (v2, 2026-08-26)

The live form implements the design with these differences from the field list above; the analysis maps as follows.

| Concept | Airtable v2 field | Notes |
|---|---|---|
| Onset definition | in "How long ago did ONSET happen?" help text | persistent change; resolved reactions excluded |
| `visit_interval` | "How many days BEFORE onset was your child's most recent well-child visit?" | bins: <1, 2, 3, 4, 5, 6, 7, 8–13, 14–29, 30–59, 60–89, 90–120, >120, never |
| `visit_confidence` | "Confidence in pediatrician visit interval" | unchanged |
| `visit_shots` (yes/no only) | "What happened at the last pediatrician visit" → Vaccination(s) checked | **no injection count**; dose–response deferred to the record-verified follow-up subset |
| short-window vaccination exposure | "Within 3 days BEFORE onset" → Vaccination checked | primary Day 0–2 exposure indicator; catches non-well-visit shots |
| pediatrician concern at last visit | "Did the pediatrician have any health concerns…" (free text) | code: none / developmental concern / illness / shots deferred |
| attribution | "Cause?" (then vs now, with reasoning) | blind-coded: vaccine / illness / other / random-no idea |
| mirror bin | 90–120 | replaces 84–97; per-day rate over 31 days |

**Primary contrast (as collected):** Day 0–2 fraction of `visit_interval` among last-well-visits *with* vaccination vs *without*. Visit-anchoring predicts equal fractions; a vaccine effect predicts a higher fraction with shots.
**Secondary:** per-day Day 0–2 rate vs per-day 90–120 rate (mirror); day-of-week overall and split by 3-day vaccination box; all of the above by attribution code and by confidence/documentation.
**Not available from this form:** injection count; vaccination interval when the last well visit had no shots and the shot was >3 days before onset.
