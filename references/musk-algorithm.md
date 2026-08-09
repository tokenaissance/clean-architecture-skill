/**
 * [INPUT]: No external dependencies. Originates from Elon Musk's engineering methodology during the Model 3 production ramp
 * [OUTPUT]: The five-step algorithm (Question → Delete → Simplify → Accelerate → Automate) and its concrete application in software engineering
 * [POS]: references/' anti-over-engineering constraint. Theoretical foundation for SKILL.md Workflow step 4
 * [PROTOCOL]: On change, update this header, then verify SKILL.md Workflow step 4 remains accurate
 */

# Musk's Five-Step Algorithm

Source: Elon Musk's engineering methodology forged during the Model 3 production hell.

Core insight: "The most common error of a smart engineer is to optimize a thing that should not exist."

School trains us to "answer questions" (convergent thinking) but rarely to "question the questions." The five steps are **order-non-negotiable**.

---

## Step 1: Make Requirements Less Dumb

All requirements are wrong to some degree.

- Question every requirement — regardless of who proposed it: top expert, boss, even Musk himself
- Requirements from smart people are MORE dangerous because you instinctively hesitate to challenge them
- Your first job upon receiving a requirement is not to execute — it is to refine it

**In software engineering:**
- When you receive a feature request, first ask "why do you need this feature?"
- User says "add a button" — the real requirement might be "let me complete task X faster"
- Question technical requirements: "Do we really need microservices?" "What problem does this abstraction layer solve?"
- Question non-functional requirements: "Is 99.99% availability truly necessary? At what cost?"
- Apply SRP: does this requirement pull the module in a new change-direction, or align with existing responsibilities?

## Step 2: Delete the Part or Process

We are wired to "add" things just in case — this is a massive trap.

- Do not retain redundancy "just in case"
- **The 10% rule**: if you don't end up having to add back 10% of what you deleted because you cut too deep, you didn't cut enough
- Delete boldly. If you haven't deleted something wrong, you're not deleting enough

**In software engineering:**
- Delete uncalled code — don't comment it out (version control remembers)
- Delete "just in case" abstraction layers — if there's only one implementation, the interface is dead weight (YAGNI)
- Delete tests that test nothing: language-feature tests, mock-only tests
- Delete unnecessary dependency packages — every dependency is an attack surface and maintenance cost
- Delete unnecessary configuration options — more config = larger test matrix
- Delete unnecessary microservices — if two services always deploy together, merge them (CCP alignment)

## Step 3: Simplify or Optimize

**This step MUST come after "Delete."**

The mistake most people make is skipping the first two steps and starting optimization immediately. If you optimize something that should have been deleted, you are doing negative work. Only when you are certain something must exist should you consider how to make it simpler.

**In software engineering:**
- Replace complex event systems with direct function calls (if there are no multiple consumers)
- Replace Strategy pattern with simple if-else (if there are only 2-3 branches)
- Replace utility functions with inline code (if used only once)
- Simplify data flow — fewer layers the data passes through, the better
- Simplify APIs — fewer parameters, convention over configuration
- KISS: the simplest solution that satisfies the constraint is the correct one

## Step 4: Accelerate Cycle Time

Only after completing the first three steps do you consider acceleration.

"If you're digging your own grave, don't dig faster. Stop first."

**In software engineering:**
- Accelerate build times (incremental compilation, caching, parallel builds)
- Accelerate testing (run only affected tests, parallel execution)
- Accelerate deployment (CI/CD pipeline optimization, shorten feedback loops)
- Accelerate code review (small-batch commits, clear PR descriptions)
- Shorten the idea-to-production cycle

## Step 5: Automate

Machines come LAST. Do not start with automation.

Musk admits his biggest mistake on the Model 3 production line was reversing the order — automate first, then accelerate, and finally discover that step wasn't even needed. Only when a process is extremely mature and proven necessary do you hand it to machines.

**In software engineering:**
- Do it manually a few times to confirm the process is correct, THEN write the automation script
- Understand the deployment flow first, THEN write CI/CD
- Manually test the critical path first, THEN write end-to-end automated tests
- Understand data transformation rules first, THEN write ETL pipelines
- Code generation and AI-assisted programming are also automation — confirm what you're generating is necessary first

---

## The Full Chain

```
Question → Delete → Simplify → Accelerate → Automate
```

Most people's workflow is inverted: automate first, accelerate, optimize, never question, never delete. That is why we are perpetually busy and ineffective.

Next time you're about to dive into optimizing some project, stop and ask yourself: **"Does this thing even need to exist?"**
