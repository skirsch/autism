# Temporal Relationship Between Vaccination and Sudden-Onset Regressive Autism (SORA)

## Executive summary
| **Item** | **Description** |
|----|----|
| Principal Investigator | Elizabeth “Liz” Mumper, M.D. \[confirm degree/title and institutional affiliation\] |
| Sponsor / coordinating organization | Medical Academy of Pediatric Special Needs (MAPS) \[confirm legal entity\] |
| Protocol number / version / date | \[IRB assigned\] / Version 1.0 / 11 August 2026 |
| Study design | Retrospective, multisite medical-record review; minimal-risk secondary research |
| Requested determination | Exempt under 45 CFR 46.104(d)(4)(ii) |
| Study population | Children with documented ASD and narrowly defined abrupt, parent-observed developmental regression |

DRAFTING NOTE. Bracketed text requires completion by the PI, relying
institution, privacy officer, or reviewing IRB. The reviewing IRB—not
the investigators—determines whether the activity is non-human-subjects
research, exempt, or requires expedited review. Public release is not
permitted until disclosure-risk review is completed.

# Part 1. Full Research Protocol

## 1. Protocol synopsis

This exploratory study will test whether the parent-observed onset of
narrowly defined sudden-onset regressive autism (SORA) clusters
temporally after vaccination. Participating clinics will identify
eligible records and derive a minimal analytic dataset locally.
Investigators receive only a nonidentifying site code, a clinic-assigned
row ID, sex, age at onset in completed months, days from the preceding
vaccination to onset (Dpre), and days from onset to the subsequent
vaccination (Dpost).
Investigators will not receive clinical phenotypes, names, contact
information, dates of birth, medical-record numbers, calendar dates,
free text, geography, clinic names, or the clinic’s re-identification key. The study
is designed to describe timing; it cannot establish that vaccination
caused regression.

## 2. Background and rationale

Developmental regression is reported in a substantial minority of
children with autism spectrum disorder (ASD), but definitions,
ascertainment methods, and estimated onset ages vary. A 2021 systematic
review of 97 studies estimated a pooled regression prevalence of 30% and
a weighted mean onset age of 19.8 months, with substantial
heterogeneity. Reviews comparing retrospective parent report with
prospective observation caution that precise onset dating is vulnerable
to recall error and that developmental change may be gradual even when
recognized abruptly.

Large cohort and meta-analytic studies have not found an association
between vaccination and autism overall, and several studies specifically
examining regression or onset pattern have not supported an MMR-related
regressive phenotype. The present study therefore does not treat a
causal association as established. Its narrower question is whether a
highly selected subgroup with a documented, abrupt, readily dated
parent-observed onset shows nonrandom temporal positioning between
adjacent vaccination encounters. This question is scientifically
testable, but selection, recall, documentation, diagnostic, and
time-varying confounding must be addressed explicitly.

The scientific value is methodological: to determine whether
clinic-derived timing data are sufficiently reliable and whether any
temporal clustering persists under prespecified,
exposure-opportunity-adjusted analyses. A positive result would be
hypothesis-generating and would require independent confirmation in
population-based records with prospectively recorded developmental
measures. A null result would constrain the magnitude of short-window
clustering in this selected phenotype.

## 3. Specific aims and hypotheses

1.  Aim 1: Test whether onset timing is distributed uniformly within the
    interval between adjacent vaccinations or is disproportionately
    concentrated near the preceding vaccination. Primary normalized
    measure: U = Dpre / (Dpre + Dpost). Under the primary null model,
    onset is uniformly distributed within each observed interval and U
    follows Uniform(0,1).

2.  Aim 2: Estimate and compare prespecified short-window
    concentrations, especially Dpre = 0–2 days and Dpre = 0–7 days,
    against their child-specific null expectations. These windows
    provide interpretable effect estimates without defining the study’s
    success by one arbitrary cutoff.

3.  Aim 3: Describe timing patterns by age at onset and sex, and assess
    robustness to same-day coding, interval length, alternative risk
    windows, and other sensitivity analyses supported by the six
    received variables.

No confirmatory causal hypothesis is proposed. All language in reports
will distinguish temporal association from causation.

## 4. Study design and setting

Retrospective, multisite clinical case series using existing medical
records. Clinic personnel will screen records, verify eligibility,
abstract source dates, calculate intervals locally, remove identifiers,
and transmit only the approved dataset. The coordinating team will not
contact patients and will not access clinic electronic medical records
or linkage keys. The study will enroll at least 300 eligible records in
total from at least five participating clinics. Each clinic will
contribute all eligible records identified during its prespecified
ascertainment period. No fixed number is required from an individual
clinic, and enrollment will not be stopped or extended based on observed
timing results. The final minimum sample-size requirement will be
confirmed through simulation by the study statistician before data
collection begins.

## 5. Operational definition of SORA

A record qualifies only when all criteria below are documented. “Sudden
onset” means a parent or primary caregiver identified a specific
calendar date, or an interval no longer than 48 hours, when persistent
new ASD-relevant behaviors or a marked loss of previously acquired
developmental skills first became obvious. Examples may include new
persistent head banging or other repetitive behavior, loss of eye
contact or reciprocal social engagement, or marked loss of language or
another acquired skill. Transient post-vaccination symptoms alone
(fever, irritability, sleep change, reduced appetite) do not constitute
regression.

## 6. Eligibility criteria

### Inclusion

- Age 0–60 months at the documented onset.

- Subsequent ASD diagnosis documented by a qualified clinician using the
  clinic’s standard diagnostic process; diagnostic method recorded when
  available.

- Documentation that development before onset was described as typical
  or meeting expected milestones, with no persistent ASD-specific
  concern recorded before the index onset.

- A parent/caregiver-reported onset date or ≤48-hour onset interval for
  a persistent change meeting the SORA definition.

- A verifiable vaccination date before onset and a verifiable
  vaccination date after onset in the source record. If no later
  vaccination exists, retain for descriptive analysis but exclude from
  normalized-position analysis.

- Record falls within the clinic’s prespecified ascertainment period:
  \[start year\] through \[end year\].

### Exclusion

- Documented genetic, neurologic, metabolic, infectious, traumatic, or
  other condition judged to explain regression (examples: Rett syndrome,
  Fragile X syndrome, epileptic encephalopathy), unless retained in a
  prespecified sensitivity stratum.

- Developmental or ASD-specific concern documented before the proposed
  onset date.

- Gradual, uncertain, or retrospectively approximated onset exceeding 48
  hours; these may be logged as screen failures or analyzed separately,
  not included in the primary cohort.

- Onset defined only by nonspecific acute symptoms without persistent
  developmental/behavioral change.

- Conflicting dates that cannot be resolved by the site adjudicator, or
  missing required timing data.

## 7. Identification, screening, and adjudication

4.  Each site defines the full source population and ascertainment dates
    before screening. Searches may use ASD diagnosis codes and terms
    indicating regression or skill loss.

5.  Site staff create a screening log containing aggregate counts only:
    records screened, excluded by each criterion, eligible, and missing
    timing data.

6.  Two trained site reviewers independently assess eligibility where
    feasible. Disagreements are resolved by a third clinician without
    considering calculated Dpre or Dpost. Eligibility details are not
    transmitted.

7.  Onset is taken from the earliest parent/caregiver report documented
    in the record that supports an unambiguous onset date under the
    protocol. The source date and narrative remain at the clinic.

8.  Vaccination dates must reflect administration, not ordering,
    billing, recommendation, or a generic well-child visit. Combination
    products and simultaneous vaccines count as one vaccination date;
    product/antigen fields are optional secondary variables.

9.  The site calculates Dpre and Dpost only after eligibility is locked.
    Negative values are invalid. Same-day administration and onset are
    coded Dpre=0, with time ordering recorded only if contemporaneously
    documented.

## 8. Variables and data collection

| **Variable** | **Definition / coding** | **Status** |
|----|----|----|
| Site code | Nonidentifying code assigned for analysis; clinic-name mapping is restricted | Required internally; recoded or removed before public release |
| Clinic row ID | Arbitrary sequential or random code; not derived from identifiers; mapping retained only by clinic | Required; replaced before public release |
| Age at onset | Completed months at onset; public release may bin to protect privacy | Required |
| Sex | Clinic-recorded value using prespecified categories; suppress small cells publicly | Required |
| Dpre | Calendar days: onset minus most recent administered vaccination before/on onset | Required |
| Dpost | Calendar days: first administered vaccination after onset minus onset | Required for primary normalized analysis |

The three temporal data points supplied for each qualifying child are
age at onset, Dpre, and Dpost. Sex is the sole demographic variable. No
calendar dates, phenotype variables, clinical narratives, vaccine
products, clinic names, or eligibility details leave the clinic. The
nonidentifying site code is retained internally only to support
site-aware analyses.

## 9. Statistical analysis plan

### 9.1 Analysis populations

- Primary analysis set: all eligible records with exact or ≤48-hour
  onset and valid vaccination dates on both sides of onset.

- Descriptive set: all eligible records, including those lacking a
  subsequent vaccination.

- Sensitivity sets available from the received variables: intervals
  ≤\[365\] days, exclusion of same-day cases when ordering is unknown,
  site-stratified results, and leave-one-site-out analyses.

### 9.2 Primary estimands and tests

For child i, let aᵢ=Dpre, bᵢ=Dpost, Lᵢ=aᵢ+bᵢ, and Uᵢ=aᵢ/Lᵢ. The primary
analysis evaluates whether U is Uniform(0,1) using a prespecified
one-sample Cramér–von Mises statistic with a Monte Carlo conditional
randomization distribution generated within each observed interval Lᵢ.
The primary directional contrast will test excess concentration near the
preceding vaccination using a prespecified statistic such as mean
−log\[max(U,ε)\]. The empirical cumulative distribution and histogram of
Dpre and U will be reported regardless of statistical significance.

The 0–2-day and 0–7-day windows are prespecified key secondary
estimands. For a window 0–w, the null probability for child i is
min((w+1)/Lᵢ,1) when eligible discrete onset days are 0,…,Lᵢ−1;
conventions will be fixed before database lock. Each observed count will
be compared with its Poisson-binomial null distribution. Report observed
and expected proportions, risk ratios, risk differences, 95% confidence
intervals, and multiplicity-adjusted p values. Holm correction will
control family-wise α=0.05 across the primary omnibus/directional test
family and the two key windows, as finalized by the statistician before
database lock.

### 9.3 Secondary and exploratory analyses

- Risk windows 0–1, 0–2, 0–7, 8–14, and 15–30 days, with exact
  exposure-opportunity denominators. The 0–2 and 0–7 windows are key
  secondary; the remaining windows are exploratory.

- Empirical cumulative distribution, histogram, and kernel density
  (descriptive only). A prespecified moving-window scan will evaluate
  every contiguous window of width 1–7 days whose endpoints fall within
  days 0–30 (for example, days 2–4). The test statistic will be the
  largest standardized observed-minus-expected excess across all scanned
  windows. Its p value and simultaneous uncertainty will be obtained
  from the conditional randomization distribution of that maximum
  statistic, thereby accounting for searching across window locations
  and widths. The window with the largest excess will be reported as
  data-adaptive and not as an independently prespecified effect.

- Stratification by age band and sex when cell sizes permit. No subgroup
  causal claims.

- Site-stratified estimates, leave-one-site-out analyses, and a
  site-level random effect or other cluster-robust method selected by the
  statistician. No single clinic will be described as an independent
  replication unless its sample size and prespecified analysis support
  that characterization.

- Sensitivity to heaping at 0, 1, 7, 14, and 30 days; interval-censored
  onset; alternative handling of simultaneous onset/vaccination; and
  exclusion of long inter-vaccination intervals.

- Negative-control assessment, if available, using timing from onset to
  non-vaccine routine visits or vaccination dates after onset. Such
  analyses require an amended instrument and analysis plan before
  database lock.

### 9.4 Missing data, exclusions, and multiplicity

Missing required dates will not be imputed for the primary analysis.
Counts and reasons for missingness will be reported by clinic. No record
will be excluded based on the magnitude or direction of Dpre/Dpost after
eligibility is determined. All deviations, exclusions, and analytic
decisions will be logged before unblinding aggregate results.
Exploratory p values will be labeled unadjusted or adjusted as
applicable.

### 9.5 Sample size

The study will target at least 300 eligible records from at least five
clinics. The final sample-size calculation must be completed by the
study statistician using the anticipated Lᵢ distribution, conservative
effect sizes, unequal site contributions, within-site dependence, the
primary distributional test, and multiplicity from the moving-window
scan. The simulation and its assumptions will be finalized before data
collection and will not use observed study outcomes to stop or extend
enrollment.

### 9.6 Interpretation limits

This case-only design cannot estimate ASD incidence or
vaccine-attributable risk, compare vaccinated with unvaccinated
children, or by itself distinguish a causal trigger from recall
anchoring, healthcare-contact patterns, concurrent illness, age-related
developmental change, or selective documentation. Conclusions will be
limited to the observed temporal distribution in the defined cohort.

## 10. Risks, benefits, and safeguards

There is no intervention and no direct participant benefit. Principal
risk is informational: re-identification or unwanted disclosure of a
child’s developmental and vaccination history. Risk is minimized by
site-level abstraction; no central access to PHI; no direct identifiers,
exact dates, free text, or MRN-derived codes; encrypted transfer and
storage; least-privilege access; audit logging;
suppression/generalization for public release; and incident-response
procedures. Clinics will not make participation or care decisions based
on study inclusion.

## 11. Quality assurance and reproducibility

- Training manual and worked examples for onset and vaccination-date
  abstraction.

- Pilot abstraction of at least 10 records per site and inter-rater
  agreement reporting.

- Frozen protocol, data dictionary, and statistical code before database
  lock.

- Aggregate screening flow by site and a reproducible analysis
  repository.

- Independent statistical review before public claims or manuscript
  submission.

## 12. Dissemination

Results will be reported regardless of direction. Public release is
limited to a disclosure-reviewed public-use dataset and analysis code.
The internal analytic dataset will not automatically be public. Cell
suppression, age binning, top/bottom coding of intervals, clinic masking
or pooling, and removal of rare combinations will be applied as needed.
If Safe Harbor cannot be established because a retained variable is a
unique characteristic or code, a qualified expert determination will be
obtained before release. Neither MAPS nor investigators will attempt
re-identification.

# Part 2. Data Privacy and Security Plan

## 1. Data flow

10. Authorized clinic workforce members access PHI inside the clinic
    under local policy and the IRB/privacy determination.

11. Clinic staff determine eligibility, record source dates in a local
    worksheet, calculate age in months, Dpre, and Dpost, and run
    validation checks.

12. Before transmission, clinic staff delete direct identifiers, exact
    dates, free text, granular geography, contact data, device/IP data,
    and any MRN-derived identifier. A random study ID is assigned. The
    linkage key remains at the clinic and is never shared.

13. The clinic submits the data electronically as the study-provided
    Excel workbook or an equivalent CSV file through \[approved secure
    upload portal\]. Paper forms, scanned forms, photographs, fax, and
    submission in an email body are not accepted. The electronic table
    contains only site code, clinic row ID, sex, age at onset in months,
    Dpre, and Dpost.

14. The coordinating center stores the internal analytic file in \[named
    institution-managed encrypted platform\], encrypted in transit and
    at rest, with multifactor authentication, role-based access, audit
    logging, endpoint encryption, and institutional backups.

15. Before public release, the received clinic row IDs are replaced with
    new public row numbers. The clinic-issued codes and mapping keys are
    not published.

## 2. Data classification and HIPAA pathway

The clinic’s source records and local mapping file contain PHI. The
transferred file contains no calendar dates or clinical phenotype
information and is intended to satisfy HIPAA de-identification. The
clinic-generated row ID must not be derived from a name, medical-record
number, date, or other identifying information, and the
re-identification mechanism must not be disclosed. Each clinic’s covered
entity/privacy officer will document the applicable de-identification
determination before transfer. If a clinic instead classifies the file
as coded PHI or a limited data set, the appropriate HIPAA
authorization/waiver and data use agreement must be in place before
disclosure.

## 3. Access matrix

| **Role** | **Source PHI** | **Mapping key** | **Received analytic data** | **Public-use data** |
|----|----|----|----|----|
| Clinic abstractor | Yes, locally | If authorized | Local/transmit | Yes |
| Clinic PI/privacy officer | As authorized | Yes | Yes | Yes |
| Coordinating PI / statistician | No | No | Yes | Yes |
| Other MAPS personnel | No | No | Only if named/authorized | Yes |
| Public | No | No | No | Yes after review |

## 4. Retention and destruction

The clinic retains its mapping key under clinic policy and never shares
it with investigators. The received analytic dataset, audit logs, code,
and regulatory records will be retained for \[institutional requirement,
commonly at least 3–7 years after study closure/publication\]. Before
public release, clinic row IDs are replaced with new public row numbers.
Public-use data cannot be recalled after publication, making pre-release
review mandatory.

## 5. Incident response

Suspected loss, unauthorized access, or disclosure will be reported
immediately to the PI and \[privacy/security office\]. Access will be
suspended, logs preserved, scope assessed, and required institutional,
IRB, HIPAA, contractual, and participant notifications completed within
applicable timelines. Corrective actions will be documented.

# Part 3. Request for Waiver of Consent and HIPAA Authorization

## A. Requested regulatory determination

Primary request: the IRB determine whether receipt and analysis of
information that investigators cannot readily link to individuals is not
human-subjects research or is exempt secondary research under 45 CFR
46.104(d)(4), as applicable. In the alternative, the investigators
request expedited review and waiver of parental permission/informed
consent under 45 CFR 46.116(f), plus waiver of HIPAA authorization under
45 CFR 164.512(i), if the transferred information is deemed PHI. These
are alternative pathways; the IRB/privacy office will select the
applicable pathway.

## B. Waiver of informed consent / parental permission justification

| **Criterion** | **Justification** |
|----|----|
| No more than minimal risk | No intervention or contact occurs. The only foreseeable research risk is informational and is reduced by clinic-side abstraction, minimal variables, removal of identifiers/dates/free text, restricted access, encryption, and disclosure review. |
| Rights and welfare not adversely affected | Clinical care, benefits, and legal rights are unchanged. Findings are aggregate; investigators cannot identify or contact families. |
| Impracticable without waiver | Eligible cases span historical records and multiple clinics; contact information may be stale, and requiring contact would produce substantial nonresponse and selection bias that defeats a valid complete-record review. “Impracticable” is based on scientific feasibility, not convenience or cost alone. |
| Additional information after participation | Individual debriefing is not appropriate because investigators cannot identify participants. Aggregate results and the public-use dataset/code will be posted at \[URL\] when available. |
| Identifiable format necessity (if applicable) | Clinic staff must temporarily inspect identifiable records to determine eligibility and derive intervals. Central investigators do not require or receive identifiers. |

## C. HIPAA waiver justification (if needed)

- Privacy risk is minimal because identifiers stay at the clinic; access
  is limited; transfer/storage are encrypted; and written assurances
  prohibit reuse, disclosure, and re-identification except as required
  by law or oversight.

- Identifiers used locally for screening will be destroyed or retained
  only under documented clinical/legal requirements at the earliest
  practicable time.

- The research cannot practicably be conducted without local access to
  PHI because eligibility and exact temporal intervals must be derived
  from source records.

- The research cannot practicably be conducted without the waiver
  because obtaining authorization from a historical multisite cohort
  would materially bias ascertainment and make complete-case screening
  infeasible.

- Only the minimum necessary PHI is accessed locally; no PHI is
  disclosed centrally unless separately approved.

# Part 4. Data Collection Instrument

This is an electronic data table, not a paper case-report form. The
clinic must enter one eligible patient per row in the study-provided
Excel workbook or an equivalent CSV file and upload the completed file
through the approved secure portal. Do not print, handwrite, scan,
photograph, fax, or paste the data into an email. Do not transmit exact
dates or free text. Keep the source-date worksheet and re-identification
key at the clinic.

| **Site code** | **Clinic row ID** | **Sex** | **Age at onset (months)** | **Dpre: days vaccination→onset** | **Dpost: days onset→next vaccination** |
|----|----|----|----|----|----|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Definitions: Dpre = onset date minus the most recent administered
vaccination date before/on onset. Dpost = first administered vaccination
date after onset minus onset date. Use 0 for same-day onset; mark
ordering unknown unless the note documents order. Do not substitute a
routine visit date for a vaccination date. Enter NA only when no
subsequent vaccination exists; explain only in the clinic-retained query
log.

| **Site-level screening summary**             | **Count** |
|----------------------------------------------|-----------|
| Unique records screened                      |           |
| Eligible SORA records                        |           |
| Excluded: onset not abrupt/dateable          |           |
| Excluded: prior developmental concern        |           |
| Excluded: alternative explanatory condition  |           |
| Excluded: missing/invalid vaccination timing |           |
| Other exclusions (per protocol)              |           |

Site certification: I certify that the transmitted file contains only
the six columns shown above. The site code is the approved
nonidentifying study code, and the clinic row ID is not derived from an
identifier. No clinic name, names, calendar dates, phenotype
information, free text, MRNs or MRN-derived codes, contact information,
or mapping key are included. Name/title: \_\_\_\_\_\_\_\_\_\_ Signature:
\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_

# Part 5. Conflict of Interest and Funding Disclosure

## Investigator disclosure statement

Each investigator and key study staff member must disclose financial and
nonfinancial interests under the reviewing institution’s policy.
Complete the statements below; do not represent “none” until each person
has submitted the institution’s required disclosure.

| **Disclosure item** | **Response / management** |
|----|----|
| Study funding and in-kind support | MAPS: \[amount/source/terms\]. Clinic compensation: up to $5,000 per clinic based on documented staff effort and record volume \[confirm structure\]. Other support: \[list/none\]. |
| PI and investigator financial interests | \[Consulting, equity, honoraria, patents, paid advocacy, litigation roles, or none after formal disclosure\]. |
| Nonfinancial interests | \[Public positions, organizational leadership, advocacy, prior public claims, or other interests reasonably perceived to affect objectivity\]. |
| Site interests | \[Recruitment/data-abstraction payments; confirm payment is for reasonable costs and is not contingent on eligible-case count or study outcome\]. |
| Management plan | Independent eligibility adjudication where feasible; blinded timing calculation until eligibility lock; prespecified analysis; independent statistician; full reporting; funding and interests disclosed in publications. \[Add institutional COI committee requirements\]. |

## Suggested publication disclosure

“This study was supported by \[full legal funder name and grant/contract
number\]. Participating sites received reimbursement for reasonable
data-abstraction costs under agreements not contingent on the number or
timing distribution of eligible cases. The funder’s roles in study
design, data collection, analysis, interpretation, manuscript
preparation, and publication decision were: \[state each role\]. Author
disclosures: \[insert\].”

# Part 6. Required Site and Submission Attachments

- Completed institution-specific IRB application and protocol signature
  page.

- PI CV/biosketch, human-subjects and HIPAA training certificates, and
  investigator roster.

- Statistical simulation/power appendix approved by a named
  statistician.

- Data dictionary, abstraction manual, and validation rules.

- Site agreement/data use agreement or reliance agreement, as
  applicable.

- Clinic payment schedule and budget justification showing reimbursement
  is not outcome-contingent.

- Recruitment/site outreach email and phone script labeled “do not use
  until IRB determination.”

- HIPAA de-identification attestation or Expert Determination
  documentation for each data flow.

- Public data disclosure-risk review plan and repository terms.

- Conflict-of-interest forms and management plan, if required.

# References

1. Tan C, Frewer V, Cox G, Williams K, Ure A. Prevalence and Age of
    Onset of Regression in Children with Autism Spectrum Disorder: A
    Systematic Review and Meta-analytical Update. Autism Research.
    2021;14(3):582–598. doi:10.1002/aur.2463.

2. Ozonoff S, et al. Changing conceptualizations of regression: What
    prospective studies reveal about the onset of autism spectrum
    disorder. Neuroscience & Biobehavioral Reviews. 2019. PMID:
    30885812.

3. Taylor LE, Swerdfeger AL, Eslick GD. Vaccines are not associated
    with autism: an evidence-based meta-analysis of case-control and
    cohort studies. Vaccine. 2014;32(29):3623–3629.
    doi:10.1016/j.vaccine.2014.04.085.

4. Hviid A, Hansen JV, Frisch M, Melbye M. Measles, Mumps, Rubella
    Vaccination and Autism: A Nationwide Cohort Study. Ann Intern Med.
    2019;170(8):513–520. doi:10.7326/M18-2101.

5. Taylor B, et al. Measles, mumps, and rubella vaccination and bowel
    problems or developmental regression in children with autism:
    population study. BMJ. 2002;324:393–396. PMID: 11850369.

6. U.S. Department of Health and Human Services, Office for Civil
    Rights. Guidance Regarding Methods for De-identification of
    Protected Health Information under the HIPAA Privacy Rule.

7. U.S. Department of Health and Human Services, Office for Human
    Research Protections. 45 CFR part 46; guidance on coded private
    information and waiver/alteration of informed consent.
