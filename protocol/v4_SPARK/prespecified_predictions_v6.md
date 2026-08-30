# Prespecified Predictions — Verified SOA Survey Data (version 6 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 raw survey responses.  
**Status:** Superseded draft. V7 replaces overlapping prediction cells with mutually exclusive scoring regions.
**Primary data:** Survey responses confirmed through the prespecified respondent-verification procedure. Document-verified records form the higher-evidence replication.  
**Outcome:** The survey-defined PARENT-observed sudden and lasting autism-consistent change.

## 1. Hypotheses

- **H-null:** vaccination does not cause a material short-window increase in the survey-defined sudden-onset phenotype. Verified onset timing is governed by background developmental timing and observation behavior, not vaccination timing.
- **H-vax:** vaccination triggers the survey-defined sudden-onset phenotype in a subgroup of children. This creates a material excess of verified onsets shortly after a vaccination visit and may create calendar- and age-pattern differences tied to vaccination timing.

H-vax does not claim that every sudden-onset case is vaccine-caused. Infections, injuries, and other mechanisms may account for other cases.

## 2. Exposure groups

- **VAX:** child received one or more vaccines before onset according to the verified schedule question.
- **NEVER:** verified answer “No vaccines were ever given.”
- **SHOT-VISIT:** verified `What happened?` answer includes `Vaccination(s)` at the last regular wellness visit before onset.
- **E:** onset same-day AFTER through day 5 after a SHOT-VISIT.
- **R:** onset days 6–59 after a SHOT-VISIT.

Unknown and unresolved responses are not converted to NEVER or no-shot.

## 3. Authoritative P1–P7 prediction table

This table—not scattered narrative—is the authoritative statement of what each hypothesis predicts.

| Test | H-null predicts | H-vax predicts | Statistic and decision rule | Role |
|---|---|---|---|---|
| **P1. Onset-year distribution, especially 2020** | After normalization within exposure group, VAX and NEVER have the same onset-year shape. There is no 2020 dip confined to VAX. | VAX has a 2020 deficit followed by rebound relative to its adjacent years; NEVER does not show the same vaccine-availability-linked deficit. | Compare within-group yearly proportions, not raw counts. Primary contrast is the VAX-minus-NEVER difference in the 2020 change relative to the mean of 2019 and 2021. H-vax is supported on P1 only if the interaction is in the predicted direction and its 95% CI excludes 0. Otherwise P1 is null-compatible or indeterminate if NEVER is too small. | Core supporting; requires adequate NEVER denominator. |
| **P2. Weekday versus weekend** | In both VAX and NEVER, verified onset follows calendar opportunity: weekday/weekend = 5:2, so \(P(weekday)=5/7\). Any observation-related weekend enrichment should occur similarly in both groups. | VAX departs from the 5:2 distribution in the direction implied by weekday vaccination visits and short post-visit lags; NEVER remains near 5:2 or shares only the general parent-observation effect. | Exact binomial tests within VAX and NEVER, plus the difference in weekday proportions. H-vax is supported on P2 only when VAX significantly departs from 5/7 and differs from NEVER in the prespecified visit-calendar direction. A pooled departure alone does not discriminate. | Core supporting. |
| **P3. Named day of week** | Each named day is approximately 1/7 in VAX and NEVER, apart from a common parent-observation weekend effect. The shapes are the same across exposure groups. | VAX named-day frequencies reflect the verified vaccination-visit calendar convolved with the short-lag window and therefore differ from NEVER; NEVER remains uniform or shows only the common weekend observation effect. | Before confirmatory analysis, calculate the H-vax expected named-day probabilities from the verified SHOT-VISIT weekday distribution and the frozen day-0–5 risk weights. Compare observed VAX days with that distribution and compare VAX with NEVER. Without the frozen convolution or adequate NEVER cases, P3 is indeterminate. | Core supporting; exact directional probabilities still require freezing. |
| **P4. A single modal onset month** | One unique modal onset month is expected from a single broad background developmental-onset process. | One or more peaks may occur near common vaccination ages. A unique peak is allowed under H-vax and therefore does not by itself distinguish the hypotheses. | Identify all modal completed-age months. One unique mode = Yes for H-null and is also compatible with H-vax. Multiple separated peaks weaken the specified single-peak H-null but do not alone establish H-vax. | Core but explicitly non-discriminating when one mode is observed. |
| **P5. Width of the onset-age peak** | The peak is broad: each immediately adjacent month has at least 80% of the modal-month count. | At least one vaccination-age-linked peak is sharp: one or both adjacent months have less than 80% of the modal count. | For unique mode \(m\), calculate \(W_- = n_{m-1}/n_m\) and \(W_+ = n_{m+1}/n_m\). H-null prediction is \(W_-\ge0.80\) and \(W_+\ge0.80\). H-vax prediction is \(\min(W_-,W_+)<0.80\), particularly where \(m\) is a common vaccination age. Report bootstrap CIs; if they span 0.80, score indeterminate. | Core supporting; sharpness is not uniquely causal. |
| **P6. Symmetry around the onset-age peak** | Around the unique modal month, the background distribution is approximately symmetric. The total left-versus-right imbalance over months 1–6 from the mode is no more than 20%. | Vaccination-age-linked peaks or multiple schedule ages produce material asymmetry or secondary shoulders; the left-versus-right imbalance exceeds 20%, with features near common vaccination ages. | For mode \(m\), define \(A=\sum_{k=1}^{6}|n_{m-k}-n_{m+k}|\,/\,\sum_{k=1}^{6}(n_{m-k}+n_{m+k})\). H-null predicts \(A\le0.20\); H-vax predicts \(A>0.20\). Use a bootstrap 95% CI: entirely ≤0.20 supports H-null on P6; entirely >0.20 supports H-vax; otherwise indeterminate. | Core supporting; 20% and ±6 months are fixed draft thresholds. |
| **P7. Verified lag after vaccination visit** | Conditional on onset in days 0–59, events are proportional to interval length: \(P(E)=6/60=0.10\), \(E/R=6/54=1/9\), and per-day \(RR=(E/6)/(R/54)=1\). | There is a material short-window excess: per-day \(RR\ge2\), with more than 10% of eligible verified events in E. | Primary one-sided exact binomial test of \(P(E)>0.10\); also report two-sided p, exact CI, E, R, and RR. P7 supports H-vax when RR≥2, p<0.05, and the 95% CI excludes 1. P7 supports H-null against a material effect when the upper 95% RR limit is <2. Otherwise indeterminate. | **Primary statistical decision test.** |

## 4. Interpretation hierarchy

P1–P7 are all core prespecified predictions and must all be reported. They do not carry equal identifying power:

1. **P7 is primary** because it directly tests the short-window vaccination-relative timing prediction.
2. **P1–P3 are calendar supporting tests.** They require VAX/NEVER denominators or a frozen visit-calendar convolution and may be indeterminate in small samples.
3. **P4 is intentionally non-discriminating** when both hypotheses predict one mode.
4. **P5–P6 are age-shape supporting tests.** A sharp or asymmetric peak may support H-vax but can also arise from rounding, visit-prompted recognition, selection, or other age-structured mechanisms.

No secondary row can rescue P7 if P7 precisely excludes a material association. Conversely, a strongly positive P7 is not erased merely because a non-discriminating row matches both hypotheses.

## 5. Overall decision matrix

After scoring every row Yes, No, or Indeterminate against each hypothesis:

- **Evidence favors H-vax** when P7 satisfies its H-vax rule and the verified/document-verified results agree in direction. Concordant P1–P3 or P5–P6 strengthen that conclusion.
- **Evidence favors H-null against a material short-window association** when P7's upper 95% RR limit is below 2 and no multiplicity-controlled product/window analysis shows a material association.
- **Evidence is inconclusive** when P7's interval includes both 1 and 2, verification is inadequate, or respondent-verified and document-verified results materially conflict.

The final report must include a seven-row-by-two-column matrix:

| Test | H-null match? | H-vax match? |
|---|:---:|:---:|
| P1 | Yes / No / Indeterminate | Yes / No / Indeterminate |
| P2 | Yes / No / Indeterminate | Yes / No / Indeterminate |
| P3 | Yes / No / Indeterminate | Yes / No / Indeterminate |
| P4 | Yes / No / Indeterminate | Yes / No / Indeterminate |
| P5 | Yes / No / Indeterminate | Yes / No / Indeterminate |
| P6 | Yes / No / Indeterminate | Yes / No / Indeterminate |
| P7 | Yes / No / Indeterminate | Yes / No / Indeterminate |

## 6. Verification procedure

Before analysis, the respondent receives a readback and confirms or corrects the sudden-onset eligibility, PARENT onset date or lag, last regular wellness visit, `What happened?` vaccination answer, same-day BEFORE/AFTER or lag, onset age/month/year/day, and VAX/NEVER schedule status. Corrections are logged without overwriting the original.

- **Respondent-verified** records form the primary analysis.
- **Document-verified** records require contemporaneous vaccination/visit evidence and independent dated support for PARENT onset; they form the higher-evidence replication.

## 7. P7 exact and Monte Carlo procedures

The exact binomial test is authoritative. Monte Carlo is a code-validation check only:

1. seed `20260830`;
2. 100,000 replicates;
3. independently draw each null lag uniformly from integers 0–59;
4. calculate simulated E and RR;
5. \(p_{MC}=(1+\#\{E_b\ge E_{obs}\})/(100000+1)\); and
6. verify agreement with the exact binomial p-value within Monte Carlo error.

Do not permute observed lag labels, because doing so preserves the early count and cannot test concentration.

## 8. Required transparency outputs

Publish total responses, VAX/NEVER and SHOT-VISIT denominators, verification flow, corrections, exclusions, E and R, all P1–P7 statistics, respondent-verified and document-verified matrices, and results by recruitment channel. Do not convert missing exposure information into NEVER or no-shot.

## 9. Version history

- **v1:** Three-column qualitative table; later amended at n=270.
- **v2:** SHOT-versus-NOSHOT primary; infeasible because no-shot visits were sparse.
- **v3:** Full-history SCCS primary; stronger data requirement than necessary for the survey test.
- **v4:** Verified 0–5 versus 6–59 primary; H-null/H-vax predictions remained scattered.
- **v5:** Fixed RR=2 and Monte Carlo procedure, but §7 still failed to put explicit H-null and H-vax predictions beside every P1–P7 test.
- **v6 draft:** Establishes one authoritative P1–P7 table with both hypothesis predictions, operational statistics, decision rules, and roles.
