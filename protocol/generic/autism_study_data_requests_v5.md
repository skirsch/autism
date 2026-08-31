# Dataset Request and Requested Analyses for Autism Studies — v5

**Version:** 5 — 2026-08-31. Supersedes v4, which is preserved unchanged.

## Vaccination and Pediatric-Visit Timing Around Abrupt Developmental Regression

### Scope of this add-on request

Please provide the requested information for all eligible records available in the existing study.

Report unavailable information as unknown rather than excluding a child solely because a requested field is missing.

These are suggested additional data fields and figures, not a requirement to redesign the study or replace its existing primary analysis.

Disclose whether analysis choices were specified before or after examining the relevant timing distributions.

### Study objective

Determine whether abrupt, persistent developmental regression in children diagnosed with autism shows temporal clustering after vaccination, and whether that clustering differs from the pattern after pediatric visits at which no vaccination occurred.

The study should distinguish **vaccination-linked timing**, **general visit-linked timing**, and **uncertainty in retrospective onset reports**, without assuming a causal explanation in advance.

## 1. Eligible children

Please identify all consecutive eligible children from a defined clinical population and study period—not only children whose parents suspect a vaccine-related event.

Include children who:

- Have an autism diagnosis.
- Were reported to be developing normally before an abrupt loss of previously acquired skills.
- Experienced a lasting change rather than a brief illness-related fluctuation.
- Have sufficient parent or caregiver information to establish that the qualifying regression occurred; an identifiable onset date is not required for this classification.

Include **never-vaccinated children**, children vaccinated on delayed or reduced schedules, and children whose vaccination history is uncertain.

Before extraction, specify the operational definitions of **previously developing normally**, **abrupt**, and **lasting**. Apply those definitions consistently and, where practicable, establish eligibility and onset timing before reviewing vaccination dates.

Define **ONSET** as the day the parent or caregiver first noticed the qualifying regression (not the autism diagnosis date, the date concerns were first discussed with a clinician, or the date the regression was complete).

Use cases with sufficiently precise, supported intervals for daily timing plots; describe the inclusion rule. Retain approximate-date cases for separately reported sensitivity analyses rather than forcing an exact date. Retain qualifying regression cases with unknown dates in the regression count and dataset, even when they cannot contribute to timing plots.

## 2. Requested dataset

Provide one de-identified record per child, with a unique study identifier and the following fields.

| Field | Requested information |
|---|---|
| **1. Age at ONSET** | Age in days when supported by available information. Otherwise provide age in months and identify its precision. Do not manufacture day-level precision from an approximate age. |
| **2. Pediatric VISIT INTERVAL** | Number of calendar days from the most recent pediatric visit that preceded ONSET to ONSET. A same-day visit qualifies only when onset was noticed **after** the visit. Separately record same-day visits occurring after onset or with unknown ordering, following the rules below. Use separate codes for no prior visit and unknown interval. |
| **3. Type of that visit** | Routine well-child visit / illness visit / developmental or behavioral concern / other / unknown. If illness or concern prompted the visit, briefly identify the reason. |
| **4. Vaccination at that visit** | Confirmed vaccination / confirmed no vaccination / unknown. If vaccination occurred, list vaccine products or types when available; at minimum identify MMR-containing vaccination as yes / no / unknown. An omitted checklist item must not be interpreted automatically as confirmed no vaccination. **If documented, indicate whether vaccination was planned but deferred (yes / no / unknown), and record the reason.** Lack of a deferral note means unknown, not confirmed absence of deferral. |
| **5. VACCINATION INTERVAL** | Number of days from the most recent **actual vaccine administration** before ONSET to ONSET, regardless of where it occurred. If vaccination occurred before onset at the pediatric visit, this may equal the visit interval. A same-day administration qualifies only when onset was noticed **after** administration. Separately record same-day administrations occurring after onset or with unknown ordering, following the rules below. Separately code no vaccination before onset and unknown vaccination history. |
| **6. Birth year** | Four-digit birth year. |
| **7. Day of week of ONSET** | Monday–Sunday / unknown. Derive it from the onset date when that date is sufficiently precise. |
| **8. Onset precision and evidence** | Exact day / approximate day / date range / month only / unknown. Record whether onset timing is supported by contemporaneous diary, video, message, clinical record, later parental recall, or a combination. Identify separately whether vaccination and visit dates were confirmed from records. |

Calculate day intervals as ONSET date minus visit or vaccination date; do not round hours to assign a calendar-day interval. Record same-day ordering explicitly as **onset before the encounter**, **onset after the encounter**, or **order unknown**. Assess ordering separately for the visit and vaccine administration.

A same-day encounter occurring after onset must not replace the actual preceding visit or vaccination: retain the earlier interval, and record the later same-day encounter separately. Visit type and vaccination status in fields 3–4 must describe the visit used for field 2; record those details separately for any additional same-day visit. If same-day ordering is unknown, mark the most-recent-pre-onset interval as uncertain, retain any earlier known preceding interval as supplementary information, and do not assume the same-day encounter preceded onset.

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

Separate routine well-child visits from illness/developmental-concern visits rather than combining them into a single comparison. Compare well-child visits with vaccination against well-child visits without vaccination; do not compare all vaccination visits against only no-vaccination well-child visits.

Identify documented deferred-vaccination visits where available. Report their counts and reasons; if numbers permit, show a separate or sensitivity analysis. Do not silently remove deferred visits based on whether they strengthen or weaken an association.

Use daily bins near onset, including individual days 0–14. Clearly label any wider bins farther from onset. Day 0 includes only visits known to precede onset that day. Show same-day visits after onset and those with unknown ordering in a separate ordering summary, not in the post-visit interval histogram. Count each child at most once in the main histogram; a child with an earlier qualifying visit and a later same-day visit can also appear in the separate summary, so its counts must not be added to the histogram totals.

Report unknown visit contents, unknown intervals, and no-prior-visit cases outside the histogram. Display counts and within-group percentages with the denominator for each panel, since group sizes may differ substantially. Label unequal-width bins and distinguish event counts from events per day of bin width.

### Figure 4 — Vaccination interval

Show the VACCINATION INTERVAL histogram for all children with a known vaccination before onset, including those whose most recent pediatric visit did not involve vaccination.

Use the same near-onset daily resolution and same-day ordering conventions as Figure 3. Report never-vaccinated, vaccinated-only-after-onset, and unknown-history counts separately—not as interval values.

A no-vaccination pediatric visit does **not** necessarily mean the child had no recent vaccination elsewhere.

## 4. Analysis and reporting

Please report the number of available cases in every figure and subgroup, including small groups. **No minimum sample size is required to fulfill this request.** A sparse comparison may be inconclusive while other parts of the dataset remain informative.

Report the existing study's clinical source population, study period, eligibility definitions, and recruitment/selection method. Where available, report numbers screened, eligible, included, and excluded, with reasons. Prefer all consecutive eligible cases within that source over cases selected because a vaccine-related event was suspected; if this is not possible, describe how cases were selected.

### Source-population and regression counts

Where available, include a short participant-flow table in the paper reporting:

| Count | Definition |
|---|---|
| **Source population** | Unique autistic children in the defined source population, before selecting for regression or date recall. Report children invited through their parents and children represented in the existing study separately if those counts differ. |
| **Assessed children** | Children with enough parent or caregiver information to classify qualifying regression as present or absent. |
| **Qualifying regression cases** | Assessed children meeting the abrupt, lasting regression definition in section 1, regardless of onset-date precision. |
| **Exact-day cases** | Qualifying regression cases for whom a parent or caregiver identifies the exact onset day, whether from recall or contemporaneous evidence. |
| **Document-supported exact-day cases** | Exact-day cases whose onset day is supported by contemporaneous evidence, using the evidence categories in field 8. |

Use unique children, not parents or submitted forms, as the counting unit. If only a parent/contact-list count is available, report it separately and label it as such; do not substitute it for a child denominator. Describe any one-child-per-family selection rule.

Report nonresponses, responses with insufficient information to classify regression, and assessed children without qualifying regression separately. Missing or uncertain regression status must not be counted as absence of regression. These aggregate counts do not require individual-level records for children without regression.

Report the following percentages alongside their numerators and denominators:

- **Qualifying regression percentage:** qualifying regression cases divided by assessed children, multiplied by 100.
- **Exact-day identification percentage:** exact-day cases divided by qualifying regression cases, multiplied by 100.
- **Document-supported exact-day percentage:** document-supported exact-day cases divided by qualifying regression cases, multiplied by 100.

If a denominator is zero or unavailable, report the percentage as not estimable, not zero. An exact recalled day is not automatically a documented day or an eligible interval for a particular timing figure; retain each figure's own inclusion rules and counts.

The qualifying regression percentage describes the assessed study population, not necessarily all autistic children or all invited children. If the existing study enrolled only regression cases, or only cases with identifiable dates, disclose that selection and do not interpret its selected-case fraction as the frequency of regression in the broader source population. These counts are requested only where available; missing source-population information does not prevent fulfillment of the record and figure request.

Where available, compare vaccination-before-onset status and whether a pediatric visit occurred within 30 days before onset between qualifying regression cases with and without an exact onset day. Report unknown or uncertain status separately; do not infer these classifications when the available onset-date range cannot support them.

### Timing analyses and interpretation

If formal comparisons are added, state the risk/reference windows, denominator, background timing model, missing-data rules, and any multiplicity handling. These are not mandated new primary analyses. Report effect estimates and confidence intervals rather than only p-values; a significant result in one group and a nonsignificant result in another does not itself establish that the groups differ.

Treat small or imprecise comparison groups as inconclusive, not as evidence of no association. Do not infer a flat interval distribution solely from the width of the plotted windows. A no-vaccination visit is not necessarily an unexposed period, because vaccination may have occurred recently at another encounter.

**Optional aggregate supplement, only if readily available:** the size and vaccination-status distribution of the screened source population, including unknown status. Specify the age/date or pre-onset reference point at which status was assessed. These aggregates are useful context but are not a prerequisite for supplying the requested records or figures.

These data can reveal or challenge a temporal-association signal. They do not, by themselves, constitute a full self-controlled case-series dataset or establish causation. Report limitations in age-related timing, visit reasons, exposure deferral, selection, and date ascertainment alongside the findings.
