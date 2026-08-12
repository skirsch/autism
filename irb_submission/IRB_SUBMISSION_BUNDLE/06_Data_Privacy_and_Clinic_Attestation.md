# Data Privacy, Electronic Transfer, and Clinic Attestation

## Data received by the coordinating investigators

The electronic dataset contains exactly six columns:

1. `site_code`
2. `clinic_row_id`
3. `sex`
4. `age_at_onset_months`
5. `dpre_days`
6. `dpost_days`

No calendar dates, phenotype variables, clinical narratives, patient names, medical-record numbers, contact information, geography, clinic names, or patient mapping keys are transmitted. The site code is a nonidentifying study code used for site-aware analyses.

## Electronic workflow

Clinic staff identify eligible records, review source information, calculate the three numeric timing variables, and assign an arbitrary row ID locally. The row ID must not be derived from a name, MRN, date, or other identifier. The clinic keeps the mapping.

The clinic completes `03_SORA_Electronic_Data_Submission_Template.xlsx` or an equivalent CSV file and uploads it through [approved secure upload portal]. Paper, handwritten, scanned, photographed, faxed, or email-body submissions are prohibited.

The coordinating team stores the received file in [institution-managed storage system] using [encryption/access controls]. Authorized roles are [PI, statistician, data manager]. Retention is [period].

Before public release, clinic-issued row IDs are discarded and replaced with new public row numbers. Site codes will be recoded, pooled, or removed following disclosure review. The public file contains no mapping mechanism.

## Clinic attestation

Study title: [title]

Clinic legal name: [name]

Authorized clinic representative: [name/title]

By electronically certifying the upload, the clinic confirms that:

- eligibility was determined locally according to the approved protocol;
- each row corresponds to one eligible record;
- the submitted file contains only the six approved columns;
- no calendar dates, phenotype information, narratives, direct identifiers, clinic name, or patient mapping key are present;
- the site code is the approved nonidentifying study code;
- the clinic row ID is not derived from identifying information;
- the clinic retains the row-ID mapping and will not disclose it to the coordinating investigators;
- the clinic privacy officer or authorized official approved the applicable HIPAA pathway; and
- the file was uploaded using the approved electronic method.

Electronic signature/name: [field]

Title: [field]

Date: [field]
