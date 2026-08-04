# clean-architecture

> A practical guide to layering, dependency direction, and anti-over-engineering: answer architecture, refactoring, technology-selection, and over-engineering questions with a four-layer model.

[![GitHub Release](https://img.shields.io/github/v/release/tokenaissance/clean-architecture-skill?display_name=tag&sort=semver)](https://github.com/tokenaissance/clean-architecture-skill/releases)
[![Stars](https://img.shields.io/github/stars/tokenaissance/clean-architecture-skill?style=flat)](https://github.com/tokenaissance/clean-architecture-skill/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/tokenaissance/clean-architecture-skill)](https://github.com/tokenaissance/clean-architecture-skill/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![English](https://img.shields.io/badge/Docs-English-black)](README.md)
[![中文](https://img.shields.io/badge/Docs-%E4%B8%AD%E6%96%87-red)](docs/README.zh-CN.md)

`clean-architecture` is not a "generate a directory scaffold" skill. It is a **decision method**: diagnose first, then layer, then use Musk's five-step algorithm to stop over-engineering.

When business logic piles up in controllers, entities depend directly on external SDKs, or a team is debating whether to adopt microservices, this skill gives you: a clear four-layer explanation, a dependency-rule verdict, a mapping to your real stack (Express/Next.js/Go/Spring), and a minimal layer-labeled code example.

```text
Use the clean-architecture skill to review this layered-code proposal,
explain the dependency direction, and tell me whether microservices are over-engineering.
```

It handles: **layering refactoring → dependency inversion (DIP) → data access layer (repository) → technology selection & migration → anti-over-engineering checks**.

**v1.1.0 local candidate verified:** 5/5 unit tests, 20/20 trigger-boundary cases (8 should / 8 should-not / 4 near-neighbor), 4 rubric output scenarios all passing, 0 package-structure issues. Publishing evidence follows the [Releases](https://github.com/tokenaissance/clean-architecture-skill/releases) page.

## Why worth using

- **Precise trigger boundary**: the description is narrowed and carries real technology terms (microservices / Kafka / Redis / caching / MongoDB→PostgreSQL / REST→GraphQL / Stripe / PayPal), passing trigger eval 20/20 with zero false positives and zero missed triggers.
- **Stack-agnostic**: no more hardcoded Express/Sequelize/Stripe templates; the four-layer terms are mapped onto the user's actual framework.
- **Built-in anti-over-engineering gate**: any "adopt the complex solution" advice first runs Musk's five steps (question → delete → simplify → accelerate → automate).
- **Lightweight output**: production-grade context budget (SKILL.md 4.5KB, far below the 14KB ceiling); judgment plus a minimal example, never a long template dump.

## Natural-language examples

- "Business logic is all in the controller and database calls go directly through it. How do I refactor it into layers?"
- "The `Order` entity imports the Stripe SDK directly to process payments. What is wrong with this design?"
- "Five people use an internal CRUD tool; a colleague suggests microservices + Kafka + Redis. Is that necessary?"
- "We are migrating from REST to GraphQL — does all the data-access code really need to be rewritten?"
- "We integrate multiple third parties (Stripe/PayPal). How should I design an adapter layer for easy switching?"

## When NOT to use

- Drawing architecture diagrams, translating, formatting, writing titles, summarizing documents
- Debugging like dependency injection not working, interface 500s, slow SQL queries
- Micro decisions like splitting a React component or whether to add a single DTO
- System-design interview questions (Twitter for millions of users, bit.ly, Saga, etc.)

## Installation

```bash
npx skills add tokenaissance/clean-architecture-skill
```

Install only this skill:

```bash
npx skills add tokenaissance/clean-architecture-skill --skill clean-architecture
```

Verify:

```bash
test -f ~/.agents/skills/clean-architecture/SKILL.md
python3 ~/.agents/skills/clean-architecture/scripts/validate_skill.py \
  ~/.agents/skills/clean-architecture
```

## Prerequisites

- [ ] Node.js 18+: `node --version`
- [ ] npx available: `npx --version`
- [ ] Python 3.11+ (PyYAML): `python3 --version && python3 -c "import yaml"`
- [ ] GitHub CLI authenticated (for publishing): `gh auth status`

## Output

Installing yields a complete Skill package:

```text
clean-architecture/
├── SKILL.md                    # routing + trigger boundary + workflow + Reference Map
├── README.md                   # this product page
├── LICENSE                     # MIT
├── manifest.json               # version, author, platforms, and release gates
├── agents/interface.yaml       # cross-agent interface
├── references/                 # clean-architecture / musk-algorithm / engineering-philosophy
├── scripts/output_eval.py      # rubric output eval
├── evals/                      # trigger_cases.json + output-eval.json
└── reports/                    # Skill IR, trigger-eval, output-eval, prior-art, handoff, upgrade-summary
```

## Local quality checks

```bash
python3 scripts/validate_skill.py .
python3 scripts/export_skill_ir.py . --output reports/skill-ir.json
python3 scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py . --output reports/output-eval.json
python3 -m unittest discover -s tests -p 'test_*.py'
```

> Note: `validate_skill.py` requires PyYAML. This repository's scripts were verified under `conda run -n google python` (Python 3.13 + PyYAML).

## Troubleshooting

| Problem | Common cause | Fix |
|---|---|---|
| Skill never triggers | Description lacks real technology terms | Add the user's actual phrasings to the description and rerun `trigger_eval.py` |
| Skill misfires everywhere | Description too broad or missing near-neighbor cases | Narrow the description; review the should-not/near-neighbor cases in `evals/trigger_cases.json` |
| Output becomes a long template | Treating this skill as a directory generator | This skill outputs only diagnosis + mapping + minimal example; a full scaffold requires an explicit user request |
| Validation script fails | Missing evidence files or a Python interpreter without PyYAML | Fill in the missing `reports/` evidence; rerun with a 3.11+ interpreter |
| Users cannot install | Only local validation, no public release | Run the full publisher (feature branch → PR → Release → clean install) |

## Credits and sources

- [`wondelai/skills`](https://github.com/wondelai/skills): clean-architecture's scoring-driven diagnostic structure inspiration.
- [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code): android-clean-architecture (6.8K installs on skills.sh) as a candidate reference.
- [`giuseppe-trisciuoglio/developer-kit`](https://github.com/giuseppe-trisciuoglio/developer-kit): clean-architecture candidate reference.
- [`pproenca/dot-skills`](https://github.com/pproenca/dot-skills): clean-architecture candidate reference.
- **Robert C. Martin (Uncle Bob) *Clean Architecture***: the original source of the four-layer concentric circles, dependency rule, and SOLID; this skill's references/ is rewritten from his method.

Upstream ideas are adopted semantically with attribution, not mirrored wholesale; search popularity is never passed off as quality. See `reports/prior-art-research.md`.

Upstream inspiration: wondelai/skills:clean-architecture; affaan-m/everything-claude-code; giuseppe-trisciuoglio/developer-kit; pproenca/dot-skills

## Security and evidence boundary

- This skill performs no network operations; `references/` and `scripts/` are local read-only assets.
- Before release, public files are checked for secrets, cookies, private paths, and unverified result claims.
- Trigger/output eval is behavior-specification evidence; provider runs and human review are honestly marked `missing evidence`, never disguised.

## License

MIT (see LICENSE for copyright holders).
