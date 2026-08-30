# Exploratory application of v5 to the n=270 raw export

**Run date:** 2026-08-30  
**Export:** `C:\Users\stk\Downloads\SOA2-Grid view.csv`  
**Rows:** 270  
**SHA-256:** `42F732E2D6DB49BA1DBC393AE20EE2FFEBA2E8A187FDE80311696824D5CBD681`  
**Status:** Exploratory only. This export has not undergone the v5 verification readback.

## Does v5 require Monte Carlo here?

No. V5 makes the exact binomial test authoritative. Its Monte Carlo randomization draws the same flat 0–59-day null and is only a reproducibility/code check. It is not required to calculate or interpret the exact result.

## Primary raw vaccination field

Classify a vaccination visit when the survey's `What happened?` field contains `Vaccination(s)`. V5 requires the respondent to confirm this value during verification; it does not require the later vaccine-type field merely to establish that vaccination occurred.

The vaccination field is populated positively in 62 rows. Of those, 44 have a lag in the v5 E or R window:

| E: days 0–5 | R: days 6–59 | N | Early fraction | Expected under null | Per-day RR | Exact 95% CI for RR | One-sided exact p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 36 | 8 | 44 | 81.8% | 10% | 40.5 | 18.5–100.9 | 7.82×10⁻²⁹ |

One additional checklist-vaccination row reports same-day BEFORE and is excluded from E and R under v5.

The current raw result satisfies v5's numerical RR≥2, p<0.05, and CI-excludes-1 criteria by a very wide margin. It cannot satisfy v5's confirmatory decision rule because:

1. the rows have not undergone verification readback;
2. the document-verified replication is unavailable; and
3. recruitment and verification-selection checks have not been completed.

## Prespecified age sensitivities

| Onset-age band | E | R | Per-day RR |
|---|---:|---:|---:|
| <12 months | 9 | 1 | 81.0 |
| 12–17 months | 17 | 4 | 38.25 |
| 18–23 months | 8 | 3 | 24.0 |
| 24–35 months | 2 | 0 | infinite (n=2) |
| ≥36 months | 0 | 0 | not estimable |

Excluding the modal onset month (18) and its adjacent months (17 and 19) leaves E=30 and R=6, for a per-day RR of 45.0. Thus the raw checklist-proxy concentration is not confined to the 17–19-month neighborhood. These subgroup results remain exploratory and sparse.

## Descriptive all-visit result

Ignoring whether vaccination occurred, all raw visits with eligible lags give E=125 and R=62 (N=187), early fraction 66.8%, and per-day RR 18.15. This shows that reported onset is also strongly concentrated after the last wellness visit in the pooled data. It cannot distinguish vaccination from visit anchoring, selection, or other visit-linked events.

## Current conclusion

The latest raw export contains an extremely large timing signal among rows whose `What happened?` field says vaccination occurred. The signal remains large across the populated age bands and after excluding ages 17–19 months. Under v5 it is a compelling **exploratory signal requiring verification**, not a confirmatory determination.

The next decisive step is not Monte Carlo. It is to perform the frozen verification readback, preserve all corrections, and rerun the same exact E/R analysis in respondent-verified and document-verified tiers.
