/**
 * [INPUT]: No external deps. Theoretical foundation referenced by all sibling references and SKILL.md Workflow.
 * [OUTPUT]: Four-layer concentric model, SOLID (SRP/OCP/LSP/ISP/DIP), component cohesion (REP/CCP/CRP) + coupling (ADP/SDP/SAP), Dependency Rule, boundary taxonomy (Humble Object / Facade / Strategy / Services), I/A metrics, decision heuristics.
 * [POS]: references/' core theory — canonical Clean Architecture principle system.
 * [PROTOCOL]: On change, update this header, then verify SKILL.md Reference Map.
 */

# Clean Architecture — Complete Principles (Robert C. Martin)

> **TL;DR**: Decouple policy from detail. Invert deps via polymorphism so all source-code deps point inward toward high-level policy. Frameworks, DBs, UI are plugins. Architecture quality = Δ(labor cost per release). If that derivative is positive, the architecture has failed.

---

## 1. Why Architecture Matters

**Metric**: Architecture quality ≡ human-labor cost of building + maintaining the system. Per-release cost monotonic increase → architectural failure.

**Two value axes**:

| Axis | Definition | Priority |
|------|-----------|----------|
| **Behavior** | System executes spec correctly (function) | Urgent, not important |
| **Architecture** | System tolerates change with minimal labor (structure) | Important, not urgent |

**Eisenhower violation**: Teams optimize behavior at architecture's expense. The architect's sole mandate: invert this priority. Architecture (quadrant II) must gate behavior (quadrant I).

---

## 2. Programming Paradigms as Constraints

Each paradigm removes capability — constrains, not enables:

| Paradigm | Constraint | Architectural Payoff |
|----------|-----------|---------------------|
| **Structured** | Bans `goto` (direct control transfer) | Modular decomposition via proof-by-contradiction testing |
| **OOP** | Bans unconstrained function pointers (indirect control transfer) | **Dependency Inversion** — polymorphism decouples source deps from control flow |
| **Functional** | Bans assignment (mutable state) | Race-condition elimination; Event Sourcing as practical immutability |

**OOP's architectural value = polymorphism → DIP.** Not encapsulation. Not inheritance. Before OOP, dep direction ≡ control flow direction. Polymorphism inverts this: concretions depend on abstractions; control and source deps run opposite directions. This single inversion underpins the entire Dependency Rule.

**Event Sourcing**: Store CRUD command log; derive state via replay. Trade storage + compute for immutability. Functional programming's lesson applied at architectural scale.

---

## 3. SOLID Design Principles

Mid-level module/class principles. Target: change-tolerant, comprehensible, reusable structures.

### SRP — Single Responsibility Principle

**Canonical**: A module is responsible to one, and only one, actor (stakeholder group).

**Anti-pattern**: `Employee{calculatePay() // CFO, reportHours() // COO, save() // CTO}`. CFO-pushed `calculatePay` change silently corrupts COO's `reportHours` output.

**Fix**: Separate data from behavior — three classes sharing `EmployeeData`, each serving one actor. Or Facade delegation.

**Architecture-level instantiation**: CCP + Axis of Change. SRP determines boundary placement.

### OCP — Open-Closed Principle

**Canonical**: Extend behavior without modifying existing source.

This IS the telos of architecture. A small spec delta requiring massive source delta = architecture failure.

**Mechanics**: SRP decomposes responsibilities → DIP orients dep direction → protection layers form. Protection hierarchy: Interactor > Controller > Presenter > View. Higher layers are oblivious to lower layers' existence.

### LSP — Liskov Substitution Principle

**Canonical**: ∀ subtype S of T, objects of type T must be substitutable by objects of type S without breaking correctness.

Applies beyond inheritance — to interfaces, protocols, REST contracts. Taxi dispatch depending on URI endpoints: one fleet's REST contract deviates (different param names) → special-case if-else in dispatcher → architecture-level LSP violation. Any `instanceof` or type-switch guarding an interface contract signals LSP breach.

### ISP — Interface Segregation Principle

**Canonical**: No client forced to depend on methods it doesn't invoke.

**Transitive-dependency corollary**: System S → Framework F → Database D. Irrelevant change in D forces F redeploy → forces S redeploy. Fat interfaces amplify blast radius. ISP slims interfaces to minimize transitive coupling.

### DIP — Dependency Inversion Principle

**Canonical**: Source-code deps reference abstractions, never volatile concretions.

**Stable-concretion exemption**: `String`, `ArrayList` (stdlib concretions) → DIP unnecessary. Apply DIP against **volatile** concrete modules exclusively.

**Four disciplines**:
1. Depend on abstract interfaces; avoid volatile concrete classes
2. Never inherit from concrete classes (inheritance = strongest dep form)
3. Never override concrete method implementations
4. Never name concrete/implementation-specific entities in policy code

**Abstract Factory pattern**: `ServiceFactory` interface produces concrete instances. All boundary-crossing deps are unidirectional: concretion → abstraction. **Control flow ⇄ source dep direction** — hence "inversion."

---

## 4. Component Principles

### Cohesion — What belongs together?

| Principle | Rule | Driver |
|-----------|------|--------|
| **REP** | Granule of reuse ≡ granule of release | Reusability |
| **CCP** | Classes sharing change reason + change cadence → same component | Maintainability (SRP at component scale) |
| **CRP** | Don't bundle what clients don't use together | Release minimization (ISP at component scale) |

**Tension triangle**: REP + CCP → larger components; CRP → smaller. Early-stage: bias CCP (velocity). Mature: bias REP (reusability). These three are mutually adversarial — optimize for current phase.

### Coupling — How do components relate?

**ADP (Acyclic Dependencies Principle)**: Component dep graph MUST be a DAG. **No cycles.**

Cycle-breaking toolkit:
1. DIP — inject interface, invert one dep direction
2. Extract new component — hoist shared classes into a new node

**SDP (Stable Dependencies Principle)**: Dep direction → increasing stability.

- Stability ≢ "unchanging." Stability ≡ "hard to change" = high Fan-in.
- **I = Fan-out / (Fan-in + Fan-out)**. I ∈ [0,1]. I=0: maximally stable (high Fan-in, zero Fan-out). I=1: maximally unstable (zero Fan-in, high Fan-out).
- Unstable → stable: ✓. Stable → unstable: ✗ (SDP violation).

**SAP (Stable Abstractions Principle)**: Stable components must be abstract.

- **A = abstract_classes / total_classes**. A ∈ [0,1]. A=0: fully concrete. A=1: fully abstract.
- **Main Sequence**: ideal components lie on line from (I=0, A=1) to (I=1, A=0).
- **Zone of Pain** (I=0, A=0): stable AND concrete. Database schema. Immutable. Untouchable.
- **Zone of Uselessness** (I=1, A=1): unstable AND abstract. Nothing depends on it. Dead code.

**I/A distance from Main Sequence** measures component health. D = |A + I - 1|. D near 0 = healthy. D near 1 = pain/uselessness.

---

## 5. Core Architecture Concepts

### Architect as Programmer

Architects who don't write code lose signal. The pain of your own design is irreplaceable feedback.

### Defer Decisions

> **A good architect maximizes the number of decisions NOT made.**

System = Policy (business rules) + Details (I/O, DB, framework, protocol). Strategy: center Policy; decouple Details as plugins.

**Defer checklist**: DB engine, web server, REST, DI framework, ORM. Even if the org mandates a technology, architect as if the decision is still open — the plugin boundary preserves optionality.

### Independence

**Conway's Law**: System topology mirrors org communication topology.

**Three decoupling axes**:
1. **Horizontal**: UI / biz logic / DB — layer separation
2. **Vertical**: Use case slicing — SRP at architecture scale
3. **Decoupling mode**: source-level (monolith) → deployment-level (jar/DLL) → service-level (microservices)

**Specious vs. true duplication**: Identical code with different change reasons + rates → NOT duplicates. Do NOT merge. Merging couples independent evolutionary paths.

**Monolith-first**: Decouple within a monolith. Extract services only on proven variation axes. Good architecture allows bidirectional evolution — merge or split without rewrite.

### Policy and Level

**Level**: distance from I/O. Policy closest to I/O = lowest level. Policy furthest from I/O = highest level.

**Rule**: Source deps decouple from data flow → couple to level. Low-level components (plugins) depend on high-level components (policy). This inverts the naive intuition that "callers depend on callees."

---

## 6. The Clean Architecture Model

Unifies Hexagonal Architecture (Ports & Adapters), DCI, BCE.

### Four-Layer Concentric Model (inner → outer)

| Layer | Contents | Stability |
|-------|----------|-----------|
| **Entities** | Enterprise-wide critical business rules + data | Maximum. Rules survive system boundary collapse. |
| **Use Cases** | Application-specific business logic. Orchestrates Entity data flow: Input → Process → Output. Zero UI/Db awareness. | High. Changes when app behavior changes. |
| **Interface Adapters** | Controllers, Presenters, Gateways. Format-conversion between inner/outer layers. MVC belongs here. | Medium. Changes when delivery mechanism changes. |
| **Frameworks & Drivers** | Web framework, DB, UI toolkit. Glue code only. | Minimum. Changes constantly. Least stable. |

### The Dependency Rule

> **∀ dep ∈ source code, dep must point inward. Outer → inner. Always.**

- Inner layer must not reference any name declared in an outer layer
- Outer-layer data formats must not leak inward
- N > 4 layers allowed; rule invariant under layer count

### Boundary Crossing

Control flow → inward (Use Case calls Presenter). Dep direction must point inward (Use Case must NOT know Presenter exists). Conflict resolved via DIP: Use Case depends on inner-layer **Output Port** (interface); Presenter implements it. Polymorphism inverts the dep.

### Data Crossing Boundaries

DTOs, hashmaps, primitive args. **Never** Entity objects, DB row objects, or framework request/response types across boundaries. Use the format most convenient for the inner layer.

### Five Invariants

1. **Framework-independent** — frameworks are plugins, not architecture
2. **Testable** — business logic testable without UI, DB, web server
3. **UI-independent** — replace UI without touching business logic
4. **DB-independent** — swap storage engines via Gateway interface
5. **External-agency-independent** — business logic knows nothing of external interfaces

---

## 7. Boundary Types and Strategy

### Boundary Forms (ascending communication cost)

| Form | Cost | Trigger |
|------|------|---------|
| **In-monolith polymorphism** | Function call | Early project, uncertain change axes |
| **Deployment components** (jar/DLL) | In-process | Independent team dev/deploy |
| **Local processes** | Syscall + context switch | Security/fault isolation |
| **Services** | Network RTT (ms–s) | Physical isolation, independent scaling |

**All boundaries share one invariant**: control source-dep direction so low-level components become plugins.

### Partial Boundaries

Full boundaries have cost. Three compromises:

1. **Skip the last step**: Design interfaces + DTOs; compile as single component. Isolation degrades without compiler enforcement.
2. **One-way boundary (Strategy)**: Interface in one direction only. DIP active; reverse protection absent. Discipline-dependent.
3. **Facade**: Skip DIP entirely. Client has transitive dep on all Services. Simplest; least isolation.

### Humble Object Pattern

At every boundary, bifurcate: hard-to-test behavior (Humble Object) vs. easy-to-test behavior.

- **View**: Humble Object — data injection only. Zero processing.
- **Presenter**: Testable object — formats data to strings/booleans/enums for View consumption.
- **DB Gateway**: Interface = testable contract; implementation = Humble Object executing SQL.
- **ORM → Data Mapper**: Humble Object in the DB layer. Not architecture.

### Main Component

Lowest-level, dirtiest component. Sole responsibility: instantiate all factories + global facilities → hand control to highest abstraction layer.

- Main is the composition root. DI wiring lives here.
- **Main ≡ plugin to the application** — design multiple Mains (dev, test, prod, staging).

---

## 8. Correct Positioning of Implementation Details

### DB Is a Detail

Data models matter; the DBMS does not. DB row objects must never circulate in system internals. DBs exist because slow spinning disks required B-tree optimization — a hardware detail, not architecture. Plugin to the Gateway interface.

### Web Is a Detail

Web = I/O device. One oscillation in the centralize/distribute cycle. Business rules must not embed HTTP semantics. Architect for the long view — UI delivery mechanisms churn; policy persists.

### Frameworks Are Details

Framework adoption = asymmetric commitment. You marry the framework; the framework owes you nothing. Framework authors solve their own problems, not yours.

**Rules**:
- Frameworks remain in outermost layer
- If framework requires base-class inheritance → proxy classes as plugins
- You should be able to unit-test all business logic without the framework

### Screaming Architecture

Source code should scream domain purpose. "This is a healthcare system" — not "this is a Spring/Next.js/Django app." Use cases define structure; frameworks are tools.

### Services Are NOT Architecture

**Two service fallacies**:
1. **Decoupling fallacy**: Shared data across services = still coupled
2. **Independent-deployment fallacy**: Behavioral coupling still requires coordinated deployment

Architecture boundaries **penetrate through** services — they exist as components inside each service. Cross-cutting concerns are the primary enemy of feature-based service decomposition.

### Test Boundary

Tests reside in outermost circle; deps point inward. **Fragile Test Problem**: GUI-verified tests break on any UI change. Solution: dedicated test API — test business logic directly, not through the delivery mechanism. One test class per production class is the wrong granularity; test API should hide application structure.

---

## 9. Code Organization Patterns

Four patterns, ascending capability:

| Pattern | Strategy | Weakness |
|---------|----------|----------|
| **Package by Layer** | Horizontal: Web/Service/Repository | Domain invisible; layers trivially bypassed |
| **Package by Feature** | Vertical slice; domain-visible | Insufficient isolation; all types public |
| **Ports & Adapters** | Domain ⇄ Infrastructure separation | Access-modifier discipline required |
| **Package by Component** | Coarse-grained components; clean interfaces | Closest to service-ready; highest ceremony |

**Compiler-as-enforcer**: All four patterns are syntactically identical if every type is `public`. Use `package-private` / `internal` access modifiers to make architectural boundaries compile-time enforceable. The compiler is the cheapest, fastest architecture linter.

---

## 10. Practical Decision Guide

### Boundary Heuristics

- **Unrelated concerns** → boundary (GUI vs. business logic, DB vs. business logic)
- **Axis of Change**: Each side changes for different reasons, at different rates → boundary
- **YAGNI-Foresight balance**: Invest boundaries on **proven** variation axes (3+ historical changes at the same seam); keep simple on unproven axes
- **Continuous observation**: Boundaries are not one-shot decisions. Watch system evolution; strike at inflection points.

### Boundary Signals

| Signal | Action |
|--------|--------|
| Two modules ALWAYS change for different reasons | Draw boundary |
| Modifying one frequently cascades into the other | Draw boundary |
| Different team subgroups conflict on the same module (SRP violation) | Draw boundary |

### FitNesse Case Study

- Deferred web server: self-built minimal server → framework decision postponed
- `WikiPage` interface between business logic and storage; in-memory implementation first
- **18 months zero-database**: no schema, no queries, no credentials
- MySQL adapter written **in one day** when customer demanded persistence
- **Takeaway**: Good boundaries convert "defer the decision" from aspiration to operational reality.

### Premature-Decision Anti-Patterns

- **Company P**: Day-1 three-layer rich architecture. Adding one field → modify 3 layer-classes × 4 message protocols × 8 handler functions. Never shipped a cluster.
- **Company W**: Enterprise SOA for a small fleet business. Adding a contact → ServiceRegistry → ContactService → ... Complexities never paid back.

### Video Sales Case Study — Full Design Walkthrough

1. **Identify actors** (Viewer, Purchaser, Administrator, Video Author) → SRP decomposition
2. **Separate by use case** → independent use cases per actor
3. **Component architecture** → Views / Presenters / Interactors / Controllers layered, then actor-grouped
4. **Dependency management** → "uses" edges align with control flow; "inherits" edges oppose control flow (OCP instantiation)
5. **Flexible deployment** → merge into 5 jars or 2 jars as needed

**Two-dimensional isolation**: SRP isolates by actor (different change reasons); Dependency Rule isolates by layer (different change rates). Orthogonal.
