# SPARK Research Match Application — Draft v1

Submitted via SFARI Base; reviewed quarterly by the Participant Access Committee (deadlines Mar 31, Jun 30, Sep 30, Dec 31). Requires an institutional PI, an executed Researcher Distribution Agreement with institutional sign-off, and IRB approval (or exemption letter) for the survey. Bracketed fields are for the PI to complete.

## 1. Study title
How Parents First Notice Developmental Change: Timing, Memory, and Surrounding Events

## 2. Principal Investigator
[Name, degree, institution, department, email]. Co-investigators: [developmental pediatrician]; [biostatistician]; [survey methodologist]. Analysis-plan owner: [adversarial co-I], see §9.

## 3. Lay summary (for SPARK families; ≤150 words)
Many parents remember exactly when they first noticed a change in their child's development — sometimes a gradual realization, sometimes a sudden change over a few days. This short (about 3 minute) online survey asks how and when you first noticed change, how you remember the timing, and what else was going on in your child's life around that time, such as illnesses, medical visits, medicines, or family events. Whether your child's differences appeared suddenly or gradually, your answers help. Findings will help researchers understand how development changes in early childhood are noticed and recalled, and will be shared back with SPARK families as a summary.

## 4. Scientific aims
1. Estimate the proportion of SPARK probands whose parents report a sudden (≤14-day) loss of skills, and characterize the losses and new behaviors reported in the following 14 days.
2. Describe the timing of parent-observed onset relative to dated events in the preceding 3–120 days — febrile illness, medications, pediatric visits with and without immunizations, dental visits, family events — and test whether onset clusters in the first 0–2 days after any such event beyond what the child's schedule would produce.
3. Quantify the evidence parents rely on to date onset (memory, photos, messages, records) and how confident they are, and compare reported age at onset with the age at loss recorded at SPARK enrollment (within-family drift).
4. Compare all of the above between children with sudden change and a comparison sample of SPARK probands whose parents report gradual emergence.

## 5. Why SPARK
Existing day-resolution data on regression timing come only from convenience samples recruited through channels focused on a single hypothesis. SPARK is the only cohort large enough to supply hundreds of parent-reported regression cases recruited without reference to any causal hypothesis, with enrollment-era regression items for drift analysis and with the option of later record linkage.

## 6. Participants requested
- **Regression sample:** parents of probands aged 2–12 whose SPARK background-history items indicate loss of language or other skills. Request: ~5,000 invitations, target 1,500 completes.
- **Comparison sample:** parents of probands aged 2–12 with no reported loss of skills, random. Request: ~2,000 invitations, target 600 completes.
- English and Spanish.

## 7. Procedures
Single online survey (≈3 min; 18 items on the regression path, 13 on the comparison path), hosted on [SPARK Research Match platform / REDCap at PI institution — TBD with SPARK]. Instrument attached (`spark_parent_survey_v1.md`, data dictionary attached). Optional consent to one follow-up contact (through SPARK) and to a later request for the child's immunization record. Compensation per SPARK convention [$ TBD].

## 8. Linked SPARK data requested
Proband age, sex, enrollment date, background-history regression items and age at loss, age at diagnosis. Individual-level linkage under bidirectional consent.

## 9. Analysis and pre-registration
The analysis plan (`spark_signal_analysis_plan.md`) and code (`spark_signal_analysis.py`) are frozen and pre-registered on OSF before invitations are sent. One confirmatory test (Day 0–2 clustering after immunizing visits among non-attributing, artifact-dated respondents); all other analyses descriptive with confidence intervals. Pre-specified interpretations for both a positive and a null result are in the plan. An adversarial co-investigator owns the analysis code. Results are published regardless of direction.

## 10. Sensitivity of the topic; steps taken
The Committee should know that one of the dated events studied is immunization, and that the funder has publicly stated views on this question. Steps taken: (a) recruitment and consent materials do not mention immunizations or any cause, only "medical visits, illnesses, medicines, and family events"; (b) immunization appears only as one of 15 options in a checklist, after the narrative is locked, and attribution is asked last; (c) equal treatment of every dated event, including non-immunizing pediatric visits as a designed control; (d) funding is an unrestricted institutional gift with no funder access to data or manuscript; (e) pre-registration with pre-specified interpretations; (f) no individual causal interpretation is returned to any family; (g) the participant results summary reports aggregate findings only.

## 11. Data sharing
De-identified analytic dataset with narrative codes (no free text, no calendar dates, age in months, day-of-week, interval bins) deposited with SFARI Base per the RDA; a coarsened public file only for respondents who consent (`share_public_ok`) and only if SPARK approves. Free text retained at the PI institution under the IRB data plan.

## 12. Ethics
IRB [institution, protocol # TBD]. Minimal risk. Consent discloses that the study examines medical events in the child's history, that the specific hypotheses are withheld until the results summary to avoid influencing recall, and that participation is voluntary and separable from SPARK membership. Distress resources provided.

## 13. Timeline
PAC submission [quarter]; IRB in parallel; field period 8 weeks; analysis 8 weeks; results summary to SPARK within 12 months of field close.

## 14. Attachments
Instrument; REDCap data dictionary; analysis plan and code; recruitment email text (below); IRB approval; RDA.

---
### Recruitment email (SPARK house style; for the Research Match team to adapt)
Subject: A 3-minute survey about how you first noticed change in [child]'s development

Researchers at [institution] want to learn how parents first notice developmental change — whether it came on suddenly or gradually — how they remember when it happened, and what was going on in their child's life at the time, such as illnesses, medical visits, or family events. The survey takes about 3 minutes. [Compensation line.] [Link] Your participation is voluntary and does not affect your SPARK membership.
