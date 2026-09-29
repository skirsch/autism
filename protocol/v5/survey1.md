# Survey 1: developmental-timing intake

**Version:** 1.0 draft  
**Date:** September 28, 2026  
**Status:** Working instrument for IRB review; not approved for recruitment  
**Controlling design:** [study_overview.md](study_overview.md)

This is a short, cause-neutral intake modeled on the structure of the [existing short survey](https://www.skirsch.com/autism/survey.htm). It deliberately replaces that survey's “less than 7 days” regression rule with an identifiable **calendar date** of first clear change. No recruitment partner is named in this instrument. All respondent-facing text below, including consent, remains subject to IRB review. Bracketed items require implementation decisions before use.

## Respondent-facing draft

### About this survey

We are studying how children developed before and around the first noticeable changes associated with their later autism presentation. We are especially interested in children who appeared to develop normally and then had a clear change in behavior or skills that a parent can place on a calendar date. The change need not have been complete in one day.

This brief survey asks about one child. You may be invited to a separate follow-up study about the timing and documentation of that change. Saying yes to follow-up now does not obligate you to complete another survey or provide records.

Participation is voluntary. [Insert IRB-approved investigator/contact information, privacy notice, estimated completion time, and any required institutional language.] The study plans to retain submitted answers for 20 years after study closure. A coded dataset may be made public; direct contact information will not. Submitted answers cannot be withdrawn after submission under the proposed study policy. These terms require IRB approval before this survey is used.

### Consent

I am at least 18 years old and the child's parent or legal guardian. I have read the information above and voluntarily agree to submit my answers for this study.

- I agree and wish to continue.
- I do not agree. [End survey; collect no study answers.]

### Which child should you answer about?

If you have more than one autistic child, answer about the **youngest child who progressed normally and then had an identifiable date, at age 6 through 24 completed months, when a clear change in behavior or skills was first noticed by one or both parents**. If no child fits that description, answer about your youngest autistic child. Please answer about only that child throughout this survey. A parent's report that the child has autism is sufficient here; a diagnostic record is not required.

1. **What year was this child born?** [Four-digit year; allow “unsure” if required by IRB/implementation.]

2. **Which description best fits this child's development?** [Select one.]
   - Development was slower than expected from early on, without a clear later loss of skills or new marked behavior.
   - Development progressed normally, then plateaued without a clear dated change.
   - Development progressed normally, then changed gradually; I cannot identify a first clear day of change.
   - Development progressed normally, then I noticed a clear loss or substantial reduction of a skill on an identifiable date.
   - Development progressed normally, then I noticed a clearly new, marked behavior on an identifiable date, even if no skill was lost.
   - Development progressed normally, then both a skill changed and a clearly new, marked behavior appeared on an identifiable date.
   - A different or mixed pattern.
   - Unsure.

**If one of the three identifiable-date options is selected, show questions 3–5.** Do not require the entire change to occur within seven days. A first noticed behavior such as head banging may qualify even without skill loss.

3. **How old was your child when you first clearly noticed that change?** Enter age in **completed months** (for example, 18 if the child had turned 18 months but not yet 19 months). [Integer months; allow “unsure.”]

4. **Can you identify the calendar date when you or the other parent first clearly noticed the change?**
   - Yes, I know the date or can determine it from information I have.
   - I can narrow it to a few possible dates, but not one date.
   - No, I cannot determine a calendar date.

   **If Yes:** What was that date? [Month/day/year; “I need to check” allowed only if the participant has said a specific date is determinable. Do not force a guess.] How certain are you? [Certain / date can be checked against materials / best estimate with possible error / unsure.] This is the first clear change date, not necessarily the first day of any preceding illness or uncertain period.

5. **How confident are you that you have, or could obtain, records or dated materials that may help establish when the change first occurred?** Examples include medical or therapy records, dated messages, calendar entries, photographs, or videos. [Select one; these four choices determine invitation order.]
   - Definitely available now.
   - Probably available; I know how to obtain them.
   - Might be available; I would need to investigate.
   - Probably unavailable.

6. **May the study team contact you about a possible follow-up survey or request for relevant records?** A Yes answer does not commit you to future participation or record sharing. [Ask everyone.]
   - Yes.
   - No.

   **If Yes:** What email address should we use? [Email, stored separately from research answers.] [Optional alternative contact method only if approved and needed.]

### Thank you

Thank you. If you agreed to follow-up, the study team may contact you with more information. You may decline any future invitation.

## Routing and data rules for implementation

- Survey 1 invitation, purpose statement, consent, and questions must not name vaccination or disclose a preferred exposure hypothesis. Recruitment source is recorded by an internal source code, not named in this instrument.
- Present one child-selection rule before the child questions. Retain and count all submitted patterns, including nonqualifying and uncertain answers; do not silently discard them.
- Preliminary Survey 2 invitation eligibility requires adult parent/guardian consent, the previously normal/identifiable-date pattern, a determinable first-clear-change calendar date, reported age **6–24 completed months inclusive**, and permission/contact information for follow-up. Missing or inconsistent answers are flagged rather than imputed. The precise treatment of “I need to check” must be fixed before launch.
- Assign one of the four records-confidence groups from question 5 only. Invitation waves must not use any later exposure information. The initial and subsequent batch algorithm is in the overview.
- Store the raw parent-entered date and certainty separately from derived age, screening flags, invitation status, and later Survey 2/reviewer dates. Survey 1's reported date is a screening value, not a reviewer-verified onset date.
- Track invitations, starts, consent decisions, completions, follow-up permission, and missingness by recruitment source. Do not infer a reason when someone stops.
- This is a **draft**, not a finalized consent or deployment-ready survey. Final privacy/public-use language and the ability to use partial responses require specific IRB review.
