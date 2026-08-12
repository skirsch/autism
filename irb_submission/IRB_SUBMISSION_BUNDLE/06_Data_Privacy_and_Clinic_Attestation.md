# Data Privacy, Electronic Transfer, and Clinic Attestation

## Data received by the coordinating investigators

The electronic patient-level dataset contains exactly seven columns:

1. `site_code`
2. `clinic_row_id`
3. `sex`
4. `age_at_onset_days`
5. `vaccination_before_onset`
6. `dpre_days`
7. `dpost_days`

Four aggregate 24-month counts and aggregate screening-flow counts are transmitted separately and contain no patient-level rows or free text.

No calendar dates, phenotype variables, clinical narratives, patient names, medical-record numbers, contact information, geography, clinic names, or patient mapping keys are transmitted. The site code is a nonidentifying study code used for site-aware analyses.

## Electronic workflow

Clinic staff identify eligible records, review source information, calculate the three numeric timing variables, and assign an arbitrary row ID locally. The row ID must not be derived from a name, MRN, date, or other identifier. The clinic keeps the mapping.

The clinic completes `03_SORA_Electronic_Data_Submission_Template.xlsx` or an equivalent CSV file and uploads it through the institution-managed encrypted portal named during site activation. Paper, handwritten, scanned, photographed, faxed, or email submissions are prohibited.

The coordinating team stores the received file only in the institution-managed system named during site activation, with encryption in transit and at rest, multifactor authentication, role-based access, audit logging, endpoint encryption, and institutional backup. Access is limited to the PI, analyst/statistician, and data manager when their roles require it. The access list is reviewed every three months. Records are retained for seven years after study closure or final publication, whichever is later, unless institutional policy requires longer.

Aggregate results, code, and a synthetic dataset may be released. Row-level study data are not public by default and may be released only after an independent qualified HIPAA statistical expert documents a very small identification risk and approves the exact file. Clinic row IDs will never be released; site codes will be removed or pooled, small cells under 11 suppressed, and age or extreme intervals generalized as directed. Without that determination, no row-level study data will be released.

## Clinic attestation

Study title: [title]

Clinic legal name: [name]

Authorized clinic representative: [name/title]

By electronically certifying the upload, the clinic confirms that:

- eligibility was determined locally according to the approved protocol;
- each row corresponds to one eligible record;
- the patient-level file contains only the seven approved columns and separately labeled aggregate counts contain no patient rows;
- no calendar dates, phenotype information, narratives, direct identifiers, clinic name, or patient mapping key are present;
- the site code is the approved nonidentifying study code;
- the clinic row ID is not derived from identifying information;
- the clinic retains the row-ID mapping and will not disclose it to the coordinating investigators;
- the clinic privacy officer or authorized official approved the applicable HIPAA pathway; and
- the file was uploaded using the approved electronic method.

Electronic signature/name: [field]

Title: [field]

Date: [field]
