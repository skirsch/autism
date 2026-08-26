# SPARK Parent Survey on Sudden Developmental Change — v1.2

**Purpose.** A ~3-minute online survey, modeled on the public Airtable "Parent Survey on Sudden-Onset Autism (SOA)" form, adapted for delivery to SPARK probands via Research Match. Same core items and coding so results can be pooled with or contrasted against the Airtable dataset; adapted so that (a) the sample is not recruited on the vaccine hypothesis, (b) attribution is asked *after* timing, (c) parents whose child did **not** regress supply a comparison arm, and (d) the date's evidence quality is recorded.

**Companion files:** `spark_survey_redcap_dictionary.csv` (importable), `spark_signal_analysis_plan.md`, `spark_signal_analysis.py`, `spark_research_match_application.md`.

**Design rules**
1. No vaccine-related word appears in recruitment text, the intro, consent, or any item before Q10 (the 3-days-before checklist, where "Vaccination" is one of 15 options).
2. Item order is fixed; the narrative (Q8) is on its own page and locked before the checklists.
3. Every timing item has a "don't remember" escape so missing ≠ zero.
4. Field names match the Airtable export where the item is the same, so the two datasets merge on column name.

---

## Page 0 — Intro and consent

**Title:** How parents first notice developmental change

*Intro text.* "Some children's development changes gradually; for others, parents remember a sudden, dramatic change over a few days or weeks — losing words or eye contact, becoming withdrawn, new repetitive behaviors, prolonged inconsolable distress, or new sensory sensitivities. We want to learn how and when parents first noticed change in their child, and what was going on in the child's life at that time. Whether or not your child had a sudden change, your answers are useful. The survey takes about 3 minutes."

**Q0 consent** `consent` (required, checkbox)
"I am at least 18, the parent or legal guardian of the SPARK participant, and I agree to take part. I understand that de-identified responses may be shared with other researchers under SPARK's data-sharing rules."

> Note: SPARK will not permit the Airtable form's unrestricted public release of row-level responses. Ask for release of a coarsened public file (age in months, day-of-week, interval bins, checklists, narrative codes; no free text, no calendar dates) in the Research Match application; see the application draft.

## Page 1 — Child and change type

**Q1** `sex` (required, radio) — What is the sex of your child? Male / Female
*(also available from SPARK; kept for standalone pooling with Airtable.)*

**Q2** `state` (required, dropdown) — What US state do you live in? [50 states + DC + Other] *(replaces Airtable `country`; used for immunization-registry follow-up)*

**Q3** `change_type` (required, radio) — Which best describes how your child's autism-related differences first appeared?
1. A sudden, dramatic change over about two weeks or less, after developing normally
2. A noticeable change over a few weeks to a couple of months
3. Gradual — differences were always there or emerged slowly
4. Not sure

> Branching: options 1–2 → **Regression path** (Q4–Q17). Options 3–4 → **Comparison path** (Q4c, Q10c, Q12c, Q14c, Q15, Q17). Comparison-path wording replaces "onset" with "the time you first became concerned."

## Page 2 — When (Regression path)

**Q4** `how_long_ago` (required, radio) — How long ago did you notice the sudden change (the "onset date")?
Within 3 months / 3–6 months / 6 months–1 year / 1–2 years / 2–5 years / more than 5 years

**Q5** `onset_date` (optional, date mm/dd/yyyy) — If you remember the exact or approximate calendar date of onset, enter it. Otherwise leave blank.

**Q6** `onset_dow` (required, radio) — Do you remember the day of the week onset happened, or whether it was a weekday or weekend?
Don't remember / Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday / It was a weekday / It was a weekend

**Q7** `age_onset_months` (required, integer 0–72) — Your child's age in months at onset (e.g., 18).

**Q7b** `date_evidence` (required, checkbox) — What is your memory of the onset timing based on? Check all that apply.
Memory alone / Calendar or diary / Photos or videos with dates / Texts, emails, or patient-portal messages / Daycare or school notes / A doctor's record / Social-media post / Other
*(new: evidence-quality stratifier)*

## Page 3 — Narrative (own page; locked on submit)

**Q8** `sequence` (required, long text) — Briefly describe the chain of events in the 15 days before onset that you think might be relevant. Use (0) as the first reference day. Example: *birthday party (0) → illness (1) → fever (2) → high-pitched screaming for 12 hours (2) → lost eye contact (4).*

## Page 4 — Structured timing

**Q10** `before3` (required, checkbox) — What do you remember happening in the **3 days BEFORE** onset? Check all that apply.
Fever / Tylenol or acetaminophen / Illness / Pediatrician or well-child visit **without** any shots / Pediatrician or well-child visit **with** shots / Ear infection / Vaccination (any setting, incl. pharmacy or clinic) / Dentist visit / Toxic environmental exposure (mold, chemical…) / New prescription drug (e.g., antibiotic) / Your child's birthday / Your birthday / New Year's Day / Other (specify in Notes) / None of the above / Too long ago, don't remember
*(Airtable list plus the split of pediatrician visit into with/without shots — the non-vaccinating-visit control.)*

**Q11** `after14` (required, checkbox) — In the **14 days AFTER** onset, which changes did you observe? Check all that apply.
High-pitched screaming / Sleepless nights / LOST existing behavior(s) (eye contact, social interaction…) / LOST existing skill(s) (words, motor skills…) / DEVELOPED new repetitive behaviors (head banging, toe walking, arching…) / Change in sensitivities (light, sound, pain, touch, being held) / Extreme fussiness / New obsessions / Other (specify in Notes)

**Q12** `visit_interval` (required, radio) — How many days **before** onset was your child's most recent doctor visit (well-child or sick visit)? Choose the closest answer, even if unsure.
Don't remember / No visit within 120 days before onset / <1 day (onset <24 h after) / 2 days (24–48 h) / 3 days (49–72 h) / 4 days / 5 days / 6 days / 7 days / 8–13 / 14–29 / 30–59 / 60–83 / 84–97 / 98–120
*(Bins identical to Airtable's vaccination-interval item through 30–59; 60–90 / >90 replaced by 60–83 / 84–97 / 98–120 so the ~90-day mirror hump is visible.)*

**Q13** `visit_confidence` (required if Q12 is an interval, radio) — How certain are you of that interval?
Absolutely certain / Within 1 day / Within 2 days / Within 3 days / Within 4 days to a week / Could be off by a week or more

**Q13b** `visit_shots` (required if Q12 is an interval, radio) — How many vaccine injections were given at that visit?
0 (no shots) / 1 / 2 / 3 / 4 / 5 or more / Don't remember

**Q13c** `vax_prior_interval` (shown only if Q13b = 0, radio) — Was there an earlier visit **with** shots within 120 days before onset? If so, how many days before onset?
Don't remember / No visit with shots within 120 days / <1 day / 2 / 3 / 4 / 5 / 6 / 7 / 8–13 / 14–29 / 30–59 / 60–83 / 84–97 / 98–120

> **Why this replaces the Airtable vaccination-interval question.** One interval for the nearest visit plus the number of injections at it gives, in the same histogram, (a) the vaccination interval (derived: `visit_interval` if `visit_shots` ≥ 1, else `vax_prior_interval`), (b) the no-shot-visit control (`visit_shots` = 0), and (c) a dose–response axis (Day 0–2 fraction by 0, 1, 2, 3, 4, 5+ injections). A visit anchors memory the same way regardless of how many shots were given, so a Day 0–2 fraction that rises with injection count cannot be produced by visit-anchoring. Two questions for most respondents; three only for those whose nearest visit had no shots.

**Q14** `documentation` (required, radio) — If we asked you for contemporaneous documentation of the onset timing (email, text, video, photo, social-media post, diary note, calendar entry, doctor call), could you provide it?
Yes, 100% certain / Yes, 80%+ certain / Maybe / Unlikely / Highly unlikely

**Q14b** `record_upload_ok` (required, radio) — Would you be willing to share your child's official immunization record (from your state registry or pediatrician) with the research team in a follow-up?
Yes / Maybe / No

## Page 5 — Attribution (after all timing items)

**Q9** `cause` (optional, long text) — What do you think might have triggered the change, and why? Do you think it was a random event with no specific trigger? *(Airtable item, moved after timing.)*

**Q9b** `attribution` (required, checkbox) — Which of these do you think contributed? Check all that apply.
Genetics / family history / Prematurity or birth complications / Something during pregnancy / An illness or infection / A vaccine / A medication / Something in the environment / Nothing in particular — random / Don't know / Other

**Q9c** `hypothesis_exposure` (required, radio) — When did you first hear the idea that vaccines might be connected to autism?
Before my child was born / Before I noticed the change / Around the time I noticed it / After the diagnosis / Never heard it / Not sure

## Page 6 — Close

**Q15** `notes` (optional, long text) — Anything else we should know, or comments on unclear questions or missing options?

**Q16** `recontact_ok` (required, radio) — May the research team contact you (through SPARK) about a follow-up? Yes / No
*(replaces the Airtable email field; SPARK holds contact info.)*

**Q17** `share_public_ok` (required, radio) — May a coarsened, de-identified version of your answers (no free text, no calendar dates) be included in a public research file? Yes / No

---

## Comparison path (change_type = 3 or 4)

Same items, reworded to "the time you first became concerned about your child's development": `age_concern_months` (=Q7), `concern_date` (=Q5), `concern_dow` (=Q6), `before3` (=Q10, relative to first concern), `visit_interval` (=Q12, relative to first concern), `visit_confidence`, `visit_shots`, `vax_prior_interval`, `attribution`, `hypothesis_exposure`, `notes`, `recontact_ok`, `share_public_ok`. Narrative Q8 becomes: "Briefly describe what you noticed and what was going on around that time." Skip Q11.

## Linked SPARK enrollment fields (request in application)
Proband age at survey, sex, enrollment date, background-history regression items (loss of language / other skills, age at loss), age at diagnosis. Enrollment-era age at loss vs `age_onset_months` gives within-family drift for free.

## Changes from the Airtable form (summary)
| Airtable | SPARK v1 | Why |
|---|---|---|
| Vaccine-heavy intro; recruited through vaccine-aware channels | Neutral intro; SPARK invitation | Sample not sorted on hypothesis; passes Participant Access Committee |
| `source` | dropped | SPARK is the only source |
| `country` | `state` | US-only; registry follow-up |
| — | `change_type` gate + comparison path | Non-regressed kids give base rates for the checklists and vaccination intervals |
| `cause` before checklists | `cause` + `attribution` + `hypothesis_exposure` after all timing | Attribution can't prime timing |
| `# days ago vaccinated` | `visit_interval` + `visit_shots` (+ `vax_prior_interval` if 0 shots) | Same vaccination interval, plus no-shot-visit control and dose–response, with no extra questions for most respondents |
| — | `date_evidence`, `record_upload_ok` | Evidence-quality strata; path to record-verified interval |
| email | `recontact_ok` via SPARK | SPARK holds identity |
| unrestricted public release | `share_public_ok`, coarsened file | SPARK data terms |
