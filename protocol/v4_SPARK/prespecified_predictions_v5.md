# Prospective Predictions and Analysis Plan — Verified SOA Survey Data (version 5 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 raw responses.  
**Status:** Superseded draft. V6 replaces the separated prose with an explicit H-null-versus-H-vax prediction and decision rule for every P1–P7 row.
**Primary data:** Responses collected by the live survey and confirmed through the verification procedure below. Raw unverified responses are reported separately and do not determine the primary conclusion.  
**Outcome:** The survey-defined PARENT-observed sudden and lasting autism-consistent change.

## 1. Competing predictions

- **M0 — no material short-window vaccine association:** among eligible verified cases whose last regular wellness visit included vaccination, verified onset lags are distributed in proportion to time across days 0–59. The per-day rate during days 0–5 is not materially greater than during days 6–59.
- **MV — vaccine-associated subgroup:** the per-day verified onset rate during days 0–5 is elevated by at least twofold relative to days 6–59.

The primary test does not require a vaccinated-versus-never-vaccinated comparison or a minimum number of no-shot visits.

## 2. Verification

Before analysis, the respondent receives a readback and confirms or corrects:

1. eligibility under the frozen sudden-and-lasting onset definition;
2. PARENT onset date or lag category;
3. that the referenced visit was the last regular wellness visit before onset;
4. whether `What happened?` includes `Vaccination(s)` for that visit, and whether that answer is correct;
5. same-day BEFORE versus AFTER or the visit-to-onset lag;
6. age in months, onset year, and onset day of week; and
7. vaccination-schedule status, including NEVER.

Corrections are logged without overwriting the original response.

- **Respondent-verified:** the parent completes the readback and confirms the retained values.
- **Document-verified:** vaccination/visit timing is confirmed from a contemporaneous record and the PARENT onset date is independently supported by a prespecified dated artifact or record.

The respondent-verified set is primary because it directly verifies the survey data. The document-verified subset is the key higher-evidence replication. Participant reconfirmation is not described as independent documentary proof.

## 3. Primary verified lag test

### 3.1 Eligibility and windows

Include a respondent-verified case when vaccination at the last wellness visit is confirmed, onset occurred after the visit, and lag is classifiable within days 0–59.

For this purpose, vaccination-at-visit status comes from the verified `What happened?` → `Vaccination(s)` field. The later vaccine-type question is used for product-specific analyses and consistency checks; it is not required merely to classify the visit as a vaccination visit.

- **E:** same-day AFTER plus days 1–5: 6 days.
- **R:** days 6–59: 54 days.
- Same-day BEFORE is reported as a temporal negative control and excluded from E and R.
- Unknown, unresolved, and out-of-window records are excluded with counts and reasons.

The current survey can recover these windows exactly.

### 3.2 Simple proportional-time null

Conditional on verified onset occurring during days 0–59, M0 predicts:

\[
P_0(E)=\frac{6}{60}=0.10,
\qquad
\frac{E_0}{R_0}=\frac{6}{54}=\frac{1}{9}.
\]

Let \(E\) and \(R\) be the observed verified counts and \(N=E+R\). Report:

\[
RR_{day}=\frac{E/6}{R/54},
\]

the early fraction \(E/N\), all four quantities \(E,R,6,54\), exact confidence intervals, a one-sided exact binomial p-value for \(P(E)>0.10\), and the two-sided p-value.

### 3.3 Fixed RR=2 decision margin

The v5 material-effect threshold is **RR = 2.0**.

The verified survey evidence favors MV when all of the following hold:

1. point estimate \(RR_{day}\ge2.0\);
2. one-sided exact p-value <0.05;
3. the 95% confidence interval excludes 1; and
4. the result has the same direction in the document-verified subset, unless that subset is explicitly too small for a meaningful check.

The evidence favors M0 against a material short-window association when the **upper** 95% confidence limit for \(RR_{day}\) is below 2.0.

All other outcomes are inconclusive. In particular, a nonsignificant result with an upper confidence limit above 2.0 does not favor M0.

This margin distinguishes statistical detectability from practical magnitude. A tiny association cannot satisfy MV merely because a very large sample makes it statistically significant.

### 3.4 Example

If 85% of verified onsets are in E and 15% in R:

\[
RR_{day}=\frac{0.85/6}{0.15/54}=51.
\]

With an adequate verified sample, this would overwhelmingly exceed the RR=2 threshold and the 1:9 proportional-time null.

## 4. Prespecified randomization procedure

### 4.1 Why it is not needed for the simple p-value

The exact binomial test already supplies the exact primary p-value under \(P_0(E)=0.10\). A simulation that independently assigns uniform lags from 0 through 59 is mathematically the same null. It is included as a reproducibility and code-validation check, not as a second gate that can overturn the exact test.

Do **not** permute the observed lag labels among children: that preserves the number of early lags exactly and therefore cannot test early concentration.

### 4.2 Fixed Monte Carlo randomization

For the \(N\) eligible verified cases:

1. Set the pseudorandom seed to `20260830`.
2. Generate \(B=100{,}000\) replicates.
3. In each replicate \(b\), independently assign every case a null lag \(L_{ib}\) drawn uniformly from the 60 integer values 0–59.
4. Calculate \(E_b=\sum_i I(L_{ib}\le5)\), \(R_b=N-E_b\), and \(RR_{day,b}=(E_b/6)/(R_b/54)\). Treat \(R_b=0\) as infinite.
5. Calculate the Monte Carlo p-value

\[
p_{MC}=\frac{1+\sum_b I(E_b\ge E_{obs})}{B+1}.
\]

6. Confirm that \(p_{MC}\) agrees with the exact one-sided binomial p-value within Monte Carlo error. A material discrepancy is an implementation failure that must be resolved before reporting results.

The exact test remains authoritative.

## 5. Why 60-day shot spacing does not by itself prove flatness

Spacing vaccination visits at least 60 days apart prevents two recent vaccination windows from overlapping. It does not guarantee that onset is equally likely on every lag day.

For example, if a non-vaccine developmental process produces an onset peak near 18 months and many children also receive a scheduled vaccination near 18 months, verified lags can cluster near zero because both processes are tied to age. No date error or overlapping shot is needed.

V5 therefore separates two questions:

1. **Primary simple question:** is the verified distribution incompatible with the explicit flat 1:9 null?
2. **Age-alignment sensitivity question:** could common age structure plausibly generate the observed concentration?

The first is answered by the exact test. The second is not answered merely by shot spacing.

## 6. Age-alignment sensitivity analysis

The live survey does not collect complete birth dates or complete vaccination histories, so it cannot support a fully nonparametric child-level age permutation without additional verified information. V5 does not pretend otherwise.

Use the following prespecified analyses available from verified survey fields:

1. Tabulate \(RR_{day}\) within onset-age bands `<12`, `12–17`, `18–23`, `24–35`, and `≥36` months.
2. Report whether the early excess is confined to a single scheduled-age band.
3. Plot the exact verified lag histogram beside the age-at-onset histogram.
4. Repeat the primary test excluding the modal onset month and its two adjacent months.
5. Repeat within routine/on-time, delayed, reduced, and early-then-stopped schedule groups where counts permit.

An excess that remains large across age bands and after excluding the modal-age neighborhood is harder to explain by a single age-alignment peak. A signal confined to one scheduled-age band is still a timing association but has a plausible common-age alternative.

If a later verification module collects exact birth dates and complete vaccination dates, a full age-preserving permutation or SCCS may be added as a separately versioned replication. It is not required to execute v5.

## 7. Seven core prespecified predictions

P1–P7 are the study's seven core predictions and must all be reported. P7 is the **primary statistical decision test** because it directly tests vaccination-relative timing against the 1:9 proportional-time null. P1–P6 are **core supporting predictions**: they can strengthen, weaken, or qualify the interpretation, but none individually overrides P7.

### P1. Onset year

Compare normalized onset-year distributions in VAX and NEVER, not equal raw counts. Under M0 their shapes should be similar. A 2020 dip confined to VAX is more compatible with vaccination availability affecting the pattern; a shared dip suggests cohort, recruitment, recall, or healthcare-visit effects. Interpret only with adequate NEVER counts and visible denominators.

### P2–P3. Weekday/weekend and named day

The simple calendar null is \(P(weekday)=5/7\), \(P(weekend)=2/7\), and \(P(day)=1/7\) for each named day. Test weekday/weekend by exact binomial and named days by an exact multinomial or chi-square test. Weekend enrichment is a prespecified observation alternative, not simultaneous evidence for uniformity. These are diagnostics, not decisive causal tests.

### P4–P6. Age shape

Report whether there is one modal month, whether each adjacent month is at least 80% of the mode, and whether counts are approximately symmetric around the mode. Before freezing v5, define the symmetry statistic, evaluated span, minimum modal count, and treatment of ties. These are user-proposed diagnostics; they do not override the primary lag test because developmental floors, right tails, rounding, and mixed mechanisms can also change the shape.

### P7. Verified lag concentration — primary statistical decision test

This is the primary days 0–5 versus days 6–59 analysis in §3.

## 8. Evidence synthesis

### More consistent with a vaccine-associated short-window trigger

- primary verified result satisfies all MV criteria;
- document-verified results agree in direction;
- same-day BEFORE does not show an analogous concentration;
- the excess is not solely a modal-age phenomenon;
- the excess is not confined to vaccine-attributing respondents or one recruitment source; and
- no recorded co-exposure explains most early cases.

### More consistent with no material short-window association

- upper 95% confidence limit for verified \(RR_{day}\) is below 2.0;
- document-verified results agree; and
- no prespecified product or subgroup result survives multiplicity control.

### Inconclusive

- confidence interval includes both 1 and 2;
- verification yield or reference-window count is inadequate;
- raw and verified results materially disagree;
- the signal is confined to one age/recruitment/attribution stratum; or
- verification selection is strongly associated with remembered vaccine proximity and cannot be bounded.

The conclusion should say whether the verified survey data favor a vaccine-associated trigger for the defined sudden-onset phenotype. It should not be generalized without qualification to all autism.

## 9. Verification-flow and transparency outputs

Publish total responses, recontact eligibility, recontact attempts, respondent-verified count, document-verified count, corrections by field, every exclusion reason, and timing results in raw/respondent-verified/document-verified tiers. Report characteristics associated with verification success.

## 10. Freeze checklist

Before v5 becomes final:

1. freeze the verification readback and document rules;
2. operationalize age symmetry and modal-width rules;
3. implement the exact and Monte Carlo tests against synthetic data;
4. simulate flat, RR=2, RR=5, age-alignment, recall-selection, and sparse-reference scenarios;
5. freeze minimum reporting and multiplicity rules;
6. publish code, simulations, timestamp, version, and cryptographic hash; and
7. analyze the verified confirmatory data once.

## Version history

- **v1:** Three mutually exclusive hypotheses with a decisive no-shot comparison.
- **v2:** Formal SHOT-versus-certain-NOSHOT primary; infeasible because no-shot visits are expected to be sparse.
- **v3:** Full-history SCCS primary; stronger data requirement than necessary for the survey's verified lag test.
- **v4:** Verified days 0–5 versus 6–59 primary with an unresolved RR margin and broadly described permutation.
- **v5 draft:** Fixes RR=2, specifies the exact and Monte Carlo procedures, explains why the Monte Carlo test duplicates the flat exact null, and replaces an infeasible age permutation with survey-supported age-alignment sensitivity analyses.

### V5 clarification log

- **2026-08-30:** Clarified that vaccination-at-visit status is supplied by the existing verified `What happened?` → `Vaccination(s)` field. The later vaccine-type field is not required for this binary classification. This clarification does not change the E/R windows, RR=2 threshold, exact test, or the previously calculated 36/8 raw result.
- **2026-08-30:** Corrected the §7 heading. P1–P7 are the seven core prespecified predictions; P7 is the primary statistical decision test and P1–P6 are core supporting predictions. They are not a separate list of merely optional secondary analyses.
