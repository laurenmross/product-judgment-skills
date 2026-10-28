# Product Judgment

**Five skills for making better product decisions when the answer isn't obvious.**

Agent skills for product decisions where evidence, consequences, and objectives don't line up neatly. The flagship, **conviction-under-uncertainty**, covers forming a belief and communicating a commitment, with one-way and two-way doors setting how much evidence is needed. Good product judgment isn't about eliminating uncertainty; it's knowing how to act responsibly despite it.

These skills produce decisions you can inspect and challenge, not summaries of generic PM frameworks. They don't prescribe RICE scores, SWOT grids, persona exercises, or a standard roadmap process. Each skill is self-contained and works when copied by itself, and each includes an annotated worked example in `references/`.

| Skill | Decision it improves | Distinct output |
| --- | --- | --- |
| [diagnose-product-performance](skills/diagnose-product-performance/SKILL.md) | What explains the change? | Causal hypotheses and discriminating checks |
| [conviction-under-uncertainty](skills/conviction-under-uncertainty/SKILL.md) | What should we commit to with incomplete evidence? | Door assessment, thesis, commitment and revision contract |
| [second-order-thinking](skills/second-order-thinking/SKILL.md) | How will the system respond? | Response chains, loops and observable guardrails |
| [evaluate-product-investment](skills/evaluate-product-investment/SKILL.md) | Is this the best next use of resources? | Incremental economics, sensitivity and staged funding |
| [resolve-competing-objectives](skills/resolve-competing-objectives/SKILL.md) | Which legitimate objective takes priority here? | Explicit tradeoff and accountable settlement |

## How they fit together

| Skill | Prevents |
| --- | --- |
| diagnose-product-performance | Jumping from a symptom to a solution |
| second-order-thinking | Optimizing locally at the expense of the wider system |
| resolve-competing-objectives | Treating conflicting priorities as if all can be maximized |
| conviction-under-uncertainty | Both analysis paralysis and unjustified certainty |
| evaluate-product-investment | Sunk-cost thinking and confusing activity with value |

They share one set of principles, repeated in each skill's safeguards so every skill stands alone: evidence over assertion, explicit assumptions, real alternatives, reversibility, opportunity cost, and intellectual honesty. They are independently usable, not a mandatory sequence; each names its adjacent skills for hand-offs.

## Install

The portable unit is `skills/<skill-name>/SKILL.md`: a folder with a matching lowercase hyphenated `name`, a triggering `description` in YAML frontmatter, and Markdown instructions. No runtime, network service, credentials, or sibling skill is required to use a skill. Automatic discovery and reload behavior depend on the host agent.

### Claude Code plugin

The repository is also a Claude Code plugin marketplace. In Claude Code:

```text
/plugin marketplace add laurenmross/product-judgment-skills
/plugin install product-judgment@product-judgment
```

### Copying skill folders

Download or clone [laurenmross/product-judgment-skills](https://github.com/laurenmross/product-judgment-skills), then run the following **from the repository root**. Copy the five folders, not the enclosing `skills` folder. Inspect any existing destination with the same name first; the command copies over matching files.

### Codex-style user skill directory

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

For agents configured to discover `.agents/skills`, copy into that directory at the project or user scope supported by your host. Project example:

```sh
mkdir -p /path/to/project/.agents/skills
cp -R skills/* /path/to/project/.agents/skills/
```

For Claude Code-style project discovery:

```sh
mkdir -p /path/to/project/.claude/skills
cp -R skills/* /path/to/project/.claude/skills/
```

The two project paths above are placeholders: replace `/path/to/project` with your project's actual path. If your agent uses a different skill root, copy the same folders there according to its documentation. The package intentionally avoids host-specific tool allowlists or dependencies. Directory examples describe installation layouts, not a guarantee that every agent implements skill discovery. Reopen/reload your agent as needed and check that the five names are discoverable. To uninstall, remove only the five folders you copied, preserving unrelated skills.

If your host does not discover skills, open the desired `SKILL.md` and provide its contents as task instructions. This fallback does not provide automatic routing.

## Use

In hosts that support dollar-name invocation:

```text
$conviction-under-uncertainty Should we migrate all customers next week?
Here are the evidence, rollback constraints, owner and deadline: ...
```

Or request the task naturally, such as “Diagnose this conversion decline” or “Evaluate whether this initiative deserves the next quarter of investment.” Supply available evidence, time window, options, constraints, and decision owner. Missing information is handled explicitly; the skills must not invent data to complete a template.

Choose the primary skill by the question being answered. A performance diagnosis may reveal an investment choice, but that does not require running every skill. Templates are working formats, not required verbosity. All skills preserve evidence limits and user authorization; recommendations do not authorize changes to live systems.

## Evaluate and validate

Python 3.9+ is needed only for the repository checker, with no third-party packages:

```sh
python3 scripts/validate.py
```

The checker verifies the five expected folders, the supported frontmatter subset, folder/name agreement, required practical sections, local Markdown links, evaluation coverage and fixture structure. It is intentionally a repository checker, not a full YAML or Agent Skills specification conformance engine. See [behavioral evaluations](evaluations/README.md) for 13 synthetic cases, scoring criteria, routing checks, and a reproducible run protocol. No behavioral pass rate is claimed.

## Contribute

Propose changes with a concrete failing decision case, the smallest useful instruction change, and evaluation evidence. Preserve each skill's boundary. Avoid adding generic PM theory, unsupported numerical thresholds, or requirements that depend on unavailable tools. Use synthetic or redacted examples only. Run the structural checker and relevant behavioral cases before submitting a change.

## License

[MIT](LICENSE).
