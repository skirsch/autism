# Onset-age histogram and CDC age reference

Input: 322 rows in the 2026-08-30 21:20:47 Downloads export. SHA-256 `9959a5c4ec61b6647036e6cba27475861ae867a6c457abc9b3e02002eb7646b6`.

The histogram uses the PARENT onset-age field, not diagnosis age, with one-month bins and zero-count bins retained. All countries and vaccination groups are included in the main plot. There are 321 plotted ages: 312 at 0–60 months and nine at 72–215 months. Record #84 is excluded because 2,212 months is implausible; no correction is imputed and source data are unchanged.

## Observed correspondence

- The three highest monthly counts are 18 months (47), 15 months (31), and 12 months (24).
- The CDC reference recommends first MMR/varicella doses and Hib/PCV boosters at 12–15 months, and a DTaP booster at 15–18 months. Thus the largest peaks overlap these recommended age ranges.
- The correspondence is partial, not a complete reproduction of the schedule. Counts at infant DTaP ages 2, 4, and 6 months are 10, 8, and 9; the adjacent 3-month count is 14. The 24-month peak (20) is not a fixed routine DTaP/MMR dose age in this reference.
- Restricting to USA respondents with affirmative pre-onset vaccination evidence (n=208 valid ages) retains the three leading peaks: 18 months (33), 15 months (22), and 12 months (17).
- NEVER has only seven valid ages: 0, 5, 24, 24, 26, 33, and 48 months. This cannot establish a contrasting population age distribution.

Reference: [CDC childhood schedule notes dated July 2, 2025](https://www.cdc.gov/vaccines/hcp/imz-schedules/child-adolescent-notes.html). The figure shows selected routine doses, not the whole schedule. Hib infant doses vary by product. The reference is illustrative, not matched to each child's historical era or country. Current USA residence does not establish where childhood vaccination occurred.

## Interpretation

There is descriptive age overlap, particularly at 12, 15, and 18 months. No statistical test of schedule alignment or causal effect was performed. A recommended age range is not an observed exposure distribution, and a uniform distribution of onset ages is not an established no-effect expectation. Developmental timing and rounding to familiar ages can also produce peaks. Actual vaccination dates, age-precision information, and a prespecified comparison preserving the background age distribution are needed to distinguish child-specific synchronization from shared age structure.

The analysis is conditional on reported values; independent documentary verification was not performed.
