/**
 * [INPUT]: Depends on references/clean-architecture.md's SOLID principles and Dependency Rule as dialectical subjects
 * [OUTPUT]: Six dialectical theses (unity of opposites / quantitative-to-qualitative change / negation of negation / base determines superstructure / practice as truth criterion / primary vs. secondary contradictions) applied to software engineering
 * [POS]: references/' philosophical-dialectical layer — provides a dialectical thinking framework for architecture decisions. Serves as a meta-level complement to the concrete principles in clean-architecture.md
 * [PROTOCOL]: On change, update this header, then verify SKILL.md Reference Map description remains accurate
 */

# Engineering Dialectics — Materialist Dialectics in Software Engineering

> Core insight: A software system is a unity of contradictions in motion. Architecture decisions are not about eliminating contradictions — they are about finding the optimal equilibrium point between opposing forces for the current stage.

---

## Table of Contents

1. [Unity of Opposites: Navigating Core Contradictions](#1-unity-of-opposites-navigating-core-contradictions)
2. [Quantitative to Qualitative Change: Technical Debt and Refactoring Dialectics](#2-quantitative-to-qualitative-change-technical-debt-and-refactoring-dialectics)
3. [Negation of Negation: Architecture Evolution as Spiral Ascent](#3-negation-of-negation-architecture-evolution-as-spiral-ascent)
4. [Base Determines Superstructure: Dependency Structure Governs Everything](#4-base-determines-superstructure-dependency-structure-governs-everything)
5. [Practice Is the Sole Criterion of Truth](#5-practice-is-the-sole-criterion-of-truth)
6. [Primary vs. Secondary Contradictions: Seizing the Key Problem](#6-primary-vs-secondary-contradictions-seizing-the-key-problem)

---

## 1. Unity of Opposites: Navigating Core Contradictions

The core contradictions in software engineering are not "problems" to eliminate — they are forces to harness. Taking either pole to its extreme is disaster.

### Flexibility vs. Simplicity

- Over-flexibility ("what if we need it later?") → complexity explosion: every operation traverses five abstraction layers
- Over-simplicity (hardcoding, quick patches) → system rigidity: one change requires a total rewrite
- **Navigation strategy**: Invest flexibility on proven variation axes (establish boundaries via DIP); keep it simple on unproven axes (YAGNI). A variation axis is "proven" by history — when the same location has been modified three or more times.

### Policy vs. Detail

- Business rules are the system's essence ("the money-making logic"); technical implementation is phenomena ("which framework")
- Consequence of conflating the two: business logic enslaved by database schemas, contaminated by HTTP protocols, invaded by framework annotations
- **Navigation strategy**: Dependency direction always points from detail to policy, never the reverse (Dependency Rule). Isolate with interfaces (Ports & Adapters); make detail a plugin to policy.

### Cohesion vs. Coupling

- Putting unrelated code together (low cohesion) → one change impacts the entire module
- Scattering related code apart (high coupling) → one feature change touches ten files
- **Navigation strategy**: Group by reason for change — code that changes for the same reason at the same time belongs together (CCP); code that changes for different reasons MUST be separated (SRP).

### Present Needs vs. Future Extensibility

- Over-engineering (building architecture for three years of hypothetical requirements) wastes current labor and complexity budget
- Under-engineering (satisfying only today's requirements) incurs exponential technical debt tomorrow
- **Navigation strategy**: Invest boundaries on proven variation axes; keep it simple on unproven axes. Be ready to strike at the inflection point (OCP: open for extension, closed for modification).

### Individual vs. Whole

- Local optimum for each component ≠ global system optimum
- A module "for its own convenience" reverses its dependency on high-level policy, destroying the entire system's dependency structure
- **Navigation strategy**: Global dependency direction takes precedence over local convenience. No local optimization may violate the Dependency Rule.

---

## 2. Quantitative to Qualitative Change: Technical Debt and Refactoring Dialectics

### Forward Quantitative Change: The Critical Point of Debt Accumulation

The harm of technical debt is non-linear. 100 small architecture compromises do not produce 100 small problems — at a critical threshold they suddenly cause:

- New feature development time going from days to weeks
- Every modification introducing new bugs
- Team morale collapse, best engineers leaving
- The entire system entering a "rewrite-only" state

Signals of the approaching critical point:
- New-member ramp-up time significantly increasing
- "Fear-to-modify" code regions expanding
- Test coverage unable to improve (because code is untestable)
- Build and deployment times continuously growing

### Reverse Quantitative Change: The Accumulation Effect of Refactoring

Continuous small improvements (refactoring) also produce a qualitative leap at a certain moment:

- The system suddenly becomes "easy to understand" — new people ramp up fast
- Modifications become "safe" — impact radius is predictable
- Adding new features becomes "natural" — the architecture guides you toward correctness

The dialectic of refactoring: not "spend a month refactoring," but "leave the code cleaner than you found it on every change" (Boy Scout Rule). Quantitative-to-qualitative change requires discipline and patience.

---

## 3. Negation of Negation: Architecture Evolution as Spiral Ascent

Software architecture is not achieved in one step — it ascends in a spiral:

1. **Thesis**: Rapid prototype (simple but fragile)
2. **Antithesis**: Over-engineering (flexible but complex)
3. **Synthesis**: Just-right architecture (flexible where needed, simple elsewhere)

Each "negation" does not wholly destroy the prior stage — it practices **Aufhebung** (sublation): preserving the rational, negating the irrational:

- From monolith to microservices is not negating "code together" — it is negating "MUST deploy together"
- From ORM to hand-written SQL is not negating "data mapping" — it is negating "the framework thinks for you"
- From inheritance to composition is not negating "code reuse" — it is negating "reuse through inheritance hierarchies"

### Negation of Negation in Historical Process

- Centralized → Client/Server → Web (centralized returns) → Microservices (distributed returns) → Service Mesh (centralized control returns)
- Each "return" is not simple repetition — it is a return at a higher level

---

## 4. Base Determines Superstructure: Dependency Structure Governs Everything

Code's "economic base" is its **dependency structure and data flow**. Every visible "superstructure" — naming, comments, file organization, documentation — is built atop this base.

### Base Determines Superstructure

- If the dependency direction is wrong, the most beautiful naming cannot save you
- If the data flow is chaotic, the most detailed documentation cannot describe it clearly
- If component boundaries are drawn wrong, the best file organization is just "neatly sorted garbage"

### Superstructure Reacts Upon Base

- Clear naming helps discover dependency direction errors
- Good file organization exposes unreasonable coupling
- Attention to superstructure in code review can drive base improvement

### Reform or Revolution

- **Reform** (refactoring): improve internal structure without changing external behavior. Applicable when the base is broadly correct and needs localized adjustment
- **Revolution** (rewrite): overthrow the existing structure and rebuild. Consider only when the base is completely rotted and reform cost far exceeds rewrite cost
- In most cases reform > revolution — rewrites rarely succeed because people underestimate the tacit knowledge accumulated in the existing system

---

## 5. Practice Is the Sole Criterion of Truth

Architecture decisions cannot be validated on whiteboards alone. Verification comes only through:

### Testing

- Business logic MUST be testable independent of the framework (Humane Object pattern)
- If writing tests is hard, the architecture is wrong — not the test's problem, but the code-under-test's problem
- The Humble Object pattern: reduce hard-to-test parts to their simplest possible form; concentrate logic in testable objects

### Deployment

- Can you deploy with one command?
- Changing one component requires redeploying how many components?
- Can failed deployments roll back quickly?

### Real Feedback

- How do users actually use the system? Does their usage match architectural assumptions?
- Which features are frequently modified? Do those modifications complete within a single component?
- Where are the system's actual bottlenecks? Do they match architectural predictions?

**An architecture decision not validated by practice is fantasy.**

---

## 6. Primary vs. Secondary Contradictions: Seizing the Key Problem

At any stage, the system has a **primary contradiction** — resolving it yields the greatest improvement. Spending energy on secondary contradictions is waste.

### How to Identify the Primary Contradiction

- Which component has the highest modification frequency and largest blast radius?
- Which dependency relationship causes the most problems?
- Which technical decision limits the most possibilities?
- What is the team's most painful workflow?

### Transformation of Contradictions

Once the primary contradiction is resolved, the former secondary contradiction may ascend to primary. Architecture evolution is a continuous process:

1. Identify the current primary contradiction
2. Concentrate forces to resolve it
3. Observe the new contradiction landscape
4. Repeat

This is why a "once-and-for-all perfect architecture" does not exist — contradictions continuously transform, and architecture must continuously evolve.

---

## Application Method

When facing a concrete engineering decision:

1. **Find the contradiction**: Which opposing poles does this decision involve? (Flexibility vs. simplicity? Present vs. future?)
2. **Judge primary vs. secondary**: At the current stage, which pole is primary? What is the system currently lacking?
3. **Find the equilibrium point**: Do not go to extremes. Find the optimal position between the two directions for the current stage.
4. **Validate through practice**: After deciding, verify through testing and deployment.
5. **Prepare to adjust**: When conditions change, the equilibrium point must move with them.
