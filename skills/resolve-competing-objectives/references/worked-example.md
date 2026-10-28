# Worked example: resolve-competing-objectives

Synthetic scenario, written to show depth and register. It is not an evaluation fixture, and no usage or cost figures are supplied.

## Request

> Design wants to remove our legacy reporting dashboard because new users find two dashboards confusing. Customer success wants to keep it because about 200 large accounts built workflows on it. Engineering wants it gone because it blocks a database upgrade. This is the third deprecation fight this year. VP of Product decides. How do we resolve it?

## Response

**Decision / accountable owner / deadline:** Whether, when, and how to retire the legacy dashboard. VP of Product. Deadline not supplied; the database upgrade schedule likely sets it.

**Objectives:**

| Group | Outcome | Measure | Horizon | Rationale |
| --- | --- | --- | --- | --- |
| Design (for new users) | Less confusion at onboarding | Onboarding completion; support tickets about dashboards | Next two quarters | Two dashboards split attention |
| Customer success (for ~200 large accounts) | Workflows keep working | Renewal; escalations | Next renewal cycle | Disruption risks expansion revenue |
| Engineering | Unblock the database upgrade; lower maintenance | Upgrade date; engineer time on legacy | This year | Legacy code holds back platform work |
| Affected users at large accounts (not in the room) | Reports they rely on still exist | Usage of specific legacy reports | — | Their preferences are unknown; don't assume them |

**Conflict type:**
- *Fact:* how many of the 200 accounts actively use the legacy dashboard, and for which reports. Not supplied; this can be measured.
- *Resource:* engineering time to maintain legacy vs. build parity in the new dashboard.
- *Preference:* how much disruption to existing large customers is acceptable to simplify things for new users.
- *Hard constraint:* none stated. Check for any contract that promises the legacy reports.

**Feasibility constraints:** Ask legal or CS whether any contract references the legacy dashboard by name. Verification status: unknown.

**Options:**

| Option | Gains | Losses | Who bears it | Timing |
| --- | --- | --- | --- | --- |
| Keep both | No disruption | Confusion continues; upgrade blocked | New users; engineering | Indefinite |
| Remove now | Simplicity; upgrade unblocked | Broken workflows | Large accounts; CS | Immediate |
| Hide for new users, migrate existing on a schedule | Simplicity for new users now; time to migrate | Engineering builds parity for the most-used reports first; upgrade delayed by the migration window | Engineering; some large accounts lose rarely used reports | One to two quarters |

**Possible redesign; remaining irreducible tradeoff:** Hiding legacy for new users solves design's problem today without touching existing accounts. That leaves one real tradeoff: how long engineering carries the legacy code, versus how much of the long tail of legacy reports large accounts lose.

**Recommendation:** Hide the legacy dashboard for new accounts now. Measure which legacy reports are actually used. Build parity only for reports used by a meaningful share of the 200 accounts (the VP sets the cutoff). Then retire legacy on an announced date. Accepted downside: some large accounts lose rarely used reports and will need help rebuilding them. Strongest dissent: CS may argue any lost report risks a renewal; that should be checked against the actual usage data.

**Settlement:** Scope: legacy dashboard only. Owner: VP of Product; CS owns account outreach; engineering owns parity work. Guardrail: zero renewal losses attributed to the change during the migration quarter. Proposed review: if two or more top-50 accounts escalate, pause and review. Reopen if usage data shows broader dependence than expected.

**Standing principle (because this is the third fight this year):** Propose a deprecation policy for the VP to approve: measure usage before announcing, give customers a fixed notice period, guarantee parity for features above an agreed usage share, and name the decision owner. Future deprecations then start from the policy instead of being re-argued.

## Why this response works

- It separates what can be measured (usage) from what must be chosen (acceptable disruption).
- It finds a sequence that dissolves part of the conflict before forcing a tradeoff.
- It names who bears the cost of each option, including users who aren't in the room.
- It uses a recurring conflict to propose a policy instead of settling the same fight again.
