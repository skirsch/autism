# Evidence handling and independent reviewer manual

**Version:** 1.0 draft
**Date:** October 4, 2026
**Status:** Proposed operational manual and review form; requires training and test-set validation

Three reviewers—Steve Kirsch, Karl Jablonowski and Brian Hooker—review all available evidence in one independent pass. They are blinded to one another's judgments, not to vaccination information. This manual does not make their judgments exposure-blinded or establish that three matching judgments are necessarily correct.

## Receipt and review packet

Receive authorized uploads only through the confirmed secure system. Assign random item IDs; preserve original bytes, receipt timestamp, checksum, reported provenance and any metadata separately. Do not strip original metadata from restricted evidence or alter the original to improve readability. Store a separately labeled derived viewing copy when conversion/redaction is needed. Reject executable content from execution, quarantine potentially unsafe uploads, and preserve a restricted inventory/disposition; confirm technical scanning/preview methods with IPAK.

Administrative staff document receipt and compensation/target completeness without seeing reviewer timing plots. They assemble a packet containing the immutable original 15-day account; neutral timing/continuity answers; additional disclosure/permission states; prompted answers and timeline; item inventory; original or labeled viewing copies; parent/evidence dates; submitted clarifications; all confirmed duplicate-parent accounts and conflicts. Parent report remains distinct from evidence. Do not include the other reviewers' assessments or a group hypothesis/desired lag.

Where dates, products or accounts materially conflict, staff seek one neutral consolidated clarification before locks, remind at day 7, and close the routine clarification window at day 14. No answer is an unresolved flag, not deletion. Ask, for example, “This item was made on [date], while you recall first notice on [date]. Does the item describe an earlier event, and how do you know?” Never suggest that the dates should match.

## Evidence support codes

Evidence is classified by its credible date and content, not by medium. The following codes are proposed operational labels, to freeze and validate before actual review:

| Code | Meaning | Supports |
| --- | --- | --- |
| E0 | No relevant item / no usable date or content | Parent report can remain; no corroboration |
| E1 | Retrospective account, including later clinical note repeating an old recollection | Reported history; not contemporaneous confirmation of old first notice |
| E2 | Credibly dated contemporaneous changed-behavior observation without content establishing first notice | Presence by a documented date; may bound chronology, not automatically ONSET |
| E3 | Credibly dated contemporaneous content specifically supporting first notice at an exact day or defensible range | Corroborated parent-first-notice precision actually supported |
| V1 | Credible actual-administration record with date/products | Vaccination administration at recorded precision; not automatically most recent visit/history completeness |
| W1 | Credible regular well-visit record and explicit support for no shots at that visit | Vaccine-free-at-visit; not automatically no vaccination elsewhere |
| H1 | Applicable documentary history with defined coverage reasonably supporting no vaccination in the full window, with other-provider limitations assessed | Record-supported window-wide absence; optional, never required for participation |

Each item may carry more than one support code. Use separate quality flags `date_uncertain`, `illegible`, `provenance_unknown`, `alteration_concern`, `content_ambiguous`, `conflicting`, `coverage_incomplete`. An item can support a range but not an exact day. Evidence code and uncertainty remain independent; do not encode unverified confidence as E3.

A contemporaneous text, diary, clinician note, lawfully recorded call/voicemail, contemporaneous call note, or dated video/photo can qualify. A call log without recorded content confirms a call, not what changed. An undated image does not establish a day. An after-only video is valid onset-related evidence for documented presence; a before-video is not required. Its filename alone is not a verified timestamp. Consider original metadata, platform/message timestamps, identifiable sequence, parent explanation and inconsistencies; do not assert forensic authentication that was not performed.

“First notice today” in credible contemporaneous content may support an exact reported notice date. A later item saying “it started two days ago” must retain its creation date and described-event date, with the reviewer assessing whether the near-contemporaneous statement supports that date and precision. A later retrospective note without contemporaneous corroboration remains E1. No fixed arbitrary “within X days” rule makes an item contemporaneous; reviewers explain temporal proximity and whether the content documents observation/notice rather than distant reconstructed history. Test these distinctions on standardized examples before review begins.

## Reviewer instructions

1. Confirm child/submission links and review the packet as a whole. Record known contradictions, not a preferred narrative. Birthdate is parent-entered; no proof required. Mark unresolved duplicate identity or authority concerns for staff.
2. Judge apparent prior baseline and the lasting skill/behavior change with concrete descriptions, observer and course. Mark SORA Yes, No or Uncertain. Record prior concerns and competing explanations; do not equate an acute symptom with the target developmental change or infer autism from an isolated video.
3. Determine parent-first-notice ONSET and its plausible bounds from report plus available evidence. Do not replace it with vaccination, illness start, an uncertain-functioning period, last-normal observation, diagnosis date or documentation date. A date can be exact but unverified. If no day can be determined, choose the applicable range/unknown status rather than a midpoint.
4. Separately identify the earliest credibly documented post-change observation among submitted materials and its precision. This field is not another onset endpoint. A first-observation date described within an item and the item's creation date remain separately available.
5. Select the applicable actual visit under the accepted window convention using the reviewer's own ONSET assessment. Check administration/products and whether a later vaccination is reported/unknown. If absence is only parent-reported, code it that way. Do not infer a vaccine from age or a nominal reference. Record all candidate visits and uncertainty at the 90-day boundary.
6. Assess B independently from the parent's timeline/baseline and all available support. Keep complete-day, partial-return, N/D/U and approximation rules. Do not compute B by subtracting fever duration, treat missing observations as abnormal, or convert a lower bound to an exact zero. Record supporting citations and raw discrepancies. No eligible vaccination or unestablished baseline produces the relevant not-applicable/unknown status.
7. Give each date/count a separate verification/support classification, precision and explanation. Lock the full assessment without discussing others' results. Do not open timing summaries until the designated review/build finalization milestone.

## Review form

Complete this same form once per reviewer/child. All dates use the date-object contract in [data_dictionary.md](data_dictionary.md). Unknown/not-applicable are permissible answers, not omissions.

| Field | Required entry |
| --- | --- |
| Reviewer and packet | Restricted reviewer ID, child ID, packet version/hash, review version and lock timestamp |
| SORA | Yes / No / Uncertain, prior-normal evidence, persistent change type, observer, prior concerns/competing explanation and coded reason |
| Birthdate | Parent-entered date, provenance, discrepancies; verification only if incidental support exists |
| ONSET | Parent-first-notice date or status; precision, lower/upper bounds; verification at that precision; support/conflict item IDs and reasoning |
| Observation context | Last adequate usual observation and first definite changed observation if known; distinct from first-notice bounds |
| Earliest documented post-change | Date/range/status, contemporaneous content, item/date provenance; do not substitute for ONSET |
| Vaccination anchor | Most recent eligible actual date/products or none/unknown; administration support; later-visit confirmation; window-membership uncertainty |
| Well-visit anchor | Conditional regular visit date, no-shots evidence and window-wide absence status/coverage; no qualifying/unknown allowed |
| Lifetime history | Parent-reported ever/never/unsure, optional corroboration kept separate |
| B | Exact/approximate/lower-bound/range/unknown/baseline-unestablished/not-applicable; value/bounds; baseline support, N/D/U, partial returns and citations |
| Earlier uncertain period | Timeline/return assessment and uncertainty, not an ONSET field |
| Conflicts | Date/product/history/B/phenotype/identity/source concerns and which judgments remain unresolved |
| Final attestation | All available packet material reviewed; no access/discussion of other judgments; assessment locked |

The locked scientific form does not decide compensation, the receipt-time 100-record count or privacy approval.

## Exact majority and consistency

After all three locks, apply exact two-of-three agreement independently to each judgment, date, status, bound, product classification and verification classification. Three matching answers are agreement class three; two matching answers class two; otherwise unresolved. For numeric dates/counts compare their normalized exact values only at supported precision; approximate or lower-bound status must not be discarded to create a numeric match. A lower-bound tuple differs from an exact count of the same number. Preserve raw text, standardized value, all original votes and the agreement provenance.

Accept lower and upper bounds separately, then calculate width, not a separate vote on width. Check lower<=upper, date within claimed bounds, birthdate<=ONSET, selected administration on/before ONSET and within window, and B bounds compatible with A. A fieldwise majority can create an inconsistent combination even when each field has two votes; such a combination stays unresolved for construction, with individual accepted votes still visible. Do not average, clamp, negotiate or revise judgments to obtain agreement. A majority date without majority corroboration is not a corroborated date.

Accepted B must be evaluated against the accepted vaccination window: record whether its supporting timeline/window matches those inputs. If reviewer B judgments concern incompatible windows, do not publish their numeric majority as a validated B for the accepted A. Record inconsistent-window status and preserve all assessments. Products on a shared visit do not yield separate child records.

Late evidence or genuine clerical errors require a separately authorized amendment, preserving the original and a reason/timestamp/packet version. Re-review after an amendment remains independently locked for all affected judgments, not an informal consensus. Routine workflow is one pass; exceptional amendments are visible, not a second planned exposure-blinding pass.

## Quality and external re-review

Before actual review, each reviewer independently codes the fictitious test set in [prelaunch_validation.md](prelaunch_validation.md); compare rule interpretations only after locks, correct manual ambiguities and version it before participant packets. Keep the calibration log. No actual evidence validation has been performed by writing this manual.

Report phenotype/date/B/evidence agreement separately, rates of three/two/unresolved agreement, date precision, missing support and conflicts. Shared reviewers/funder positions and access to exposure information remain limitations. Approved qualified independent researchers may re-review retained source evidence only through [privacy_security_and_release.md](privacy_security_and_release.md), with appropriate protocol/access approvals and confidentiality terms. No outside access is assumed already authorized.
