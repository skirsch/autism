# CHD Multisite SORA Parent-Survey Data-Resource Study

## Executive Summary and Study Definition

**Document status:** Planning summary for development of the IRB submission packet  
**Version:** 0.35
**Date:** 13 August 2026

1. Sponsor is CHD. PI is Brian Hooker.
2. We enroll between 4 and 10 large autism diagnosis/treatment clinics.
3. Each clinic emails every contactable parent or guardian in its defined patient population a link to the survey. We never receive the clinic's mailing list.
4. The parent fills out the survey.
5. We will publish a disclosure-reviewed record-level public-use dataset, or protected
   aggregate and controlled-access data if row-level public release is
   not safe.
6. The data produced by this study can be analyzed by third parties to evaluate whether the observed temporal pattern is consistent with a prespecified null hypothesis, while accounting for the study's voluntary-response, parent-report, missingness, and measurement limitations.

## 1. Study identity

| Item | Proposed specification |
|---|---|
| Working title | Multisite Parent-Reported Data Resource of Sudden-Onset Regressive Autism (SORA) |
| Coordinating principal investigator | Brian Hooker, Ph.D. [confirm exact degrees, title, and CHD affiliation]; has accepted this role |
| Sponsor/coordinating organization | Children's Health Defense (CHD) [confirm legal entity]; has accepted this role |
| Participating clinics | Target of 4–10 activated clinics; initial 30-calendar-day enrollment period with a prospectively defined automatic extension, if needed, until the fourth clinic activates or Day 90, whichever occurs first |
| Clinic capacity requirement | The clinic must have at least 500 unique patients with a documented ASD diagnosis, but invitations go to every contactable parent or guardian in the clinic's broader defined patient population, including families whose children were evaluated but not diagnosed with ASD |
| Study type | Minimal-risk, multisite, clinic-distributed, parent-completed coded electronic survey with an embedded record-validation substudy |
| Primary purpose | Create, quality-check, document, and release a coded and disclosure-reviewed parent-reported dataset for subsequent independent analysis |
| Initial publication | Recruitment, cohort, missingness, data-quality, and descriptive report—not a causal analysis |
| Proposed subject characterization | Adult parents/legal guardians and the children about whom identifiable, linkable health information may be collected; final characterization and Subpart D findings are subject to IPAK-EDU IRB determination |
| Child contact | None |
| Intervention | None |
| Requested regulatory pathway | **Minimal-risk expedited IRB review under 45 CFR 46.110**, using applicable expedited Category 7 for the parent survey and Category 5 for validation of records collected for nonresearch purposes, as finally determined by IPAK-EDU IRB. The study is **not requesting exempt status as its primary pathway**. Request adult informed consent, parental permission, a waiver of signed documentation under 45 CFR 46.117(c) if approved, a minimal-risk finding for the child under 45 CFR 46.404, and an IRB determination under 45 CFR 46.408(a) that child assent is not required or may be waived because children are not contacted or asked to perform research procedures. Obtain separate authorization before validation records are uploaded or requested; request a HIPAA waiver only if a covered-entity use or disclosure without authorization is later proposed. |
| Reviewing IRB | IPAK-EDU IRB ([IPAK Institutional Review Board website](https://ipak-institutional-review-board.yolasite.com/)) |

This design replaces clinic-wide chart abstraction. Clinics distribute a
neutral, IRB-approved invitation but do not provide CHD with their
patient mailing lists. Parents provide survey information directly,
including an email stored separately from research responses. A randomly
selected, separately authorized validation subset may provide or permit
secure retrieval of limited vaccination and contemporaneous-onset
records.

## 2. Key personnel and access

Credentials, training, and conflict-of-interest disclosures will be
confirmed before IRB submission.

| Role | Person | Responsibility | Permitted access |
|---|---|---|---|
| Coordinating principal investigator | Brian Hooker, Ph.D. [confirm exact degrees, title, and CHD affiliation] | Protocol compliance, clinic activation, IRB reporting, survey and validation oversight, and release authorization | Clinic identities, coded research data after the applicable lock, aggregate recruitment metrics, validation reports, and audit records; no routine contact-table access |
| Clinic outreach and activation | Ben Jackson; Mila Radetich | Clinic recruitment, activation queue, agreements, and campaign completion tracking | Clinic contacts, agreements, and aggregate campaign metrics; no individual survey responses |
| Data management and quality monitoring | Karl Jablonowski; Steve Kirsch | Prespecified mechanical validation, missingness monitoring, version control, and data-quality reporting | Before lock, only the minimum response fields or blinded technical reports required for mechanical quality control; no substantive timing distributions |
| Contact/validation coordinator | TBD | Manage secure contact, random validation invitations, authorizations, record receipt, and participant questions | Contact table and validation workspace; no analytic timing distributions |
| CHD data custodian | TBD | Approved survey/storage environment, access control, separation of contact/research/validation stores, retention, and incident response | Privileged system access under documented controls; no routine content access |

Access will follow least-privilege rules. The study will create a
restricted contact table linking required parent email to a random
`survey_id`, but it will be technically and administratively segregated
from the coded research table. Clinics will not know which individual
recipients respond, and CHD will not receive clinic recipient lists.
Routine mapping access is limited to the contact/validation coordinator
and data custodian. All joins, exports, and privileged access will be
purpose-limited, logged, and periodically reviewed.

## 3. Study objective and scope

The study will create a multisite resource describing age at
parent-recognized SORA onset, the abrupt changes observed, and temporal
proximity to vaccination among voluntary parent respondents whose
children have a clinical ASD diagnosis.

### Scientific rationale and measurement gap

The relevant unresolved question is narrower than whether vaccination is
associated with ASD as a broad diagnostic category. It is whether a
specifically defined, abrupt, parent-recognized regressive presentation
has a reproducible temporal distribution in relation to vaccination.
Studies addressing vaccination and autism or regression have generally
used vaccination receipt, age-at-vaccination thresholds, mean intervals,
or post-vaccination windows measured in months. Examples include analyses
of regression in relation to MMR using mean intervals or multi-month risk
windows and a large parent study comparing vaccine receipt across broad
ASD-onset patterns. These designs address important questions but do not
resolve whether a narrowly defined SORA onset clusters within individual
days after vaccination.

The targeted literature review conducted during protocol development has
not identified a population-based study that combines all of the present
study's proposed measurement features:

- a discrete SORA Day 0 distinguished from gradual change;
- directional sub-24-hour and individual-day vaccination proximity;
- exact and ranged intervals retained separately;
- explicit measurement of elapsed recall time, information source,
  confidence, and whether vaccination served as the timing anchor;
- evidence-tiered and blinded assessment of available onset support; and
- random record validation of vaccination timing with transparent
  accounting for refusal, failed retrieval, and disagreement.

This measurement gap is the principal scientific justification for the
study. A strong concentration, a diffuse distribution, or absence of a
concentration would each add information because the question has not
been measured using this phenotype definition and level of temporal and
measurement-quality resolution. The initial study will not claim that
temporal concentration proves causation. It will determine whether a
precisely measured signal exists, quantify its robustness to recall and
validation characteristics, and provide the definitions, feasibility
estimates, and open methods needed for independent replication and a
later population-based causal-inference study.

The full protocol will support this rationale with a reproducible search
strategy and literature table. Until that review is complete, the packet
will use "we have not identified" rather than an absolute claim that no
such study has ever been performed.

### How the design addresses selection and reporting bias

No voluntary survey can eliminate selection bias. This study will reduce,
measure, and disclose it through complementary controls rather than claim
that any one subgroup is an unbiased control:

- every participating clinic distributes the same neutral invitation to
  its complete defined contactable parent/guardian population, rather
  than selecting families by ASD diagnosis, suspected regression,
  vaccination history, or beliefs;
- clinic compensation is flat and independent of response count, SORA
  yield, timing, or results;
- clinic-level delivery, landing-page, Start, consent, completion,
  breakoff, missingness, and reminder metrics characterize the recruitment
  funnel without revealing preliminary outcome distributions;
- the consent page discloses vaccination timing before enrollment, while
  the primary onset reconstruction is completed before detailed
  vaccination questions to reduce question-order cueing;
- after primary timing questions, the survey measures the parent's
  pre-survey causal attribution, whether vaccination anchored the recalled
  onset, and whether vaccination continued or the plan changed after
  onset;
- timing results will be reported for prespecified attribution, anchor,
  subsequent-vaccination, recall-horizon, information-source, and
  evidence-quality strata, with denominators and uncertainty intervals;
- random record validation, primary blinded onset review, and a secondary
  unblinded comparison assess reporting and adjudication error; and
- independent replication under different sponsorship and recruitment
  conditions is required to evaluate sponsor- and volunteer-selection
  effects.

Prior belief and post-onset vaccination decisions may themselves result
from the experienced timing and therefore are not exchangeable control
groups. Stratification can show whether a pattern is confined to prior
vaccine attributors or families who subsequently changed vaccination,
but it cannot make nonresponse irrelevant or establish causation. The
study will report this residual selection limitation explicitly.

The prespecified interpretation will be:

> Similar timing distributions across prior-attribution, onset-anchor,
> subsequent-vaccination, recall-source, and evidence-quality groups would
> reduce concern that an observed pattern is attributable solely to
> pre-existing vaccine attribution or differential reporting. Recipients
> who never select Start are not exposed to the detailed questions or the
> full vaccination-timing disclosure, although their underlying outcomes
> remain unknown. These findings would make selection-based explanations
> less sufficient but would not eliminate nonresponse bias or establish
> causation.

CHD's initial work will be limited to recruitment accounting, cohort
construction, internal quality checks, missingness and breakoff analysis,
record-agreement assessment in the validation subset, data documentation,
and descriptive characterization. The initial study will
not estimate population incidence, compare vaccinated and unvaccinated
ASD rates, test a causal hypothesis, or claim that vaccination causes or
does not cause autism. Subsequent investigators may conduct separately
documented and, where appropriate, preregistered analyses using an
approved public-use or controlled-access version of the dataset.

The embedded validation substudy will estimate agreement between
parent-reported timing and independent documentary evidence. It is not a
clinical adjudication of causation and will not assume that absence of an
onset note disproves the parent's report. Validation results—including
failed retrieval, refusal, missing records, and disagreement—will be
reported regardless of whether they strengthen or weaken the survey
findings.

An additional scientific purpose is to establish a feasible,
fully documented method that independent institutions can replicate.
This initial study will estimate recruitment yield, response and
completion rates, SORA-screening yield, missingness and breakoff,
record-source availability, and between-clinic variation. Those results
will permit later investigators to assess feasibility, plan sample size,
and improve—not silently alter—the method in prospectively versioned
replications.

Before outcome access, the study team will run feasibility-yield
simulations across prespecified ranges of clinic distribution size,
delivery rate, survey-start rate, consent and completion rates,
parent-reported ASD frequency, SORA-screen yield, and exact-versus-ranged
timing availability. These simulations will estimate the likely size and
precision of the descriptive resource; they will not be presented as
power calculations for a causal or confirmatory 0–2-day hypothesis test.

## 4. Parent and child eligibility

A response is eligible for the SORA analytic resource when all of the
following are satisfied:

- the respondent is age 18 or older;
- the respondent is the child's parent or legal guardian and reports
  sufficient direct knowledge of the child's development and onset;
- the child subsequently received a clinical ASD diagnosis;
- parent-recognized SORA onset occurred before the child's fifth
  birthday;
- the parent can distinguish a discrete onset day (Day 0), on which the
  first obvious, dramatic, and persistent change began, from a gradual
  period of change, even if the historical calendar date is no longer
  remembered; and
- at least one of the three SORA categories below is reported during Day
  0 through Day 6, with at least one qualifying category beginning on
  Day 0; and
- the qualifying change either remained present for at least 30 days or
  was documented or remembered as an enduring change still present at a
  later clinical evaluation.

The final protocol must define how respondents confirm the ASD diagnosis
and how competing explanations and pre-existing developmental concerns
are handled. Because the parent supplies linkable private information
about a living child, the submission will conservatively treat the child
as a research subject and request the applicable Subpart D findings. No
child assent will be sought because children are not contacted or asked
to perform research procedures; IPAK-EDU IRB will determine under 45 CFR
46.408(a) whether assent is not required or may be waived.

## 5. Operational definition of SORA

For this study, SORA is an abrupt, dramatic, and persistent change first
recognized by a parent or primary caregiver in a child whose prior
development had been described as typical or meeting expected
milestones. The parent must be able to distinguish a discrete onset day
(Day 0), on which the first obvious persistent change began, from a
gradual period of change. Remembering the historical calendar date is
not required, and the survey will not collect it.

The child must exhibit a dramatic rapid change in at least one of these
three categories:

1. **Acquisition of a new pathological behavior:** abrupt emergence of
   one or more persistent abnormal behaviors that were not previously
   present, such as head banging, self-injury, repetitive movements,
   inconsolable screaming, rage, rigidity, fixation, or another
   conspicuous pathological behavior.

2. **Loss of an existing behavior or skill:** abrupt loss or marked
   diminution of one or more previously acquired behaviors or skills,
   such as speech or language, eye contact, social engagement, play,
   motor ability, toileting, attention, or another established skill.

3. **Change in sensitivity of the senses:** abrupt, marked, and
   persistent increase or decrease in sensory sensitivity or sensory
   response, including a major change involving sound, touch, light,
   taste, smell, pain, temperature, movement, or food texture.

The qualifying change must be obvious rather than a gradual or
retrospectively approximated developmental difference. Transient fever,
irritability, appetite change, sleep disturbance, or another short-lived
symptom alone does not qualify.

For eligibility, `persistent` means that the qualifying developmental,
behavioral, skill, or sensory change either continued for at least 30
days or was still present and recognized as an enduring change at a later
clinical evaluation. A symptom that resolved within 30 days does not
qualify by itself. `Not sure` does not satisfy the persistence criterion.
A transient illness may precede an enduring qualifying change; in that
case Day 0 is the day the first enduring qualifying change became
obvious, not automatically the first day of fever or illness.

Example: if loss of language becomes obvious and persistent on Day 0 and
a new pathological behavior first appears on Day 4, both corresponding
seven-day fields are `Yes`, but Day 0 remains the single SORA onset date.
A change that becomes obvious only gradually over several weeks does not
qualify.

## 6. Clinic eligibility, activation, and recruitment campaign

CHD will use IRB-approved materials during an initial 30-calendar-day
clinic-enrollment period. The study targets 4–10 activated clinics and
will activate up to the first 10 clinics that:

- document at least 500 unique patients with a documented ASD diagnosis
  and separately define the clinic's complete patient distribution
  population, including patients evaluated or treated by the clinic who
  did not ultimately receive an ASD diagnosis;
- can distribute the approved electronic invitation to the complete
  defined population of contactable parents or guardians without
  disclosing the list to CHD;
- designate an authorized clinic representative;
- agree not to select recipients based on suspected SORA, vaccination
  history, beliefs, timing, or expected response;
- complete applicable IRB, privacy, legal, contracting, and technical
  requirements; and
- are formally activated by the coordinating study.

Clinics will be ordered by the date all activation requirements are
completed. An expression of interest does not reserve a position. If an
activated clinic withdraws before beginning its campaign, the next fully
qualified clinic in activation order may replace it. Clinic selection or
replacement may not depend on survey responses or preliminary results.

Clinic enrollment will close when 10 clinics activate. If at least four
but fewer than 10 clinics activate by Day 30, clinic enrollment will
close on Day 30. If fewer than four activate by Day 30, enrollment will
continue automatically until the fourth clinic activates or Day 90,
whichever occurs first. This extension is triggered solely by the
prespecified clinic-count rule. If fewer than four clinics activate by
Day 90, further recruitment will stop and the PI will seek IRB direction
regarding closure. Under the prospectively disclosed default rule,
responses already collected as coded records will be retained and used
only for
a clearly labeled pilot-feasibility report of recruitment, completion,
missingness, data quality, and respondent descriptions; they will not be
represented or released as the planned 4–10-clinic primary data resource
without a prospective IRB-approved amendment. The shortfall and
disposition will be reported, and the rule will not change based on the
observed timing distribution.

A fully activated clinic may begin its approved parent campaign while
clinic enrollment remains open. During that period, survey responses
will be collected in the approved system but substantive outcome data
will be sequestered from personnel involved in clinic recruitment,
ordering, and activation. Those personnel will not receive SORA yield,
vaccination answers, Dpre or Dpost values or distributions, site-level
outcomes, or other preliminary results. They may receive only the
technical and safety information required to operate the study, such as
system availability, aggregate messages sent, survey starts, consent
status, support requests, and incident reports. Clinic-enrollment or
extension decisions may not depend on observed survey data.

Each clinic will conduct a standardized campaign consisting of:

1. on Campaign Day 0, one clinic-branded, IRB-approved invitation sent
   through the clinic's ordinary patient-communication system to its
   complete defined patient distribution population, including patients
   without an ASD diagnosis, rather than a subset selected for diagnosis,
   suspected regression, SORA, vaccination history, or likely response;
2. on Campaign Day 7, one clinic-branded, IRB-approved reminder to the
   same population, subject to clinic opt-out and delivery rules;
3. on Campaign Day 21, a second clinic-branded, IRB-approved reminder to
   the same population, subject to the same rules;
4. closure of that clinic's parent survey on Campaign Day 35;
5. management of undeliverable messages and opt-outs under clinic policy;
6. provision of frozen aggregate counts for unique patients/children in
   the defined population, unique intended parent/guardian recipients,
   contactable coverage percentage, messages attempted, messages
   delivered where available, undeliverable messages, opt-outs, and each
   reminder; and
7. signed certification of complete, nonselective distribution.

CHD will not receive recipient identities or learn which individual
clinic patients did or did not respond. The final protocol will define
the clinic source-population date, whether former patients are included,
contactability rules, and handling of multiple guardians. The campaign
and survey-open periods are fixed above and will not be changed in
response to participation or substantive results.

The 500-ASD-patient threshold is an administrative clinic-capacity rule
intended to provide a reasonable opportunity to obtain usable ASD and
SORA responses despite voluntary response and screening. It is not the
invitation denominator and is not a minimum SORA-case requirement. The
invitation denominator is the clinic's broader complete contactable
patient population. The threshold will exclude some smaller practices
and may affect representativeness; that limitation will be reported. A
unified practice group or clinic network may qualify as one site only if
it uses one defined, nonoverlapping distribution population, one
agreement, and one accountable campaign operator.

## 7. Clinic compensation

Each activated clinic will receive a flat $5,000 institutional payment
after satisfactory completion and acceptance of the approved recruitment
campaign and deliverables. Payment is not made to parents or children.

An expression of interest, activation alone, or an undocumented email
does not earn payment. Required deliverables include the executed
agreement, verified eligibility and source-population count, approved
initial invitation and reminders, aggregate campaign metrics, and signed
final campaign attestation. CHD may reject a selectively distributed,
incomplete, unverifiable, or materially nonconforming campaign.

Payment will not depend on:

- survey response or completion rate;
- the number or proportion of respondents meeting the SORA definition;
- vaccination status or temporal proximity;
- any survey answer, missingness pattern, or result; or
- publication.

Unused clinic-payment funds will not be redistributed among participating
clinics merely because fewer than 10 clinics activate. The IRB packet
will include the payment terms, completion checklist, fair-value
justification, and funding disclosure.

## 8. Neutral invitation, consent, and progressive survey presentation

The invitation and reminders will appear to come from the participating
clinic, use clinic branding, and be sent through the clinic's ordinary
patient-communication system. They will use neutral framing, will not
advertise a desired result, and will invite participation from the
clinic's complete defined parent/guardian population, regardless of
whether the child ultimately received an ASD diagnosis. CHD will not be concealed:
before consent, the information page will plainly identify CHD as the
sponsor and coordinating organization, identify who holds the data, and
disclose funding and relevant investigator or organizational interests.

Proposed neutral invitation principle:

> If your child experienced a sudden change, your response is important
> regardless of when the change occurred, what preceded it, or what you
> believe caused it.

The clinic-branded invitation will lead to a neutral landing page with a
single **Learn about the study / Start** button. The button is a navigation
step, not consent: it opens the complete information and consent page,
including sponsor identity and the vaccination-timing purpose, before any
eligibility or health answer is collected. The system may count landing-
page views and button clicks only as privacy-minimized operational events
under the IRB-approved paradata plan.

Affirmative electronic consent and parental permission will occur before the survey retains any
eligibility or health response. A person who declines consent or is
age-ineligible will exit without substantive answers being retained as
research data. The information/consent page will state in plain language
that the study asks about autism diagnosis, developmental history,
sudden behavioral or developmental changes, vaccination history, and
the timing between those events. It will disclose data
collection, required email and coded linkage, possible random selection
for validation, separate record authorization, partial-response retention, privacy limits,
voluntariness, risks, benefits, funding, investigator interests, data
release, withdrawal procedures and limits,
and contacts as required by the IRB. It will explain that participation,
nonparticipation, and individual answers are not known to treating clinic
staff and will not affect care, benefits, or payment.

The information page will state explicitly that the parent's responses
and information reported about the child are research data. It will also
state that the required email makes the response linkable during the
approved contact period, identify who may perform that linkage, and
explain the additional identifiers and source dates that may be collected
only if the parent separately authorizes record validation.

A person who chooses not to participate may be offered one optional
categorical reason: Not interested; Too busy; Privacy concerns; Do not
want to answer questions about development/autism; Do not want to answer
questions about vaccination; Child does not have a relevant developmental
history; Other/prefer not to say. No narrative response will be requested.
The reason will be retained only if IPAK-EDU approves the applicable
consent or narrow waiver/alteration; otherwise only an aggregate decline
event will be retained as permitted operational metadata.

The information page will explain that the working dataset is coded, not
anonymous; authorized staff can link a response to the required email for
approved contact, withdrawal, duplicate review, or validation. Separate,
affirmative authorization will be obtained before records are uploaded or
requested from a provider. Declining record validation will not cancel
the main survey response or affect care or benefits.

Questions will be displayed progressively. Respondents will not be shown
the entire questionnaire or later vaccination questions in advance.
Progressive presentation is intended to reduce priming and permit
measurement of item- and section-level breakoff. It will not be used to
make a false or materially incomplete statement about the study. The
study is designed to operate with the plain vaccination disclosure
above; it does not depend on an alteration of consent. IPAK-EDU IRB may
nonetheless require revised language or an end-of-survey explanation.

Proposed purpose language:

> This study asks about autism diagnosis, developmental history, sudden
> behavioral or developmental changes, vaccination history, and the
> timing between those events. The study is intended to create a dataset
> for descriptive and subsequent independent analysis. It cannot by
> itself determine whether vaccination caused or did not cause a
> developmental change.

Accuracy language will remain neutral:

> Accurate participation from all parents whose children experienced
> sudden-onset regression is important, regardless of whether the child
> had received any vaccination before onset, how close or distant any
> vaccination was from onset, or whether the parent believes vaccination
> was related. Complete and accurate responses—including responses
> showing no temporal proximity—are essential to producing a useful
> dataset.

## 9. Electronic survey and data elements

The final electronic instrument will use branching logic and will be
tested on desktop and mobile devices. Proposed domains are:

### Eligibility and background

- confirmation that the respondent is age 18 or older;
- parent/legal-guardian relationship and direct knowledge of onset;
- recruiting `site_code` supplied by the clinic-specific link;
- child sex: Female, Male, Intersex, or Unknown/prefer not to answer;
- confirmation of a clinical ASD diagnosis;
- highest ASD support level known to the parent: 1, 2, 3, or Not known/not
  documented; and
- prior-development questions required by the final SORA definition.

### SORA onset

- the parent-reported overall developmental pattern, asked of all
  respondents before SORA-specific branching:
  - development was atypical or delayed from the earliest period the
    parent can recall, without a later regression;
  - development progressed and then reached a plateau without an obvious
    loss of existing behavior or skill;
  - development was described as typical or meeting expected milestones
    and then an abrupt, obvious drop occurred;
  - development was described as typical or meeting expected milestones
    and then a gradual decline occurred;
  - another pattern; or
  - not sure;
- whether an abrupt, obvious, and persistent change occurred;
- before any vaccination-history question, a structured reconstruction
  of the onset sequence and the basis for remembering its timing;
- whether the parent can distinguish a discrete day on which the first
  obvious and persistent change began from a gradual period of
  developmental or behavioral change: Yes, No, or Not sure;
- the child's age at Day 0, entered as the best known number with units
  (days, weeks, months, or years) or as a structured age range;
- onset-age source and precision: contemporaneous record or message,
  developmental/medical record, memory, or other; exact, best estimate,
  range only, or unknown;
- the timing anchor or anchors consulted or remembered: calendar;
  date-stamped photo or video; parent message or email; clinical,
  therapy, school, or childcare record; family event or holiday;
  vaccination record or vaccination event; another documented event;
  unaided memory; or Not sure;
- whether knowledge of vaccination timing helped the parent identify or
  reconstruct Day 0: Yes, No, or Not sure;
- confidence in identifying the discrete Day 0: Very sure, Somewhat
  sure, Not very sure, or Not sure;
- elapsed time from the parent-recognized onset or developmental change
  to survey completion, reported in broad prespecified categories rather
  than an event date (for example, less than 1 year, 1–2, 3–5, 6–10,
  11–20, or more than 20 years ago, plus Not sure);
- `new_pathological_behavior_within_7d`: Yes, No, or Not sure;
- `loss_existing_behavior_or_skill_within_7d`: Yes, No, or Not sure;
- `change_in_sensory_sensitivity_within_7d`: Yes, No, or Not sure; and
- whether the qualifying change continued for at least 30 days, was
  present at a later clinical evaluation, resolved within 30 days, or is
  not known.

At least one SORA category must begin on Day 0. Additional categories may
first appear during Day 1 through Day 6. The survey will explain this
with a worked example. Only `Yes` to the discrete-onset question proceeds
into the SORA timing pathway. `No` and `Not sure` remain in screening and
recruitment-flow counts but do not enter the SORA analytic cohort.

For each field ending in `_within_7d`, the seven-day window is Day 0
through Day 6 inclusive. Day 0 counts as the first day; Day 7 is outside
the window.

The overall developmental-pattern question is a recruitment-composition
and measurement-quality variable, not an independent validation that all
eligible parents responded. Its distribution may be compared with
prespecified external estimates only when the populations, definitions,
and ascertainment methods are sufficiently comparable. Differences may
reflect nonresponse, clinic case mix, question wording, recall, or other
selection and measurement factors.

The structured onset reconstruction is asked before vaccination history
to reduce cueing from later questions. The main survey will not request
an unrestricted narrative. A limited narrative or documentary account
may be obtained only in the separately authorized validation workspace.
The analysis will preserve vaccination-anchored recollection as an
observed measurement-quality characteristic rather than treating it as
proof that the timing is either correct or biased.

Respondents reporting that the child did not receive an ASD diagnosis,
or that diagnosis status is unknown, contribute only to prespecified
recruitment, screening, developmental-pattern, and missingness summaries.
They do not enter the SORA analytic resource or vaccination-proximity
analysis. The survey and SAP will define the limited questions shown to
these respondents and avoid collecting unnecessary vaccination timing.

### Vaccination history and timing

- whether any vaccination was administered before or on SORA Day 0:
  Yes, No, or Unknown;
- the number of complete 24-hour periods from the most recent vaccination
  before onset to Day 0 when an exact interval is known (`0` means onset
  occurred after the vaccination but less than 24 hours later);
- when an exact Dpre interval is not known, one structured range: less
  than 1 day, 1–2, 3–4, 5–7, 8–14, 15–30, 31–90, more than 90 days, or
  Unknown;
- whether a vaccination was administered after Day 0: Yes; No, with
  adequate follow-up; No follow-up sufficient to know; or Parent does not
  know;
- the exact number of complete 24-hour periods to the first vaccination
  after onset, or one structured Dpost range when an exact interval is
  not known: less than 1 day, 1–2, 3–4, 5–7, 8–14, 15–30, 31–90, more
  than 90 days, or Unknown (`Dpost = 0` means the vaccination occurred
  after onset but less than 24 hours later); and
- for each timing answer, whether the respondent consulted a vaccination
  card, patient portal, pediatric record, immunization registry, or
  relied on memory/another source, plus parent confidence.

The survey will ask about administered vaccinations and elapsed time,
not beliefs about causation. It will not collect dates of birth, onset
calendar dates, or vaccination calendar dates. Vaccine product or
antigen will not be collected in this initial study. The instrument will
encourage parents to consult a record when feasible but will preserve
record-based, remembered, estimated, ranged, and unknown answers as
distinct categories.

`Dpre = 0` means the parent reports that vaccination occurred first and
the first obvious persistent change began less than 24 hours later.
`Dpost = 0` means the parent reports that onset occurred first and the
next vaccination occurred less than 24 hours later. These values preserve
within-day proximity; the study will not discard them merely because the
events occurred on the same date. If the parent cannot establish order,
the response is coded as unknown rather than assigned to Dpre or Dpost.

### Other acute events around Day 0

After vaccination timing, the survey will ask whether any of the
following occurred close to Day 0:

- febrile illness or infection;
- initiation of a medication or a major medication change;
- injury, surgery, anesthesia, or another medical procedure;
- another major acute health event;
- none known; or
- not sure.

For each selected event, the parent will report whether it occurred
before Day 0, on the same calendar day, or after Day 0; an exact elapsed
interval or the applicable structured range; information source; and
confidence. These are contextual competing-event measures, not a control
group or proof of an alternative cause. No narrative free text will be
requested. The SAP will define the maximum look-back/look-forward window
and mechanically distinguish no event from unknown history.

### Pre-survey causal attribution and post-onset vaccination decisions

Only after the primary onset, vaccination-timing, and competing-event
questions are complete, respondents will be asked whether, before
starting the survey, they had formed an opinion about what contributed to
the child's developmental condition or change. Neutral, multiple-choice
responses will include genetic/inherited, prenatal/birth, illness,
medication/procedure, vaccination, environmental, psychosocial/life
event, another factor, no particular event, uncertain, not previously
considered, and prefer not to answer. A separate item will measure the
strength of pre-survey belief that vaccination contributed and whether
vaccination timing contributed to that belief.

Respondents will also report whether the child received vaccination after
Day 0 and whether the vaccination plan continued unchanged, continued
with delay, continued with one or more vaccinations declined, stopped,
required no subsequent decision, or is unknown. For a delayed, declined,
or stopped plan, structured reasons will distinguish concern about a
relationship to the developmental change, professional advice, illness
or medical condition, a previous reaction, access, pre-existing general
concerns, concerns beginning after the change, no vaccine due, another
reason, and prefer not to answer. No free text is required.

These fields are bias-characterization and sensitivity variables. They
will not be used to label participants, infer intent, or define an
unbiased causal control group.

### Derived analytic fields

The restricted processing environment will standardize or derive:

- `age_at_onset_value`, `age_at_onset_unit`, `age_at_onset_precision`,
  and, only when justified by the reported units and precision, a
  standardized onset-age value or interval;
- `vaccination_before_onset`;
- exact `dpre_days` or lower and upper Dpre bounds for a ranged response;
- `dpost_status`; and
- exact `dpost_days` or lower and upper Dpost bounds for a ranged
  response.

Exact intervals and ranged responses will remain distinguishable. The
study will not replace a range with a midpoint or present an estimate as
an exact observation.

The final analytic resource will not contain names, email addresses,
dates of birth, onset calendar dates, vaccination calendar dates, IP
addresses, device fingerprints, medical-record numbers, or free text.

## 10. Coded contact architecture, final confirmation, and validation

The survey will require a valid parent email address. It will not request
the child's name, street address, telephone number, medical-record
number, patient-portal identifier, or another direct child identifier in
the main survey. A high-entropy, nonsemantic `survey_id` will link three
segregated environments:

| Restricted contact store | Coded research store | Validation workspace |
|---|---|---|
| `survey_id`, parent email, contact/withdrawal status | `survey_id`, survey responses, derived fields, quality flags | Random-selection status, authorization, received source documents, abstracted comparison variables |
| No substantive survey answers | No email or uploaded source document | Direct identifiers only to the extent required for authorized record retrieval and reconciliation |

Before final survey submission, respondents will review their substantive
answers and derived timing interpretation and may correct them. The
system will not force agreement or alter an unexpected answer. After
submission, authorized staff may send a neutral secure-message notice to
resolve a mechanical ambiguity, process withdrawal while the mapping is
retained, or invite a randomly selected respondent to validation.
Substantive health information will not be placed in ordinary email.

### Embedded record-validation substudy

Validation eligibility will be limited to timing-eligible SORA responses
with a reported vaccination history and will be determined by
prespecified survey status, not the observed interval or whether the
answer supports a hypothesis.
Before substantive timing distributions are accessible, reproducible
software will randomly select validation invitees within prespecified
clinic and elapsed-time-since-onset strata. Selection will not favor
short Dpre values, exact values, particular developmental patterns, or
other interesting results. Twenty usable vaccination-record comparisons
is the minimum feasibility threshold, and the operational target is 60
usable comparisons if obtainable. Invitations will continue toward 60
until the prespecified validation period closes or the eligible sampling
frame is exhausted. Invitation numbers and stopping rules will be set
from blinded feasibility assumptions and will not change in response to
agreement or disagreement results. If fewer than 20 usable comparisons
are obtained, the study will report the validation effort as feasibility
information and will not present it as a quantitative estimate of the
cohort-wide disagreement rate.

Selected parents will receive a separate information and authorization
form and may:

- upload a vaccination card, registry extract, patient-portal record, or
  comparable administered-vaccination record through the secure system;
- authorize limited retrieval from a pediatric practice, immunization
  registry, or other lawful source; and
- optionally provide contemporaneous documentation relevant to onset,
  such as a clinical note, parent message, calendar entry, therapy or
  school record, or comparable time-stamped material approved by the IRB.

Parents may decline validation. Validation reviewers will receive the
minimum source material necessary and, where feasible, will be blinded to
the parent's reported Dpre/Dpost and to aggregate timing results. Using a
locked abstraction manual, two trained reviewers will independently
classify vaccination-date agreement and onset-documentation support;
disagreements will follow a prespecified adjudication process.

The primary onset-evidence assessment will be performed while reviewers
are blinded to parent-reported vaccination timing and aggregate timing
results, using an explicit redaction and cue-leakage protocol. After the
primary blinded assessments are locked, a separately labeled secondary
review may use unredacted material, including vaccination timing. The
blinded-versus-unblinded difference will be reported as a measure of
possible adjudicator anchoring; the unblinded result will not replace the
primary assessment.

The locked manual will assign an onset-evidence tier without implying
causation: (1) contemporaneous date-stamped evidence; (2) contemporaneous
clinical, school, therapy, or childcare documentation; (3) a specific
remembered onset anchored to another documented event; (4) approximate
or ranged memory; or (5) uncertain or unsupported timing. Evidence tier
will describe support and precision, not whether vaccination caused the
reported change.

Validation categories will distinguish exact agreement, agreement within
prespecified tolerances, disagreement and its direction, unusable or
incomplete records, failed retrieval, declined participation, and no
contemporaneous onset evidence. Lack of an onset document is not evidence
that the reported onset did not occur. Original survey responses will not
be overwritten by validation findings.

The consent and platform will disclose retention of post-consent partial
responses for breakoff and missingness. The parent may request withdrawal
while the identity mapping exists and before the applicable analysis or
release cutoff. The protocol will state what can and cannot be removed
from audit logs, backups, completed validation abstractions, locked
analyses, and released datasets. No pre-consent health response will be
retained as research data.

## 11. Survey paradata, partial responses, and duplicates

The study will retain privacy-minimized paradata needed to assess
missingness and breakoff:

- section and question reached;
- last question answered;
- whether the vaccination section and vaccination-status question were
  displayed;
- answered, skipped, and breakoff indicators;
- completion status; and
- coarse section-duration measures if approved.

The system will not intentionally collect IP addresses, precise location,
device fingerprints, advertising identifiers, or third-party tracking
data. The consent page will disclose whether incomplete responses are
retained. Breakoff after a vaccination question will be described as an
observed missingness pattern, not proof that the question caused dropout.

The final protocol must define prevention and adjudication of duplicate
responses, including repeated submissions for the same child, a parent
reporting more than one child, multiple guardians reporting the same
child, forwarded links, and invitations received from more than one
clinic. The procedure will use privacy-minimizing survey logic and
restricted contact-store review without placing email in the research
dataset or creating a reusable cross-study identifier. Contact/research
joins for duplicate review will be purpose-limited and audited. No
response will be silently merged or deleted; suspected and confirmed
duplicates will follow prespecified outcome-blinded rules.

The survey will ask, without requesting identity:

- whether this respondent has previously submitted this survey for this
  child;
- whether another parent or guardian may already have submitted for this
  child;
- whether the respondent is reporting more than one child, using a
  separate response for each child; and
- whether the invitation was received through more than one clinic.

Affirmative or uncertain answers will create duplicate-risk flags, not
automatic exclusions. The frozen adjudication tree will specify when to
retain all reports as separate parent-child responses, select one under
an outcome-blinded rule, or exclude unresolved probable duplicates from
child-level counts while preserving them in sensitivity summaries.

## 12. Validation and data quality

Automated checks will cover required fields, allowed values, plausible
ranges, interval direction, cross-field logic, duplicate indicators, and
derived interval bounds. Potential misunderstandings will generate a neutral,
standardized on-screen explanation and review prompt before submission.
No answer will be changed merely because it is unexpected or
inconsistent with a study hypothesis.

Before clinic enrollment closes and the prespecified survey lock occurs,
quality-control personnel may monitor completeness, missingness, allowed
values, impossible ranges, cross-field errors, duplicate indicators,
on-screen validation flags, and system performance. Routine pre-lock dashboards and
reports will not display Dpre/Dpost histograms, peaks, cumulative timing
windows, site comparisons, or other substantive outcome distributions.
Outcome-aware exclusions, cleaning rules, eligibility changes, and
survey revisions are prohibited. Any necessary correction to an
approved rule will be documented, versioned, and submitted for IRB review
when required before implementation.

The random validation sample will be generated from a blinded sampling
frame that contains only variables authorized by the locked sampling
plan. Contact staff will see selection and contact status but not timing
outcomes. Record abstractors will see source documents and assigned
validation identifiers but will be blinded to parent-reported intervals
where feasible. Analysts will not see agreement results until validation
abstraction and adjudication are locked.

The survey-response lock will occur 30 calendar days after the last
activated clinic's Campaign Day 35 survey closure. The validation sample
will then be generated from the frozen, blinded eligibility frame.
Validation invitations will be sent within seven calendar days, with
neutral reminders 14 and 35 days after the invitation. The validation
collection period will close 90 calendar days after the initial
validation invitation, and the validation abstraction and adjudication
lock will occur no later than 30 calendar days afterward. The initial
descriptive report and release file will not be finalized until both
locks are complete. Neither lock will be advanced or delayed because
of response count, SORA yield, missingness pattern, Dpre/Dpost values or
distributions, or any other substantive result. A safety, privacy, or
material technical incident may justify a documented pause,
with IRB notification or approval as required.

After lock, the prespecified descriptive outputs may be generated and
reviewed by the PI and approved study team. An independent statistician
or data-governance reviewer will confirm the lock and reproduce or
verify the first substantive timing report. The original response,
on-screen validation flags, respondent correction before submission, and
applicable audit history will be preserved. Direct identifiers required
for contact or validation will remain segregated and will be retained or
destroyed according to the IRB-approved schedule, never placed in an
analytic or release file.

The data-quality report will distinguish:

- parent-reported values supported by a cited record source;
- values reported from memory or another source;
- values corrected by the respondent before final submission;
- unresolved inconsistencies;
- unknown and skipped answers;
- incomplete responses; and
- records excluded by each prespecified rule.

The validation report will show the full cascade: eligible, sampled,
invited, authorized, records requested, records received, usable
vaccination comparisons, usable onset documentation, adjudicated, and
not completed. Agreement will be reported overall and by prespecified
elapsed-time and source strata with uncertainty intervals. Differences
between validation completers, decliners, failed retrievals, and the main
survey cohort will be described using variables available for all.

The protocol will prespecify whether incomplete or unresolved responses
remain in descriptive releases with flags or are excluded from particular
derived analyses.

The embedded validation substudy requests only the minimum records
specified in Section 10. Broader chart review, clinical phenotype
adjudication, or causal evaluation remains outside this protocol and
would require a later study or approved amendment.

## 13. Initial descriptive outputs

The initial publication will describe rather than test causal hypotheses.
Prespecified outputs will include:

- clinics approached, interested, activated, withdrawn, and completing;
- each clinic's eligible distribution-population size and aggregate
  campaign delivery metrics;
- parent-reported ASD diagnosis status among consented respondents;
- survey starts, consent decisions, eligibility flow, completions, and
  partial responses by site;
- response, completion, item-missingness, and section-breakoff rates;
- breakoff before, at, and after the vaccination section;
- parent-reported overall developmental-pattern distribution among all
  eligible respondents, with the comparison population and definitions
  stated explicitly for any external benchmark;
- elapsed-time-since-onset/change categories and timing completeness by
  elapsed-time category;
- exact and ranged Dpre/Dpost summaries stratified by prespecified
  elapsed-time-since-onset categories and record-versus-memory source;
- age-at-onset distribution;
- counts meeting each SORA category and observed category combinations;
- reported ASD support-level distribution;
- vaccination-before-onset counts and source-of-information categories;
- exact and interval-censored Dpre and Dpost distributions, reported
  separately or analyzed with prespecified interval-censored methods;
- Dpre counts and proportions for each exactly reported day, with ranged
  responses shown separately and subject to disclosure protection; and
- on-screen validation and pre-submission correction rates; and
- validation sampling and completion flow, vaccination-timing agreement,
  onset-documentation support, disagreement direction, and comparison of
  validation completers with noncompleters; and
- prespecified measurement-quality summaries by elapsed time since onset,
  exact versus ranged timing, record consulted versus memory only,
  vaccination-anchored versus other recollection, onset-evidence tier,
  validation completion status, and blinded-adjudication agreement; and
- prespecified timing summaries by pre-survey vaccine attribution and
  post-onset vaccination-plan category, including a clearly labeled
  sensitivity subset with no prior vaccine attribution, a non-vaccination
  onset anchor, and continued vaccination where sample size and disclosure
  review permit.

Selected cumulative Dpre windows, confirmatory hypothesis tests, causal
claims, vaccine-attributable risk, and population-incidence estimates are
outside the initial data-resource publication. Site-specific results will
be displayed only when permitted by disclosure-risk review.

The initial report will not preferentially weight or highlight a recent-
onset subgroup because its pattern appears stronger after lock. Recall-
horizon, anchor, evidence-tier, record-source, and validation-status
strata will be specified in the SAP before outcome access. These will be
descriptive or sensitivity analyses with denominators and uncertainty
intervals, not a search for the subgroup with the strongest signal. A
record-supported subset may be shown as a sensitivity analysis but will
not replace the full cohort or be represented as population-
representative. The report will characterize the
voluntary respondent cohort and will not treat these strata as estimates
for all clinic patients or all children with SORA.

Exact-day observations and ranged observations will first be tabulated
separately. If an interval-censored distribution is included, the SAP
will prespecify a nonparametric interval-censored estimator, treatment of
open-ended responses such as more than 90 days as right-censored, and
the software, package, and version. The analysis code and synthetic test
cases will be frozen before outcome access. No range will be converted
to an artificial midpoint.

## 14. Privacy, security, and regulatory characterization

The study requires a valid Common Rule/IRB pathway and every applicable
privacy-law authority. Affirmative consent will precede retention of
health responses. Required parent email and authorized validation records
make the working dataset identifiable or coded during collection. The
protocol will not call it anonymous or HIPAA-de-identified merely because
contact, research, and validation data are separated. The main survey
will not solicit a child's name or historical calendar dates, but
authorized validation records may contain identifiers and source dates
that must remain inside the restricted validation workspace.

The IRB packet will identify whether CHD, the survey vendor, and each
clinic are HIPAA covered entities or business associates and will state
the lawful basis for every regulated use or disclosure. A clinic's use of
its own contact information to distribute an approved invitation does not
authorize disclosure of its patient list to CHD. The clinic must obtain
and document the applicable authorization, waiver/alteration, or other
lawful basis for selecting its complete clinic distribution population and sending
research invitations, as determined by its privacy authority and IRB or
Privacy Board. Each site also requires the applicable engagement,
reliance, or local-review determination.

The final packet will include a data-flow legal matrix covering the
clinic's list use and campaign, clinic-to-CHD/vendor information flows,
parent-to-CHD responses and email, validation authorization and record
transfer, vendor processing, operational metadata, and public or
controlled release. It will also establish a site- and
respondent-jurisdiction review process for medical-confidentiality,
minor/developmental and mental-health information, consumer-health-data,
electronic-communications, breach-notification, and deletion laws.

The approved environment must provide encryption in transit and at rest,
MFA, role-based access, audit logging, backups, managed export controls,
incident response, access termination, retention schedules, and secure
destruction. Survey analytics and tracking technologies will be disabled
unless explicitly reviewed and approved. The packet must name the vendor,
hosting region, contractual safeguards, data custodian, privacy official,
incident contact, authorized roles, and breach-reporting procedure.

Contact, coded research, source-document, and validation-abstraction data
will use separate stores or equivalent cryptographic/access segregation,
separate role permissions, prohibited combined analyst exports, access
alerts, periodic mapping review, and a documented join procedure.
Validation documents will be quarantined from ordinary downloads,
malware-scanned, and accessed only by authorized validation personnel.
The protocol will specify when source documents and the contact mapping
are destroyed or retained, how deletion propagates to backups, and how
legal or regulatory holds are handled.

The web service may necessarily process operational metadata such as a
network address, consent timestamp, audit timestamp, delivery event, or
security log. Such metadata will not be included as research variables.
The platform will minimize and segregate it, prohibit session replay,
keystroke capture, advertising identifiers, profiling, sale, unrelated
analytics, and model training, and apply documented access, retention,
deletion, backup, subprocessor, referrer, and incident controls.

## 15. Data release and access

An independent disclosure-risk expert will be engaged during protocol
and instrument finalization, before outcome data are available. The
expert will define provisional rules for site removal or pooling, age and
timing binning or top-coding, rare-combination treatment, small-cell
suppression, and release review. Final approval must still be applied to
the exact proposed release file, but protective transformations may not
be loosened or selectively changed because of the observed timing
pattern.

Every release will have a version number, cutoff date, clinic count,
record count, instrument/data-dictionary version, validation report, and
change log. Release timing will not depend on the apparent timing
distribution.

Public materials will include the protocol, survey instrument after
recruitment closes, codebook, recruitment and data-quality flow,
appropriately protected descriptive results, analytic code, synthetic
data, and release metadata.

Exact row-level data may be released publicly only if an independent,
qualified disclosure-risk expert documents that identification risk is
very small and approves the exact file. Required protections may include
removal or pooling of `site_code`, binning of age or timing values,
suppression of small cells, and removal of rare combinations. If an
acceptable unrestricted file cannot be produced, exact data will be
available only through an approved controlled-access process. Consent
records, emails, contact mappings, authorization forms, source documents,
raw source dates, and operational security metadata will never be
included in a research-data release. Only prespecified validation
classifications and disclosure-reviewed agreement variables may enter an
analytic or released dataset.

## 16. Governance, funding, and independence

Brian Hooker has accepted coordinating PI responsibility. CHD has
accepted the sponsor and coordinating-organization roles. Ben Jackson
and Mila Radetich will conduct clinic outreach and activation. Karl
Jablonowski and Steve Kirsch will perform the approved data-quality
functions. The contact/validation coordinator, data custodian,
privacy/security official, incident contact, independent validation
reviewers, and independent statistician/data-governance reviewer remain
to be named.

CHD's mission, public positions, funding, clinic-payment arrangements,
and relevant investigator financial and nonfinancial interests will be
disclosed to the IRB. A committed funder's identity and terms will be
disclosed at submission or by amendment before funded activity begins.
Funders will have no authority to select clinics or respondents, access
clinic patient lists, alter data, suppress results, or control
publication.

## 17. Independent-replication roadmap

The CHD-sponsored study is intended to be the first implementation of a
portable method, not the final evidentiary study. After recruitment
closes, CHD plans to publish the approved protocol, complete survey
instrument, branching and derivation rules, codebook, recruitment and
missingness definitions, synthetic test data, and reproducible analysis
code, subject to intellectual-property and security review. Publication
of these materials will allow independent investigators to reproduce the
method without relying on undocumented CHD judgments.

The preferred sequence is:

1. **Initial CHD implementation:** establish operational feasibility,
   characterize the responding cohort, identify data-quality problems,
   estimate record agreement, and produce planning estimates.
2. **Separately approved nonresponse substudy:** participating clinics or
   an independent team may draw a structured random sample of
   nonresponders and conduct a short, neutral callback assessment of
   contact, survey awareness, and broad reasons for nonparticipation.
   This is not part of the present protocol. It requires its own IRB,
   privacy, clinic-engagement, sampling, consent/waiver, and data-flow
   determinations and may not disclose individual survey participation
   or collect vaccination/onset outcomes without specific approval.
3. **Independent academic replication:** an independent university-led
   team repeats a prospectively locked version of the method in a
   different clinic network under independent governance and, where
   feasible, a sponsor and recruitment frame perceived differently from
   CHD.
4. **Population-based record study:** a health-system or registry team
   uses independently documented onset and vaccination records in a
   prespecified self-controlled risk-interval, self-controlled case-
   series, case-crossover, or target-trial-emulation design appropriate
   to the data and assumptions.
5. **Prospective pediatric sentinel network:** pediatric practices enroll
   children before the relevant outcome period, import vaccination data,
   perform brief developmental assessments at fixed intervals, capture
   abrupt changes promptly, and use blinded adjudication. Enrollment and
   follow-up must be independent of vaccination beliefs and emerging
   results; the required network size would be determined from preceding
   feasibility and event-rate estimates.
6. **Federally supported confirmation:** an academic investigator or
   consortium may seek NIH funding for a larger preregistered replication
   or multisite confirmatory study.
7. **International replications:** independent sponsors may translate and
   culturally adapt the instrument and repeat it in other countries,
   with adaptation and measurement-equivalence procedures documented in
   advance.

Each replication would be a separate study—not an extension authorized
by this IRB submission. Each sponsor would require its own protocol,
funding, prospective registration or preregistration where appropriate,
IRB or research-ethics approval, privacy and cross-border data review,
clinic agreements, consent materials, security controls, and release
plan. No commitment by NIH, a university, a foreign institution, or any
other future sponsor is represented unless documented separately.

For an independent replication, the new sponsor should control clinic
recruitment, survey hosting, contact information, data cleaning,
analysis, interpretation, and publication. CHD should not receive its
respondent-level data or possess authority to alter or suppress its
results. Core definitions and outputs should be frozen before outcome
data are examined; deviations and country-specific adaptations should
be versioned and disclosed. Replication success criteria and comparisons
with the initial study should be prespecified rather than chosen after
results are known.

This roadmap strengthens the justification for the initial minimal-risk
collection: the study will create openly documented feasibility evidence
and a reusable method for independent testing. It does not increase the
direct benefit to current participants, cure selection or recall bias,
or make later replication certain.

## 18. Principal limitations

The resource will be a voluntary-response sample recruited through a
convenience sample of up to 10 clinics, not a random or nationally
representative sample. Clinic patients without a deliverable approved
electronic contact channel may be underrepresented.
Requiring a valid email for contact, withdrawal, duplicate review, and
random validation may also reduce participation or change the responding
sample.
Parents who experienced an abrupt regression, who associate onset with a
particular event, or who hold strong views may respond at different rates.
Nonresponse and breakoff measurements describe but do not eliminate that
self-selection bias.

The distribution of parent-reported developmental patterns can reveal
whether the respondent sample differs from a prespecified external
benchmark, but it cannot establish that every clinic family was invited
or that all invited families responded. Aggregate clinic campaign
metrics and signed complete-distribution attestations address invitation
coverage; differential nonresponse remains possible.

Responses depend on parent recall, understanding, record availability,
and accurate reporting. The embedded validation substudy can estimate
agreement for selected participants with obtainable records, but it will
not verify every response and may itself be affected by authorization,
record-availability, and validation-participation bias. Clinic identity,
survey wording, reminder practices, and
referral patterns may affect participation. The study can describe the
responding cohort and generate hypotheses, but cannot by itself establish
causation, estimate SORA incidence, or estimate vaccinated-versus-
unvaccinated ASD risk.

Main-cohort Dpre and Dpost measures remain parent-reported and must not be
presented as universally verified clinical intervals. Validation
agreement, disagreement, missing-record rates, and selection into
validation must accompany interpretation. Replication of the survey tests
reproducibility; record agreement tests measurement quality; neither
alone establishes causation.

## 19. Punchlist for IRB-packet development

`Pending` means an item genuinely depends on CHD, IPAK-EDU IRB, a clinic,
or a vendor. “Source draft exists” means earlier packet language can be
adapted but is not yet valid for this redesigned parent-survey study.

### A. CHD information and authorization

| # | Item | Status |
|---|---|---|
| A1 | Brian Hooker's exact degrees, title, CHD affiliation, contact information, CV/biosketch, training, and COI disclosure | Pending CHD/PI |
| A2 | Exact roles, affiliations, contacts, training, and COI disclosures for Ben Jackson, Mila Radetich, Karl Jablonowski, and Steve Kirsch | Pending CHD/personnel |
| A3 | Name and authorize the contact/validation coordinator, data custodian, privacy/security official, incident-response contact, independent validation reviewers/adjudicator, and independent statistician/data-governance reviewer | Pending CHD |
| A4 | CHD legal entity name, status, address, authorized institutional official, and signed institutional authorization | Pending CHD |
| A5 | Funding sources, amounts, terms, in-kind support, recipients, and funder roles | Pending CHD; disclose committed funding to the IRB |
| A6 | Clinic-payment budget and fair-value justification | Basic model fixed at flat $5,000 per clinic; budget and justification pending CHD |
| A7 | Organizational and investigator financial/nonfinancial COI forms and management plan | Pending CHD/IPAK requirements |

### B. Study decisions and documents

| # | Item | Status |
|---|---|---|
| B1 | Final adult-parent and child eligibility/exclusion rules, including ASD confirmation, prior development, competing explanations, diagnosis timing, and deceased children | **Persistence rule fixed:** at least 30 days or still present at a later clinical evaluation; remaining parent-survey rules require completion |
| B2 | Exact age-at-onset boundary and validation rule | **Fixed:** onset must occur before the child's fifth birthday; the survey will ask for direct confirmation rather than infer eligibility from an artificial universal day cutoff |
| B3 | Clinic source-population definition: date, active/former patient status, age range, complete inclusion of patients with and without an ASD diagnosis, contactability, multiple guardians, undeliverables, affiliated-network treatment, and separate evidence for at least 500 ASD-diagnosed patients | Threshold and universal clinic-population distribution rule fixed; detailed verification rules required |
| B4 | First-10 activation procedure, initial 30-day period, automatic minimum-four extension through no later than Day 90, early clinic campaign start, sub-four pilot-data rule, withdrawal/replacement rule, activation-order log, and outcome-blinding controls | Core rules fixed in Section 6; operational SOP and dates required |
| B5 | Clinic recruitment campaign specification: clinic-branded invitation on Day 0, reminders on Days 7 and 21, closure on Day 35, approved channels, opt-outs, and frozen unique-patient, unique-recipient, contactable-coverage, attempted, delivered, undeliverable, and reminder metrics | Schedule and metric classes fixed in Section 6; detailed campaign SOP required |
| B6 | Clinic agreement, $5,000 completion checklist, payment timing, rejection/cure procedure, and final campaign attestation | Earlier agreement concepts reusable; recruitment-campaign terms are new |
| B7 | Clinic-branded neutral invitation, reminders, FAQ, call script, and prohibition on selective distribution or outcome-oriented claims | Branding and neutrality fixed; earlier outreach drafts require substantial redesign |
| B8 | Electronic adult consent/parental-permission language explicitly disclosing developmental changes, vaccination history, timing, required email/linkage, random validation selection, partial responses, withdrawal limits, data release, CHD role, funding, and COI; plus separate validation-record authorization | Controlling disclosure principles fixed; main consent and validation authorization required |
| B9 | Neutral landing page and Start button, progressive question-display specification, optional categorical decline-reason pathway, and any IPAK-required revised disclosure or end-of-survey explanation | Start is navigation rather than consent; no health data before consent; decline-reason retention requires IPAK approval |
| B10 | Complete electronic survey, including the all-respondent developmental-pattern item, pre-vaccination structured onset reconstruction, timing anchors, vaccination-anchor question, elapsed-time-since-onset/change categories, Day 0 confidence, persistence screen, competing acute-event module, post-timing pre-survey causal-attribution items, post-onset vaccination-plan and reason items, branching logic, definitions, worked examples, response options, accessibility, and mobile/desktop testing | Core domains fixed; draft instrument created; cognitive and usability testing required |
| B11 | Exact/ranged vaccination-interval and source-of-information questions, sub-24-hour (`0`) rules, separate later-vaccination/follow-up/unknown states, parent confidence, and Dpre/Dpost bound derivation | Core interval/status rules fixed; parent-facing implementation and test cases required |
| B12 | Coded-contact workflow, segregated email mapping, neutral secure messages, final review, pre-submission corrections, partial-response rules, withdrawal workflow, abandonment timeout, and audit trail | Core architecture fixed; detailed SOP required |
| B13 | Duplicate-prevention and adjudication plan for repeat submissions, siblings, multiple guardians, forwarded links, and multiple-clinic invitations | Privacy-minimizing questions, restricted mapping review, and no-silent-merge principle fixed; outcome-blinded adjudication tree and sensitivity rules required |
| B14 | Paradata and breakoff specification, landing/start/decline event handling, legal basis for any retained categorical decline reason, consent for incomplete-response retention, timing granularity, and tracking-technology prohibition | New rule and instrument specification required |
| B15 | Automated survey validation, missingness, query resolution, exclusion, analytic inclusion, pre-lock outcome blinding, restricted dashboards, random validation sampling, blinded record abstraction/adjudication, and audit-trail SOP | Core principles fixed; complete operational SOP required |
| B16 | Feasibility-yield simulations and SAP covering survey flow, respondent composition, timing distributions, competing events, interval censoring, prespecified anchor/evidence/recall/source/validation subgroups, record-supported sensitivity analysis, random validation sampling/stopping, agreement tolerances, missing records, validation-selection analysis, and independent first-report verification | Core principles fixed in Sections 3 and 10–13; formal simulations and SAP required |
| B17 | Survey-response lock 30 days after the last activated clinic's Day 35 closure; blinded validation sampling within seven days; validation reminders on Days 14 and 35; validation collection through Day 90; validation lock no later than 30 days afterward; outcome-independent locks, version control, correction before submission, coded-response withdrawal limits, incident-pause, and retraction SOP | Lock sequence and outcome-independence fixed; formal SOP required |
| B18 | Privacy/security plan for segregated contact, coded survey, authorization, source-document, validation-abstraction, consent, paradata, audit, and operational-log stores, including encryption, MFA, malware scanning, exports, incidents, retention, backup deletion, and destruction | Earlier security draft reusable; coded validation architecture and named infrastructure required |
| B19 | Public-release and controlled-access governance, disclosure-risk expert, DUA, license, correction policy, and enforcement | Earlier release safeguards reusable; complete process required |
| B20 | Replication package: frozen protocol/instrument version, machine-readable codebook, derivation rules, synthetic test cases, reproducible code, adaptation/versioning policy, and prespecification template | New formal package required before claiming the method is replication-ready |
| B21 | Embedded record-validation manual: eligibility, random sampling, minimum feasibility threshold of 20 usable vaccination comparisons, operational target of 60 if obtainable, outcome-independent stopping, separate authorization, secure upload/retrieval, evidence tiers, primary blinded and secondary unblinded onset review, redaction/cue-leakage controls, dual abstraction, adjudication, agreement definitions, and source destruction | New formal substudy materials required |
| B22 | Full revised protocol, application/cover form, consent/parental-permission and authorization materials, privacy plan, funding/COI attachment, personnel roster, and attachment index | Earlier packet is source material; full restructuring required after B1–B21 |

### C. IPAK-EDU IRB information and determinations

| # | Item | Status |
|---|---|---|
| C1 | Reviewing board identity | Confirmed from supplied OHRP screenshot: IPAK-EDU LLC IRB #1, IRB00014237, St. Clair Shores, OHRP/FDA type, Active as viewed 12 August 2026 |
| C2 | Legal/operator name, address, administrator, submission process, fees, schedule, and service agreement | Pending IPAK-EDU |
| C3 | Written confirmation that IPAK-EDU will review the CHD-sponsored multisite parent-survey study and accept Brian Hooker as PI | Pending IPAK-EDU |
| C4 | Expedited-review determination under 45 CFR 46.110, with requested Category 7 for the parent survey and Category 5 for validation records collected for nonresearch purposes | **Requested pathway fixed:** minimal-risk expedited review; exemption is not the primary request. Final category determination pending IPAK-EDU |
| C5 | Child-subject and Subpart D findings, including minimal risk under 45 CFR 46.404, parental permission, determination under 45 CFR 46.408(a) that assent is not required or may be waived because children are not contacted, and treatment of deceased children | Requested approach fixed; final findings pending IPAK-EDU |
| C6 | IPAK-EDU approval of the plain vaccination-purpose disclosure, progressive question display, and whether any additional end-of-survey explanation is required | Pending IPAK-EDU; protocol does not rely on incomplete disclosure or altered consent |
| C7 | Adult consent and parental permission; waiver of signed documentation under 45 CFR 46.117(c) if approved; separate validation-record authorization; any HIPAA waiver only for a later covered-entity use/disclosure without authorization; affirmative-consent placement; partial responses; withdrawal; and retention | Requested approach fixed; final determinations pending IPAK-EDU |
| C8 | Clinic engagement/reliance model and limits on feasibility outreach before determination | Pending IPAK-EDU and clinics |
| C9 | Training, COI, amendments, deviations, unanticipated-problem reporting, continuing/status review, and closure requirements | Pending IPAK-EDU policies |
| C10 | Written determination/approval and approved/stamped study documents | Pending review; required before recruitment begins |

The OHRP registration confirms the board identity and active registration
shown in the supplied screenshot. It does not establish a service
relationship, confirm acceptance of this study, or decide its regulatory
status.

### D. Survey vendor and CHD infrastructure

| # | Item | Status |
|---|---|---|
| D1 | Survey/storage vendor, product tier, hosting location, and system owner | Pending CHD |
| D2 | Contract, DPA and BAA if applicable, security documentation, breach terms, subprocessors, deletion/export controls, and tracking configuration | Pending vendor/legal review |
| D3 | Exact determination of whether CHD/vendor are covered entities or business associates and which HIPAA obligations apply | Pending legal/privacy review |
| D4 | Role-access matrix separating contact, validation coordination, source-document review, research, outreach, analytic, security-log, and privileged administrative functions | Draft required; named personnel pending |
| D5 | Retention schedule for emails/mapping, complete/partial responses, consent and authorization, source documents, validation abstraction/adjudication, paradata, logs, analytic data, releases, and backups | Decision required |
| D6 | Tested configuration proving no intentional IP, device-fingerprint, advertising-ID, or third-party analytics collection | Pending platform selection and validation |
| D7 | Incident-response and participant/clinic/IRB notification procedure | Draft required; contacts pending |

### E. Requirements for each clinic

| # | Item | Status |
|---|---|---|
| E1 | Legal name, address, authorized representative, privacy/legal contact, and campaign operator | Pending clinic |
| E2 | Documentation of at least 500 unique ASD-diagnosed patients plus a frozen count of the broader complete contactable clinic patient/guardian distribution population, including patients without an ASD diagnosis | Pending clinic activation |
| E3 | Local authorization to use clinic contact information to distribute the study invitation and reminders | Pending clinic privacy/legal authority |
| E4 | Local IRB/exemption/reliance or non-engagement determination required by the reviewing model | Pending clinic/IPAK-EDU |
| E5 | Executed participation/payment agreement and letter of cooperation | Pending parties |
| E6 | Approved complete distribution list method and confirmation that no recipient identity is disclosed to CHD | Pending clinic |
| E7 | Aggregate initial/reminder delivery metrics and undeliverable/opt-out counts | Pending campaign completion |
| E8 | Signed certification of complete, nonselective distribution and material compliance | Pending campaign completion |

### F. Release requirements

| # | Item | Status |
|---|---|---|
| F1 | Independent qualified disclosure-risk expert or qualifying engagement | Required during protocol/instrument finalization, before outcome data are available |
| F2 | Expert determination on the exact proposed release file and required transformations | Pending final file |
| F3 | Controlled-access operator, access committee, application, DUA, security requirements, and enforcement | Draft/process required; operator pending |
| F4 | Public repository for protocol, closed survey instrument, codebook, aggregate results, code, synthetic data, metadata, and change log | Pending selection |
| F5 | Final quality report, disclosure review, PI authorization, dataset version/DOI, license, and correction contact | Pending each release |

### G. Operational gates

- **Before IRB submission:** close material B decisions; identify the
  proposed platform and security architecture; complete required CHD
  personnel, funding, compensation, and COI disclosures; and obtain
  IPAK-EDU submission/service information. Engage the disclosure-risk
  expert early enough for provisional release rules to inform the final
  instrument, data dictionary, and consent.
- **Before clinic recruitment beyond IRB-permitted feasibility contact:**
  obtain the applicable IPAK-EDU determination and use only approved
  clinic materials.
- **Before clinic activation:** execute the agreement; confirm the
  500-patient threshold, lawful distribution authority, local regulatory
  pathway, and technical capability.
- **Before parent recruitment:** approve and test the exact invitation,
  reminders, consent/parental permission, survey, coded contact and final-review workflow, validation authorization, privacy
  notices, and platform configuration.
- **Before data collection:** verify role access, security controls,
  retention settings, paradata settings, tracking prohibition, and
  incident procedures.
- **Before any exact row-level public release:** complete F1–F2. If the
  expert does not approve the proposed file, release only approved
  aggregates, code, synthetic data, and controlled-access materials.
