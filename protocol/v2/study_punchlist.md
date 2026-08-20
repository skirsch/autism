The v2 documents are substantially more responsive to Morris, and they generally track your written response. However, they do not yet fully implement several commitments, and the main statistical disagreement Morris identified remains unresolved.

I compared the complete text of the \[Morris review\](C:/Users/stk/Documents/GitHub/autism/feedback on protocol/Morris review of draft protocol.docx), your \[response\](C:/Users/stk/Documents/GitHub/autism/feedback on protocol/Response to Morris review.docx), the \[v2 study overview\](C:/Users/stk/Documents/GitHub/autism/protocol/v2/SORA\_study\_v2.md), and the \[v2 parent survey\](C:/Users/stk/Documents/GitHub/autism/protocol/v2/parent\_survey\_v2.md).

What is now responsive
----------------------

The documents successfully implement or acknowledge several major recommendations:

-   A concrete SORA definition now specifies a first substantial departure within five days, persistence for four weeks, and eligible change domains.
-   The survey captures onset-date confidence and the source used to reconstruct the date.
-   Unaided recall and causal belief precede prompted exposure questions.
-   A validation pilot will evaluate onset-date resolution before choosing the primary risk window.
-   The survey asks whether vaccination continued, changed, or stopped after onset and why.
-   The symmetric "previous versus next vaccination" test is no longer presented as the null hypothesis.
-   Negative controls now include vaccine-free well-child visits, dental visits, holidays, and birthdays.
-   The public dataset will use relative rather than calendar dates, with more granular data under controlled access.
-   Contact information will be separated from analytic data.
-   IRB, HIPAA, privacy, and legal review are explicitly required before recruitment.
-   The overview now states important inferential limits: it cannot estimate population autism risk or population prevalence of regression subtypes.
-   The "definitive answer," refusal-to-replicate, MMR-age-shift, and AI-chat rhetoric criticized by Morris has been removed.
-   Goldberg's video work is no longer characterized as validating day-level dating.

Punchlist
---------

### Priority 1 --- Complete and validate the primary null/reference construction

The three-prong analysis has replaced the former interval-uniformity proposal. The descriptive vaccination-relative lag histograms and chronological-age onset plot do not require a formal reference distribution. The primary Day 0--2 stratified permutation lag-concentration test does require a fully specified and validated null construction.

Complete Items 1A--1E in order before proceeding to Priority 2.

#### Item 1A --- Define the primary estimand and statistic

-   Define the primary observed interval as the parent's direct report of elapsed days from the actual most recent pre-onset vaccination to parent-observed onset; calendar dates are not required for this report.
-   Lock the primary window as Day 0 through Day 2, inclusive.
-   Define the primary statistic as the number and proportion of eligible cases whose onset falls in that window.
-   Define the Day 0--2 versus Day 90--92 count difference as a prespecified secondary contrast whose null distribution comes from the validated permutations rather than an assumed equality of raw counts.
-   Specify eligibility and exclusion rules for the direct-interval statistic, including the precision needed to classify Day 0–2 membership and treatment of contradictory or irreconcilable responses.
-   Define the key secondary high-evidence Day 0–2 statistic and ordered interval-error/evidence tiers without treating self-rated precision as independent validation.
-   Restrict the child-specific permutation component to cases with sufficient separate onset and vaccination timing information.
-   State prospectively that the result measures temporal synchronization, not population autism risk or causation.

#### Item 1B --- Specify candidate permutation procedures

-   Define exactly what is permuted: raw vaccination dates, vaccination-age deviations, onset dates, or another prespecified unit.
-   Define the mandatory strata and any optional refinements.
-   Apply the same most-recent-pre-onset vaccination-selection rule to the observed and permuted data, or justify a different conditional test precisely.
-   Specify how candidate pairings that place vaccination after onset are handled without introducing outcome-dependent filtering.
-   Specify treatment of tied dates, same-day events, multiple vaccines at one visit, sparse strata, and singleton strata.
-   Retain singleton or otherwise non-randomizable strata as deterministic contributions where appropriate rather than silently dropping them.

#### Item 1C --- Validate candidate procedures through simulation

-   Simulate realistic age-dependent onset and vaccination timing under a true null, including scheduled visits, early or delayed appointments, catch-up vaccination, multiple visits, clinic and geographic variation, date error, date heaping, and selection of the most recent vaccination before onset.
-   Verify that each candidate procedure maintains the prespecified false-positive rate under realistic null scenarios.
-   Estimate power when 10%, 20%, 40%, and 90% of cases occur during Days 0--2 after vaccination.
-   Test sensitivity to sparse strata, incomplete dates, onset-date anchoring, delayed vaccination, and incomplete vaccination histories.
-   Use the simulation to select a valid procedure, not merely the procedure with the greatest power under the alternative.

#### Item 1D --- Freeze the permutation-analysis specification

-   Lock the permutation unit, strata, sparse-stratum rules, eligibility rules, number of permutations, random seed, and p-value calculation before examining main-study responses.
-   Define the full lag histogram and chronological-age plot as required descriptive outputs regardless of the primary result.
-   Extend the required three-day lag histogram through Days 177--179, with 180 days or more reported separately, so schedule-spaced peaks such as Day 90 remain visible.
-   Prespecify secondary lag bins, subgroup analyses, sensitivity analyses, and multiplicity handling.
-   Repeat the frozen primary analysis in the record-verified vaccination-date subset as a key replication, while reporting validation consent and record-availability selection.

#### Item 1E --- Confirm that the survey collects sufficient information

-   Map every variable required by the validated permutation procedure to a survey field or record-verification field.
-   Confirm that the direct interval, maximum plausible error in days, evidence source, and optional separate event timing are captured distinctly.
-   Confirm whether the current most-recent-pre-onset vaccination module is sufficient for both the full-sample lag statistic and the exact-timing permutation subset.
-   Add prior vaccination-history fields only if the validated procedure requires them.
-   Confirm that exact-day cases, month-only cases, missing dates, unvaccinated cases, and vaccinations more than 60 days before onset have explicit analysis and routing rules.
-   Close Priority 1 only after the procedure passes simulation validation and the final survey-to-analysis variable map is complete.

### Priority 2 --- Vaccination-interval precision and evidence source — addressed

The survey now asks separately for the direct parent-reported vaccination-to-onset interval, the maximum number of days by which that interval could reasonably be wrong, and the records or memories used to determine it. Onset-date error and vaccination-date error are collected separately. The analysis treats self-rated precision as a measurement-quality variable rather than independent validation.

### Priority 3 --- Make the SORA classification algorithm operational

The current instrument still relies heavily on parents selecting the "SORA Pattern," followed by two yes/no checks. It does not fully implement Morris's recommendation for classification from underlying structured items.

Consider adding:

-   Confirmation that each allegedly lost skill or behavior was consistently present before the change.
-   Duration for each change domain, not merely one global persistence question.
-   Degree of change or functional significance.
-   Whether the change represents loss, fluctuation, failure to progress, or emergence of a new behavior.
-   Start and completion dates or intervals, distinguishing the first departure from later progression.
-   A locked scoring/classification algorithm applied after the raw responses are collected.
-   A "possible SORA/uncertain" category for cases with incomplete evidence.
-   Blinded developmental or clinical adjudication in a subset.
-   Confirmation of an ASD diagnosis and its source, because the current survey appears to assume rather than document it.

The present five-day question could describe either a change completed within five days or merely noticed sometime during a five-day interval. Clarify that onset means the first clear substantial departure from the prior baseline, separately from how quickly the full regression progressed.

### Priority 4 --- Collect timing, duration, and indication for co-occurring exposures

Morris specifically noted that illness, fever, medication, medical visits, and vaccination commonly occur together. Q3.1 currently captures only whether each happened within the five days before onset.

For every major endorsed exposure, add:

-   Start date or interval relative to onset.
-   Duration.
-   Indication or reason.
-   Whether it was part of the same illness or medical encounter as another exposure.
-   For medication: name, dose if known, and first versus continuing use.
-   For fever: highest temperature and measurement method, if known.
-   For illness: symptoms or diagnosis.
-   For vaccination: vaccine products and whether fever/illness/medication followed vaccination.

Predefine vaccination as the primary exposure if that is the primary hypothesis. Treat the other checklist results as descriptive or exploratory unless they receive their own valid reference/control construction.

### Priority 5 --- Implement the promised retention of imprecisely dated cases

Your response says month and year will remain available as a fallback "so that no one is lost." Q1.2 supports an unknown day, but Q1.1 may redirect anyone whose change cannot be confirmed as occurring within five days.

Clarify that:

-   Uncertain or interval-dated cases remain in the study.
-   They are retained for descriptive and age-at-onset analyses.
-   Only cases meeting the required timing resolution enter the applicable day-level confirmatory analysis.
-   "No," "not sure," and missing responses have distinct routing rules.

This is important because excluding uncertain cases could enrich the sample for regressions anchored to salient, dateable events.

### Priority 6 --- Add a complete recruitment-flow plan

The overview says reasons for dropout will be tracked, but neither document specifies the full clinic-level flow Morris requested.

For each clinic, plan to report:

-   Families or children potentially eligible.
-   Invitations sent and successfully delivered.
-   Link opens, if ethically and technically appropriate.
-   Surveys started.
-   Consent obtained.
-   Surveys completed.
-   Cases assigned to each developmental pattern.
-   SORA-confirmed, possible-SORA, and excluded cases.
-   Follow-up consent.
-   Records requested and successfully obtained.
-   Reasons for noncompletion or exclusion when available.

The opt-out question alone cannot capture families who never open or begin the survey.

### Priority 7 --- Define verification-subset selection precisely

The overview's executive summary says "random record-selection follow-up," while the validation section says the subset will be selected from respondents who consent, targeting 20--30% of SORA cases. Those descriptions are not equivalent.

Specify:

-   Whether selection among consenting respondents is random.
-   Whether it is stratified by clinic, causal belief, date confidence, anchor source, schedule status, or reported vaccine proximity.
-   Whether all consenting cases will be sought until the target is met.
-   How unsuccessful record retrieval will be handled.
-   Whether reviewers will be blinded to reported causal beliefs and exposure timing.
-   How verified and unverified respondents will be compared for selection bias.

Avoid saying the subset cannot have been "manipulated" merely because its protocol is preregistered; preregistration improves transparency but does not itself eliminate consent and record-availability selection.

### Priority 8 --- Put the preregistration commitments into the protocol itself

The overview says the null and verification protocol are preregistered, but the documents do not yet contain or identify a locked protocol or statistical analysis plan. If preregistration has not occurred, change "it is pre-registered" to "it will be preregistered before the first main-study response."

The future SAP should specify at minimum:

-   Primary exposure and hypothesis.
-   Primary SORA definition.
-   Primary risk and control windows.
-   Exact reference/null construction.
-   Age adjustment.
-   Handling of delayed, partial, bundled, repeated, and undocumented vaccinations.
-   Co-exposure treatment.
-   Missing onset days and interval-censored dates.
-   Event-dependent post-onset vaccination.
-   Site effects.
-   Multiplicity.
-   Exclusions and censoring.
-   Confirmatory versus exploratory analyses.
-   Sensitivity analyses by causal belief, recall recency, confidence, anchor source, and verification status.
-   A commitment to report the primary analysis regardless of direction.

### Priority 9 --- Align the negative controls with the response

Your response mentions holidays, weekends, and vaccine-free visits; the survey includes dental visits, well-child visits, holidays, and birthdays, but not weekends.

Either add weekends or remove that example from the planned analysis. More importantly, explain how each control will be dated and what comparison it supports. A yes/no control event in the pre-onset window is not automatically a valid reference distribution.

Also prespecify exclusions where a proposed negative control may be related to emerging symptoms---for example, a dental or medical visit prompted by behavioral change.

### Priority 10 --- Correct internal survey routing and consent details

There is a concrete numbering error: Q0.4 says nonsudden patterns route to Section 6, but the Non-SORA Path is Section 5.

Also consider:

-   Adding an explicit affirmative consent question before collecting study data.
-   Separating research contact consent, record-release willingness, gift-card email, and study-results email.
-   Making clear whether email is optional if every SORA completer is promised a gift card.
-   Explaining that actual record release will require a later authorization, not treating the survey's "would you sign" question as authorization.
-   Adding routing for "I'm not sure" in Q0.4.
-   Ensuring the opt-out item actually terminates the survey without collecting unnecessary information.

Bottom line
-----------

Your v2 documents are directionally and substantially responsive, especially on validation, privacy, negative controls, rhetoric, and acknowledgment of limitations. They are also mostly consistent with your response.

They are not yet a complete implementation of that response. The most important remaining work is to:

1.  Make the vaccination reference/null statistically operational.
2.  Replace parent self-classification with a locked item-based SORA algorithm.
3.  Capture timing and indication for correlated exposures.
4.  Preserve and explicitly analyze imprecisely dated cases.
5.  Define recruitment flow, verification sampling, and the SAP in enough detail to preregister them.

Until those changes are made, I would describe the documents as a strong revised study concept and draft instrument---not yet a fully specified, preregistration-ready protocol.
