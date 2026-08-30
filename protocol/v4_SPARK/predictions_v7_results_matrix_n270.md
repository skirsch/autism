# V7 paired results matrix — n=270 assumed-verification exercise

**Data:** `C:\Users\stk\Downloads\SOA2-Grid view.csv`, 270 rows, SHA-256 `42F732E2D6DB49BA1DBC393AE20EE2FFEBA2E8A187FDE80311696824D5CBD681`.  
**Exercise assumption:** Treat retained survey values as verified and correct. This does not assert that real-world verification has occurred.

For VAX/NEVER supporting tests, VAX is identified from any affirmative pre-onset vaccination evidence in the schedule question, `What happened?`, or `3 days before onset`; NEVER is the verified schedule answer. This yields VAX=185, NEVER=3, and unknown=82, with no VAX/NEVER contradictions in this export.

| Test | H-null | H-vax | Reason |
|---|:---:|:---:|---|
| **P1. VAX-specific 2020 dip** | **Indeterminate** | **Indeterminate** | A large descriptive dip is present: all dated cases are 2019=5, 2020=1, 2021=10; VAX dated cases are 5, 1, and 5. But only 2 NEVER cases have dates, neither in 2019–2021, so the required VAX-minus-NEVER interaction cannot be estimated. Within VAX alone, 1 of the 11 cases across 2019–2021 occurred in 2020 (one-sided equal-year p=0.075); pooled, 1 of 16 gives p=0.0137. |
| **P2. Weekday/weekend difference** | **Indeterminate** | **Indeterminate** | VAX has 71 weekday and 12 weekend responses (85.5%; exact p=0.00336 versus 5/7), but NEVER has only 1 classifiable response. The required between-group difference cannot be established. |
| **P3. Named-day distribution difference** | **Indeterminate** | **Indeterminate** | VAX named-day n=30 is compatible with uniformity (chi-square p=0.731), but NEVER has only 1 named day and the vaccination-calendar model is not frozen. |
| **P4. Modal onset-age alignment** | **Indeterminate** | **Indeterminate** | VAX has a unique mode at 18 months (n=30), a prespecified vaccination age. NEVER n=3 has three tied ages (0, 26, 48), below v7's minimum and without a stable mode. |
| **P5. Peak-width difference** | **Indeterminate** | **Indeterminate** | The VAX peak is extremely sharp: the minimum adjacent-month ratio is 0.10, far below 0.80. NEVER n=3 has no stable peak, so the required width difference cannot be scored. |
| **P6. Peak-asymmetry difference** | **Indeterminate** | **Indeterminate** | VAX asymmetry is 0.495, above the draft 0.20 threshold. NEVER n=3 has no stable mode, so the required asymmetry difference cannot be scored. |
| **P7. Verified 0–5-day lag excess** | **No** | **Yes** | SHOT-VISIT E=36, R=8, per-day RR=40.5, exact 95% CI 18.5–100.9, one-sided p=7.82×10⁻²⁹. This satisfies the mutually exclusive H-vax region. |

## Overall

| H-null | H-vax | V7 conclusion under the exercise assumption |
|:---:|:---:|---|
| **No** | **Yes** | P7 is the primary statistical decision test and falls decisively in the H-vax region. P1, P2, P4, P5, and P6 show descriptive patterns in the H-vax-predicted direction, but they cannot enter the formal vaccine region because the NEVER comparison is too small. P3 is uninformative. |

Every row follows the paired v7 rule: Yes/No, No/Yes, or Indeterminate/Indeterminate.

## Bottom line

Under the assumed-verification exercise, v7 gives the overall paired result **H-null=No / H-vax=Yes**, driven by P7. The 2020 dip is plainly visible and should be reported, but it is supporting descriptive evidence rather than a formally resolved P1 result because the NEVER comparator is absent.
