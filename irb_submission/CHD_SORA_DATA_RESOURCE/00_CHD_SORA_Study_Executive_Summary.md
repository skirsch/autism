# CHD Multisite SORA Data-Resource Study

## Executive Summary and Study Definition

**Document status:** Planning summary for development of the IRB submission packet  
**Version:** 0.11
**Date:** 12 August 2026

## 1. Study identity

| Item | Proposed specification |
|---|---|
| Working title | Multisite Data Resource of Sudden-Onset Regressive Autism (SORA) |
| Coordinating principal investigator | Brian Hooker, Ph.D. [confirm exact degrees, title, and CHD affiliation]; has accepted this role |
| Sponsor/coordinating organization | Children's Health Defense (CHD) [confirm legal entity]; has accepted this role |
| Participating sites | The first 10 qualifying clinics to complete all activation requirements |
| Study type | Retrospective, multisite medical-record data-resource study |
| Primary purpose | Create, validate, document, and release a privacy-protected dataset for subsequent independent analysis |
| Initial publication | Dataset/cohort descriptor, data-quality report, and basic descriptive summaries—not a causal analysis |
| Participant contact | None |
| Intervention | None |
| Proposed regulatory pathway | Exempt secondary research under 45 CFR 46.104(d)(4), subject to IPAK-EDU IRB's determination and site-specific requirements |
| Reviewing IRB | IPAK-EDU IRB |
| Key coordinating personnel | See Section 2 |

## 2. Key personnel

Named coordinating roles are assigned as follows. Credentials, training,
and conflict-of-interest disclosures will be confirmed before IRB
submission. Site investigators and clinic abstractors are designated at
activation and are not listed here.

| Role | Person | Responsibility | Access |
|---|---|---|---|
| Coordinating principal investigator | Brian Hooker, Ph.D. [confirm exact degrees, title, and CHD affiliation] | Protocol compliance, site activation authority, reporting, and communication with the reviewing IRB | Clinic identity as needed for activation and IRB reporting; de-identified study files as required for PI oversight. No mapping key or identifiable charts unless a separately authorized audit permits it |
| Site outreach / activation | Ben Jackson; Mila Radetich | IRB-approved clinic contact, site-eligibility screening, activation queue, and replacement of sites that withdraw before submission | Clinic names, contacts, and contracting only. No row-level SORA or timing data |
| Data manager / quality monitor | Karl Jablonowski; Steve Kirsch | Receipt of submitted files, mechanical sanity checks, queries by `clinic_row_id`, version control, and data-quality reporting | De-identified submitted files only. No mapping key, identifiable charts, or family contact |
| CHD data custodian | TBD | Approved storage environment, access control, retention, and incident response | System administration of the approved environment; not a substitute for clinic source-record access |

Outreach staff will not receive row-level timing values and will not
select, exclude, add, or replace clinics because of preliminary results.
Data managers will apply the mechanical checks in Section 9; they will
not open source charts to alter values. The clinic site investigator
remains responsible for source-record verification.

## 3. Study objective

The study will create a multisite research resource describing age at
parent-recognized onset and vaccination proximity among children
meeting the sudden-onset regressive autism (SORA) definition.
Participating clinics will identify all qualifying records within a
retrospective ascertainment period whose source population, search
method, and dates are documented and locked before clinic personnel
calculate or review vaccination-proximity values. Clinics will verify
eligibility locally, derive the approved variables, and transmit a
restricted electronic dataset without direct identifiers or calendar
dates.

CHD's initial work will be limited to cohort construction, validation,
data documentation, and descriptive characterization sufficient to
establish the provenance, completeness, and usability of the resource.
The initial study will not test or claim that vaccination causes autism.
Subsequent investigators may conduct separately documented and, where
appropriate, preregistered analyses using an approved public-use or
controlled-access version of the dataset.

## 4. Operational definition of SORA

For this study, SORA is an abrupt, dramatic, and persistent change first
recognized by a parent or primary caregiver in a child whose prior
development had been described as typical or meeting expected
milestones. The caregiver must have identified a specific calendar date
on which the first obvious persistent change began. That source date is
used locally but is not transmitted. Parent-recognized SORA onset must
occur from birth through 60 completed months of age.

The child must exhibit a dramatic rapid change in at least one of the
following three categories:

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
irritability, appetite change, sleep disturbance, or other short-lived
symptoms alone do not qualify. The child must subsequently have a
documented ASD diagnosis by a qualified clinician. A documented DSM-5
support level is not required for eligibility because it may be absent
or reported separately by domain.

Example: if loss of language becomes obvious and persistent on Day 0
and a new pathological behavior first appears on Day 4, both
corresponding seven-day fields are coded `Yes`, but Day 0 remains the
single SORA onset date. A change that becomes obvious only gradually
over several weeks does not qualify.

## 5. Clinic enrollment

CHD will use IRB-approved clinic-outreach materials to identify
prospective sites. The study will enroll the first 10 clinics that:

- meet the prespecified site eligibility criteria;
- designate a responsible site investigator;
- agree to perform complete rather than selective ascertainment;
- demonstrate adequate medical and vaccination records;
- complete required IRB, privacy, contracting, training, and data-
  security documentation; and
- are formally activated by the coordinating study.

Sites will be ordered by the date all activation requirements are
completed. An expression of interest does not reserve a position. If an
activated site withdraws before submitting data, the next fully
qualified site in activation order may replace it. Sites will not be
selected, excluded, added, or replaced because of preliminary timing
values or results.

The target is 10 activated clinics. If fewer than 10 clinics complete
activation by the recruitment closing date, the study may proceed with
all activated clinics only if at least two clinics have activated. The
shortfall and reasons will be reported. A clinic that withdraws after
submitting data will not be silently removed or replaced; retention or
destruction of its submitted data will follow its agreement and IRB
requirements. Any replacement will be documented and may not depend on
observed data.

Feasibility discussions may occur before approval if permitted by the
reviewing IRB, but no research-specific chart screening, abstraction,
or data transfer may begin until the applicable written determinations
and site activation are complete.

## 6. Record ascertainment and enrollment

Each site will define and lock its ASD source population, search method,
record-system start date, and ascertainment end date before examining
study timing results. Each site must apply the common eligibility
criteria to all candidate records and submit every eligible record from
that period. Sites may not submit only memorable cases or cases selected
because onset occurred close to vaccination.

There is no minimum number of records required from an individual site
and no outcome-based total sample-size target. The total resource will
contain all validated eligible records contributed by the activated
sites by the prespecified data cutoff. A site that identifies no
eligible records remains part of the study flow and will be reported as
a zero-case site. Withdrawals, exclusions, missing submissions, and
zero-case sites will be disclosed.

## 7. Patient-level data elements

The proposed transmitted record contains only the following fields:

| Field | Definition |
|---|---|
| `site_code` | Study-assigned site code; clinic identity mapping is restricted |
| `clinic_row_id` | Arbitrary clinic-issued code not derived from patient information; linkage retained only at clinic |
| `sex` | Clinic-recorded value: Female, Male, Intersex, or Unknown/not recorded; never inferred |
| `age_at_onset_days` | Whole days of age on the parent-recognized onset date, calculated locally; permitted range 0–1,826 days |
| `new_pathological_behavior_within_7d` | Whether the parent/caregiver reported acquisition of at least one new persistent pathological behavior during the seven-day period beginning on the SORA onset date |
| `loss_existing_behavior_or_skill_within_7d` | Whether the parent/caregiver reported loss or marked diminution of at least one existing behavior or acquired skill during the seven-day period beginning on the SORA onset date |
| `change_in_sensory_sensitivity_within_7d` | Whether the parent/caregiver reported a marked persistent change in sensitivity or response to sensory input during the seven-day period beginning on the SORA onset date |
| `asd_support_level` | Highest documented ASD support level: 1, 2, 3, or not documented; never inferred |
| `vaccination_before_onset` | `Yes`, `No`, or `Unknown/insufficient records`, using the rules below |
| `dpre_days` | Days from the most recent documented vaccine administration before/on onset to onset; populated only when vaccination-before-onset is `Yes` |
| `dpost_status` | `Documented later vaccination`, `Adequate follow-up/no later vaccination documented`, or `Insufficient follow-up/unknown` |
| `dpost_days` | Days from onset to the first documented vaccine administration afterward; populated only when `dpost_status` is `Documented later vaccination` |

The allowed values for each of the three SORA-category fields are `Yes`,
`No`, and `Not documented`. The seven-day period is Day 0, the specific
parent-recognized SORA onset date, through Day 6. `Yes` requires record
documentation that the qualifying dramatic and persistent change was
observed during that period. `No` requires documentation sufficient to
establish that the category was not observed during the period. Missing
or ambiguous documentation is coded `Not documented`, never `No`.

At least one of the three SORA-category fields must be `Yes`, and the
first qualifying obvious persistent change must begin on the specific
Day 0 onset date. The seven-day fields may capture additional categories
that emerge through Day 6; they do not permit a gradual or seven-day-
interval onset date. The site will retain the detailed behaviors,
clinical narrative, source dates, diagnostic report, and patient
mapping. CHD will not receive names, contact information, dates of
birth, calendar dates, medical-record numbers, free text, granular
geography, vaccine product information, or the linkage key.

The ASD support level is collected because it adds useful context at
minimal abstraction burden. It is optional and is not an eligibility
requirement. The clinic will report the highest ASD support level
documented in the available diagnostic record: 1, 2, or 3. If different
levels are documented by domain or across qualifying diagnostic
assessments, the highest documented level will be transmitted. If no
support level is stated, the value will be `not documented`. Clinic
staff will not infer a level from symptoms, services, or narrative.

The allowed values for `vaccination_before_onset` are:

- `Yes`: at least one administered vaccination before or on Day 0 is
  documented. `dpre_days` must contain a nonnegative integer.
- `No`: sufficiently complete records establish that no vaccination was
  administered before or on Day 0. `dpre_days` is coded `NA—not
  applicable`.
- `Unknown/insufficient records`: the available history cannot establish
  either answer. `dpre_days` is coded `NA—unknown history`.

Records with `Unknown/insufficient records` remain in the SORA data
resource and may contribute to age, category, sex, and ASD-support-level
descriptions, but they do not contribute to vaccination-proximity
summaries. Missing vaccination documentation is never coded `No`.

`dpost_status` distinguishes a documented later vaccination from
adequate follow-up with none documented and from insufficient follow-up.
Thus, absence of a Dpost interval does not imply that the child was
never vaccinated again. `dpost_days` is a nonnegative integer only when
a later administered vaccination is documented; otherwise it uses the
status-specific nonapplicable or unknown code.

## 8. Site-level information

Each site will submit an aggregate screening flow containing:

- number of unique candidate records screened;
- number eligible;
- number excluded under each protocol criterion;
- number of eligible/transmitted records with `Unknown/insufficient
  records` for vaccination-before-onset status; this is a subset of
  eligible records, not an exclusion;
- number of eligible records transmitted; and
- confirmation whether all eligible records were transmitted.

Each site will also submit four aggregate counts when they can be
calculated consistently:

1. all clinic patients with records sufficient to establish vaccination
   status through 24 months of age;
2. those patients with no documented vaccination through 24 months of
   age;
3. qualifying SORA cases with records sufficient to establish
   vaccination status through 24 months of age; and
4. those SORA cases with no documented vaccination through 24 months of
   age.

These are site-level counts, not patient-level records. Unknown or
incomplete histories will not be classified as unvaccinated. A child
whose SORA onset occurs after 24 months of age remains eligible for the
row-level resource and is included in the SORA aggregate denominator
when the record is sufficient to establish vaccination status through
24 months of age.

## 9. Data submission, validation, and source verification

Sites will enter data electronically into the approved workbook, CSV
template, or secure electronic data-capture system. Paper, scanned,
photographed, faxed, or ordinary-email submissions are prohibited.

CHD will perform mechanical validation, including required-field,
range, allowed-value, cross-field, duplicate-row, and interval checks.
CHD may return a query using the clinic row ID. The clinic will resolve
the query against its source records and return a correction or
confirmation. CHD personnel will not receive the mapping key or access
identifiable charts merely to verify a value. Any source-data audit
requiring identifiable access must be separately authorized by the
clinic and reviewing IRB.

## 10. Initial descriptive outputs

The initial dataset publication will describe rather than test causal
hypotheses. Prespecified outputs will include:

- sites approached, interested, activated, withdrawn, and contributing;
- screening, exclusion, eligibility, and submission counts by site;
- completeness and validation-query rates for every field;
- age-at-onset distribution;
- numbers meeting each of the three SORA change categories and every
  observed category combination;
- documented ASD support-level distribution;
- vaccination-before-onset counts;
- complete Dpre and Dpost distributions;
- Dpre counts and proportions for each observed day, subject to
  disclosure-protection requirements;
- median, interquartile range, range, and missingness for timing fields;
  and
- site-stratified descriptive displays where disclosure protections
  permit them.

The initial publication will not estimate how SORA onset would be
distributed in the absence of vaccination. It will not estimate a
causal effect, vaccine-attributable risk, population incidence, or a
confirmatory p value. Any analysis using selected cumulative Dpre
windows will be left to a separately documented subsequent analysis.

## 11. Data releases and access

The study will define a fixed initial data cutoff and publish all
validated submissions received from activated sites by that cutoff.
Release timing will not depend on the apparent Dpre distribution.
Every release will have a version number, cutoff date, participating-
site count, record count, data-dictionary version, validation report,
and change log.

Maximum responsible access is the goal, but unrestricted row-level
release is not guaranteed in advance. The default release structure is:

### Public materials

- protocol and abstraction manual;
- data dictionary and validation rules;
- aggregate screening and data-quality results;
- aggregate or appropriately binned descriptive tables;
- analytic code;
- synthetic demonstration data; and
- release metadata and change log.

### Exact row-level study data

Exact row-level data may be released publicly only if an independent,
qualified disclosure-risk expert documents that the risk of identifying
an individual is very small and approves the exact release file. The
expert may require removal or pooling of site codes, suppression of
cells smaller than 11, binning of age or timing values, or removal of
rare combinations. If unrestricted release cannot meet that standard,
exact data will be made available through a controlled-access process
with a research proposal, data-use agreement, security requirements,
prohibition on re-identification or linkage, prohibition on
redistribution, and end-of-use destruction requirements.

## 12. Governance and independence

Brian Hooker has accepted coordinating PI responsibility for protocol
compliance, site-activation authority, reporting, and communication
with IPAK-EDU IRB. Children's Health Defense has accepted the
sponsor and coordinating-organization roles. Ben Jackson and Mila
Radetich will conduct site outreach and activation. Karl Jablonowski
and Steve Kirsch will monitor submitted files and apply the mechanical
data-quality checks. The CHD data custodian is TBD. Each clinic will
designate a site investigator responsible for local record access,
eligibility, privacy compliance, and source verification. Role-specific
access limits are stated in Section 2.

CHD's mission, public positions, funding, and relevant investigator
financial and nonfinancial interests will be disclosed. Clinic
reimbursement, if any, will be limited to reasonable documented effort
and will not depend on the number of eligible cases, vaccination
proximity, findings, or publication. Funders will have no authority to
select records, access clinic linkage keys, suppress results, or control
publication.

## 13. Principal limitations

The resource will be a convenience sample of the first 10 qualifying
clinics to complete activation, not a random or nationally
representative sample. It will depend on retrospective records and
parent-recognized onset and may be affected by referral, recall,
documentation, diagnostic, and clinic-selection factors. The study can
describe the collected SORA cohort and generate hypotheses, but it
cannot by itself establish that vaccination caused regression or
estimate the incidence of SORA in vaccinated or unvaccinated children.

## 14. Punchlist for IRB-packet development

This punchlist separates facts CHD must supply, documents and protocol
decisions the study team can complete, and determinations or records
that must be issued by IPAK-EDU IRB or participating clinics. `Pending`
means the item genuinely depends on a named person or outside entity;
`Draft` means the study team can prepare it now; and `Fixed` means the
planning summary already establishes the controlling rule.

### A. Information and authorization CHD must provide

| # | Item | Status / completion evidence |
|---|---|---|
| A1 | Brian Hooker: exact degrees, title, CHD affiliation, email, telephone, mailing address, CV/biosketch, human-subjects/privacy training, and COI disclosure | Pending CHD/PI |
| A2 | Ben Jackson and Mila Radetich: exact titles/affiliations, contact information, applicable human-subjects/privacy training, and COI disclosures | Pending CHD/personnel |
| A3 | Karl Jablonowski and Steve Kirsch: exact titles/affiliations, contact information, applicable human-subjects/privacy training, and COI disclosures | Pending CHD/personnel |
| A4 | CHD data custodian: name, title, contact information, authority, and detailed responsibilities | Pending CHD |
| A5 | CHD privacy/security official and incident-response contact, if different from A4 | Pending CHD |
| A6 | Full legal name, legal status, address, and authorized institutional official for the CHD entity undertaking the research | Pending CHD |
| A7 | Signed institutional authorization naming CHD as sponsor/coordinating organization, Brian Hooker as PI, and the approved data custodian | Pending authorized CHD official; sponsor and PI acceptance reported but formal authorization still required |
| A8 | Complete funding and in-kind-support disclosure: each source, amount, mechanism, recipient, terms, and funder role | Pending CHD |
| A9 | Clinic reimbursement decision and, if applicable, effort-based schedule, budget justification, and payment terms unrelated to eligible-case count or results | Pending CHD |
| A10 | Official CHD financial and nonfinancial COI forms and any management plan, including organizational advocacy interests and relevant public positions | Pending CHD/IRB requirements |

### B. Protocol decisions and packet materials the study team must complete

These are work items, not facts to leave indefinitely TBD.

| # | Item | Status / controlling rule |
|---|---|---|
| B1 | Resolve the age boundary so the prose and validation rule are identical (`through 60 completed months` versus `0–1,826 days`) | Decision required before data dictionary |
| B2 | Final inclusion/exclusion criteria, including prior developmental concern, alternative explanatory diagnoses, conflicting reports, acceptable ASD diagnosis/clinician, diagnosis timing, and treatment of records of deceased children | **Substantial source draft exists;** revise to the current three-category data-resource design and close the listed decisions |
| B3 | Operational rule for “persistent,” including the minimum documentation or follow-up required to distinguish a persistent change from a transient symptom | **Partial source language exists;** a measurable final rule is still required |
| B4 | Vaccination abstraction rules: administered dates only, same-day administration/onset, multiple products on one date, outside records, adequate pre-onset history, and adequate post-onset follow-up | **Substantial source draft exists;** add the new three-state pre-onset and `dpost_status` rules |
| B5 | Duplicate-person rule for a child appearing at more than one clinic, without transferring identity or linkage keys | **New rule required** |
| B6 | Recruitment opening/closing dates, initial data cutoff, data-cleaning interval, and prospective rules for later versioned releases | CHD/PI decision required before submission |
| B7 | Secure submission method: approved workbook/CSV upload, electronic data-capture system, or both; ordinary email remains prohibited | **Workbook/CSV and secure-upload language already drafted;** CHD must name and approve the actual system |
| B8 | Retention, destruction, and access-review schedule | **Seven-year retention and quarterly review source draft exists;** confirm against CHD/IPAK policy |
| B9 | Site eligibility and activation checklist, activation-order log, zero-case-site rule, withdrawal/replacement record, and site-specific locked ascertainment form | **Partially drafted across existing protocol/recruitment/attestation materials;** consolidate and add activation-order and withdrawal forms |
| B10 | IRB-ready clinic outreach email, telephone script, feasibility-contact script, and “do not use before authorization” controls | **Substantial outreach and telephone source draft exists;** revise personnel, purpose, fields, first-10-site rule, and IPAK status |
| B11 | Clinic participation/data-transfer agreement and prohibition on releasing the patient mapping key or attempting re-identification | **Required terms already drafted;** convert them into a CHD agreement and obtain legal/IRB approval |
| B12 | Electronic patient-level collection instrument containing the approved fields and validation rules | **Working electronic workbook already exists;** rebuild its schema for the current category fields, ASD level, three-state vaccination status, and `dpost_status` |
| B13 | Data dictionary, SORA abstraction manual, worked examples, eligibility checklist, and reviewer-disagreement procedure | **Substantial instructions and definitions already drafted;** consolidate and revise for Version 0.11 decisions |
| B14 | Aggregate screening/exclusion log and four vaccination-status-through-24-months-of-age site counts | **Already drafted in the instrument and protocol;** revise eligibility reasons and terminology only |
| B15 | Clinic electronic attestation covering complete ascertainment, nonselective submission, row-ID construction, prohibited fields, and retention of source records/key | **Substantial attestation already drafted;** add the first-10-site/current-field and complete-ascertainment terms |
| B16 | Validation/query-resolution SOP: required-field, range, allowed-value, duplicate, and cross-field checks; clinic correction/confirmation; audit trail; no central chart access | **Validation rules and query principles partially drafted;** update the workbook builder and create the standalone SOP |
| B17 | Data-lock, version-control, correction, withdrawal, and retraction procedure, including treatment of data already included in an immutable public release | **Version-control concepts exist;** formal correction/withdrawal/retraction SOP is new |
| B18 | CHD security plan: named access owner, authorized roles, MFA, encryption, audit logs, backups, managed-device/download rules, quarterly access review, role-termination removal, incident reporting, and secure destruction | **Substantial privacy/security source draft exists;** replace generic infrastructure with the CHD system, custodian, and officials |
| B19 | Initial descriptive-output plan and reproducible code; selected Dpre windows remain outside the initial data-resource publication | Fixed in Sections 10–11; implementation required |
| B20 | Public-release and controlled-access governance: approval authority, access committee, application criteria, DUA, access duration, no linkage/re-identification/redistribution, destruction, dataset license, citation, corrections, and enforcement | **Public-release safeguards and DUA principles partially drafted;** controlled-access committee/process, license, and enforcement terms remain new; repository vendor may remain pending |
| B21 | Complete IRB protocol, application/cover form, waiver contingency, privacy/security plan, funding/COI disclosure, investigator roster, and attachment index | **A substantial complete packet and separate waiver/privacy/funding/personnel attachments already exist as source material;** restructure and revise them to the current CHD data-resource design after B1–B20 |

### C. IPAK-EDU IRB information and determinations

| # | Item | Status / completion evidence |
|---|---|---|
| C1 | Reviewing board identity | **Confirmed from OHRP database screenshot:** IPAK-EDU LLC IRB #1, IRB00014237, St. Clair Shores, OHRP/FDA type, Active as viewed 12 August 2026 |
| C2 | Exact IPAK-EDU legal/operator name, mailing address, IRB administrator/contact, submission instructions, fees, meeting/review schedule, and service agreement | Pending IPAK-EDU |
| C3 | IPAK-EDU confirmation that it will review this CHD-sponsored multisite data-resource study and accept Brian Hooker as coordinating PI | Pending written confirmation/service agreement |
| C4 | Primary requested pathway | Fixed request: exempt secondary research under 45 CFR 46.104(d)(4); packet must explain the proposed applicable subparagraph(s) without presuming the IRB's determination |
| C5 | Final determination of exempt/not-human-subjects/nonexempt status and applicable 45 CFR 46.104(d)(4) subparagraph | Pending IPAK-EDU determination |
| C6 | Whether and under what limits clinic feasibility outreach may occur before determination; no research-specific screening or transfer before authorization | Pending IPAK-EDU; script can be drafted under B10 |
| C7 | Whether IPAK-EDU will serve as reviewing/single IRB for engaged clinics, accept reliance, or review only CHD's coordinating activities | Pending IPAK-EDU and each clinic |
| C8 | Required investigator training, COI forms, continuing review/status reporting, amendments, deviations, unanticipated-problem reporting, and closure requirements | Pending IPAK-EDU policies |
| C9 | Contingency determinations if any activity is nonexempt: expedited category, waiver of informed consent under 45 CFR 46.116(f), waiver of parental permission under 45 CFR 46.408(c), assent not practicable, and HIPAA authorization waiver if applicable | **Substantial waiver justification already drafted;** revise to the current study. Final determinations remain pending IPAK-EDU/site decisions |
| C10 | Written determination/approval letter and approved/stamped study documents | Pending review; required before applicable research activity begins |

The OHRP registration establishes the board identity and active
registration shown in the supplied screenshot. It does not replace the
service agreement, confirm that IPAK-EDU accepts this protocol, or decide
the regulatory status of CHD or any clinic.

### D. Documents and determinations required for every participating clinic

Individual investigators and abstractors will be named during site
activation, but the templates and requirements must be included in the
central packet.

| # | Item | Status / completion evidence |
|---|---|---|
| D1 | Clinic legal name, address, site investigator, abstractors, privacy contact, and authorized signatory | Pending each site |
| D2 | Site investigator CV/biosketch and required human-subjects/HIPAA/privacy training; abstractor training and protocol competency | Pending each site |
| D3 | Site determination of whether it is a HIPAA covered entity and the lawful basis for research-specific local PHI access | Pending clinic privacy/legal authority |
| D4 | Site engagement determination and local IRB approval/exemption, IPAK-EDU reliance, or other documented pathway | Pending each site/IPAK-EDU |
| D5 | HIPAA authorization or waiver, if required for local PHI use, and waiver documentation if applicable | Pending each site/IRB/privacy authority |
| D6 | Pre-transfer HIPAA determination for the exact outbound file: Safe Harbor or Expert Determination, including actual-knowledge assessment | Pending each site privacy authority |
| D7 | Certification that `clinic_row_id` is not derived from patient information, is not otherwise translatable, and the re-identification mechanism/key will never be disclosed to CHD | Pending signed site attestation |
| D8 | Executed participation, data-transfer/data-use, reliance, business-associate, or other agreements required for that site's pathway | Pending parties |
| D9 | Locked source population, search method, record-system dates, ascertainment dates, and complete-case commitment established before timing review | Pending site activation |
| D10 | Letter of cooperation and confirmation of secure electronic submission capability | Pending each site |
| D11 | State-law or institutional privacy requirements beyond HIPAA | Pending each site |
| D12 | Signed final site certification and screening flow, including zero eligible records where applicable | Pending data submission |

### E. Data release and post-collection approvals

| # | Item | Status / completion evidence |
|---|---|---|
| E1 | Independent qualified disclosure-risk expert or qualifying engagement arrangement | Pending before any proposed exact row-level public release; qualification standard fixed in Section 11 |
| E2 | Expert determination on the exact proposed public file and required suppression, binning, pooling, or removal rules | Pending final release file; unrestricted row-level release prohibited without it |
| E3 | Controlled-access repository/operator and executed access-governance documents | Process drafted under B20; vendor/administrator pending |
| E4 | Public repository for protocol, codebook, aggregate results, code, synthetic data, release metadata, and change log | Pending repository selection before publication |
| E5 | Final data-quality report, disclosure review, PI release authorization, dataset version/DOI, license, and public correction contact | Pending each release |

### F. Submission and activation gates

- **Before IRB submission:** complete Sections A where required by the
  application; close B1–B8; draft B9–B21; obtain C2–C3; and attach the
  available personnel, funding, security, and COI documents.
- **Before clinic outreach beyond IRB-permitted feasibility contact:**
  obtain C6 and use only the approved B10 materials.
- **Before activating a clinic:** complete D1–D11 and all required
  agreements and determinations.
- **Before screening or transferring research data:** obtain the written
  determinations applicable to that site and verify the approved secure
  system.
- **Before any exact row-level public release:** complete E1–E2. If the
  expert does not approve the proposed file, release only approved
  aggregates, code, synthetic data, and controlled-access materials.
