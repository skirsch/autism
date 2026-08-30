# Prespecified Predictions — Verified SOA Survey Data (version 10 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 survey responses.  
**Status:** Draft. This version replaces v9 and requires separate VAX and NEVER tables without requiring a formal VAX-minus-NEVER interaction.  
**Primary data:** Respondent-verified survey responses. For the present exercise, retained survey values are assumed correct.  
**Outcome:** The survey-defined PARENT-observed sudden and lasting autism-consistent change.

## 1. Question and hypotheses

The purpose of these predictions is to ask whether the verified survey patterns are more consistent with no material vaccine-triggered short-window effect or with a material vaccine-triggered effect in a subgroup.

- **H-null:** vaccination does not produce a material short-window increase in the defined sudden-onset phenotype.
- **H-vax:** vaccination triggers the defined sudden-onset phenotype in a subgroup, producing detectable clustering after vaccination and related calendar or age patterns.

H-vax does not claim that every sudden-onset case is vaccine-caused. These survey tests compare prespecified patterns; by themselves they do not eliminate every non-vaccine explanation for those patterns.

## 2. The seven predictions and how each is measured

### P1 — 2020 dip

If reports merely reflect when parents observed onset, 2020 should not have a special deficit relative to 2019 and 2021. If vaccination-related exposure contributes materially, 2020 should show a substantial dip followed by a rebound.

Count cases by the year of PARENT-observed onset. Compare the 2020 count with the average of the 2019 and 2021 counts. Call that ratio $Q_{2020}$. A value of 1 means no dip; a value of 0.50 means that 2020 had half as many cases as the average adjacent year. H-vax requires $Q_{2020}\leq0.50$ plus a one-sided exact $p<0.05$. H-null requires the lower 95% confidence limit to be greater than 0.50. Results between those regions are indeterminate.

### P2 — Weekday concentration

Under H-null, weekday versus weekend onset reports should be close to the ordinary $5:2$ calendar ratio, meaning $5/7$ or about 71.4% on weekdays. Under H-vax, reports should be more concentrated on weekdays because routine pediatric visits and vaccinations occur predominantly on weekdays and the hypothesized lag is short.

Among responses classifiable as weekday or weekend, calculate the weekday fraction $p_W$. H-null requires its 95% confidence interval to lie within 10 percentage points of $5/7$. H-vax requires at least 80% weekday reports plus a one-sided exact $p<0.05$ against $5/7$. Results between those regions or in the weekend direction are indeterminate.

### P3 — Named day of week

Under H-null, Monday through Sunday onset reports should be approximately uniform. Under H-vax, the seven days should show a statistically detectable nonuniform pattern consistent with the weekday vaccination calendar.

For records naming a particular day, compare the observed seven-day proportions with $1/7$ on each day. Measure the overall departure using total-variation distance: half the sum of the seven absolute differences from $1/7$. H-null requires a simultaneous 95% procedure to rule out every departure larger than 0.15. H-vax requires $p<0.05$, total-variation distance greater than 0.15, and departure in the vaccination-calendar direction frozen before analysis. Otherwise the result is indeterminate.

### P4 — Modal onset age

Under H-null, the most common onset month need not align closely with a common vaccination age. Under H-vax, a stable onset-age mode should lie near 12, 15, or 18 months.

Count cases at each whole month of PARENT-observed onset age and identify the unique modal month. H-null requires a stable mode more than 1 month away from all three target ages. H-vax requires a stable mode within 1 month of at least one target age. A tied or unstable mode is indeterminate. Mode stability is assessed with the frozen bootstrap procedure.

### P5 — Narrow age peak

Under H-null, the onset-age peak should be broad: both adjacent months should retain at least 80% of the modal-month count. Under H-vax, the peak should be sharper than that.

For the unique modal month, divide each immediately adjacent month's count by the modal-month count and retain the smaller ratio; call it $B$. H-null requires the lower 95% confidence limit for $B$ to be at least 0.80. H-vax requires the upper limit to be below 0.80. An interval crossing 0.80 is indeterminate.

### P6 — Age-peak asymmetry

Under H-null, counts should be approximately symmetric around the modal onset month. Under H-vax, a substantial directional asymmetry is expected if onset is concentrated around scheduled exposure ages.

For each distance from 1 through 6 months on either side of the mode, take the absolute difference between the two counts. Add those six differences and divide by the total count in those 12 surrounding months; call the resulting fraction $A$. H-null requires the upper 95% confidence limit for $A$ to be no more than 0.20. H-vax requires the lower limit to exceed 0.20 and the excess to follow the vaccination-age direction frozen before analysis. Otherwise the result is indeterminate.

### P7 — Excess onset shortly after a vaccination visit

Among children whose last regular wellness visit included vaccination, H-null predicts that events are proportional to time at risk. The early window $E$ is same-day AFTER through day 5, lasting 6 days. The reference window $R$ is days 6–59, lasting 54 days. H-null therefore predicts $E/R=6/54=1/9$ and a 10% probability that an event in the combined window falls in $E$.

Calculate the per-day rate ratio as the early events per 6 days divided by the reference events per 54 days. H-null requires the upper 95% rate-ratio limit to be below 2. H-vax requires a point rate ratio of at least 2, a one-sided exact $p<0.05$, and a lower 95% limit greater than 1. Results spanning both regions are indeterminate.

## 3. Required analysis groups

Every dataset produces two independently scored tables:

- **VAX table:** children with verified receipt of one or more vaccines before onset.
- **NEVER table:** children with verified confirmation that no vaccines were ever given before onset.

Unknown or missing vaccination status is included in neither table. A record with contradictory VAX and NEVER evidence is not silently assigned; it is resolved during verification or excluded with the contradiction reported.

P1–P6 are calculated separately within VAX and NEVER using the same definitions, thresholds, and missing-data rules. This is stratification, not a required interaction test: neither table's result depends on the other table having enough observations, and no VAX-minus-NEVER significance test is required.

For P7 in the VAX table, the last regular wellness visit must be verified to have included vaccination. For the P7 negative control in the NEVER table, use the same early and reference windows after the last regular wellness visit, verified to have included no vaccination. This tests whether the early clustering is specific to vaccination visits or also occurs after non-vaccination visits.

The same numerical result labels appear in both tables, but their interpretation differs:

- In the **VAX table**, `Vaccine` means the result entered the pattern prespecified under H-vax.
- In the **NEVER table**, `Vaccine-pattern` means only that the unvaccinated data resemble that numerical pattern. It does not mean a vaccine caused those cases; it is evidence against the pattern's specificity to vaccination.
- `Null` and `Indeterminate` retain their ordinary meanings in both tables.

## 4. Summary decision table and mutually exclusive scoring

Each row receives exactly one of three results:

| Result | Meaning |
|---|---|
| **Null** | The statistic enters the prespecified null region. |
| **Vaccine** | The statistic enters the separate prespecified vaccine region. |
| **Indeterminate** | The statistic enters neither region, data are inadequate, or the direction was not predicted. |

Because only one result is recorded, Null and Vaccine cannot both be satisfied. Failure to enter the Null region does not automatically produce a Vaccine result: the statistic must satisfy the separately defined Vaccine criteria. Otherwise it is Indeterminate.

All confidence intervals are 95%. Draft thresholds for P1–P6 must be frozen before a new confirmatory dataset is examined.

| Test | Null region | Vaccine region | Indeterminate region |
|---|---|---|---|
| **P1. 2020 dip** | The lower confidence limit for $Q_{2020}$ is greater than $0.50$. | $Q_{2020}\leq0.50$ and the one-sided exact test for a 2020 deficit gives $p<0.05$. | The interval crosses $0.50$, too few dated cases, no rebound, or an unpredicted direction. |
| **P2. Weekday concentration** | The confidence interval for $p_W$ lies inside the equivalence band $[5/7-0.10,\,5/7+0.10]$. | $p_W\geq0.80$ and a one-sided exact test against $5/7$ gives $p<0.05$. | The interval or point estimate falls between regions, the excess is toward weekends, or too few classifiable records exist. |
| **P3. Named-day distribution** | A simultaneous 95% goodness-of-fit procedure excludes every departure from uniformity having total-variation distance greater than $0.15$. | The seven-day distribution differs from uniformity at $p<0.05$, has total-variation distance greater than $0.15$, and the departure is in the frozen weekday vaccination-calendar direction. | Precision is inadequate, the departure is smaller, or it points in an unpredicted direction. |
| **P4. Modal onset age** | A stable unique mode lies more than 1 month from each of 12, 15, and 18 months. | A stable unique mode lies within 1 month of 12, 15, or 18 months. | The mode is unstable, tied, or its uncertainty spans both regions. |
| **P5. Peak width** | The lower confidence limit for $B$ is at least $0.80$. | The upper confidence limit for $B$ is below $0.80$. | The interval crosses $0.80$ or the mode/adjacent counts are inadequate. |
| **P6. Peak asymmetry** | The upper confidence limit for $A$ is at most $0.20$. | The lower confidence limit for $A$ is greater than $0.20$ and the excess is in the frozen vaccination-age direction. | The interval crosses $0.20$, the direction is unpredicted, or the mode is unstable. |
| **P7. Verified 0–5-day lag excess** | The upper RR confidence limit is below $2.0$. | Point $RR\geq2.0$, one-sided exact $p<0.05$, and the lower RR confidence limit is greater than $1$. | The confidence interval spans both regions, the reference count is inadequate, verification tiers conflict, or the effect points in the opposite direction. |

For P1–P6, confidence limits and stability are obtained by the frozen nonparametric bootstrap procedure. P3 uses a simultaneous multinomial procedure. Those procedures and the vaccination-calendar directions must be specified in executable code before v8 is frozen.

## 5. P7 exact procedure

The authoritative P7 significance test is the one-sided exact binomial test of $P(E)>0.10$, conditional on $E+R$. Report $E$, $R$, $RR$, the two-sided exact RR confidence interval, and the one-sided p-value. Monte Carlo is optional as a code check and is not needed to calculate the result.

Vaccination at the last regular wellness visit is established by `What happened?` containing `Vaccination(s)`. The separate “vaccination in the 3 days before onset” response may be reported as a consistency field, but it must not be unioned into P7 because it cannot identify the 6–59-day reference window symmetrically. In the NEVER table, P7 uses verified non-vaccination wellness visits and is explicitly labeled a negative-control result.

## 6. Cross-table prediction and overall decision

The prespecified cross-table prediction is:

- The **VAX table** contains only Vaccine or Indeterminate results, with VAX P7 in the Vaccine region.
- The **NEVER table** contains only Null or Indeterminate results, including a Null or Indeterminate P7 negative control.

This expected separation is the fair directional test. It does not require every row to be determinate, nor does it require a formal interaction p-value. A Null result in the VAX table or a Vaccine-pattern result in the NEVER table is a prespecified contradiction and must be displayed, not converted to Indeterminate.

P7 remains the primary statistical decision test; P1–P6 are supporting predictions.

- **Vaccine specificity favored:** VAX P7 is Vaccine, verification tiers agree, the VAX table has no Null results, and the NEVER table has no Vaccine-pattern results.
- **Null favored against a material short-window effect:** VAX P7 is Null and no prespecified multiplicity-controlled product/window analysis finds a material association.
- **Specificity contradicted:** NEVER P7 is Vaccine-pattern or other adequately powered NEVER rows reproduce the VAX patterns.
- **Overall indeterminate:** VAX P7 is Indeterminate, verification tiers conflict, or the NEVER table is too sparse to assess specificity. Report any partial directional matches separately.

P1–P6 cannot substitute for the within-vaccination-visit timing result in VAX P7. Even perfect directional separation in these survey tables does not by itself eliminate selection, recall, visit anchoring, or other causal explanations.

## 7. Required output: two tables for every dataset

Always publish both tables, even when one group is sparse. Validate in code that every VAX row is exactly `Null`, `Vaccine`, or `Indeterminate`, and every NEVER row is exactly `Null`, `Vaccine-pattern`, or `Indeterminate`.

### Table A — VAX

| Test | Result | Statistic and reason |
|---|:---:|---|
| P1 | Null / Vaccine / Indeterminate | Report the estimate, interval, and applicable decision rule. |
| P2 | Null / Vaccine / Indeterminate | Report the estimate, interval, and applicable decision rule. |
| P3 | Null / Vaccine / Indeterminate | Report the estimate, interval, and applicable decision rule. |
| P4 | Null / Vaccine / Indeterminate | Report the mode and stability assessment. |
| P5 | Null / Vaccine / Indeterminate | Report $B$ and its interval. |
| P6 | Null / Vaccine / Indeterminate | Report $A$, its interval, and direction. |
| P7 | Null / Vaccine / Indeterminate | Report $E$, $R$, $RR$, its interval, and the exact p-value. |

### Table B — NEVER

| Test | Result | Statistic and reason |
|---|:---:|---|
| P1 | Null / Vaccine-pattern / Indeterminate | Report the estimate, interval, and applicable decision rule. |
| P2 | Null / Vaccine-pattern / Indeterminate | Report the estimate, interval, and applicable decision rule. |
| P3 | Null / Vaccine-pattern / Indeterminate | Report the estimate, interval, and applicable decision rule. |
| P4 | Null / Vaccine-pattern / Indeterminate | Report the mode and stability assessment. |
| P5 | Null / Vaccine-pattern / Indeterminate | Report $B$ and its interval. |
| P6 | Null / Vaccine-pattern / Indeterminate | Report $A$, its interval, and direction. |
| P7 negative control | Null / Vaccine-pattern / Indeterminate | Report non-vaccination-visit $E$, $R$, $RR$, its interval, and the exact p-value. |

After the two tables, publish a one-paragraph cross-table assessment stating whether the predicted separation was observed, contradicted, or could not be assessed.

## 8. Freeze checklist

Before v8 is final:

1. approve or replace the draft P1–P6 margins;
2. freeze the bootstrap, simultaneous multinomial, and vaccination-calendar direction procedures in code;
3. simulate Type I error, power, mode instability, rounding, and selection;
4. implement the single-state validator;
5. freeze VAX, NEVER, contradiction, verification, and missing-data rules; and
6. publish code, simulations, timestamp, version, and cryptographic hash before applying v8 confirmatorily to new data.

## 9. Version history

- **v1–v5:** developed the hypotheses, verification rules, lag windows, $RR=2$ threshold, and optional Monte Carlo check.
- **v6–v7:** introduced paired mutually exclusive scoring, but incorrectly required VAX-versus-NEVER comparisons for P1–P6.
- **v8 draft:** removes the NEVER interaction, applies P1–P6 to the pooled eligible verified records, retains the confirmed vaccination-visit cohort for P7, and adds plain-English descriptions of all seven predictions.
- **v9 draft:** replaces the redundant H-null/H-vax output columns with one mutually exclusive result: Null, Vaccine, or Indeterminate. Both decision regions remain explicit so rejection or failure of the null alone cannot be mislabeled as vaccine evidence.
- **v10 draft:** requires two independently scored tables for every dataset: VAX and NEVER. It prespecifies the expected directional separation without making either table depend on a formal between-group interaction test and adds a NEVER non-vaccination-visit P7 negative control.
