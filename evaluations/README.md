# Behavioral evaluations

These are synthetic fixtures, not customer data or measured model results. Run them with the target agent before relying on these skills. Structural validation alone does not establish judgment quality.

## Run protocol

1. Use a fresh conversation for each case in `cases.json`. Provide only the indicated skill's `SKILL.md` and the exact `prompt`; leave out `references/`, so results reflect the instructions alone. Do not provide the expected criteria to the agent. No external actions or browsing are needed for these fixtures.
2. Save the complete response, agent/model version, date, skill revision, and any tool use in a local `.evaluation-runs/` directory. Keep private data out of public results.
3. Review against `must_include` and `critical_failures`. Grade each required criterion 0 (absent/wrong), 1 (partial), or 2 (explicit and usable). A case passes only with every criterion at 2 and no critical failure. Record quotations supporting each grade. Equivalent reasoning and output formats are acceptable.
4. Repeat failures after a targeted revision with a fresh conversation. Re-run cases for the changed skill and any affected routing boundary. Compare results without silently replacing the original run.

## Routing checks

Ask the agent to choose a skill using only names and descriptions:

| Prompt | Expected primary skill |
| --- | --- |
| Why did activation fall? | diagnose-product-performance |
| Evidence is mixed; should we commit now? | conviction-under-uncertainty |
| How will sellers adapt to this incentive? | second-order-thinking |
| Is this worth two engineers versus another project? | evaluate-product-investment |
| Growth and trust goals conflict; who should give what up? | resolve-competing-objectives |
| Write a basic product requirements document. | None required |
| Summarize these interview notes. | None required unless judgment is requested |

Multiple skills may apply. Choose the one matching the decision being requested; use another only when it resolves a concrete remaining question. Do not produce five reports automatically.

## Result record

```text
Case / date / model / skill revision:
Required criterion: grade; supporting response excerpt; reviewer note
Critical failure: absent/present; evidence
Outcome: pass/fail
Correction and retest reference:
```

## Validation status

The repository includes structural checks, run on every push by GitHub Actions, and hand-checked arithmetic in the eval cases and worked examples. No model-executed behavioral pass rate is claimed. The cases are a starting regression suite, not a benchmark of real-world product outcomes.
