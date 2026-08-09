---
name: clean-architecture
description: |
  Clean Architecture practitioner's guide. Trigger when users ask about four-layer architecture, dependency direction & inversion (DIP), an entity directly depending on external SDKs, ORM/data access layer (Repository pattern) design, microservice decomposition, technology selection, over-engineering, or architecture refactoring. Covers business logic organization in Express/Next.js/Go/Spring projects, MongoDB→PostgreSQL migrate, REST→GraphQL migrate, third-party integration (Stripe/PayPal), Redis caching, and Kafka message queue evaluation. Evaluates architecture against Robert C. Martin's Clean Architecture, SOLID principles, and the Dependency Rule; uses Musk's five-step algorithm as an anti-over-engineering gate. Do NOT trigger on: pure code quality, DDD, system design interviews, single-DTO micro-decisions, cache library selection, DI framework debugging, diagram drawing, translation, or formatting requests — answer directly without invoking this skill.
metadata:
  author: Tokenaissance
  version: "1.2.1"
  upstream_inspiration: wondelai/skills:clean-architecture; affaan-m/everything-claude-code; giuseppe-trisciuoglio/developer-kit; pproenca/dot-skills
---

# Clean Architecture

A practical guide to layering, dependency direction, and anti-over-engineering — grounded in Robert C. Martin's Clean Architecture, SOLID, and Musk's five-step algorithm.

## Router Rules

- The frontmatter `description` routes first: only trigger on genuine architecture scenarios — four-layer decomposition, DIP violations, data access layer design, microservice/technology evaluation, over-engineering.
- Once triggered, follow the Workflow below. This skill is an architecture guide, not a general-purpose code review or debugging entrypoint.
- For "pure code quality, DDD, system design interviews, single-DTO micro-decisions, cache library selection, DI framework debugging, diagram drawing, translation/formatting" — answer directly; do NOT invoke this skill.
- Respect the user's stack: explain in four-layer terms first, then map to their actual framework (Express/Next.js/Go/Spring). Never hardcode a single framework.
- Terminology is suggestive: default to Entities / Use Cases / Interface Adapters / Frameworks as the canonical layer names. Service/Repository/Controller are implementation-pattern mappings only — not primary layer names. If the user already has established conventions, adopt those.
- Read-only audit requests do NOT modify any files.

## Use when

- Business logic is piled into controllers/routes — how to refactor into layers (SRP + DIP)
- Entities/Use Cases directly import external SDKs (Stripe/PayPal) or database drivers — is the dependency direction correct?
- Evaluating whether to adopt microservices / Kafka / Redis / caching — technology selection under bounded context constraints
- REST→GraphQL, MongoDB→PostgreSQL migrations — impact on data access code and Repository pattern boundaries
- Integrating multiple third-party services — how to design an Adapter layer (Ports & Adapters pattern) for swappability

## Do NOT use when

- Drawing architecture diagrams, translating, formatting, writing titles, summarizing documents
- Debugging: DI not injecting, HTTP 500, slow SQL queries
- Micro-decisions: splitting a React component, whether to add a single DTO
- System design interview questions (Twitter-scale, bit.ly, Saga, multi-tenancy) — answer directly
- User explicitly says "don't talk about architecture" or "just explain"

## Workflow

1. **Diagnose first — ask before prescribing**: Confirm input scale, team size, concurrency, and change frequency. Code that changes for the same reason at the same time belongs together (CCP); code that changes for different reasons must be separated (SRP). Only invest boundaries on proven variation axes; keep it simple on unproven ones.
2. **Apply principles**: Evaluate architecture against the four-layer concentric model and Dependency Rule (Entities → Use Cases → Interface Adapters → Frameworks; source-code dependencies point inward only), SOLID (SRP/OCP/LSP/ISP/DIP), component principles (CCP/CRP/ADP/SDP/SAP), Musk's five-step algorithm, and engineering dialectics. See Reference Map for specifics.
3. **Structured answer** (deliver when the scenario hits):
   - Four-layer terminology: Entities / Use Cases / Interface Adapters / Frameworks & Drivers
   - Dependency Rule: source-code dependencies point inward only — draw the direction arrows
   - Stack mapping: map the four layers onto the user's actual framework and directory structure
   - Code example: minimal before/after with layer labels, ≤ 50 lines
4. **Anti-over-engineering gate**: Any "adopt the complex solution" advice must first pass Musk's five steps — Question → Delete → Simplify → Accelerate → Automate, order non-negotiable. If a monolith suffices, do not propose microservices.
5. **Documentation isomorphism (as needed)**: Architecture decisions MUST be discoverable by downstream Agents and developers — code changes without documentation updates are incomplete. Documentation granularity matches decision impact: a cross-layer refactor walks the full L3→L2→L1 loop; a single import change updates one L3 line. See Reference Map → Documentation Isomorphism.

## Output Contract

- Hit scenario: diagnosis + four-layer mapping + Dependency Rule explanation + stack mapping + minimal code example + anti-over-engineering verdict. For major architecture decisions, append L2/L3 documentation skeletons.
- Miss scenario: answer directly; do not apply this skill's template.
- Do NOT output a full directory scaffold (> 5 directories or containing specific file names) unless the user explicitly requests it. Default to layer-level directory suggestions (≤ 5 directory names, no specific files).

## Reference Map

- Theory & Principles: `references/clean-architecture.md`
- Anti-Over-Engineering: `references/musk-algorithm.md`
- Engineering Philosophy: `references/engineering-philosophy.md`
- Documentation Isomorphism: `references/geb-fractal-docs.md`
