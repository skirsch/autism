# V5 results matrix — latest n=270 raw export

**Export:** `C:\Users\stk\Downloads\SOA2-Grid view.csv`  
**SHA-256:** `42F732E2D6DB49BA1DBC393AE20EE2FFEBA2E8A187FDE80311696824D5CBD681`  
**Status:** Assumed-verification exercise. At the user's instruction, treat every retained survey value as verified and correct for purposes of scoring v5. This is a counterfactual analytic assumption, not a statement that actual verification has occurred.

## Scoring key

- **Yes:** the observed raw result matches the stated prediction.
- **No:** the observed raw result conflicts with the stated prediction.
- **Indeterminate:** the required comparison, sample size, verification, or operational definition is unavailable.

“Yes” means compatible with that model; it does not mean uniquely explained by that model. A row can be Yes for both columns when it does not discriminate.

## Compact 7×2 result matrix

| Test | H-null | H-vax |
|---|:---:|:---:|
| **P1. Onset year** | **Indeterminate** | **Indeterminate** |
| **P2. Weekday/weekend** | **No** | **Indeterminate** |
| **P3. Named day** | **Yes** | **Indeterminate** |
| **P4. One age peak** | **Yes** | **Yes** |
| **P5. Broad age peak** | **No** | **Yes** |
| **P6. Age symmetry** | **Indeterminate** | **Indeterminate** |
| **P7. Days 0–5 vs 6–59** | **No** | **Yes** |

The matrix contains three kinds of rows:

- **Discriminating:** P5 and P7 favor H-vax over H-null; P7 is the prespecified primary test.
- **Non-discriminating:** P4 is Yes for both models.
- **Unavailable or incompletely specified:** P1 and P6; P2–P3 do not yet have sufficiently precise H-vax predictions to score every H-vax cell.

## Matrix

| Test | Latest raw result | H-null | H-vax | Why / limitation |
|---|---|:---:|:---:|---|
| **P1. Onset-year shape; especially 2020** | All dated rows: 2020=1, 2021=10. Schedule-era VAX has 36 dated rows; NEVER has only 2 dated rows, in 2018 and 2025. | **Indeterminate** | **Indeterminate** | The required VAX-versus-NEVER shape comparison cannot be made with two dated NEVER cases. Raw yearly counts also lack birth-cohort and recruitment denominators. |
| **P2. Weekday/weekend = 5:2** | All classifiable answers: 92 weekday, 15 weekend; expected approximately 76.4 and 30.6 under 5:2; exact p=0.00055. Schedule-era VAX: 21 weekday, 1 weekend; NEVER: n=1. | **No** | **Indeterminate** | The pooled and VAX data show more weekday reports than 5:2. This is compatible with vaccination/visit timing, but v5 has no frozen vaccine-date-based weekday prediction, and NEVER is empty. |
| **P3. Seven named days uniform** | Named-day n=38: Mon 7, Tue 4, Wed 8, Thu 5, Fri 7, Sat 5, Sun 2; chi-square p=0.578. | **Yes** | **Indeterminate** | Named days do not significantly depart from uniformity. Only 6 schedule-era VAX and 1 NEVER record give a named day, so the exposure comparison is unavailable. |
| **P4. One modal onset month** | Pooled mode is uniquely 18 months, n=43. Schedule-era VAX mode is uniquely 15 months, n=12. NEVER ages are 0, 26, and 48 months. | **Yes** | **Yes** | A unique pooled peak is compatible with both models and therefore does not discriminate. Equality of VAX and NEVER shapes is indeterminate because NEVER n=3. |
| **P5. Broad peak: adjacent months no more than 20% below mode** | Around pooled mode 18: month 17 has 5 and month 19 has 6 versus 43 at the mode—drops of 88.4% and 86.0%. Around VAX mode 15: months 14 and 16 have 3 and 0 versus 12. | **No** | **Yes** | The observed peak is far sharper than the proposed broad-null criterion and occurs near scheduled-visit ages. That is compatible with H-vax but also with age rounding, visit-prompted recognition, or selection; it is not uniquely causal. |
| **P6. Symmetry around onset-age peak** | Immediate neighbors of pooled mode are similar (5 versus 6), but farther ages are visibly irregular and the symmetry span/statistic was never frozen. NEVER n=3. | **Indeterminate** | **Indeterminate** | V5 requires a numerical symmetry statistic, evaluated span, tie rule, and tolerance before this can be scored. |
| **P7. Vaccination-visit lag: days 0–5 versus 6–59** | `What happened?` includes `Vaccination(s)` in 62 rows. Eligible E=36, R=8, N=44; early=81.8%; per-day RR=40.5; exact 95% CI 18.5–100.9; p=7.82×10⁻²⁹. | **No** | **Yes** | Under the exercise's verified-and-correct assumption, this overwhelmingly rejects the 1:9 proportional-time null and exceeds v5's RR=2 threshold. |

## Overall score

| Level | H-null | H-vax | Interpretation |
|---|:---:|:---:|---|
| **Numerical evidence** | **No** | **Yes** | P7 is the primary and strongest row: RR=40.5 with an extremely small exact p-value. P2 and P5 also conflict with their simple null predictions, although they are not vaccine-specific by themselves. |
| **V5 determination under assumed verification** | **No** | **Yes** | Treating all retained responses as verified and correct, the primary result meets every numerical v5 H-vax criterion and strongly rejects H-null. |

## Bottom line under the exercise assumption

Under v5 and the instruction to assume all retained documents and survey values are verified and correct, the observed data are **much more consistent with H-vax than H-null**. The decisive result is P7: 36 early versus 8 reference-window events, compared with the null expectation of approximately 4.4 early and 39.6 reference events at N=44.

This conclusion concerns a vaccine-associated short-window trigger for the survey-defined sudden-onset phenotype. It is not, by itself, an estimate for all autism or the percentage of cases caused by vaccination.

## Important cross-check

Across all last wellness visits regardless of whether `What happened?` includes vaccination, E=125 and R=62, for a per-day RR of 18.15. Thus the raw data contain substantial general visit-relative clustering as well as the larger RR=40.5 in vaccination-visit rows. Verification and the prespecified age/recruitment checks are needed to determine how much of the vaccination-row excess remains after data confirmation.
