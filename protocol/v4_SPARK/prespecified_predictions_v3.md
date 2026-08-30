# Prospective Predictions and Verified-Data Analysis Plan — SOA Survey (version 3 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 raw survey responses.  
**Status:** Superseded draft. Preserved because it correctly describes a full-history SCCS, but complete vaccination histories are not required for the simpler verified last-visit lag test selected for v4.  
**Confirmatory data:** A future locked dataset satisfying the verification rules below. Raw parent-recalled intervals and Airtable records 46–318 are exploratory and cannot confirm v3.

## 1. Primary scientific prediction

If vaccination timing is unrelated to parent-observed sudden onset, verified onset events should occur in post-vaccination lag windows in proportion to the **eligible person-time contributed by those windows**, after accounting for the child's age and calendar period.

If vaccination contributes to sudden onset in a subgroup, the verified onset-event rate per eligible day should be higher during the prespecified post-vaccination risk window than during eligible control time.

The primary hypotheses are therefore:

- **H0V:** the incidence-rate ratio in days 0–5 after vaccination is \(IRR_{0-5}=1\).
- **H1V:** the incidence-rate ratio in days 0–5 after vaccination is \(IRR_{0-5}>1\).

This is a within-child, exposure-opportunity analysis. It does **not** require a vaccinated-versus-never-vaccinated comparison or a large sample of non-vaccinating visits.

### Important wording correction

“Events proportional to interval length” is the **null prediction**, not the vaccine-effect prediction. Under H0V, a six-day interval containing 6% of the adjusted eligible person-time should contain about 6% of events. H1V predicts more events than that schedule- and age-adjusted expectation.

## 2. Confirmatory data requirements

A child enters the primary verified analysis only when all of the following are available:

1. the child meets the frozen sudden-onset phenotype definition;
2. the PARENT onset date is supported by prespecified contemporaneous evidence and adjudicated without access to vaccination dates;
3. the complete vaccination history over the observation window is abstracted from an official immunization or medical record, including actual administration dates and products;
4. date precision meets the primary point-date standard, or the record can be handled under the prespecified interval-censoring rule;
5. the observation window and all censoring dates are known; and
6. the record passes mechanical consistency checks fixed before analysis.

The primary analysis assumes these accepted dates and classifications are accurate. Recall error, disagreement with the original survey, and verification yield are reported in a separate validation analysis; they are not used to widen the primary risk window or redefine the primary null.

## 3. Observation period and time classification

- **Observation window:** ages 6 through 36 months, with explicit truncation at the earliest of loss to records, death, or the administrative study end. Any different window must be selected before outcomes are linked to vaccination dates.
- **Primary risk window:** days 0–5 inclusive after each recorded vaccine administration date.
- **Primary control time:** all eligible observation days outside every prespecified post-vaccination risk window and washout window.
- **Same-day ordering:** when time of day is unavailable, calendar day 0 is included. A sensitivity analysis excludes day 0. If verified onset preceded administration on the same day, that day is unexposed.
- **Overlapping vaccine windows:** overlapping days count once as “any vaccination” in the primary analysis. Product-specific overlaps are handled by the prespecified secondary model, not duplicated as person-time.
- **Washout:** days 6–14 are reported separately and are not silently added to control time. Before freezing v3, simulations must determine whether days 6–14 are secondary risk time or washout for the primary model.

Every eligible child contributes exact numbers of risk and control days. Raw response-bin widths are not the denominators.

## 4. Primary analysis

### 4.1 Descriptive observed-versus-expected calculation

For each child \(i\), calculate the adjusted null probability \(q_i\) that an onset event would fall in days 0–5, based on that child's actual vaccine dates, eligible risk days, observation time, and the prespecified age/calendar baseline-rate model.

Let \(O=\sum_i I_i\), where \(I_i=1\) if the child's verified onset falls in days 0–5 after vaccination. The null expected count is \(E=\sum_i q_i\).

Report \(O\), \(E\), \(O/E\), and an exact or simulation-based 95% confidence interval and p-value from the **Poisson-binomial** distribution implied by the unequal \(q_i\). Do not use an ordinary binomial test unless all children genuinely have the same null probability.

### 4.2 Confirmatory self-controlled model

Fit a conditional Poisson self-controlled case-series model with:

- risk indicator for days 0–5 after any vaccination;
- log eligible person-time as the offset;
- child-specific conditioning;
- flexible age-in-month or finer age effects fixed before unblinding;
- prespecified calendar-period adjustment; and
- the event-dependent vaccination/censoring method selected and validated by simulation before freezing the plan.

The primary effect is \(IRR_{0-5}\). Statistical support for a vaccine-associated timing signal requires:

1. \(IRR_{0-5}>1\);
2. a two-sided primary-test p-value below 0.05;
3. the 95% confidence interval entirely above 1; and
4. successful recovery of the null and injected effects in prespecified simulation tests.

Report the effect estimate and interval regardless of significance. Statistical significance establishes a temporal association under the model; it does not, by itself, establish causation or the fraction of all sudden-onset cases caused by vaccination.

## 5. What a 95% early concentration means

Suppose 95% of verified onsets occur in days 0–5:

- If days 0–5 constitute only 5% of adjusted eligible person-time, \(O/E\) and the SCCS IRR will be extremely large and H0V should be rejected. This plainly satisfies the v3 statistical prediction, subject to model validity.
- If vaccination is so frequent that days 0–5 constitute 95% of eligible person-time, 95% of events is exactly what H0V predicts and supplies no vaccine-timing signal.
- If the exposure-opportunity denominator is unavailable because only the last visit was collected, the 95% observation cannot be used as a confirmatory SCCS result.

Thus the decisive quantity is not the raw early percentage. It is the observed event count relative to the verified, age- and schedule-adjusted person-time expectation.

## 6. Why the raw last-visit histogram is not the formal null

Simply expecting counts to equal bin width assumes onset hazard is constant over age and that vaccination opportunities are distributed independently of age. Pediatric vaccination and developmental recognition are both strongly age-structured. A raw 6-day-versus-54-day comparison can therefore create or hide peaks even when dates are perfectly recorded.

The formal null must preserve the actual vaccination schedule and age distribution. The SCCS age baseline does this directly. A separately frozen stratified-permutation analysis may serve as a robustness check by preserving vaccination-age and onset-age marginals while breaking each child's own pairing.

## 7. Event-dependent exposure safeguard

Sudden onset may change later vaccination behavior. Standard SCCS assumes that an event does not alter subsequent exposure, so an ordinary model can be biased here. Before v3 is frozen:

1. choose an established event-dependent-exposure SCCS implementation or a validated alternative conditional model;
2. specify how post-onset vaccinations and observation time are handled;
3. test the implementation under null, causal, age-peak, delayed/catch-up, and vaccination-stopping simulations; and
4. document model failure conditions.

Post-onset vaccination is not treated as a simple negative control.

## 8. Secondary verified-data analyses

These do not replace or gate the primary test:

1. **Risk-window shape:** days 0–1, 0–2, 0–5, 6–14, and 15–30, with a multiplicity plan fixed before analysis.
2. **Product windows:** product-specific analyses only where record counts and overlap rules support them. Any MMR/live-virus day 5–12 hypothesis must be frozen with its own window before inspection.
3. **Non-vaccinating visits:** apply the same person-time method where complete verified visit histories exist. This is a useful visit-anchoring control, but it is not required for the primary vaccine-timing test.
4. **Other verified exposures:** infections or injuries may receive analogous risk-window analyses only with prespecified definitions, dates, evidence standards, and denominators.
5. **Chronological age:** publish the onset-age distribution and model diagnostics to show the extent of age adjustment.
6. **Stratified permutation:** compare each child's onset alignment with the child's own vaccination dates against comparable reassigned schedules while preserving prespecified age, product/dose, calendar, clinic, and schedule strata.

## 9. Separate validation and data-quality analysis

The following are important but are not part of H0V or H1V:

- fraction of survey respondents who enter the verified analysis;
- differences between verified and unverified respondents;
- reported versus record-derived vaccination dates and products;
- reported versus artifact-adjudicated PARENT onset dates;
- direction and magnitude of date errors;
- attribution belief, recruitment channel, and time since onset; and
- missingness and reasons records could not be verified.

These analyses determine generalizability and possible selection bias. They must not be used after results are known to broaden the risk window, change eligibility, or rescue an unsuccessful primary test.

## 10. Interpretation rules

- **IRR significantly above 1:** evidence of verified temporal synchronization beyond the prespecified person-time null. Causal alternatives such as co-administered illness, healthcare events, or residual age/time confounding still require evaluation.
- **IRR near 1 with a narrow interval:** the prespecified large short-window association is not supported in the verified analysis.
- **Wide interval including 1:** inconclusive, not evidence of no association.
- **Raw signal disappears after verification:** the raw parent-recall signal is not confirmed.
- **Verified signal is present despite noisy raw recall:** the verified analysis governs the primary inference.
- **Signal depends on an analysis choice not frozen in advance:** exploratory only.

No result from this outcome-selected case series estimates “vaccines cause ≥80% of sudden-onset autism.” Estimating an attributable fraction requires additional population denominators and causal assumptions beyond this timing analysis.

## 11. Freeze checklist

Before v3 becomes final:

1. freeze the phenotype and evidence-adjudication manuals;
2. freeze the observation, risk, washout, and control windows;
3. select and cite the event-dependent SCCS method;
4. freeze age/calendar adjustment, overlap, censoring, and interval-date rules;
5. implement code against synthetic data without access to confirmatory outcomes;
6. demonstrate calibrated false-positive rates and adequate power in simulations;
7. freeze primary and secondary outputs and multiplicity handling;
8. publish the code, synthetic tests, version, timestamp, and cryptographic hash; and
9. then lock and analyze the confirmatory verified dataset once.

## Version history

- **v1:** Mutually exclusive H-null/H-vax/H-artifact prediction table; later amended at n=270.
- **v2:** Draft SHOT-versus-certain-NOSHOT early-fraction comparison; rejected as the primary design because certain-NOSHOT visits are expected to be too sparse and data quality was mixed into the hypothesis test.
- **v3 draft:** Makes the verified-date exposure-opportunity/SCCS analysis primary; uses the complete vaccination schedule and eligible person-time; and moves raw-recall quality and no-shot comparisons to separate secondary analyses.
