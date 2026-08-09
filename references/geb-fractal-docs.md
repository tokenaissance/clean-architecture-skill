/**
 * [INPUT]: Depends on references/clean-architecture.md's four-layer model as the mapping target
 * [OUTPUT]: Code-document isomorphism ontology, three-layer fractal templates (L1/L2/L3), Clean Architecture mapping table, application-timing decision matrix
 * [POS]: references/' documentation-discipline layer — extends architecture decisions from code-only (machine-phase) to code-document dual-phase. Theoretical foundation for SKILL.md Workflow step 5
 * [PROTOCOL]: On change, update this header, then verify SKILL.md Workflow step 5 and Reference Map descriptions remain accurate
 */

# GEB Fractal Documentation System — Code-Document Isomorphism Discipline

> Core concept originates from @chunxiang's GEB fractal documentation protocol: code is the machine-phase of an entity (for computer execution); documentation is the semantic-phase (for Agent and human understanding). The two phases must be isomorphic — any change in one phase MUST manifest in the other, or the task is incomplete.

---

## Table of Contents

1. [Ontology: Dual-Phase Isomorphism](#1-ontology-dual-phase-isomorphism)
2. [Three-Layer Fractal Templates](#2-three-layer-fractal-templates)
3. [Clean Architecture Mapping](#3-clean-architecture-mapping)
4. [Application Timing](#4-application-timing)

---

## 1. Ontology: Dual-Phase Isomorphism

Traditional documentation is an afterthought — write code first, document later, documentation perpetually stale. GEB inverts this assumption:

- **Code is the machine-phase** of an entity, for computer execution
- **Documentation is the semantic-phase**, for Agents and humans to understand
- **The two phases must be isomorphic**: any change in one phase must synchronously manifest in the other

This is not a "write better docs" exhortation — it is an **architecture discipline**. A wrong dependency direction cannot be rescued by beautiful documentation; undocumented code cannot have its correctness verified by downstream consumers.

Minimum discipline: **before every commit, check whether the L3 headers of touched files and the L2 of their parent module remain accurate.** This micro-habit, compounded over three months, keeps your system comprehensible to any Agent or new team member within 5 minutes.

---

## 2. Three-Layer Fractal Templates

The fractal core is **self-similarity** — each layer is a fold of the layer above.

| Layer | Location | Responsibility | Trigger for Update |
|-------|----------|----------------|-------------------|
| L1 | `/CLAUDE.md` | Project constitution · tech stack · module map | Architecture change / top-level module add/remove |
| L2 | `/{module}/CLAUDE.md` | Member inventory · exposed interface · parent link | File add/remove / interface change |
| L3 | File header comment | INPUT/OUTPUT/POS contract | Dependency change / responsibility change |

### L1 — Project Constitution (≤ 50 lines)

Minimal navigation. Tech stack, top-level directory structure, key configuration. Readable in 30 seconds.

### L2 — Module Map

One line per file. State what each file does and why it exists. The parent link maintains fractal connectivity.

### L3 — File Header Contract

```
/**
 * [INPUT]: depends on {module/file}'s {specific capability}
 * [OUTPUT]: exposes {exported functions/components/types/constants}
 * [POS]: {role} within {module}, {relationship to sibling files}
 * [PROTOCOL]: On change, update this header, then check CLAUDE.md
 */
```

Writing L2/L3 is not listing variable names — it answers: **what it is, why it exists, who it collaborates with, and why the dependency direction was chosen.** If you cannot write a sentence that would cause information loss when deleted, don't write it.

---

## 3. Clean Architecture Mapping

GEB is Clean Architecture projected onto the **semantic layer**. The three-layer fractal maps directly onto the four-layer architecture.

### L1 → Architecture Boundary Declaration

L1 records not "what libraries we use" but **architecture boundaries and dependency direction**: which directories correspond to which of the four layers? What is the dependency direction? What mechanism crosses boundaries (interface + DI? Ports & Adapters?)?

### L2 → Layer Interface Definition

Each module's L2 defines what interface that layer exposes: what types does the Entities layer export? What input/output ports do Use Cases expose? What Repository implementations and Controllers do Interface Adapters provide?

### L3 → Earliest DIP-Violation Detection Point

**The L3 INPUT field catches architecture violations faster than tests and earlier than code review**:

| Pattern in L3 INPUT | Problem | Rule Violated |
|---|---|---|
| HTTP request object in Use Case | Use Case depends on transport layer | Inner depends on outer (Dependency Rule) |
| ORM/database driver in Entity | Entity depends on data access layer | Inner depends on outer |
| Third-party service SDK in Entity | Entity directly depends on external service | Inner depends on outer |
| Concrete class instead of interface in Adapter OUTPUT | Adapter exposes implementation detail | DIP violation |

> The table above is pattern-level. Framework equivalents: Node's `express.Request` = Go's `*http.Request` = Spring's `HttpServletRequest`. Any framework's HTTP request object appearing in a Use Case layer is the same DIP violation.

### Cold Start: Seeder Protocol

When entering a new project or module:

1. **Recon**: Check if L1/L2 exist. Scan directory structure, identify module boundaries.
2. **Seed**: L1 missing → analyze `package.json`/`go.mod`, sow L1. L2 missing → enumerate files, infer responsibilities, sow L2. L3 missing → analyze import/export, infer position, sow L3 headers.
3. **Root**: Once documentation is in place, every subsequent code change triggers the loop check automatically.

---

## 4. Application Timing

Not every scenario demands the full three-layer documentation suite. Match documentation granularity to decision impact:

| Scenario | Minimum Documentation |
|----------|----------------------|
| New project / module | L1 + L2 + L3 on all files |
| New file | L3 on the file + append one line to parent module L2 |
| Dependency direction change (import changed) | L3 INPUT update |
| Cross-layer refactor | L3 → L2 → L1 full-loop check |
| Quick Q&A ("which layer does this go in?") | No documentation change needed |

**Principle**: documentation granularity matches decision impact radius. A single import adjustment changes one L3 line. An architecture restructure walks the full loop. Do not over-document for the sake of "completeness" — that behavior is itself a Musk Step-2 violation.
