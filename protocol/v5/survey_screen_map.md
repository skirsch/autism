# Survey screen and branch specification

**Version:** 1.2 draft
**Date:** October 4, 2026
**Status:** Proposed implementation specification; platform behavior not verified

Question wording comes from [survey1.md](survey1.md), [survey2.md](survey2.md) and the stage-specific text in [consent_and_disclosure.md](consent_and_disclosure.md). This map splits compound drafting prompts into individual screens. Dictionary names are defined in [data_dictionary.md](data_dictionary.md).

## Display and saving contract

Display one substantive question at a time. Consent pages may contain the complete information needed for that stage and its consent control. No future-screen preview, survey progress labels naming candidate events, preloaded event-specific answers, browser document titles, help text or emails may reveal named candidate events before A1–A4 are saved. Participants may themselves mention an event; never remove it.

Each routed question offers a substantive answer and, where appropriate, an explicit unknown/unsure/cannot determine option. Required means answer-or-explicit-unknown, not a forced number. Free narratives can be brief; there is no word-count quality threshold or favorable-content requirement. An explicit cannot-remember account is retained and may limit review, not payment through scientific quality. Optional uploads and contact permissions can be declined.

Save acknowledged answers after affirmative consent; show that saved partials are retained. Do not record unsent keystrokes. On A1 provide Save draft and Confirm original account. Confirm locks the original server-side; later corrections use a separate clarification record. A parent can revisit A1 read-only, but not undo the lock after disclosure. If a platform cannot provide the lock, consent audit, partial capture or reviewer isolation, do not deploy it as compliant.

## Survey 1 — partner contact-interest screen

| Screen | Partner content | Route / custody |
| --- | --- | --- |
| S1-P | Partner information/privacy notice; identified receiving study team | Approved source-specific notice; not study research consent |
| S1-01 | Possible sudden-onset child: Yes / No / Unsure | Partner retains answer; no child data transferred |
| S1-02 | Interest and explicit permission to share email: Yes / No | Permission for contact, not research participation |
| S1-E | Email entry/confirmation | Yes permission only |
| S1-END | Submit and thanks | Yes/Unsure possible case plus authorized usable email enters referral list |

The study receives authorized emails only, with source/batch administrative metadata and a permission attestation. Partner individual answers remain partner-held; aggregate screen/recruitment counts are requested where available. Survey 1 asks no age, birth year, date, date confidence, records-confidence or candidate-event information. Its privacy/retention and institutional role require review. Every authorized possible-case referral receives a Survey 2 invitation within the approved recruitment window.

## Survey 2 before disclosure

| Screen | Content | Export and route |
| --- | --- | --- |
| S2-C | Neutral stage-2 information, funding/team contact, retention/public sharing/payment overview and affirmative consent | No research answers before agreement |
| A1 | Unprompted account of 15 days before the first clear change through that change, baseline/change/observer/course | `narrative_unprompted`; first substantive question; Save then Confirm lock |
| A2 | First-notice ONSET date / best estimate / range / unknown | `onset_parent`; precision, bounds and `date_confidence_s2` on separate follow-up screens; no confidence gate |
| A3a | Earlier period when usual functioning could not be assessed? | yes/no/unsure; no named causes |
| A3b–d | Most recent uncertain period start/end/duration | Yes/unsure branch; date/range/unknown; no lookback cutoff |
| A3e | Full return before clear change? | Yes/No/Unsure; parental assessment |
| A3f | When full return began, brief/partial return description | Yes or partial/uncertain return branch |
| A4 | Four neutral records-confidence choices; unsure allowed | `records_confidence_s2`; save before disclosure; used only for later records requests |
| B1 | Full additional named-event disclosure and choice | Show only after A1 lock and A2/A3/A4 answered; Yes continues, No ends, departure separately logged |

Each A2 and A3 date-control sequence shows exact date, approximate day/week/month/range or unknown; plausible lower and upper dates only if known. Do not auto-fill from another event. An uncertain period is not another ONSET.

## Survey 2 after affirmative continuation

All compound prompts below become separate screens, with neutral screen labels. C02 precedes the structured event checklist. Routing C02 is based on the parent's account, not a vaccination entry the platform has secretly collected earlier; give vaccination/well/no-visit alternative wording in the disclosed prompt. Structured C07/C08 later establish the eligible visit and may trigger an additional timeline clarification without changing A1.

| Screen group | Separate prompts | Required route |
| --- | --- | --- |
| C01 | Confirm Survey 2 selected child; birthdate; country at ONSET | All continuers; unknown retained; no partner child data to prefill |
| C02 | Prompted full-window chronology, including every normal period and uncertain/abnormal period | All; explicitly allow no eligible visit |
| C03a–f | New behavior; reduced/absent skill; prior usual pattern; observer; persistence; subsequent course | All; none/unsure allowed |
| C04 | Date/uncertainty and last-normal/first-changed clarification | All; context not replacement onset |
| C05 | Diagnosis status, then approximate date and clinician type if Yes | All status; conditional details |
| C06 | Free-text other events, then one event type per screen and conditional dates/descriptions | All; yes/no/unsure, no preferred answer |
| C07a–d | Regular well visit within 90 days; most recent date; shots actually given; later vaccination | All presence; conditional details; separate well-comparator eligibility |
| C08a–d | Any vaccination on/before ONSET; most recent date with no maximum lookback; products on that date; later vaccination; same-day order | All presence; conditional details; allow approximate/unknown dates; `vax_on_or_before_onset` |
| C08e | Any vaccination within 90 days of ONSET? Yes / No / Unsure | All; `vaccination_within_90_days`, independent well-comparator assessment; no cutoff on vaccination request |
| C01b | Country living in at selected eligible vaccination | Eligible reported vaccination only; same as ONSET/unknown allowed |
| C09a–e | Illness/unusual observations before vaccination; description; observed pre-vaccination baseline; usual functioning immediately before; last usual date if not clearly Yes | Eligible reported vaccination only |
| C10a/b | Routine/modified/unsure plan; immediately previous distinct vaccination date or interval/no earlier/unknown | Every reported eligible vaccination, not modified-plan-only |
| C11 | Ever vaccinated, parent report | All |
| C12a–e | Acute symptoms after vaccination before ONSET; type; start; end/ongoing; end lag | Vaccination branch; details if Yes/unsure |
| C12f | Total complete normal days B and precision | Vaccination branch; zero/approximate/lower-bound/unknown/baseline-unestablished |
| C12g/h | Observations on non-normal/unassessable days, free text first then categories | Vaccination branch, including B unknown |
| C12i/j | Partial-day returns; approximate timing/duration | Vaccination branch |
| C12k–n | N; D; U; unassessable/unremembered reason | Vaccination branch; separate screens, unknown allowed |
| C13 | Available dated materials | All; none/unsure allowed |
| C14a | Permission for records contact | All; No does not erase answers |
| C14b | Records-sharing authorization and current payment terms | Deferred to opened records-request phase; before upload/work; consent separately logged |
| C14c | Secure upload or secure invitation link | Opened request phase and affirmative authorization only; never ordinary email attachments |
| C14d–h | Per-item creation date; event date described; parent first notice; certainty/bounds; documentation delay explanation | Submitted items; unknown allowed |
| S2-END | Submit, retained-data/payment/contact reminder and thanks | All completers; no payment promise based on scientific result |

Repeat C08 date/products when a later visit is identified; retain prior entry and change link. Unsure history does not branch automatically to confirmed vaccine-free well visit. An older vaccination remains the A/B anchor even when a separate well-visit lag applies; never substitute the well date. No known vaccination on/before ONSET means A/B are not applicable or unresolved as appropriate, not zero. All routes still reach lifetime history, materials, authorization and closing. C02 and B cover the full vaccination-to-ONSET period; allow approximate periods and unknown days rather than forced precision for long lookbacks. Conflicting birthdate/ONSET values trigger a neutral review warning and clarification, not loss of submitted material.

## Partial and operational states

Distinguish invited, opened, consent declined, consented start, A1 draft saved, A1 locked, A2/A3/A4 saved, disclosure displayed, affirmative continuation, explicit decline, departed without choice, completed, records requested and records received. Each state has a timestamp/version in restricted logs. A closed browser alone does not establish deliberate decline or its reason.

Survey 2 invitation tracking and supporting-material request batches are separate stages. Record request phase/group/permission, request sent, request deadline, authorization and receipt independently of survey completion; C14b–h may occur in a separate secure follow-up after S2-END. Do not mark a completed survey incomplete merely because its records phase has not opened.

For survey disposition calculations, mark an uncompleted session operationally open until its invitation's 14-day response window closes; then mark `operationally_closed_incomplete` without deletion. Later resumptions/submissions are amendments to disposition, remain accepted under approved deadlines, and are not double-counted. This is a proposed administrative convention; IPAK must confirm resume-token expiration, security session timeout, data-saving and retention behavior. Security timeout is separate from the 14-day research window. Stop-contact requests suppress future research reminders without deleting existing authorized answers or blocking an owed payment.

For records-batch yield, mature the denominator from the records request's own 14-day window, not its Survey 2 invitation. Stop new records requests at the administrative target; Survey 2 access is not ranked by confidence.

Before launch measure completion times on fictitious participants and insert realistic estimates in consent/invitations. Freeze screen text, IDs, branches, dictionary/export adapter and approval version together. Live tests in [prelaunch_validation.md](prelaunch_validation.md) are mandatory; this map is not a completed platform deployment.
