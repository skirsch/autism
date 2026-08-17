# CHD Multisite SORA Parent Survey

## Complete Draft Electronic Instrument and Branching Specification

**Document status:** Draft IRB attachment; not approved for deployment  
**Instrument version:** 0.1  
**Date:** 13 August 2026  
**Related planning document:** `00_CHD_SORA_Study_Executive_Summary.md`, Version 0.32

## 1. Instrument principles

This instrument is designed for electronic administration on mobile and
desktop devices. Questions appear progressively. Field names shown in
backticks are implementation names and are not displayed to parents.

- No eligibility or health response is retained before affirmative
  consent and parental permission.
- The invitation and landing page are neutral, but the consent page
  identifies CHD and plainly discloses the developmental and vaccination-
  timing subject matter before enrollment.
- The onset reconstruction appears before detailed vaccination questions.
- Pre-survey causal beliefs and later vaccination decisions are asked
  only after primary timing questions.
- No child name, date of birth, onset calendar date, vaccination calendar
  date, medical-record number, or unrestricted narrative is collected in
  the main survey.
- A required parent email is stored in a segregated contact table, not in
  the coded research export.
- A separate authorization and restricted workspace are used if a
  randomly selected parent later agrees to record validation.
- “Prefer not to answer” and “Not sure” are never recoded as “No.”

Estimated completion time must be inserted only after timed usability
testing. The invitation must not promise five minutes unless testing
supports that statement for the relevant survey branch.

## 2. Clinic invitation and landing page

### 2.1 Clinic invitation

> **Help improve objective information about childhood development**
>
> [Clinic name] is inviting parents and legal guardians in our patient
> community to consider a brief research survey about childhood
> development and health events. Accurate information is important
> whether or not your child experienced a developmental change. Taking
> part is voluntary and will not affect care or benefits.
>
> Most participants complete the applicable questions in approximately
> **[insert validated completion-time estimate]**.
>
> Select the link below when you have time to read about the study and
> decide whether to participate.

The invitation must not promise a desired finding or state that the clinic
endorses CHD’s positions. It must include the clinic’s ordinary opt-out
instructions and the approved study link.

### 2.2 Landing page

> **Parent survey about childhood development and health events**
>
> Thank you for considering this research survey. The next page explains
> who is conducting the study, what questions are asked, how information
> will be protected, and your choices.

Button: **Learn about the study / Start**

`landing_viewed` and `start_selected` may be retained only as approved,
privacy-minimized operational events. Selecting Start is not consent.

## 3. Information, consent, and parental permission

The final consent must be approved by IPAK-EDU IRB. The following is the
required content and proposed parent-facing text; bracketed institutional
details remain to be completed.

### 3.1 Key information

> **Invitation to take part in research**
>
> Children’s Health Defense (CHD) is sponsoring this research. Brian
> Hooker, Ph.D. [confirm title and affiliation], is the coordinating
> principal investigator. Your clinic sent you the invitation but has not
> given CHD its patient mailing list.
>
> The study asks about your child’s autism diagnosis, developmental
> history, sudden behavioral or developmental changes, vaccination
> history, and the timing between these events. It is intended to create
> a carefully documented dataset for descriptive and independent
> analysis. This survey cannot by itself determine whether vaccination
> caused or did not cause a developmental change.
>
> Participation takes approximately **[validated estimate]** for the
> applicable branch. Participation is voluntary. You may skip optional
> questions or stop. Your decision will not affect your child’s care,
> benefits, or relationship with the clinic.

### 3.2 What participation involves

> You will answer structured questions about one child. If you report
> more than one child, complete a separate survey for each child. We ask
> for your email so authorized study staff can process a withdrawal,
> resolve a mechanical ambiguity securely, identify possible duplicate
> submissions, or invite a randomly selected subset to optional record
> validation.
>
> Your email is stored separately from survey answers and linked by a
> random survey code. The working data are coded, not anonymous. Your
> clinic will not receive your individual answers or be told whether you
> participated. Authorized study staff may perform a documented linkage
> for the limited purposes described above.
>
> If randomly selected for validation, you may decline without affecting
> your survey response. No record will be requested or uploaded without a
> separate information and authorization process.

### 3.3 Risks, benefits, and data use

> Possible risks include discomfort when recalling your child’s history
> and loss of privacy if coded information were accessed improperly.
> Security controls and restricted access reduce but cannot eliminate
> this risk. There is no expected direct benefit to you or your child.
>
> Researchers plan to publish the protocol, survey, aggregate findings,
> and a disclosure-reviewed dataset. Names, emails, authorization forms,
> source records, and calendar dates will not be released. If independent
> review finds that row-level public data could identify someone, only
> protected aggregate, synthetic, or controlled-access information will
> be released. Publicly released information cannot be recalled.
>
> CHD’s role, funding source(s), clinic compensation, and relevant
> investigator interests are disclosed here: **[insert final disclosures]**.

### 3.4 Contact and withdrawal

> Questions about the study: **[study contact]**  
> Questions about research rights: **[independent IRB contact]**  
> Privacy or security concerns: **[privacy contact]**
>
> You may request withdrawal while the study retains the email-to-survey
> link and before the applicable analysis or release cutoff. The final
> consent will state the cutoff, treatment of partial responses, audit
> records and backups, and the limits after data have been locked,
> de-linked, or released.

### 3.5 Affirmative decisions

`adult_age_confirm`

> I confirm that I am 18 years of age or older.

- Yes
- No → exit without retaining substantive responses

`adult_research_consent`

> I have read the information above. I understand that this is research,
> that participation is voluntary, and that the survey asks about
> development and vaccination timing. I agree to participate.

- Yes, I agree
- No, I do not agree → optional decline path, then exit

`parental_permission`

> I am the child’s parent or legal guardian and give permission for the
> study to collect and use the information I provide about this child as
> described above.

- Yes, I give permission
- No → optional decline path, then exit

The system records consent version and timestamp in the restricted consent
record. It does not retain pre-consent health answers.

### 3.6 Optional decline reason

Display only after a consent or permission decline. Retain only under the
IRB-approved authority.

`decline_reason`

> You do not need to explain. If you wish, what is the main reason you
> chose not to participate?

- Not interested
- Too busy right now
- Privacy concerns
- Do not want to answer questions about development or autism
- Do not want to answer questions about vaccination
- My child does not have a relevant developmental history
- Another reason / prefer not to say

No free-text box is displayed.

## 4. Contact and respondent eligibility

`parent_email`

> Enter the email address that authorized study staff may use for the
> limited study purposes described in the consent.

- Email field; required

`parent_email_confirm`

> Enter the same email again.

- Must match; required

The email is written only to the restricted contact store. The research
table receives `survey_id`, not the email.

`respondent_relationship`

> What is your relationship to the child described in this response?

- Parent with current legal authority
- Other legal guardian
- Parent without current legal authority
- Other caregiver
- Prefer not to answer

Only the first two categories continue unless the IRB approves a broader
knowledgeable-caregiver rule.

`direct_knowledge_onset`

> Did you personally observe the child’s development during the period
> when the earliest concerning change may have occurred?

- Yes
- No
- Not sure

No/Not sure responses may contribute to approved recruitment-flow counts
but do not enter the SORA timing cohort.

`prior_submission_same_child`

> Have you previously submitted this survey for this child?

- No
- Yes
- Not sure

`other_guardian_submission`

> To your knowledge, may another parent or guardian already have submitted
> this survey for this child?

- No
- Yes
- Not sure

`multiple_clinic_invitation`

> Did you receive an invitation to this survey from more than one clinic?

- No
- Yes
- Not sure

These answers create duplicate-risk flags, not automatic exclusions.

## 5. Diagnosis and broad developmental pattern

`clinical_asd_diagnosis`

> Has this child received a clinical diagnosis of autism spectrum disorder
> from a qualified healthcare professional?

- Yes
- No
- Not sure

`developmental_pattern`

> Which statement best describes the child’s overall developmental
> pattern? Choose the closest answer.

- Development was atypical or delayed from the earliest period I can
  recall, without a later loss of existing behavior or skill
- Development progressed and then reached a plateau, without an obvious
  loss of an existing behavior or skill
- Development was typical or met expected milestones and then an abrupt,
  obvious drop occurred
- Development was typical or met expected milestones and then a gradual
  decline occurred
- Another pattern
- Not sure

Ask this item of all consented respondents. If ASD diagnosis is No or Not
sure, record the approved screening information, do not collect detailed
vaccination timing, and proceed to Section 13.

`highest_asd_support_level`

> What is the highest ASD support level ever diagnosed for this child, if
> known?

- Level 1
- Level 2
- Level 3
- ASD was diagnosed but no support level is known/documented
- Not sure
- Prefer not to answer

Do not use “mixed.” Record the highest diagnosed level reported.

`child_sex`

> What sex was recorded for the child at birth?

- Female
- Male
- Intersex
- Unknown
- Prefer not to answer

## 6. Discrete onset and SORA screen

Display to respondents reporting a clinical ASD diagnosis.

> In this survey, **Day 0** means the recognizable day on which the first
> obvious, dramatic, and persistent change began. A parent may remember
> that it was a discrete day without remembering the historical calendar
> date. Day 0 does not mean a change that became apparent only gradually
> over weeks.

`abrupt_persistent_change`

> Did the child experience an abrupt, obvious change that persisted for at
> least 30 days or was still present at a later clinical evaluation?

- Yes
- No
- Not sure

`discrete_day0`

> Can you distinguish a discrete onset day from a gradual period of
> change, even if you cannot remember the calendar date?

- Yes
- No
- Not sure

Only Yes continues through the detailed SORA timing branch. Others proceed
to Section 13 after the limited screen.

For each category below, first ask whether it began on Day 0, then whether
it was observed at any time from Day 0 through Day 6 inclusive. Day 0 is
the first of the seven days; Day 7 is outside the window.

### 6.1 New pathological behavior

> This means acquiring a new behavior that was clearly pathological or
> harmful, rather than simply losing an existing skill.

`new_pathological_behavior_day0`

> Did a new pathological behavior begin on Day 0?

- Yes
- No
- Not sure

`new_pathological_behavior_within_7d`

> Was a new pathological behavior observed at any time from Day 0 through
> Day 6?

- Yes
- No
- Not sure

### 6.2 Loss of an existing behavior or skill

`loss_existing_behavior_or_skill_day0`

> Did the child lose an existing behavior or skill beginning on Day 0?

- Yes
- No
- Not sure

`loss_existing_behavior_or_skill_within_7d`

> Was loss of an existing behavior or skill observed at any time from Day
> 0 through Day 6?

- Yes
- No
- Not sure

### 6.3 Change in sensory sensitivity

`change_in_sensory_sensitivity_day0`

> Did an obvious change in sensitivity to sound, light, touch, taste,
> smell, pain, temperature, or another sensory input begin on Day 0?

- Yes
- No
- Not sure

`change_in_sensory_sensitivity_within_7d`

> Was an obvious change in sensory sensitivity observed at any time from
> Day 0 through Day 6?

- Yes
- No
- Not sure

At least one Day 0 category must be Yes for SORA eligibility. A response
cannot be Yes within seven days while all three Day 0 categories are No;
display a neutral review prompt rather than silently changing the answer.

`change_persistence`

> Which best describes how long the qualifying change continued?

- Continued for at least 30 days
- Was still present at a later clinical evaluation
- Resolved within 30 days
- Not sure

The first two satisfy persistence.

## 7. Onset age, recall horizon, and timing anchors

`onset_before_fifth_birthday`

> Did Day 0 occur before the child’s fifth birthday?

- Yes
- No
- Not sure

Only Yes enters the primary SORA resource.

`age_at_onset_value` and `age_at_onset_unit`

> What was the child’s age on Day 0? Enter the best value you know and
> choose its unit. Do not enter a birth date or calendar date.

- Number
- Unit: days / weeks / months / years
- I know only a range
- Not sure

If range only, `age_at_onset_range`:

- Younger than 6 months
- 6–11 months
- 12–17 months
- 18–23 months
- 24–35 months
- 36–47 months
- 48 months through the day before the fifth birthday
- Not sure

`onset_precision`

> How precisely can you identify Day 0?

- Exact day
- Within 1–2 days
- Within 3–7 days
- Only a broader period
- Not sure

`day0_confidence`

> How confident are you that you can distinguish the discrete Day 0?

- Very sure
- Somewhat sure
- Not very sure
- Not sure

`elapsed_since_onset`

> Approximately how long ago did Day 0 occur?

- Less than 1 year ago
- 1–2 years ago
- 3–5 years ago
- 6–10 years ago
- 11–20 years ago
- More than 20 years ago
- Not sure

`onset_information_sources` — select all:

> What information did you consult or rely on to identify Day 0?

- Calendar
- Date-stamped photo or video
- Parent message or email
- Clinical or patient-portal record
- Therapy, school, or childcare record
- Family event or holiday
- Vaccination record or vaccination event
- Another documented event
- Unaided memory
- Not sure

`vaccination_helped_anchor_onset`

> Before answering the detailed vaccination questions below, did your
> memory of a vaccination help you identify or reconstruct Day 0?

- Yes
- No
- Not sure

This question measures the timing anchor; it does not determine whether
the recalled date is correct or incorrect.

## 8. Vaccination timing

> The following questions ask about vaccinations that were administered,
> not what you believe caused the change. Please consult a vaccination
> card, registry, portal, or other record if readily available. Do not
> enter calendar dates.

### 8.1 Most recent vaccination before onset (Dpre)

`vaccination_before_onset`

> Was any vaccination administered before Day 0?

- Yes
- No
- Not sure

If Yes:

`dpre_precision`

> Can you report the elapsed time from the most recent vaccination before
> onset to Day 0 as an exact number of complete 24-hour periods?

- Yes, exact number
- No, range only
- Not sure

If exact, `dpre_days`:

> How many complete 24-hour periods elapsed after that vaccination before
> Day 0 began?

- Whole number 0 or greater

Help text: `0` means the parent reports that vaccination occurred first
and Day 0 began less than 24 hours later. It does not mean that event order
is unknown.

If range, `dpre_range`:

- Less than 1 day
- 1–2 days
- 3–4 days
- 5–7 days
- 8–14 days
- 15–30 days
- 31–90 days
- More than 90 days
- Not sure

`dpre_source`

> What did you use for this vaccination-timing answer?

- Vaccination card
- Immunization registry
- Patient portal or pediatric record
- Another contemporaneous record
- Memory without consulting a record
- Another source
- Not sure

`dpre_confidence`

- Very sure
- Somewhat sure
- Not very sure
- Not sure

### 8.2 First vaccination after onset (Dpost)

`dpost_status`

> Was a vaccination administered after Day 0?

- Yes
- No, and there was enough follow-up to know
- No follow-up sufficient to know
- I do not know

If Yes, repeat exact-versus-range, source, and confidence questions as
`dpost_precision`, `dpost_days` or `dpost_range`, `dpost_source`, and
`dpost_confidence`.

Help text: `dpost_days = 0` means the parent reports that Day 0 occurred
first and vaccination followed less than 24 hours later. If event order
cannot be established, code the applicable timing as unknown rather than
assigning Dpre or Dpost.

## 9. Other acute events around Day 0

`acute_events_near_onset` — select all:

> Which of these occurred within 5 days before onset?

- Febrile seizure
- Illness
- Vaccination
- Pediatrician wellness appointment
- Dentist visit
- Tylenol
- Fever
- New medication started
- Anesthesia
- None of the above
- Not sure/don't remember

For each selected event, ask:

- `acute_event_order`: before Day 0 / same calendar day / after Day 0 /
  order unknown
- `acute_event_precision`: exact complete 24-hour periods / range / unknown
- exact value or the same structured ranges used for Dpre/Dpost
- `acute_event_source`: contemporaneous record / memory / another source /
  unknown
- `acute_event_confidence`: Very sure / Somewhat sure / Not very sure /
  Not sure

The SAP must define the maximum event window before deployment. No free
text is collected.

## 10. Pre-survey causal beliefs

Ask only after Sections 6–9 are complete.

`presurvey_contributor_beliefs` — select all:

> Before beginning this survey, had you formed an opinion about what may
> have contributed to the child’s developmental condition or change?

- Genetic or inherited factors
- Prenatal or birth-related factors
- Infection or illness
- Medication, anesthesia, or another medical event
- Vaccination
- Environmental exposure
- Psychosocial or life event
- Another factor
- I believed no particular event caused it
- I was uncertain
- I had not previously considered the cause
- Prefer not to answer

Mutually exclusive choices—no particular event, uncertain, had not
considered, and prefer not to answer—cannot be combined with causal-factor
selections.

`presurvey_vaccine_attribution_strength`

> Before beginning this survey, how strongly did you believe vaccination
> contributed to the child’s developmental condition or change?

- Definitely contributed
- Probably contributed
- Unsure
- Probably did not contribute
- Definitely did not contribute
- Had not considered it
- Prefer not to answer

`timing_contributed_to_vaccine_belief`

> Before beginning this survey, did the timing between vaccination and
> the developmental change contribute to your opinion about vaccination?

- Yes
- No
- Not sure
- Not applicable / no prior opinion
- Prefer not to answer

These variables characterize prior attribution. They do not classify
someone as “antivaccine” and do not form an unbiased causal control group.

## 11. Vaccination after onset and changes in the plan

`post_onset_vaccination_plan`

> After Day 0, what happened with the child’s vaccination plan?

- Continued according to the existing plan
- Continued, but one or more vaccinations were delayed
- Continued, but one or more vaccinations were declined
- All further vaccinations were stopped
- No vaccination decision was required afterward
- Not sure
- Prefer not to answer

If delayed, declined, or stopped, `post_onset_plan_reasons` — select all:

> What contributed to that decision?

- Concern that vaccination might be related to the developmental change
- Advice from a healthcare professional
- The child’s illness or medical condition
- A previous reaction or adverse event
- Change in access, insurance, or healthcare provider
- General vaccination concerns that existed before the developmental
  change
- General vaccination concerns that began after the developmental change
- No additional vaccination was recommended or due
- Another reason
- Prefer not to answer

No free-text box is displayed.

## 12. Final review and submission

Display a plain-language summary of:

- ASD diagnosis and highest level;
- broad developmental pattern;
- whether a discrete Day 0 was reported;
- Day 0 age and precision;
- three Day 0 and seven-day SORA-category answers;
- Dpre and Dpost interpretation, including event order;
- information sources and confidence; and
- acute-event answers.

> Please review these answers. Correct anything that does not reflect what
> you intended. Unexpected answers are allowed and will not be changed by
> the study team.

Buttons:

- **Return and edit**
- **Submit my survey**

`final_submit_confirm`

> I confirm that these answers reflect my best knowledge. I understand
> that authorized staff may contact me only for the purposes described in
> the consent and that I may or may not later be randomly invited to
> optional record validation.

- Confirm and submit

After submission, display the random `survey_id`, withdrawal instructions,
study and IRB contacts, and a link to save the consent information. Do not
display aggregate or preliminary timing results.

## 13. Limited completion path for respondents without confirmed ASD or SORA

Respondents who do not report confirmed ASD, direct knowledge, persistent
abrupt change, discrete Day 0, onset before the fifth birthday, or at least
one Day 0 category do not receive detailed vaccination-timing questions.
With consent, retain only the prespecified screening, developmental-pattern,
completion, and missingness fields necessary for recruitment accounting.

Display:

> Thank you. Based on your answers, the detailed timing questions do not
> apply to this response. Your answers remain valuable for describing who
> received and completed the survey.

Then proceed to final submission. Whether the causal-belief questions are
shown on this limited path must be fixed in the SAP; the recommended
default is not to collect them when detailed timing was not collected.

## 14. Random validation follow-up module

This module is not displayed during the main survey. Reproducible software
selects eligible respondents under the locked sampling plan after the
survey-response lock. Contact staff send a neutral invitation without
substantive health information in ordinary email.

The validation module must include:

1. separate information and affirmative authorization;
2. identity fields only to the extent required to retrieve or reconcile
   an authorized record, stored only in the validation workspace;
3. choice to upload a vaccination card, registry extract, portal record,
   or comparable administered-vaccination record, or authorize limited
   retrieval from a lawful source;
4. optional upload of approved contemporaneous onset evidence;
5. explicit ability to decline validation without removing the main
   survey response; and
6. secure confirmation and contact instructions.

The authorization form and record-request specification will be separate
IRB attachments because their required language depends on the selected
vendor, providers, jurisdictions, and HIPAA determinations.

## 15. Branching and eligibility summary

1. Landing page → Start.
2. Adult consent and parental permission required before retained health
   data.
3. Required email is segregated from research responses.
4. Broad developmental pattern is asked of all consented respondents.
5. Confirmed clinical ASD is required for the detailed SORA branch.
6. Detailed timing requires direct knowledge, persistent abrupt change,
   discrete Day 0, onset before the fifth birthday, and at least one SORA
   category beginning on Day 0.
7. Onset reconstruction and anchor questions precede detailed vaccination
   questions.
8. Causal-belief and vaccination-plan questions follow primary timing and
   competing-event questions.
9. Final review precedes submission.
10. Validation is randomized and separately authorized after survey lock.

## 16. Required automated checks

- email confirmation matches;
- no health response persists after declined consent;
- mutually exclusive choices cannot be combined;
- at least one Day 0 category is Yes for SORA eligibility;
- a Day 0 category cannot be Yes while its corresponding seven-day field
  is No without a review prompt;
- onset-before-fifth-birthday response agrees with age entry or generates
  a review prompt;
- exact interval is a whole number 0 or greater;
- Dpre 0 displays vaccination-first language;
- Dpost 0 displays onset-first language;
- unknown event order is not assigned to Dpre or Dpost;
- exact and ranged values cannot both be stored as the final response;
- No vaccination and Unknown remain distinct;
- No post-onset vaccination, inadequate follow-up, and unknown remain
  distinct;
- plan-change reasons display only for delayed, declined, or stopped
  vaccination;
- parent may review and correct answers before final submission; and
- no unexpected value is silently altered or excluded.

## 17. Paradata specification

Subject to IRB approval, retain only:

- landing-page view and Start selection;
- consent decision and approved decline reason;
- section and question reached;
- answered, skipped, review-prompt, correction, and breakoff indicators;
- completion status; and
- coarse section duration with idle time excluded.

Do not intentionally retain IP address, precise location, device
fingerprint, advertising identifier, session replay, keystrokes, or third-
party tracking data as research variables. Operational security logs must
be segregated and deleted under the approved schedule.

## 18. Analysis cautions attached to the instrument

- Prior vaccine attribution, vaccination anchoring, and post-onset
  vaccination decisions are prespecified bias-characterization variables.
- Continued vaccination is a post-onset behavior and is not an unbiased
  control condition.
- The intersection of no prior vaccine attribution, a non-vaccination
  anchor, and continued vaccination may be reported as a sensitivity
  subset only if sample size and disclosure review permit.
- Subgroups require denominators and uncertainty intervals and cannot be
  selected because their results appear stronger.
- Parent-reported ASD, onset, and timing remain parent-reported unless
  separately validated.
- Missing, Not sure, and Prefer not to answer are never interpreted as No.

## 19. Items requiring resolution before IRB submission

- validated median and upper-quartile completion time for each branch;
- final sponsor, funding, compensation, conflict, contact, and withdrawal
  language;
- whether parent without current legal authority or another knowledgeable
  caregiver may participate;
- treatment of reports concerning deceased children;
- exact competing-event window;
- handling of limited-path causal-belief questions;
- consent documentation or waiver of signed documentation;
- approved treatment of post-consent partial responses;
- selected survey and storage vendor, access roles, retention, deletion,
  and incident procedures;
- final validation authorization and record-request language;
- cognitive interviews and mobile/desktop usability results;
- translations and accessibility accommodations; and
- final IPAK-EDU IRB edits and approval.
