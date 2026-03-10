# Clean Architecture Skill for Claude Code

A Claude Code skill that guides architectural design decisions using Robert C. Martin's Clean Architecture principles, SOLID design, and Musk's 5-step engineering algorithm.

## What it does

When you ask architecture questions, this skill ensures Claude:

- **Uses Clean Architecture terminology** — Entities, Use Cases, Interface Adapters, Frameworks & Drivers (not generic "Service Layer" / "Repository Layer")
- **Explains the Dependency Rule** — dependencies point inward, outer layers depend on inner layers
- **Provides concrete code examples** — before/after refactoring with explicit layer labels
- **Pushes back on over-engineering** — applies Musk's Algorithm to question unnecessary complexity
- **Treats infrastructure as detail** — databases, caches, message queues belong in the outermost layer

## Eval Results

Tested across 14 scenarios (3 core + 11 system design):

| Category | Without Skill | With Skill |
|----------|:---:|:---:|
| Core evals (refactoring, DIP, over-engineering) | 83% | 92% |
| System design (Twitter, microservices, caching, etc.) | 50% | **100%** |

The skill's biggest impact is on system design — without it, Claude defaults to infrastructure-first thinking. With it, Claude consistently separates business rules from implementation details.

## Installation

### Option 1: npx skills (recommended)

```bash
npx skills add tokenaissance/clean-architecture-skill
```

To install for a specific agent only:

```bash
npx skills add tokenaissance/clean-architecture-skill -a claude-code
```

### Option 2: Claude Code plugin

```bash
claude plugin add tokenaissance/clean-architecture-skill
```

### Option 3: Manual

```bash
git clone https://github.com/tokenaissance/clean-architecture-skill.git
cp -r clean-architecture-skill/clean-architecture ~/.claude/skills/
```

After installation, restart Claude Code. The skill triggers automatically when you ask about architecture, layering, refactoring, dependency management, or technology selection.

## Example prompts

```
我有一个 Express.js 的后端项目，所有业务逻辑都写在 controller 里。怎么重构？

Order 实体直接 import 了 Stripe SDK 来处理支付，这样设计有什么问题？

5 个人用的内部工具，同事建议用微服务 + Kafka + Redis，你觉得呢？

我们要设计一个类似 Twitter 的社交媒体平台，如何设计架构？

从 MongoDB 迁移到 PostgreSQL，需要重写所有代码吗？
```

## Skill structure

```
clean-architecture/
├── SKILL.md                          # Main skill instructions
├── references/
│   ├── clean-architecture.md         # Clean Architecture principles (Robert C. Martin)
│   ├── musk-algorithm.md             # Musk's 5-step engineering algorithm
│   └── engineering-philosophy.md     # Dialectical engineering philosophy
└── evals/
    ├── evals.json                    # 3 core eval scenarios
    └── system-design-evals.json      # 11 system design eval scenarios
```

## Covered scenarios

| # | Scenario | What it tests |
|---|----------|---------------|
| 1 | Architecture refactoring | Clean Architecture layers, dependency rule, code examples |
| 2 | Dependency direction | DIP violations, interface-based decoupling |
| 3 | Over-engineering detection | Musk's Algorithm, questioning requirements |
| 4 | Twitter-scale system | CA layers in distributed systems |
| 5 | Microservices vs monolith | Modular monolith recommendation |
| 6 | Caching strategy | Cache as infrastructure detail |
| 7 | URL shortener | Core business rules as Entities |
| 8 | Database sharding | Repository abstraction |
| 9 | Distributed transactions | Saga pattern with CA layers |
| 10 | REST to GraphQL | API as Interface Adapter |
| 11 | Multi-tenancy | Tenant-agnostic business logic |
| 12 | Third-party adapters | Ports & Adapters pattern |
| 13 | Database migration | Zero business logic change |
| 14 | Real-time chat | Transport as infrastructure detail |

## References

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- SOLID Principles
- Elon Musk's 5-Step Engineering Algorithm

## License

MIT
