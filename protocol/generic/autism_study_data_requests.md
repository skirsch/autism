# Dataset Request and Requested Analyses for Autism Studies

## Vaccination and Pediatric-Visit Timing Around Abrupt Developmental Regression

### Study objective

Determine whether abrupt, persistent developmental regression in children diagnosed with autism shows temporal clustering after vaccination, and whether that clustering differs from the pattern after pediatric visits at which no vaccination occurred.

The study should distinguish **vaccination-linked timing**, **general visit-linked timing**, and **uncertainty in retrospective onset reports**, without assuming a causal explanation in advance.

## 1. Eligible children

Please identify all consecutive eligible children from a defined clinical population and study period—not only children whose parents suspect a vaccine-related event.

Include children who:

- Have an autism diagnosis.
- Were reported to be developing normally before an abrupt loss of previously acquired skills.
- Experienced a lasting change rather than a brief illness-related fluctuation.
- Have a parent or caregiver able to describe the regression and estimate when it began.

Include **never-vaccinated children**, children vaccinated on delayed or reduced schedules, and children whose vaccination history is uncertain.

Before extraction, specify the operational definitions of **previously developing normally**, **abrupt**, and **lasting**. Apply those definitions consistently and, where practicable, establish eligibility and onset timing before reviewing vaccination dates.

Define **ONSET** as the first day of the qualifying regression—not the autism diagnosis date, the date concerns were first discussed with a clinician, or the date the regression was complete.

Use exact-day cases for the primary daily timing analysis. Retain approximate-date cases for separately reported sensitivity analyses rather than forcing an exact date.

## 2. Requested dataset

Provide one de-identified record per child, with a unique study identifier and the following fields.

| Field | Requested information |
|---|---|
| **1. Age at ONSET** | Age in days when supported by available information. Otherwise provide age in months and identify its precision. Do not manufacture day-level precision from an approximate age. |
| **2. Pediatric VISIT INTERVAL** | Number of days from the most recent pediatric visit before ONSET to ONSET. Include visits on the onset day and identify whether onset was noticed **before**, **after**, or at an **unknown time relative to the visit**. Use separate codes for no prior visit and unknown interval. |
| **3. Type of that visit** | Routine well-child visit / illness visit / developmental or behavioral concern / other / unknown. If illness or concern prompted the visit, briefly identify the reason. |
| **4. Vaccination at that visit** | Confirmed vaccination / confirmed no vaccination / unknown. If vaccination occurred, list vaccine products or types when available; at minimum identify MMR-containing vaccination as yes / no / unknown. An omitted checklist item must not be interpreted automatically as confirmed no vaccination. |
| **5. VACCINATION INTERVAL** | Number of days from the most recent **actual vaccine administration** before ONSET to ONSET, regardless of where it occurred. If vaccination occurred at the pediatric visit, this may equal the visit interval. Identify same-day onset as before / after / unknown relative to administration. Separately code no vaccination before onset and unknown vaccination history. |
| **6. Birth year** | Four-digit birth year. |
| **7. Day of week of ONSET** | Monday–Sunday / unknown. Derive it from the onset date when that date is sufficiently precise. |
| **8. Onset precision and evidence** | Exact day / approximate day / date range / month only / unknown. Record whether onset timing is supported by contemporaneous diary, video, message, clinical record, later parental recall, or a combination. Identify separately whether vaccination and visit dates were confirmed from records. |

Distinguish **never vaccinated**, **vaccinated only after onset**, **vaccinated before onset**, and **unknown history**. Do not treat absence of a record as proof that vaccination did not occur.

Where multiple countries or clinical sites contribute data, retain a site/country identifier so differing schedules and recruitment settings can be considered.

## 3. Requested figures in the paper

### Figure 1 — Age at regression onset

Show a histogram of **age at ONSET**, using one-month bins from 0 through 60 months.

- Retain zero-count months.
- Report older-onset cases separately.
- Show vaccinated-before-onset and never-vaccinated children in separate panels where feasible.
- If vaccination-schedule ages are overlaid, identify the schedule’s country and year and display recommended age ranges—not just selected point ages.

### Figure 2 — Day of week of onset

Show Monday–Sunday onset counts and proportions.

- Report the number with an identifiable weekday and the number with unknown weekday.
- Distinguish contemporaneously supported dates from recall-only dates where sample size permits.
- State the expected distribution used for comparison.

### Figure 3 — Pediatric-visit interval

Show the VISIT INTERVAL histogram separately for:

- Visits with confirmed vaccination.
- Visits with confirmed no vaccination.

Separate routine well-child visits from illness/developmental-concern visits rather than combining them into a single comparison.

Use daily bins near onset, including individual days 0–14. Clearly label any wider bins farther from onset. Display same-day-before and same-day-after events separately; do not combine them.

Report unknown visit contents, unknown intervals, and no-prior-visit cases outside the histogram.

### Figure 4 — Vaccination interval

Show the VACCINATION INTERVAL histogram for all children with a known vaccination before onset, including those whose most recent pediatric visit did not involve vaccination.

Use the same near-onset daily resolution and same-day ordering conventions as Figure 3. Report never-vaccinated, vaccinated-only-after-onset, and unknown-history counts separately—not as interval values.

A no-vaccination pediatric visit does **not** necessarily mean the child had no recent vaccination elsewhere.

## 4. Analysis and reporting requirements

Before examining the results, specify:

- The primary risk and reference windows.
- The background timing model and why it is appropriate.
- Missing-data, uncertain-date, and same-day-ordering rules.
- The primary comparison and any multiplicity adjustment.

Report counts, effect estimates, and confidence intervals—not only p-values. Compare vaccination-visit and no-vaccination-visit patterns directly, with uncertainty; significance in one group and nonsignificance in another does not establish a difference between them.

Report the numbers screened, eligible, included, and excluded, with reasons. Preserve small or imprecise comparison groups as **indeterminate**, not as evidence of no association.

These data support descriptive and comparative timing analyses. A flat interval distribution should not be assumed automatically, and these fields alone do not constitute a full self-controlled case-series dataset. Any causal interpretation must address age-related timing, visit reasons, recruitment, and onset-date ascertainment.