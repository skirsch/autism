# Eligibility and dataset construction

**Version:** 1.2 draft
**Date:** October 4, 2026
**Status:** Proposed operational rules for study-team and IRB review; not approved for enrollment

This manual implements the single-ONSET design in [study_overview.md](study_overview.md). It separates screening, receipt, compensation, scientific review and public-release decisions. No eligibility rule is chosen from an interim timing plot.

## Population and phenotype

The partner keeps its two-question contact screen and transfers only authorized possible-case email referrals. Every such referral may receive Survey 2 within the approved recruitment window, without age, date-confidence or records-confidence screening. An adult parent or legal guardian who understands the English research consent and has the required legal authority may complete Survey 2 according to the stated one-child rule. Autism is parent-reported at intake; a diagnosis document is not required. Select the youngest child meeting the previously normal, identifiable-change and 6–24-completed-month description; if none meets it, select the youngest autistic child. Retain other, out-of-range and uncertain study-collected reports in the Survey 2 dataset; partner individual screening answers are not transferred.

The target phenotype is apparent normal development followed by a dateable first notice of a substantial loss/reduction of an acquired skill, a clearly new marked behavior, or both, associated with the child's later autism presentation. A new behavior without skill loss can qualify. Fever, transient distress or illness alone does not qualify. There is no seven-day cutoff and no requirement that the whole change develop overnight.

Persistent means the parent describes a lasting change in the child's usual functioning, rather than only a temporary acute symptom followed by full recovery without that developmental change. Collect concrete examples, prior skill/behavior, direct observer, subsequent course, and competing explanations. Do not introduce a new fixed number-of-days rule. Unclear persistence is Uncertain, not an assumed Yes. Prior developmental concerns are retained and reviewed: substantial evidence contradicting the previously normal description produces No or Uncertain with a reason, not deletion. A diagnosis alone does not establish this phenotype.

ONSET is when either parent first noticed the qualifying lasting change. It is not biological onset, the start of an illness, an acute reaction, an appointment, or the date a clinician wrote a retrospective report.

## Separate flags

The target is 100 administratively complete documented-visit unique-child submissions, but 25 fully validated unique-child cases is the organizer's minimum acceptable dataset for proceeding if recruitment falls short. Validation is scientific, not an administrative receipt check or payment criterion. Freeze the exact minimum-count flag before enrollment, including how corroborated no-anchor cases and approximate-date cases contribute; do not silently assume every retained case, every paid response or every documented visit is fully validated. Existing evidence-supported vaccination/well-visit tiers and retained no-anchor evidence flags remain distinct. Meeting the minimum does not require all 25 to have the same vaccination history or imply B/C/every subgroup has 25 exact values.

| Flag | Operational rule |
| --- | --- |
| `s2_invitation_authorized` | Authorized possible-case email referral with usable contact and no stop-contact request; every such referral is invited within the approved recruitment window. No confidence or age gate. |
| `records_request_eligible` | Affirmative research/required authority and records-contact permission; receipt-time parent-reported qualifying phenotype and onset age 6–24 completed months. Uncertain ages remain unresolved; exact-date confidence is not a gate. Four A4 confidence groups determine request order, not survey access. |
| `s2_complete` | Every routed required screen has an explicit submitted answer, including allowed unknown/not-applicable answers; narrative submitted and locked; affirmative continuation; date of birth entered or explicit inability recorded; ending submitted. Required screens do not force invented dates or evidence. |
| `admin_target_complete` | Receipt-time reported phenotype/age eligible in Survey 2; required Survey 2 fields submitted including birthdate and narratives; at least one apparently dateable document for a reported in-window vaccination or regular vaccine-free well visit. Administrative staff inspect presence/dateability, not proof of SORA or first notice. |
| `full_payment_eligible` | Required Survey 2 fields including birthdate/narratives plus a qualifying visit document OR an apparently dateable contemporaneous item with onset-related content. No-anchor families can qualify. Reviewer conclusions are irrelevant. |
| `good_faith_payment_eligible` | Good-faith submission of requested materials under disclosed deadline/terms, even if incomplete or scientifically unusable. Guaranteed $25; no automatic denial for an unresolved duplicate. |
| `review_sora` | Exact majority Yes / No / Uncertain / unresolved. |
| `review_age_eligible` | Accepted ONSET and parent-entered birthdate establish 6–24 completed months; otherwise out of range or unresolved. |
| `documented_vax_timing` | Majority SORA Yes, age eligible, accepted eligible administered vaccination anchor, accepted ONSET corroborated at stated precision, no material unresolved chronology/history conflict. Exact-day summaries additionally require exact accepted dates. |
| `documented_well_timing` | Same onset/phenotype/age requirements, documented regular well visit without shots, and sufficiently supported absence of vaccinations elsewhere in the full window. Parent-only absence is separately labeled, not promoted to corroborated history. |
| `public_row_approved`, `public_narrative_approved` | Approved consent scope, licensing permission and documented two-person disclosure-risk signoff; independent of all timing findings. |

Explicit unknowns permit survey completion but do not supply the evidence or dates needed for the target count, full payment or a given scientific subset. Survey completion covers routed research-answer screens and records-contact permission; deferred records authorization/upload/item-detail screens are separate tasks, not required before that person's request phase opens. Birthdate inability is a complete screen answer but does not meet those administrative definitions requiring an entered birthdate. Record the receipt-time eligibility snapshot and its uncertainty before records review; do not impute an in-range age or exact date. Administrative completeness is fixed from receipt-time parent reports; a later reviewer ONSET or age discrepancy does not retroactively remove a submission from the target. Correct documented duplicate counts and clerical receipt errors through an audit amendment, not a scientific reclassification.

## Unique children and duplicate submissions

Use random submission and child identifiers. Never use an email as a research key. Restrict matching to authorized staff using existing contact/link tokens and child details; do not request new names, addresses or government identifiers solely to deduplicate. Exact agreement in birthdate alone is not confirmation. Confirm through existing linkage or a neutral contact question when necessary. Record suspected, confirmed-same-child, confirmed-distinct, or unresolved status and the reason/checker/date. Preserve all original accounts and sources, including conflicting accounts by two parents. Review the combined packet without selecting a favorable account.

Confirmed duplicates count as one child toward 100 and once per plot; count actual submissions separately in response funnels. Report a known-confirmed count and unresolved-duplicate count rather than falsely guaranteeing unique cases. Do not blend incompatible parent dates; preserve each response's derived series until a primary parent-report input is identified by provenance. For a child-level parent-report series, use the first completed consenting submission by receipt timestamp, with deterministic submission-ID tie break; later conflicting reports stay visible. This is a proposed implementation convention to freeze before enrollment, not a preference based on results.

## Calendar and date precision

Store calendar dates in ISO `YYYY-MM-DD`, separate from UTC system timestamps. Use the event's reported local calendar date; do not shift an event date using the server timezone. Derive completed months from the original birthdate using calendar-month anniversaries, clamping the day to month end if absent. Exactly 6 months qualifies; a child who has turned 25 months is outside the cohort. Thus 24 completed months includes the period until the 25-month anniversary, not only the birthday itself. Flag birthdate after ONSET as inconsistent.

For exact dates, lower and upper bounds equal the date and uncertainty width is zero. For a known week/month, store actual period bounds and precision; do not manufacture its midpoint. Unknown bounds have null values and explicit status, not zero. An exact recollection can remain unverified. When interval arithmetic is supported, `lag_low = onset_low - anchor_high` and `lag_high = onset_high - anchor_low`; use only eligible pairings, and flag uncertainty in selection of the most recent visit. These are bounds, not exact histogram entries.

## Actual visit selection

The actual window is inclusive: `0 <= ONSET - visit_date <= 90` calendar days. Same-day administration is eligible but its order within the day remains unknown unless reported. A future visit or a visit 91 days earlier cannot be an anchor. Keep outside-window information as context.

First choose the most recent actual vaccination on or before ONSET within that window, supported by administration rather than a planned schedule. Multiple products on one date form one visit. Preserve whether the parent confirms no later vaccination, reports a later visit, or is unsure; a single record verifies administration but not complete most-recent history.

Only when no vaccination in the window is established at the relevant evidence tier, choose the most recent regular vaccine-free well visit in the same window. A record with no vaccine mentioned is not automatically proof none was given. Keep parent-reported no-vaccination, record-supported vaccine-free-at-visit, and supported window-wide absence distinct. Sufficiently supported absence requires records explicitly covering the window or an applicable clinical/registry history that, together with the parent's report about other providers, reasonably supports completeness; record coverage limitations. Such history is optional, not a participation requirement.

If history, dates or membership in the window are uncertain, retain candidate visits and flags without forcing a confirmed anchor. Cases with neither visit remain available for phenotype, age, narratives and C where inputs permit. Never-vaccinated means parent-reported lifetime status unless separately corroborated; no recent visit does not prove it.

## A, B and C

A is ONSET minus the selected vaccination date. Derive parent-report, each reviewer and majority series from their own inputs. Never fill an unresolved reviewer field from another reviewer. B is a direct count/assessment, not A minus acute-symptom duration. It adds all complete normal calendar days from vaccination day through the day before ONSET, including disconnected normal periods. Count vaccination day only if at baseline throughout ordinary observation. Exclude ONSET day and pre-vaccination days. Partial-day returns remain separate. Known exact values satisfy `0 <= B <= A`; A zero implies B zero. No eligible vaccination means A/B not applicable.

Normal means observed pre-vaccination behavior and skills, not merely absence of fever. An observed non-normal portion excludes a complete normal day. A genuinely unassessable or unremembered day is unknown, not abnormal. For exact classifications, N definitely complete-normal + D definitely not complete-normal + U unknown = A. If U > 0, supported B bounds are N through N+U; N is not an exact B. Approximate counts stay approximate. Keep raw B>A, conflicting narratives and inconsistent category totals; clarify, do not clamp or rewrite. Baseline-unestablished stays its own status.

Calendar-quarter C uses the latest January 1, April 1, July 1 or October 1 on/before ONSET, with no artificial 90-day truncation; quarter offsets can reach 91 days. Nominal-age C uses original birthdate plus 2, 4, 6, 12, 15 or 18 calendar months, selecting the latest on/before ONSET within 90 days or no anchor. No added 9/21/24-month point, historical customization or vaccine-product inference. Record `nominal_grid_v1` and `calendar_quarter_v1`. Both are descriptive references, not validated no-effect controls.

## Subsets and denominators

Report separately intake responses, invited responses, consenting Survey 2 starts, locked narratives, disclosure shown, explicit continuation/decline, abandonment, submitted evidence, administratively complete unique children, payment eligibility and evidence-supported cases. Denominators are defined by the screen/field reached, not by available favorable answers. Retain partials and uncertain cases; use only fields they support. Lower bounds do not enter exact-count bins. Each later plot states parent/reviewer/majority source, evidence/precision tier, selected-child/sample restrictions and its own missing/no-anchor counts. Product-specific plots overlap and are not independent cohorts. These data do not estimate population incidence or causal risk.
