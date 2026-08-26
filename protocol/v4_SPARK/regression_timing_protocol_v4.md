# Timing and Attribution of Parent-Reported Developmental Regression in Autism

## A pre-registered study of onset dating, date evidence, and dated exposures in the SPARK cohort

**Protocol v0.1 — draft for adversarial review**
**Status:** not yet submitted. Intended for pre-registration (OSF) and Registered Report submission before any participant contact.

Principal Investigator: [TBD — academic institution]
Adversarial Co-Investigator (analysis plan owner): [TBD]
Co-Investigators: [developmental pediatrician, SPARK clinical site]; [survey methodologist]; [biostatistician]
Funder: [university gift / donor-advised fund]; see §11 for conflict-of-interest disclosure.

---

## 1. Background and rationale

Roughly a fifth to a third of children later diagnosed with autism are reported by parents to have lost previously acquired skills, most often between 12 and 24 months. This is the same period in which children on the US schedule receive vaccines at the 12-, 15-, and 18-month well visits, and in which the 18-month visit includes formal developmental screening (M-CHAT). Parents' reports that regression followed a vaccination have been central to public concern about vaccines and autism for nearly thirty years.

Two accounts of those reports are in play, and they make different predictions.

**The biological account** holds that in some children, regression begins within days of a vaccination visit as a consequence of the vaccination. It predicts that parent-observed onset clusters in the days immediately after vaccinating visits at a rate above what the schedule alone would produce; that the clustering is present regardless of what the parent believes caused the child's autism; that it is present when the onset date is anchored by contemporaneous evidence (photos, video, messages); and that it does not appear after non-vaccinating well visits or after other dated events.

**The artifactual account** holds that the reported clustering is produced by (a) selection — parents who believe vaccines were involved are more likely to volunteer for surveys on the topic; (b) reconstruction — onset of a gradual process is dated retrospectively and anchored to the most salient dated event in the window, which is often a well visit; (c) visit-prompted noticing — the 18-month visit asks parents directly about pointing, response to name, and joint attention, so parents go home and observe deficits already present; and (d) narrative exposure — reported timing drifts toward vaccination dates after parents encounter the hypothesis (Andrews et al., *Arch Dis Child* 2002). It predicts that clustering is concentrated among vaccine-attributing parents and memory-dated cases, that it appears after M-CHAT visits whether or not vaccines were given, and that within-family reports move toward vaccination dates over time.

Population studies using records (Taylor et al. 1999, 2002; Madsen et al. 2002; Hviid et al. 2019) have found no month-scale clustering of regression or diagnosis after MMR. Those studies had a temporal resolution of weeks to months and relied on clinician-documented concern, which lags onset and is itself anchored to visits. They therefore do not directly test the day-scale claim, and their reliance on clinical documentation is a legitimate limitation given evidence that parental concerns are frequently not charted. Conversely, existing day-scale evidence comes entirely from convenience samples recruited through channels sorted on the vaccine hypothesis, with onset dates from unaided or aided recall, and cannot distinguish the two accounts.

No study has (i) collected unaided onset narratives from a large sample not recruited on the hypothesis, (ii) measured the parent's attribution belief and the evidence behind the date separately from the date itself, (iii) linked parent-observed onset to immunization records rather than recalled shots, (iv) compared vaccinating visits against non-vaccinating visits and other dated exposures in a self-controlled framework, and (v) measured within-family drift in reported timing. This protocol does all five.

The study is designed so that either account can lose. The confirmatory hypothesis test is specified in a stratum where the artifactual mechanisms are weakest; the secondary analyses measure those mechanisms directly.

## 2. Objectives and hypotheses

**Primary objective.** Estimate whether parent-observed onset of regression clusters in the days immediately following vaccinating well visits, beyond the rate expected from each child's own immunization schedule, among parents who do not attribute their child's autism to vaccines and whose onset date is anchored by contemporaneous evidence.

**H1 (biological).** In the confirmatory stratum (non-attributing, artifact-dated), the observed proportion of onset dates falling in days 0–2 after a vaccinating visit exceeds the schedule-expected proportion, with relative risk ≥ 2.0.

**H0 (artifactual / null).** In the confirmatory stratum, the observed proportion does not exceed the schedule-expected proportion; any excess in the full sample is concentrated among vaccine-attributing and memory-dated respondents.

**Secondary objectives.**

1. Estimate the rate of spontaneous vaccine mention in unaided onset narratives, by attribution stratum, against the rate in narratives from parents of non-regressive children describing first concern.
2. Compare onset clustering after vaccinating well visits with clustering after non-vaccinating well visits (9-, 24-, and 30-month, where no vaccine was given per record) and after other dated exposures (febrile illness, antibiotics, hospitalization, daycare entry, household move, sibling birth).
3. Measure within-family drift: difference between age-at-loss reported at SPARK enrollment and age-at-loss reported in this survey, as a function of time elapsed, attribution belief, and reported timing of first exposure to the vaccine hypothesis.
4. Characterize how parents date onset (evidence type), and whether clustering differs by evidence quality.
5. Estimate the interval between first parental concern and clinical documentation, and whether parents report having raised concerns that were not acted on.

Predictions for each hypothesis are stated in §8.6 so that outcomes are interpretable in advance.

## 3. Design

Cross-sectional online survey delivered through SPARK Research Match, with (a) linkage to phenotypic data collected at SPARK enrollment, (b) participant upload of the child's official immunization record, and (c) optional consent to a 12-month re-contact. Self-controlled analysis of onset timing relative to record-dated exposures. Unaided narrative collected first and locked before any structured item.

## 4. Population

**Source.** SPARK probands, US residents, with a parent or guardian as respondent.

**Regression sample (primary).** Probands aged 2–12 years at survey whose enrollment data indicate loss of language or other skills (SPARK Basic Medical Screening / background history regression items). Age cap limits recall interval and ensures immunization records are retrievable from state registries.

**Comparison sample.** Probands aged 2–12 years with no reported loss of skills, drawn at random, invited with identical materials. Their narratives of *first concern* supply the base rate of spontaneous vaccine mention among parents describing onset without regression, and their exposure data supply a second reference distribution for visit timing.

**Exclusions.** Proband not living with respondent during the 6–36 month age window; respondent unable to complete in English or Spanish (instrument to be translated); proband with a known genetic syndrome diagnosed before onset (recorded, analyzed as a sensitivity exclusion rather than a hard exclusion — TBD with co-I).

**Recruitment.** Standard SPARK Research Match invitation, drafted by the Research Match team to SPARK's house style. Invitation and landing page describe the study as research on how parents first notice developmental change and how they remember it. No mention of vaccines, immunizations, suddenness, or causes in any recruitment material or in any instrument text preceding §6.4.

## 5. Sample size

Assumptions, to be revised against SPARK's eligible counts:

- Expected proportion of onset dates in a 3-day post-vaccinating-visit window under the null, computed from each child's uploaded record over an observation window of 6–36 months: approximately 0.015 (three vaccinating visits × 3 days / ~600 days of observation, before catch-up and influenza doses, which raise it). The per-child expected value is computed from the record, not assumed; this figure is for planning only.
- Confirmatory stratum (non-attributing and artifact-dated) as a fraction of regression completes: approximately 25–30% (assuming ~65% non-attributing, ~40% of those with artifact-dated onset).
- Response to Research Match invitation: 35–40% (SPARK reports response rates up to 60% for online surveys).

Power (one-sample test of observed vs schedule-expected proportion, α = 0.05 two-sided):

| Confirmatory-stratum N | Detectable RR at 80% power (e = 0.015) |
|---|---|
| 400 | ~2.4 |
| 800 | ~1.9 |

Secondary narrative-mention comparison (two-proportion, base 10% vs 15%): 680 per group at 80% power; 10% vs 17%: 368 per group.

**Targets.** 2,000 regression-sample completes (≈ 500–600 in the confirmatory stratum), 700 comparison-sample completes. Requires roughly 5,500 regression-sample invitations and 2,000 comparison invitations at the assumed response. SPARK's regression-reporting proband pool is expected to exceed this; feasibility to be confirmed with the Research Match team by the PI.

Interim look: none for efficacy. A single blinded feasibility check at 25% of target on response rate, upload rate, and coder agreement, with pre-specified stopping only for infeasibility.

## 6. Instrument

Ordering is a design constraint, not a formatting choice. Each section is locked on submission; respondents cannot return to earlier sections.

### 6.1 Unaided narrative (locked before anything else)

> "Think back to when you first noticed a change in [child's name]'s development, or first became concerned. In your own words, tell us what you noticed, when it was, and what was going on in your family's life around that time."

Free text, minimum 50 words, no examples, no prompts. This is the sole item on the page.

### 6.2 Date evidence

- "About how old was [child] when you first noticed the change?" (months; also "not sure")
- "How confident are you in that timing?" (4-point)
- "What is your memory of the timing based on?" (multi-select: memory alone; calendar or diary; photos or videos with dates; text messages, emails, or patient-portal messages; daycare or school notes; a doctor's record; other)
- If photos/videos: "Are you able to find the date of the last video or photo that shows [child] doing the skill that was lost, and the first that shows the change?" (dates, with option to skip). Instructions specify these should be looked up, not recalled.
- "Did you tell anyone about the change at the time? Who, and roughly when?"

### 6.3 Structured onset items

Adapted from ADI-R loss items: skills lost (language, gestures, social engagement, play, motor); duration of loss; pattern (abrupt over days / over weeks / gradual over months); whether skills returned; whether anyone outside the household noticed; age at first professional concern; what the first clinician said; whether the respondent raised concerns that were not acted on; age at diagnosis.

### 6.4 Attribution and hypothesis exposure

Only after §6.1–6.3 are locked.

- "What do you think contributed to [child]'s autism?" (open text first)
- Checklist: genetics/family history; prematurity or birth complications; something during pregnancy; an illness or infection; a vaccine; something in the environment; don't know; other. Multi-select.
- "When did you first hear the idea that vaccines might be connected to autism?" (before child was born; before I noticed the change; around the time I noticed it; after diagnosis; never)
- "Was that before or after you had settled in your own mind on when the change happened?"
- "Where did you first encounter the idea?" (multi-select)

### 6.5 Dated exposures and records

- Upload of the child's official immunization record from the state immunization registry portal or pediatric practice (guidance provided per state). Manual entry accepted only as fallback and flagged.
- "In the months around the change, did any of the following happen, and roughly when?" — febrile illness; antibiotics; ER visit or hospitalization; started daycare; moved house; new sibling; travel; other. Dates or month, with evidence type for each.
- Optional: authorization for SPARK-affiliated site to request immunization record from registry on the family's behalf.

### 6.6 Closing

Demographics not already held by SPARK; consent to 12-month re-contact; resources for families (developmental screening, early intervention). No results, no other parents' responses, and no interpretive content are shown at completion. The SPARK-required participant results summary is delivered after analysis, as aggregate findings only.

### 6.7 Linked enrollment data

With Research Match bidirectional consent: enrollment date; enrollment-era regression items and reported age at loss; developmental milestones; diagnosis age; site of enrollment.

## 7. Outcome definitions

**Primary outcome.** Indicator that the parent-observed onset date falls within days 0–2 inclusive after a vaccinating well visit, where the visit date and vaccination status are taken from the uploaded immunization record, and the onset date is the artifact-anchored date from §6.2 where available, else the §6.2 age in months converted to a date interval (analyzed with interval-censoring, see §8.3).

**Confirmatory stratum.** Respondent did not select "a vaccine" in §6.4 checklist and did not mention vaccines as a cause in the §6.4 open text (coded blind), AND onset date is supported by at least one contemporaneous artifact in §6.2.

**Secondary outcomes.** Spontaneous vaccine mention in §6.1 narrative (blind-coded, binary, with sub-codes for temporal framing); onset within 0–2 and 3–14 days after non-vaccinating well visits; onset within the same windows after each other dated exposure; drift = (age at loss, this survey) − (age at loss, enrollment); evidence quality category.

## 8. Analysis plan

Analysis code is written and frozen by the adversarial co-investigator before data collection closes, against a synthetic dataset matching the instrument. Coding of narratives is completed before the immunization records are merged, and coders never see records or attribution items.

### 8.1 Narrative coding

Two coders blind to all structured data and to study hypotheses beyond "code for events mentioned and their temporal relation to the change." Codebook fixed at pre-registration: events mentioned (vaccination; illness; injury; family event; medical visit without vaccine; none), temporal relation (before / same day / days after / weeks after / unrelated), and pattern language (abrupt / gradual). Cohen's κ reported; disagreements resolved by a third blind coder. A 10% random sample double-coded again at study end to check drift.

### 8.2 Schedule-expected proportion

For each child, from the uploaded record: define the observation window as ages 6–36 months (truncated at survey date for younger children). Identify all vaccinating visit dates. Compute the fraction of window days that fall in each risk window (0–2, 3–14 days) after any vaccinating visit. This is the child's expected probability under the null of no temporal association. The sum across children is the expected count; the observed count is compared by exact binomial test and by a conditional Poisson (self-controlled case series) model with age-in-months as the baseline hazard.

Non-vaccinating well visits (from record: visits with no vaccine administered) and other dated exposures (§6.5) get identical risk windows and identical analysis.

### 8.3 Handling date precision

Artifact-anchored dates: used as point dates. Month-only dates: treated as interval-censored; the analysis integrates the risk-window indicator over the uniform interval, and a sensitivity analysis restricts to point-dated cases. Cases with no date: excluded from timing analysis, retained in narrative analysis; count reported.

### 8.4 Confirmatory test

One test: observed vs schedule-expected count in the 0–2 day post-vaccinating-visit window, in the confirmatory stratum, α = 0.05 two-sided, reported with RR and 95% CI. No other analysis is labeled confirmatory.

### 8.5 Secondary and stratified analyses

Pre-specified, reported in full, hierarchical with no confirmatory claim:

1. Same test in the full regression sample, and in each of the four cells of attribution × evidence quality.
2. Same test for 3–14 day window.
3. Same test after non-vaccinating well visits (M-CHAT visits without vaccination as the key comparison) and after each other exposure.
4. Ratio of ratios: RR after vaccinating visits ÷ RR after non-vaccinating well visits, with CI.
5. Spontaneous-mention rate, by stratum, vs comparison sample.
6. Drift regression: drift on years elapsed, attribution belief, timing of hypothesis exposure, and evidence quality.
7. Pattern language (abrupt vs gradual) by evidence quality and attribution.
8. Concern-to-documentation interval and proportion reporting unacted concerns.

### 8.6 Pre-specified interpretation

The following will be written into the pre-registration so that both investigators are bound to it:

- **Supports H1:** confirmatory test significant with RR ≥ 2; excess present after vaccinating visits and absent (RR CI includes 1) after non-vaccinating M-CHAT visits; excess not substantially larger in attributing than non-attributing stratum.
- **Supports H0:** confirmatory test not significant; any full-sample excess concentrated in attributing and/or memory-dated cells; comparable excess after non-vaccinating M-CHAT visits; drift positive toward vaccination dates with narrative exposure.
- **Mixed / requires prospective follow-up:** confirmatory test significant but excess also present after non-vaccinating M-CHAT visits (visit-prompted noticing cannot be excluded), or significant only in the 3–14 day window.

Either investigator may add to this list before pre-registration; neither may after.

### 8.7 Missing data and sensitivity

Upload rate reported; respondents without records analyzed separately using manual entry, flagged. Multiple imputation not used for exposure dates. Sensitivity analyses: exclude probands with pre-onset genetic diagnosis; exclude respondents who report hearing the vaccine hypothesis before onset; restrict to probands under 6 at survey; restrict to respondents whose narrative was coded "abrupt."

## 9. Bias and limitations, and what is done about each

| Threat | Mechanism | Mitigation | Residual |
|---|---|---|---|
| Cohort selection | SPARK families volunteered for genetic research; likely under-represent vaccine-attributing parents | Stratify by attribution; report attribution prevalence; interpret positive result as conservative | Generalizability of prevalence estimates limited |
| Responder selection | Parents with a timing story more likely to respond | Neutral invitation; comparison sample gets identical materials; response rate by enrollment-era regression status reported | Unknown magnitude within the invited pool |
| Recall reconstruction | Onset dated retrospectively, anchored to salient visits | Unaided narrative first; artifact-anchored dates; confirmatory stratum restricted to artifact-dated cases; drift measured against enrollment data | Artifact dates locate the change, not necessarily its beginning |
| Visit-prompted noticing | M-CHAT at 18 months prompts observation | Non-vaccinating M-CHAT visits (24-month, and 18-month visits where record shows no vaccine) as control | Vaccinating and non-vaccinating visits differ in age; handled by SCCS age baseline |
| Narrative exposure | Timing drifts after hearing hypothesis | Exposure timing item; drift analysis; sensitivity excluding pre-onset exposure | Self-reported exposure timing is itself recalled |
| Record incompleteness | Registry records may miss doses given elsewhere | Flag records with gaps; sensitivity analysis on complete records only | Missed vaccinating visits bias expected proportion downward, i.e. toward H1 |
| Resolution | 0–2 day window is narrow; power depends on stratum size | Sample target set for the stratum; 3–14 day secondary window | Effects with RR < 2 in the narrow window not detectable |
| Regression vs. noticing | "Onset" is when the parent noticed, not when the process began | Stated explicitly; prospective companion study (§13) addresses it | Unavoidable in retrospective design |

## 10. Ethics

IRB review at the PI's institution. Consent describes the study as research on how parents first notice and remember developmental change, including what was happening around that time, and states that the study will look at medical events including illnesses and immunizations in the child's record; the specific hypotheses are not disclosed pre-completion, and the consent explains why (to avoid influencing recall) with full disclosure at results-return. Respondents who report distress are routed to resources. No individual-level causal interpretation is returned to any family. Immunization records stored under the PI's institutional data security plan and destroyed per IRB schedule. Participant results summary provided to SPARK as required.

## 11. Governance and conflict of interest

- Pre-registration on OSF with the full analysis plan, codebook, and §8.6 interpretations, before any invitation is sent.
- Registered Report submission; data collection begins only after in-principle acceptance.
- The adversarial co-investigator owns the analysis code, runs the primary analysis, and has authority to halt release for protocol deviation. The PI owns data collection and participant contact.
- Funding is provided as an unrestricted gift to the PI's institution. The funder has no access to raw data, no role in analysis, and no approval over the manuscript. Funder identity and the funder's publicly stated views on the study question are disclosed in the pre-registration and the manuscript.
- All investigators commit in writing to publication of the results regardless of direction, and to release of a de-identified analytic dataset and code with the paper, subject to SPARK data-use terms.
- Any deviation from the pre-registered plan is documented and reported as such.

## 12. Timeline and budget (planning figures)

| Phase | Duration |
|---|---|
| Protocol finalization with adversarial co-I; codebook; synthetic-data code freeze | 8 weeks |
| Pre-registration; Registered Report submission and review | 12–16 weeks |
| IRB; SPARK Research Match application and Participant Access Committee | parallel, 8–12 weeks |
| Field period | 8 weeks |
| Narrative coding (blind) | 6 weeks |
| Record processing and analysis | 8 weeks |
| Manuscript | 6 weeks |
| Optional 12-month re-contact | +12 months |

Budget lines: participant incentives (SPARK convention, ~2,700 completes); coder salaries; data management and record-abstraction staff; statistician effort; PI and co-I effort; translation; OSF/journal fees. Order of magnitude: low-to-mid six figures. To be costed by the PI's institution.

## 13. Companion prospective study (separate protocol)

The retrospective design cannot observe onset in real time. A companion study recruits parents at the moment of concern via search advertising on pre-theory queries ("toddler stopped saying words," "stopped responding to name"), collects the same unaided week-before narrative with a control arm on unrelated toddler-symptom queries, and re-contacts at 12 months to measure reconstruction within subjects. It is referenced here so that the two studies use identical narrative items and codebook, allowing direct comparison of contemporaneous and retrospective accounts.

## 14. Items for adversarial review

The co-investigator is asked to specify, before pre-registration:

1. Any additional control exposure or window without which a positive result would be unconvincing.
2. The RR threshold and window definition for §8.6, if different from those proposed.
3. Whether the confirmatory stratum should additionally exclude respondents reporting any pre-onset exposure to the vaccine hypothesis.
4. Whether the 24-month visit is an acceptable non-vaccinating M-CHAT control given the age difference, or whether within-visit comparison (18-month visits with vs. without vaccination per record) should be primary.
5. Any element of the instrument order or wording that, in the co-investigator's judgment, primes the outcome.

---

*Appendix A (to follow): full item text and response options. Appendix B: narrative codebook. Appendix C: state-by-state immunization record retrieval instructions. Appendix D: SPARK Research Match application draft.*
