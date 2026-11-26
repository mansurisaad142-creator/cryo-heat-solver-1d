i am building a 1d wire heat solver for cryogenic system without any library 
and a 100k parameters ai in [numpy] and a 10k neurons custom architecture ai in [pytorch] 
and comparing it against ansys as a benchmark and bind it in a complete end to end workflow 

# Cryo Heat Solver

1D heat solver for a cryogenic copper wire, built three ways: my own
finite-difference solver, an AI surrogate, and Ansys. (Status: Week 1)

## What works now
Constant-k rod: analytic T(x) plot and heat flow Q.

![T(x)](docs/figures/analytic.png)

## How to run
python plot_analytic.py     (jo bhi tera file path ho)

## Concepts (my words)
- T(x): temperature at each point of the rod
- Q = k·A·(T_hot − T_cold)/L: heat flow rate in W
- Steady state, constant k: T(x) is a straight line

## Roadmap
Own solver, then AI surrogate, then Ansys, then benchmark all three.
