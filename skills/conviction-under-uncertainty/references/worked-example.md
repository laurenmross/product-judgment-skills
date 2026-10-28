# Worked example: conviction-under-uncertainty

Synthetic scenario, written to show depth and register. It is not an evaluation fixture, and all figures are supplied inputs rather than real data.

## Request

> We want to remove API access from the free plan to push upgrades. Finance projects 3–6% of the 4,000 free accounts using the API will upgrade. Two enterprise prospects said free API access is why they trialed us. Support thinks churn complaints will be manageable. The VP needs a recommendation Friday. Should we do it?

## Response

**Decision / owner / deadline:** Whether to remove free-plan API access, and how. VP of Product decides by Friday.

**Recommendation and commitment scope:** I recommend removing API access for *new* free signups only, keeping existing free accounts unchanged for one quarter, because this tests the upgrade thesis without breaking integrations people already rely on. The largest unresolved risk is that free API access is a top-of-funnel source for enterprise deals, which neither the projection nor the support view measures.

**Door assessment:**

| Component | Reversible elements | Irreversible residue | Rollback time/cost | Latest safe reversal point |
| --- | --- | --- | --- | --- |
| New-signup restriction | Plan config | Minor: some developers never trial | Hours | Any time |
| Removing access from existing accounts | Plan config | Broken customer integrations; public perception that we revoke features | Config in hours; trust not restorable on demand | Before the announcement |

**Evidence threshold:** The new-signup change is a cheap two-way door, so a bounded test is justified on mixed evidence. Revoking existing access is closer to a one-way door on trust, so it needs evidence that upgrades outweigh lost enterprise pipeline. We don't have that evidence yet.

**Thesis:** Restrict API → free API users hit a limit → some upgrade for continued access → paid conversion rises, provided pipeline loss stays smaller than the gain.

**Belief ledger:**

| Assumption | Evidence for / against | Confidence rationale | Decision sensitivity |
| --- | --- | --- | --- |
| 3–6% of API users upgrade | Finance projection (method not supplied) / none | Unanchored: no comparable past change cited | High: the case for the full change rests on it |
| Free API seeds enterprise deals | Two prospects said so / no pipeline attribution data | Two anecdotes; direction plausible, size unknown | High: could flip the recommendation |
| Complaints manageable | Support's judgment / none | Opinion; doesn't cover integrations breaking silently | Medium |

**Strongest alternative and objection:** Remove access for everyone now. That gets the full revenue effect a quarter sooner, and the staged version delays learning about existing users. My answer: the delay costs at most one quarter of upside at 3–6% of 4,000 accounts. Getting the enterprise question wrong costs trust that can't be rebuilt on a schedule.

**Why learn first:** The upgrade rate among new signups and pipeline attribution for free API users can both be measured within a quarter. Either result could change the decision about existing accounts.

**Learning plan:** Tests whether restricted new signups upgrade at the projected rate. Cap: new signups only. Duration: one quarter. Success: proposed at ≥3% upgrade among new signups who attempt API use, to be agreed by the VP; this threshold is my proposal, not a finding. Guardrail: sales tags any lost deal citing API access. Branches: above threshold and no tagged losses → plan an announced migration for existing accounts; below threshold → keep free API and look elsewhere for upgrades.

**Revision contract:** Owner: VP of Product. Checkpoint: end of quarter. Stop early if two or more qualified enterprise deals cite the restriction. If the result is ambiguous (for example, upgrades near threshold but tiny sample), extend by one month instead of expanding.

**Stakeholder message:** "I recommend restricting API access for new free signups only this quarter. It tests Finance's upgrade projection at low risk. The open risk is enterprise pipeline that starts on free API use, which we haven't measured. If upgrades hit the agreed rate and sales sees no lost deals, we plan an announced change for existing accounts next quarter. If two qualified deals cite the change, we reverse it."

## Why this response works

- It splits one proposal into two components with different doors instead of judging the whole change at once.
- It labels the success threshold as a proposal needing owner agreement.
- It treats two prospect comments as a reason to measure, not as proof either way.
- It gives the strongest rival option a real answer instead of dismissing it.
