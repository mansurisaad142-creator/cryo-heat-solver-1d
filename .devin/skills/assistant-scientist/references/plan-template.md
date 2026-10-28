# Learning and problem-solving plan template

Read this before building any schedule or resource list.

## Contents
- Capacity arithmetic
- Session shape
- Plan output format
- Dependency order for quantum, AI and simulation
- Candidate resources (verify before recommending)
- Failure rules

## Capacity arithmetic

Default: 3 hours per week. Show the numbers before the plan.

- 3 h/week = about 12 h/month = about 150 h/year (allowing a few missed weeks).
- A typical university course (one semester, one subject) is on the order of 120 to 150 hours of study including problems. So 3 h/week is roughly one serious course per year.
- Say this plainly when the user's goal needs more. Then give the best plan inside the budget and name exactly what is delayed or dropped. Offer a second version if the user can raise the hours.

## Session shape

For a 3-hour week, default split is one 2-hour block and one 1-hour block, or three 1-hour blocks. Each block:

1. Recall (about 10 minutes): write from memory what the last session covered.
2. New material (about 40% of the block): one concept, with derivation.
3. Problems (about 40%): solved by the user, not the assistant.
4. Close (about 10%): write what was learned and what is still unclear. That list is the start of the next session.

## Plan output format

Give the plan in this order, in a table when it is multi-part:

1. **Goal and horizon** (one line, measurable).
2. **Capacity** (hours per week, total hours, arithmetic).
3. **Sequence** (topics in dependency order with hours per topic).
4. **Weekly structure** (what each block does).
5. **Checkpoints** (monthly test, with the pass criterion).
6. **Evidence of completion** (what the user brings to the next session).
7. **Stop/adjust rule** (the result that means the plan is failing and what to change).

## Dependency order for quantum computing, AI and simulation

Do not schedule a topic before its prerequisites.

1. Calculus (single and multivariable), linear algebra, probability and statistics.
2. Ordinary and partial differential equations, Fourier analysis.
3. Numerical methods: floating point, linear solvers, ODE and PDE integration, error and stability analysis.
4. Classical mechanics (Lagrangian and Hamiltonian forms).
5. Quantum mechanics (states, operators, measurement, spin, perturbation theory).
6. Simulation methods: finite difference and finite element, Monte Carlo, molecular dynamics; verification and validation practice.
7. Quantum computing: qubits, gates, circuits, core algorithms, error correction basics.
8. Machine learning fundamentals, then deep learning, then scientific machine learning (surrogate models, physics-informed methods).

Programming practice (Python, numerical libraries) runs alongside steps 3 to 8 as part of the problem time.

## Candidate resources (verify before recommending)

These are well-known starting points. Confirm title, edition, availability and current access via search before presenting any of them as a recommendation. Mark as unverified if you cannot confirm.

- Linear algebra: Gilbert Strang, *Introduction to Linear Algebra*; MIT OpenCourseWare 18.06.
- Numerical linear algebra: Trefethen and Bau, *Numerical Linear Algebra*.
- Classical mechanics: John R. Taylor, *Classical Mechanics*.
- Quantum mechanics: David J. Griffiths, *Introduction to Quantum Mechanics*; later, J. J. Sakurai, *Modern Quantum Mechanics*.
- Quantum computing: Nielsen and Chuang, *Quantum Computation and Quantum Information*.
- Optimization: Boyd and Vandenberghe, *Convex Optimization* (free from the authors' site).
- Deep learning: Goodfellow, Bengio and Courville, *Deep Learning*.
- Preprints: arXiv.org for primary research papers.

## Failure rules

- Two missed weeks in a row: stop and re-plan with the real available hours.
- Checkpoint below the pass criterion: repeat the topic, do not advance.
- A resource is too hard or too easy after one session: replace it, do not push through.
