# Recruitment records requests and compensation procedures

**Version:** 1.3 draft
**Date:** October 4, 2026
**Status:** Proposed staff procedure and participant messages; requires IRB and operational approval

Use approved versions only. Partners are described generically in this public working package; source identities/contracts belong in the restricted regulatory file. Contact authority, delivery systems and staff access must be confirmed before use. This procedure implements [eligibility_and_construction.md](eligibility_and_construction.md) and [consent_and_disclosure.md](consent_and_disclosure.md).

## Partner onboarding and denominators

Approach large autism membership organizations first; if none agrees, approach diagnosis/treatment clinics. If initial recruitment is insufficient, approach up to three additional approved sources sequentially. No source, mailing-list size or delivered count is assumed. Use the same approved survey versions; any local administrative questions are labeled separately and may not change research wording/order.

Record source code, actual host, permission to send invitations, invitation batches/dates, attempted/delivered/undeliverable/opt-out counts and technically available opens. Availability of an email or delivery does not mean it was read. Document denominators that cannot be obtained; never reconstruct them from responders. Track unique invitations, message attempts and response records separately. Keep source-specific funnels, overlaps and confirmed duplicates visible. Do not select membership subgroups based on vaccination opinions/history or a reported vaccine-linked story.

## Partner screen invitation draft

**Subject:** Would you like an invitation to a study of developmental changes?

We are helping a research team contact parents of autistic children who appeared to develop normally and then had a clear, lasting change in behavior or skills. This brief English-language screen asks whether that description might fit and whether you authorize us to share your email with [identified study team] for an invitation. Dates, records and research answers are not requested here. Uncertainty about an exact date is fine. Saying Yes does not commit you to the study or affect membership, services or benefits.

[Approved partner screen link and partner privacy/contact notice; truthful study/funder/interest information required by approved recruitment materials.]

Do not add named candidate events, anecdotal case examples or causal claims. The partner's retention/privacy policy and role require review; its individual answers are not transferred to the study.

## Survey 2 invitation and reminder drafts

**Subject:** Invitation to the developmental-timing follow-up

You authorized a participating organization to share your email so we could invite you to learn about this study. Everyone referred may respond, including parents uncertain about dates or records; best estimates and confidence are useful. We invite you to describe your child's usual behavior and skills, the 15 days before the first clear change, and when the change was first noticed. Additional information and optional questions/materials requests come later; you may decide then whether to continue. Read the information at the link before participating. Participation is voluntary. The current proposed materials-task payment is [active approved amount and link to full terms]; a good-faith materials submission earns the guaranteed $25 under the stated rules. An account alone is not automatically a paid materials submission.

[Secure personal invitation link; do not forward]

Please respond by [invitation date plus 14 calendar days, actual date]. Contact Steve Kirsch at [confirmed study mailbox] for help or to stop future reminders. Do not send evidence by email.

**Day-7 reminder:** This is one reminder about the optional developmental-timing follow-up sent on [date]. If you wish to take part, please use your invitation by [date]. You may decline or ask us not to contact you again. [Same neutral link/contact/payment terms.] No reminder after an explicit decline or stop-contact request; payment/correction communications are separate.

Use one day-7 reminder as a proposed operational default, subject to IRB approval. Do not introduce named events in invitation subject lines, help pages or emails before the original narrative lock.

## All-referral Survey 2 invitations and phased records requests

100 remains the administrative documented-visit recruitment target; 25 fully validated unique-child cases is the minimum acceptable evidence-supported resource if recruitment falls short. These are not confidence gates on Survey 2, result-driven stopping thresholds or power guarantees.

Invite every authorized possible-case referral to Survey 2 within the approved recruitment window. Do not select its invitees by records-confidence, onset-date precision or age absent from the partner screen. Research consent/authority is obtained before answers. Retain best estimates, uncertain dates and low-confidence reports.

Use Survey 2 A4's original pre-disclosure records-confidence for subsequent requests only: definitely available now; probably available/know how; might be available/need to investigate; probably unavailable. Missing/unsure stays unclassified; seek a neutral clarification without excluding survey answers or creating a fifth ranked group. The request pool additionally requires records-contact permission and receipt-time reported phenotype/6–24-month eligibility; unknown/out-of-range answers remain retained outside that focused request pool.

Selection staff receive a minimized queue containing IDs, permission, reported eligibility and records-confidence, not exposure fields, causal beliefs or reviewer judgments. Freeze the random seed/method before first request; archive sorted input IDs, pool hash, selected IDs and version. Never redraw to obtain desired cases.

Initially request materials from a random 100 eligible consenting candidates in Group 1; fill from the next group if needed. If fewer candidates have completed Survey 2, cap at the available pool and record later entrants under the same frozen ordering method. After each request batch's 14-day window, count matured requests I_m and their administrative documented-visit yield C_m; total complete documented-visit unique children is C. If C < 100 and C_m > 0, request `ceil(1.20 * (100-C) / (C_m/I_m))` next; if yield is zero/unestimable, request 100 or the remainder. Exhaust groups in order and cap at unrequested candidates. Credit confirmed duplicate children to the earliest qualifying records request; retain all overlapping accounts without double credit.

Only administrative request/receipt counts inform batch sizing or adding up to three approved sources. Stop opening new records requests at C >= 100; accept already requested submissions beyond target. Do not stop or replace cases based on reviewer conclusions or plots. Correct confirmed duplicate/clerical count errors through an audit. Survey 2 invitation access, approved enrollment ceiling/end date and stop-contact requests remain separate. The public dataset contains study-collected responses, not the partner's individual screen answers.

## Record request draft after authorization

Thank you. Please use [approved secure route] to share the narrow set described on your authorized records screen: the most recent actual vaccination date/products record on/before first notice, with no maximum lookback; separately, if no vaccination occurred within 90 days, the most recent qualifying regular well-visit document without shots within that period, if available; plus any existing dated onset-related material. If neither visit exists, relevant dated onset material is still welcome. No full immunization history or birthdate proof is required. Provide dates and certainty as remembered, even when a document was made later. Do not change evidence to match an answer. Deadline: [actual approved date]. Current full-response payment: [amount and objective criteria]. Scientific conclusions do not determine payment.

If material clarification is necessary, send one consolidated request and one day-7 reminder, allowing 14 calendar days from that request. Ask neutral factual questions about conflicts/dateability; do not suggest an onset date or preferred answer. Preserve nonresponse and late clarifications. Late data become auditable additions, not silent changes to locked reviews. Stop-contact requests end research requests.

## Payment operations

The first two-week compensation checkpoint is 14 calendar days after the first Survey 2 invitation batch. At each checkpoint with C < 100, increase full-response compensation by $25: $25 to $50 to $75 to $100. Subsequent increase checkpoints are 14 days after the previous increase. Do not increase after C >=100 or beyond $100. Log actual activation times/counts; the amount displayed to participants is a deployed approved value, never a placeholder. Even if there is no new wave, earlier equivalent completions are eligible for the activated top-up.

Full payment requires all routed required answers/narratives and parent-entered birthdate plus either a qualifying most-recent vaccination item on/before ONSET (any lag) or vaccine-free well-visit item within 90 days OR an apparently dateable contemporaneous item with onset-related content. No-visit submissions with onset evidence receive full payment but do not count toward 100. Scientific strength and reviewers' conclusions do not matter. A good-faith requested-material submission failing full-response criteria receives $25. Do not imply all unpaid survey-only responses earn a gift card.

Normally there is one full-response entitlement per confirmed child. Link repeated uploads/corrections and top-ups to that entitlement, not another full payment. Honor separate promises already made to separately invited parents and all guaranteed good-faith commitments; do not claw back issued/promised payments. Unconfirmed duplication is not an automatic reason to deny payment. Document exceptional honored promises and avoid soliciting unnecessary financial identifiers.

Authorized administrative staff record amount promised, active tier, objective completion checklist, payee authorization, issue date/transaction, successful/failed delivery and top-up owed. A second authorized staff check compares the ledger against objective criteria and duplicate commitments before issue; designate staff before launch. Do not show them reviewer results to decide payments. Proposed payment service standard is within 14 calendar days after administrative determination or top-up activation, contingent on IPAK/funder confirmation and disclosure before work. Maintain an unpaid/failure queue and reconcile it; never mark an undelivered card paid. Gift-card vendor contact/payment data handling must be documented.

Any partner reimbursement is pending agreement and IRB review. Do not import prior clinic-payment amounts from other protocol versions. Proposed basis is reasonable documented administrative costs, independent of response rate, SORA cases, exposure history, timing pattern or outcome. Confirm budget, receipts, beneficiaries and conditions in [governance_and_confirmations.md](governance_and_confirmations.md).
