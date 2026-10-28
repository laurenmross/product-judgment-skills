# Worked example: evaluate-product-investment

Synthetic scenario, written to show depth and register. It is not an evaluation fixture, and all figures are supplied inputs rather than real data.

## Request

> We've spent two quarters on our Slack integration. It was scoped for one. 400 of 6,000 eligible workspaces installed it, and installers renew at 88% versus 80% for everyone else. Average workspace ARR is $3,000. The team wants one more quarter (three engineers) for workflow features they expect to lift installs to 700. The alternative for those engineers is SSO: sales says 15 late-stage enterprise deals are blocked on it, our late-stage win rate is 30%, and those deals average $12,000 ARR. What should we fund?

## Response

**Allocation decision:** Three engineers for one quarter. Owner: Head of Product. Next commitment: one quarter of work.

**Options:** Baseline (maintain the Slack integration, no new features) | smaller scope (instrument Slack retention for causality, no new features) | proposal (Slack workflow features) | best alternative (SSO).

**Value chain and evidence:**
- *Slack:* 6,000 eligible → +300 installs (team projection) → retention lift among new installers → retained ARR. The 88% vs 80% gap is observed, but installers likely differ from non-installers (more engaged teams install integrations), so the causal lift is unknown and probably smaller than 8 points.
- *SSO:* 15 blocked deals → 30% historical win rate (supplied) → new ARR. The dependency is whether SSO is actually the blocker, which is sales' judgment, not verified.

**Economics (first-year ARR, ignoring discounting):**
- SSO: 15 × 30% × $12,000 = **$54,000** new ARR, if SSO is the binding blocker.
- Slack features: 300 new installs × causal retention lift × $3,000. At the full 8 points: 300 × 0.08 × $3,000 = **$72,000** retained ARR. At half: **$36,000**. At zero: **$0**.

**Scenarios:**

| Assumption | Result | Limitation |
| --- | --- | --- |
| Full 8-pt lift is causal; installs reach 700 | Slack $72k > SSO $54k | Ignores selection; install projection unvalidated |
| Half the lift is causal | Slack $36k < SSO $54k | Split is illustrative |
| No causal lift | Slack $0 | — |

These are scenarios, not probability intervals.

**Break-even / ranking sensitivity:** Slack beats SSO only if the causal retention lift is at least $54,000 ÷ (300 × $3,000) = **6 points** *and* installs actually reach 700. Both are load-bearing. The timeline is also unanchored in the team's favor: the integration took twice its scope, so a one-quarter estimate for workflow features deserves skepticism.

**Recommendation and opportunity cost:** Fund SSO. Its value depends on one checkable claim (SSO is the blocker). Slack features depend on two unvalidated assumptions and a timeline the team has already missed once. The opportunity cost is the Slack upside if the full lift turns out to be causal. Continuing Slack work is itself a funding decision; the two quarters already spent don't count toward it.

**Next increment:**
- SSO: cap at one quarter, three engineers. Before starting, sales confirms in writing with at least five of the 15 prospects that SSO is the remaining blocker. Stop or reduce scope if fewer than half confirm.
- Slack: no new features this quarter. One analyst spends two weeks estimating causal lift, for example comparing renewal before and after install within the same workspaces. Reopen Slack funding next quarter if the estimate is at or above 6 points.

## Why this response works

- It compares against the best alternative use of the same engineers, not against doing nothing.
- It treats the observed retention gap as possibly selection, and shows what each interpretation implies.
- It computes a break-even that names the exact assumption that would flip the ranking.
- It ignores sunk cost while still using the overrun as evidence about estimate reliability.
