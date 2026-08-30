# Prospective Predictions and Analysis Plan — Verified SOA Survey Data (version 4 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 raw responses.  
**Status:** Superseded draft. V5 fixes the RR=2 decision margin and specifies the randomization procedure.  
**Primary dataset:** Responses collected by the live survey and subsequently verified under §2. Raw unverified responses are not used for the primary decision.  
**Outcome:** The survey's defined PARENT-observed sudden and lasting autism-consistent change, not autism diagnosis date and not every presentation of autism.

## 1. Question and inferential target

The practical question is whether the verified survey patterns are more consistent with:

- **M0 — no short-window vaccine association:** vaccination at the last regular wellness visit does not increase the probability of sudden onset during days 0–5; or
- **MV — vaccine-associated subgroup:** vaccination at the last regular wellness visit triggers sudden onset in some children, producing a statistically detectable excess during days 0–5.

The analysis can determine whether the verified timing data favor a short-window vaccine-associated explanation over the specified no-association model. Because this is an observational survey of selected sudden-onset cases, it cannot by itself prove that vaccines cause autism generally or estimate a population attributable fraction.

The primary comparison does **not** require a vaccinated-versus-unvaccinated cohort or a large number of no-shot wellness visits. Those comparisons are secondary diagnostics when data permit.

## 2. Verification and analysis-ready records

The primary analysis uses the fields the survey collects after a verification readback. Before analysis, the respondent is shown or read the submitted values and separately confirms or corrects:

1. that the child meets the frozen sudden-and-lasting onset definition;
2. the PARENT onset date or reported lag category;
3. that the referenced visit was the last regular wellness visit before onset;
4. whether vaccination occurred at that visit;
5. the reported visit-to-onset interval, including same-day BEFORE versus AFTER;
6. age in months at onset;
7. onset day of week and onset year; and
8. vaccination-schedule status, including NEVER.

Corrections are logged; the original response is never overwritten. A record is “respondent-verified” when the parent completes this readback and reports that the retained values are correct. “Document-verified” is a separate higher-evidence tier requiring contemporaneous records for the visit/vaccination date and independent dated support for the PARENT onset date.

The primary result is reported in all respondent-verified eligible records and repeated in the document-verified subset. Participant confirmation is not represented as independent documentary proof.

## 3. Primary test: verified lag concentration after a vaccination visit

### 3.1 Eligibility

Include a verified record when:

- vaccination at the last regular wellness visit is confirmed;
- onset occurred after that visit;
- the verified lag is classifiable from day 0 through day 59; and
- the response passes the frozen phenotype and consistency rules.

Same-day BEFORE records are temporal negative controls and are not counted as post-vaccination events. Unknown vaccine status, unknown lag, and internally unresolved records are excluded with counts and reasons reported.

### 3.2 Windows and null

- **Early window E:** same-day AFTER plus days 1–5, covering 6 calendar-day categories.
- **Reference window R:** days 6–59 inclusive, covering 54 days. This is exactly recoverable from the live survey bins.
- **Simple proportional-time null:** conditional on onset occurring in days 0–59, each day has equal probability. Therefore:

\[
P_0(E)=\frac{6}{60}=0.10,
\qquad
\frac{E_0}{R_0}=\frac{6}{54}=\frac{1}{9}.
\]

This is the prespecified simple null. It assumes a flat baseline across the 60-day window. Its limitations are addressed by the age/schedule robustness analysis in §3.5, not by widening the primary bands after results are seen.

### 3.3 Statistic and test

Let \(N=E+R\), where \(E\) is the verified early count and \(R\) the verified day-6–59 count.

Report:

- early fraction \(E/N\);
- count ratio \(E/R\);
- per-day rate ratio

\[
RR_{day}=\frac{E/6}{R/54};
\]

- exact 95% confidence intervals; and
- a one-sided exact binomial test of \(H_0:P(E)=6/60=0.10\) against \(H_1:P(E)>0.10\).

The directional test is prespecified because MV predicts an excess, not a deficit. Also report the two-sided p-value for transparency.

### 3.4 Primary decision rule

The verified timing data statistically favor a short-window vaccine-associated model over the simple proportional-time null when:

1. \(RR_{day}>1\);
2. the one-sided exact p-value is below 0.05;
3. the 95% confidence interval for \(RR_{day}\) is entirely above 1; and
4. the result remains directionally consistent in the document-verified subset and the prespecified age/schedule robustness analysis, or those analyses are explicitly labeled too small to decide.

Failure to reject H0 is not positive evidence for no association unless the confidence interval excludes a prespecified meaningful effect. For a “more likely no material short-window association” conclusion, require the upper 95% confidence limit for \(RR_{day}\) to be below **2.0**. The 2.0 margin is a draft choice and must be approved or replaced before v4 is frozen.

### 3.5 Age- and schedule-structure robustness test

Even perfectly verified dates can align because vaccination visits and developmental changes are age-structured. Therefore, repeat the primary statistic against a frozen empirical null that preserves the observed onset-age and vaccination-age distributions while breaking each child's own onset-to-visit pairing.

Use a stratified permutation within sufficiently populated strata fixed before analysis, including onset-age band, vaccination-visit age or schedule position, birth cohort/calendar period, and routine versus delayed/catch-up schedule where available. Report the permutation p-value and null distribution of \(RR_{day}\).

This robustness analysis does not require complete vaccination histories. It requires each included child's verified PARENT onset timing and verified relevant pre-onset vaccination-visit timing. A full-history SCCS is a stronger optional replication, not the primary requirement.

### 3.6 Example: 85% in days 0–5

If 85% of eligible verified events fall in E and 15% in R:

\[
RR_{day}=\frac{0.85/6}{0.15/54}=51.
\]

That is an extreme departure from the simple proportional-time null. If it is based on an adequate verified sample and survives the frozen age/schedule permutation, v4 classifies it as strong evidence favoring a vaccine-associated short-window explanation. It does not become inconclusive merely because raw recall data would require wide uncertainty bands.

## 4. Prespecified descriptive and diagnostic predictions

The following operationalize the seven proposed predictions. They do not all carry equal causal weight. P7 is primary; P1–P6 are secondary diagnostics.

### P1. Onset-year distribution in VAX versus NEVER

**Proposed prediction:** after normalization within group, VAX and NEVER should have the same onset-year shape under M0. In particular, a 2020 dip limited to VAX is more consistent with vaccination availability affecting onset timing; a shared dip suggests recruitment, birth-cohort, recall, or healthcare-visit effects.

**Required analysis:** compare within-group yearly proportions, not raw counts. Report the number of eligible children contributing to each exposure group and year. A statement that “all years have the same number” is not valid without source-population denominators because birth cohorts, recruitment, age eligibility, and recall opportunity differ by year.

**Test:** chi-square or exact homogeneity test for the VAX-by-year versus NEVER-by-year distributions, with 2020 specified as the focal contrast. Interpret only if the NEVER group is adequately sized.

### P2–P3. Weekday/weekend and named day of week

**Simple null:** verified onset dates are uniform across calendar days:

\[
P(weekday)=5/7, \qquad P(weekend)=2/7,
\]

and each named day has probability \(1/7\).

**Alternative observation model:** weekend enrichment may occur because parents spend more time with children then. This alternative must be stated before testing and cannot simultaneously be counted as support for uniformity.

**Tests:** exact binomial weekday/weekend test and chi-square or exact multinomial named-day test. Repeat in VAX and NEVER when sample size permits. These tests diagnose calendar structure; alone they do not identify vaccination as the cause.

### P4–P6. Age-at-onset shape

The proposed no-vaccine-association shape is:

1. one modal onset month;
2. each immediately adjacent month is at least 80% of the modal month's count; and
3. counts are approximately symmetric around the mode.

Before freezing v4, define:

- whether age is exact completed months or rounded parent report;
- the minimum count required to define a stable mode;
- the span over which symmetry is evaluated;
- a numerical symmetry statistic and tolerance; and
- whether smoothing is allowed.

As currently written, the 20% and symmetry rules are user-proposed diagnostics, not established null consequences. Developmental floors, right tails, digit heaping, and mixed mechanisms can violate them without vaccination. Conversely, scheduled-age peaks can reflect vaccination timing, visit-prompted recognition, or age-dependent developmental change. Report these results, but do not let P4–P6 override the verified lag test.

### P7. Days 0–5 versus days 6–59

This is the primary test in §3. Under the simple proportional-time null, expected \(E/R=6/54=1/9\). MV predicts a statistically significant per-day excess in E.

## 5. Evidence synthesis: which model is better supported?

The conclusion is based on the following hierarchy:

### Evidence favoring MV

- Primary verified \(RR_{day}\) is significantly above 1;
- the excess remains in the document-verified subset;
- the excess survives the frozen age/schedule permutation;
- same-day BEFORE records do not show the same pattern;
- results are not confined to vaccine-attributing or vaccine-aware recruitment channels; and
- secondary calendar and age patterns are compatible with the actual verified vaccination dates.

### Evidence favoring M0 for a material short-window effect

- Primary verified estimate is near 1;
- its upper 95% confidence limit excludes the frozen meaningful-effect margin;
- document-verified and age/schedule-adjusted analyses agree; and
- no isolated product/window signal survives multiplicity control.

### Inconclusive

- verification yield is too low;
- confidence intervals include both no association and a material effect;
- the raw signal disappears or materially changes during verification;
- the result fails the age/schedule empirical-null test; or
- selection into the survey or verification subset is strongly related to remembered vaccine proximity and cannot be bounded.

Do not convert a merely significant timing association into “vaccines cause autism” without stating the observational assumptions. The defensible conclusion is whether the verified survey data favor or do not favor a vaccine-associated trigger for the defined sudden-onset phenotype.

## 6. Raw-data and validation reporting

Raw responses are used to report recruitment, missingness, and verification flow—not to define wider confirmatory bands. Publish:

- total responses;
- eligible for recontact;
- recontacted;
- respondent-verified;
- document-verified;
- excluded with each reason;
- corrections by field and direction;
- timing results in raw, respondent-verified, and document-verified tiers; and
- characteristics associated with successful verification.

The verified analysis is primary, but differential verification remains a possible selection bias and must be visible.

## 7. Secondary controls and extensions

- Certain no-shot wellness visits receive the same lag analysis when available, but no minimum no-shot count gates the primary result.
- NEVER children contribute to calendar and age-shape diagnostics, not the primary post-vaccination lag test.
- Prespecified verified infections and injuries can receive analogous lag analyses only after evidence definitions and windows are frozen.
- Vaccine-product and live-virus windows are secondary and multiplicity-controlled.
- A complete-record SCCS over ages 6–36 months is an optional stronger replication where full histories are available.

Negative controls can reveal some bias but cannot mechanically prove its absence; their assumptions and limitations must be reported.

## 8. Freeze checklist

Before v4 is final:

1. finalize the respondent-verification script and document-verification rules;
2. confirm that the live export continues to preserve the exact days 0–5 and days 6–59 categories used by the primary test;
3. approve or replace the RR=2.0 no-material-effect margin;
4. operationalize the age-peak width and symmetry statistics;
5. freeze permutation strata, sparse-stratum handling, iterations, seed, and p-value calculation;
6. simulate flat-null, age-peak, vaccine-effect, delayed-schedule, and selection scenarios;
7. implement the full output table against synthetic data;
8. freeze multiplicity rules for secondary tests; and
9. publish the version, timestamp, code, simulation results, and cryptographic hash before confirmatory analysis.

## 9. Version history

- **v1:** Three mutually exclusive hypotheses with a decisive no-shot comparison.
- **v2:** Formalized SHOT versus certain-NOSHOT as primary; superseded because no-shot visits are expected to be too sparse.
- **v3:** Required complete histories for a full SCCS; superseded because that requirement was stronger than necessary for the verified last-vaccination lag test.
- **v4 draft:** Uses verified survey data and a simple days 0–5 versus 6–59 proportional-time test as primary, adds an age/schedule permutation robustness test, and makes full SCCS and no-shot comparisons secondary.

## References

- Farrington CP. Control without separate controls: evaluation of vaccine safety using case-only methods. *Vaccine*. 2004;22:2064–2070. PMID 15121324.
- Petersen I, Douglas I, Whitaker H. Self controlled case series methods: an alternative to standard epidemiological study designs. *BMJ*. 2016;354:i4515.
- Lipsitch M, Tchetgen Tchetgen E, Cohen T. Negative controls: a tool for detecting confounding and bias in observational studies. *Epidemiology*. 2010;21:383–388.
