# V10 update — 303 records

Source: `C:\Users\stk\Downloads\SOA2-Grid view.csv`, modified 2026-08-30 14:58:39 local time. SHA-256: `4d7288a6f591330cb26f73838768b4c45f0e20d8464ced54c5d96f7b025679a6`.

303 unique record numbers, through 351: 14 additional records numbered 338–351 since the previous export. Same survey columns; no new broad developmental-trajectory classification question appears. Continue the assumed-verification exercise, without interpreting missing or impossible values as verified.

Classification uses the same affirmative pre-onset vaccination evidence as the n=289 analysis: VAX=217, NEVER=4, unknown=82, with no conflicting VAX/NEVER evidence. Among the 14 additional records, 13 are VAX and one NEVER. Nine report vaccination at the last visit. All 14 answer the schedule question; 12 report specialist diagnoses and two report no formal diagnosis. These tables retain the existing survey-defined cohort, not a newly imposed diagnosed-only subset.

## Table A — VAX

| Test | V10 result | Observation |
|---|---|---|
| P1 — 2020 dip | Indeterminate | 2019/2020/2021 counts remain 5/2/5; $Q=0.40$, exact one-sided $p=0.1811$. |
| P2 — Weekday concentration | Vaccine | 79 weekday / 12 weekend; 86.8% weekday; exact one-sided $p=0.0004147$. |
| P3 — Named weekdays | Indeterminate | Monday–Sunday counts 5/3/6/4/9/5/2; descriptive chi-square $p=0.3848$. Unfrozen simultaneous/direction procedure is not replaced by this descriptive test. |
| P4 — Modal onset age | Indeterminate | Mode 18 months, 33 cases. Required mode-stability procedure remains unspecified. |
| P5 — Peak width | Indeterminate | Counts at 17/18/19 months: 5/33/4; $B=0.1212$. Required interval procedure remains unspecified. |
| P6 — Peak asymmetry | Indeterminate | $A=51/103=0.4951$. Required interval/direction procedures remain unspecified. |
| P7 — Vaccination-visit lag | Vaccine | $E=50$, $R=13$; 79.4% early; lag ratio $RR=34.62$, exact 95% interval 18.53–69.46; one-sided $p=2.738\times10^{-38}$. |

## Table B — NEVER

| Test | V10 result | Observation |
|---|---|---|
| P1 — 2020 dip | Indeterminate | No onset dates in 2019–2021. |
| P2 — Weekday concentration | Indeterminate | Only one classifiable weekday/weekend response. |
| P3 — Named weekdays | Indeterminate | Only one named day, Tuesday. |
| P4 — Modal onset age | Indeterminate | Four tied onset ages: 0, 5, 26, and 48 months. |
| P5 — Peak width | Indeterminate | No unique, stable mode. |
| P6 — Peak asymmetry | Indeterminate | No unique, stable mode. |
| P7 — No-vaccination-visit control | Indeterminate | Still $E=0$, $R=1$. Two report no prior visit; the new NEVER record has an unknown lag. No precise Null result. |

## Timing update and data checks

- Vaccination-at-visit rows: 88. P7-eligible: 63; other/unknown/outside-window: 25.
- New batch alone: seven early, one reference, one other among nine vaccination-visit rows. $RR=63.0$, exact 95% interval 8.09–2839.35, one-sided $p=7.30\times10^{-7}$. The interval is very wide because the reference count is one; the batch is descriptive rather than a new confirmatory trial.
- Record #350 has onset date `8/10/0000`. Excluded only from calendar-year calculations; no year imputed, source unchanged. Of 181 nonblank onset dates, 180 parse as valid calendar dates.
- Record #349 reports same-day AFTER onset, selected developmental checks but not vaccination at the visit, and vaccination in the prior three days. VAX classification is supported, but the visit exposure requires clarification. It is not included in vaccination-visit P7 and is not treated as confirmed no vaccination. Other recent vaccination could have occurred elsewhere; do not assume the checklist omission resolves this.
- The new NEVER record #347 reports no vaccines ever, other procedures at the last visit, age five months, and unknown lag; it supplies no new P7 timing evidence.
- Blank/unknown last-visit contents remain unknown. Nine records select other procedures without vaccination; omission is not an affirmative no-shot confirmation.

Overall: VAX has two Vaccine-region results and five Indeterminate results; NEVER has seven Indeterminate results. The timing signal remains under the stipulated flat 10% null, but cross-group specificity is still indeterminate. `Vaccine` is a model-region label, not a demonstrated causal conclusion. No Monte Carlo, bootstrap, threshold revision, or source-data edit was performed.
