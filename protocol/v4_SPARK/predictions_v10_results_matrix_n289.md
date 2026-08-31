# V10 application — 289 responses, 2026-08-30

## Input and assumptions

- Source: `C:\Users\stk\Downloads\SOA2-Grid view.csv`, modified 2026-08-30 at 13:10:55 local time.
- SHA-256: `c3d8c507dbd3bc1dbffd3ec796a4907f3b06e268306b581eb7ccc6eacf40e01b`.
- 289 rows with 289 unique record numbers; 19 additional rows numbered 319–337 beyond the prior 270-row export.
- Continue the user's exercise assumption that provided values are correct and verified. Actual record verification is not established by an answer about willingness or ability to produce documents.
- VAX: affirmative pre-onset schedule answer, vaccination at last visit, or vaccination in the three days before onset. NEVER: explicit no-vaccines-ever schedule answer. Unknown is not converted to NEVER or a no-vaccine visit. No contradictory VAX/NEVER classifications detected.
- Cohorts: VAX=204; NEVER=3; unknown=82. The VAX count includes all 19 additional records.
- P7 vaccination-visit eligibility uses only `What happened?` containing `Vaccination(s)`, not the onset-relative three-day vaccination question.
- Existing v10 thresholds are unchanged. Bootstrap, simultaneous multinomial, and directional procedures that remain unspecified are not silently invented for this analysis. No Monte Carlo or bootstrap run was performed.

## Completeness

All 19 additional records answer the schedule and last-visit-content questions. Seventeen name vaccination at that visit; two do not remember what happened. Seven supply an onset date; all supply an onset age. Only three add a classifiable weekday/weekend answer. Five state absolute confidence that records can be obtained; this is not documentary confirmation.

Across the entire export, 177 have onset dates, 80 have schedule answers, and 98 have last-visit-content answers. Of those last-visit answers, 79 name vaccination, 12 say they do not remember, and seven name other procedures without vaccination. Another 191 are blank. The two latter kinds of missing/unknown response must not be treated as confirmed no-vaccine visits.

## Table A — VAX (204 children)

| Test | V10 result | Evidence |
|---|:---:|---|
| P1 — 2020 dip | Indeterminate | Among 134 dated VAX cases, the 2019/2020/2021 counts are 5/2/5. The dip ratio is $Q_{2020}=0.40$, but the one-sided exact deficit test gives $p=0.1811$, failing the Vaccine criterion. The data do not establish the Null equivalence region either. |
| P2 — Weekday concentration | Vaccine | 74 weekday and 12 weekend responses: 86.0% weekday, versus $5/7=71.4\%$. One-sided exact $p=0.001119$; the point fraction exceeds the 80% threshold. |
| P3 — Named-day distribution | Indeterminate | Monday–Sunday counts are 5/3/6/3/7/5/2 ($n=31$). Descriptive chi-square $p=0.6158$; total-variation distance from uniformity is 0.1705. Neither the Vaccine significance criterion nor Null equivalence criterion is met. Sparse-cell chi-square is descriptive, not a substitute for the unfrozen simultaneous procedure. |
| P4 — Modal onset age | Indeterminate | Unique mode at 18 months, with 33 cases. The point pattern aligns with the Vaccine region, but the required mode-stability/bootstrap procedure remains unspecified. |
| P5 — Peak width | Indeterminate | Counts at 17/18/19 months are 5/33/4. $B=4/33=0.1212$, below 0.80; the required confidence-interval procedure remains unspecified. |
| P6 — Peak asymmetry | Indeterminate | $A=47/99=0.4747$, above 0.20. The required interval and directional procedure remain unspecified. |
| P7 — Vaccination-visit lag | Vaccine | $E=43$, $R=12$, early fraction 78.2%; $RR=(43/6)/(12/54)=32.25$. Exact 95% RR interval 16.71–67.18; one-sided exact $p=1.278\times10^{-32}$. All numerical Vaccine criteria are met. |

## Table B — NEVER (3 children)

| Test | V10 result | Evidence |
|---|:---:|---|
| P1 — 2020 dip | Indeterminate | Two dated cases, neither in 2019–2021; no usable three-year comparison. |
| P2 — Weekday concentration | Indeterminate | One weekday response and no weekend responses; exact interval spans 2.5%–100%. |
| P3 — Named-day distribution | Indeterminate | One named day, Tuesday. Insufficient data for the specified distribution test. |
| P4 — Modal onset age | Indeterminate | Ages 0, 26, and 48 months: a three-way tie rather than a stable mode. |
| P5 — Peak width | Indeterminate | No unique, stable mode. |
| P6 — Peak asymmetry | Indeterminate | No unique, stable mode. |
| P7 — No-vaccination-visit negative control | Indeterminate | Under the verified-NEVER assumption, $E=0$, $R=1$; the other two report no pre-onset pediatric visit. Exact 95% RR interval 0–351, which does not establish an upper limit below 2. One record has inconsistent visit-history answers that need verification; its reported no-prior-visit answer excludes it from the lag test. |

The separate apparent no-shot-visit cell is not the NEVER cohort. Seven rows name detailed visit procedures but omit vaccination; only three have usable P7 lags, all in the reference window. Omission from a checklist should be affirmed as no vaccination at that visit, rather than assumed to establish it. This sparse cell does not establish a null effect.

## Earlier records versus the additional batch: P7

| Batch | Vaccination-visit records | Eligible E/R total | Early E | Reference R | Early fraction | V10 lag RR | Exact 95% interval | One-sided p |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Earlier IDs through 318 | 62 | 44 | 36 | 8 | 81.8% | 40.50 | 18.51–100.86 | $7.816\times10^{-29}$ |
| Additional IDs 319–337 | 17 | 11 | 7 | 4 | 63.6% | 15.75 | 4.00–73.37 | $2.290\times10^{-5}$ |
| Combined | 79 | 55 | 43 | 12 | 78.2% | 32.25 | 16.71–67.18 | $1.278\times10^{-32}$ |

The new batch points in the same direction, with a smaller point estimate. It is a temporal batch sensitivity, not demonstrated independent or neutral recruitment. Six of the 17 new vaccination-visit records are outside the analysis: five unknown lags and one over 120 days.

The reported RR is v10's ratio of lag counts per assumed window-day, not an observed incidence ratio comparing vaccinated and unvaccinated children. Its exact p-value is conditional on the flat $p_0=0.10$ lag model. The exact two-sided binomial p-values equal the displayed one-sided values for these three observed counts. Confidence limits are Clopper–Pearson binomial limits transformed as $9p/(1-p)$.

## Assessment

VAX: two Vaccine results, zero Null results, five Indeterminate results. NEVER: seven Indeterminate results.

The additional records maintain a strong short-lag signal under the stipulated flat-lag model, but the predicted VAX/NEVER separation remains untested because NEVER has only three cases. Overall specificity is Indeterminate under v10's sparse-control rule. `Vaccine` is the name of a numerical decision region, not a conclusion that causation has been established.

The earlier v9 P1 result was calculated on pooled records; v10 requires VAX-only scoring. Pooled current counts are 5/2/10 ($p=0.04415$), but these must not be substituted into the VAX table. The previous VAX-only counts were 5/1/5 ($p\approx0.075$), already below the required evidence level for the Vaccine decision.
