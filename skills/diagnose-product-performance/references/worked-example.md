# Worked example: diagnose-product-performance

Synthetic scenario, written to show depth and register. It is not an evaluation fixture, and all figures are supplied inputs rather than real data.

## Request

> Trial-to-paid conversion jumped from 12% to 15% in the four weeks after we redesigned the pricing page. Over the past year it ranged 11–13%. Before: 5,000 trials, 600 paid. After: 5,200 trials, 780 paid. Split by path: self-serve 4,000 → 400 before, 3,900 → 390 after; sales-assisted 1,000 → 200 before, 1,300 → 390 after. The after window included quarter end. Can we credit the redesign and roll the pattern out to other pages?

## Response

**Symptom:** Trial-to-paid conversion, four-week windows: 600/5,000 (12.0%) before, 780/5,200 (15.0%) after, +3.0 points. That is outside the stated 11–13% range for the past year, so it is worth explaining rather than only monitoring.

**Integrity:** Not yet checked. Before relying on the sales-assisted numbers, confirm that CRM attribution of "paid" did not change at quarter end (for example, deals backdated or reclassified). Self-serve figures come from billing and are less exposed to this.

**Contribution:**

| Segment | Before | After | Rate change |
| --- | --- | --- | --- |
| Self-serve | 400/4,000 = 10% | 390/3,900 = 10% | none |
| Sales-assisted | 200/1,000 = 20% | 390/1,300 = 30% | +10 pts |

Holding before-period rates at after-period weights gives 12.5%, so about 0.5 points comes from more trials being sales-assisted (20% → 25% of trials) and about 2.5 points from the sales-assisted rate rising.

**Evidence ledger:**

| Claim | Source / window | Status | Limitation |
| --- | --- | --- | --- |
| Self-serve rate unchanged at 10% | Supplied counts, both windows | Observed | Four weeks each |
| Sales-assisted rate rose 20% → 30% | Supplied counts | Observed | CRM attribution not verified |
| Quarter end fell in after window | Supplied | Observed | Discounts or deal timing not supplied |
| Redesign caused the rise | None | Assumed | Contradicted by flat self-serve rate |

**Hypotheses:**

| Mechanism | Prediction | Support | Counterevidence | Discriminating check |
| --- | --- | --- | --- | --- |
| Pricing page redesign | Self-serve rate rises most, since those users see the page and buy unassisted | Timing | Self-serve flat | Self-serve conversion among visitors who viewed the new page |
| Quarter-end deal push or discounting | Sales-assisted rate spikes, concentrated in the last weeks, then falls back | Timing; the whole within-segment change is sales-assisted | None yet | Weekly sales-assisted conversion and discount rate across the window |
| CRM attribution change | Paid count rises without matching billing records | None yet | None yet | Reconcile sales-assisted "paid" against billing |

**Judgment:** Leading explanation is quarter-end sales activity, not the redesign. The redesign may have done nothing measurable, and the data supplied does not support crediting it. Unresolved: whether CRM numbers match billing.

**Action:** Don't roll the pattern out on this evidence. Owner: growth analyst. This week: reconcile sales-assisted conversions against billing and plot weekly sales-assisted conversion with discount rates. Recheck the overall rate four weeks after quarter end. The conclusion changes if self-serve conversion among new-page viewers rises, or if the sales-assisted rate stays near 30% after quarter end without heavier discounting.

## Why this response works

- It diagnoses an improvement with the same rigor as a decline, instead of accepting good news.
- It checks the movement against the historical range before building a causal story.
- It shows the mix and within-segment split with arithmetic that can be checked.
- The flat self-serve rate counts as evidence against the obvious explanation.
