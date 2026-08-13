# CHD Multisite SORA Data-Resource Study

## Executive Summary and Study Definition

**Document status:** Planning summary for development of the IRB submission packet  
**Version:** 0.8  
**Date:** 12 August 2026

## 1. Study identity

| Item | Proposed specification |
|---|---|
| Working title | Multisite Data Resource of Sudden-Onset Regressive Autism (SORA) |
| Coordinating principal investigator | Brian Hooker, Ph.D. [confirm exact degrees, title, and CHD affiliation] |
| Sponsor/coordinating organization | Children's Health Defense (CHD) [confirm legal entity] |
| Participating sites | The first 10 qualifying clinics to complete all activation requirements |
| Study type | Retrospective, multisite medical-record data-resource study |
| Primary purpose | Create, validate, document, and release a privacy-protected dataset for subsequent independent analysis |
| Initial publication | Dataset/cohort descriptor, data-quality report, and basic descriptive summaries—not a causal analysis |
| Participant contact | None |
| Intervention | None |
| Proposed regulatory pathway | Exempt secondary research under 45 CFR 46.104(d)(4), subject to the reviewing IRB's determination and site-specific requirements |
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

Brian Hooker will have coordinating PI responsibility for protocol
compliance, site-activation authority, reporting, and communication
with the reviewing IRB. Ben Jackson and Mila Radetich will conduct
site outreach and activation. Karl Jablonowski and Steve Kirsch will
monitor submitted files and apply the mechanical data-quality checks.
The CHD data custodian is TBD. Each clinic will designate a site
investigator responsible for local record access, eligibility, privacy
compliance, and source verification. Role-specific access limits are
stated in Section 2.

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

## 14. Punchlist — items still to supply

Use a prior CHD IRB submission as the first source for legal entity,
IRB of record, data environment, training, COI forms, contracting, and
privacy language. Check each item when the value is written into this
summary or the draft packet.

### A. People and organization

| # | Item | Status |
|---|---|---|
| A1 | Brian Hooker: exact degrees, title, CHD affiliation, and study contact information | TBD |
| A2 | Ben Jackson, Mila Radetich, Karl Jablonowski, and Steve Kirsch: credentials/titles, human-subjects training, and COI disclosures | TBD |
| A3 | CHD data custodian: name, title, and responsibilities | TBD |
| A4 | Security/privacy official(s), if different from the data custodian | TBD |
| A5 | CHD legal entity name | TBD |
| A6 | Written acceptance that this entity is sponsor, data custodian, and coordinating organization | TBD |

### B. IRB and site pathway

| # | Item | Status |
|---|---|---|
| B1 | Reviewing IRB (name and whether it will accept CHD and Hooker as coordinating PI) | TBD |
| B2 | Requested determination: confirm 45 CFR 46.104(d)(4) and which subclause, if any | TBD |
| B3 | Reliance or local-review pathway for participating clinics | TBD |
| B4 | Whether feasibility contact with clinics is permitted before IRB approval | TBD |
| B5 | Site eligibility checklist | TBD |
| B6 | Clinic participation agreement / data-use terms | TBD |
| B7 | IRB-ready clinic-outreach email, phone script, and related materials | TBD |

### C. Dates, money, and infrastructure

| # | Item | Status |
|---|---|---|
| C1 | Clinic-recruitment opening and closing dates | TBD |
| C2 | Initial data cutoff date and rules for later versioned releases | TBD |
| C3 | Approved secure transfer and storage environment (system name, encryption, access control) | TBD |
| C4 | Submission system: workbook/CSV portal, electronic data capture, or both | TBD |
| C5 | Record-retention period and access-list review interval | TBD |
| C6 | Study funding source, amount, and terms | TBD |
| C7 | Clinic reimbursement: none, or amount and documentation rules | TBD |

### D. Disclosure, access, and packet attachments

| # | Item | Status |
|---|---|---|
| D1 | Independent disclosure-risk reviewer (name or qualifying arrangement) | TBD |
| D2 | Controlled-access repository and data-use agreement process | TBD |
| D3 | Public posting location for protocol, codebook, aggregates, and code, if any | TBD |
| D4 | CVs/biosketches and training certificates for named coordinating personnel | TBD |

Site investigators and clinic abstractors are named at activation, not
on this punchlist.
