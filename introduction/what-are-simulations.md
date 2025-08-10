# What are Simulations?

Computer simulation is the running of a model on a computer or cluster, where the model is meant to represent the behaviour of either a physical system or a theory.
Simulations are complementary methods to experiments and theory, as shown in {numref}`directive-fig`.

```{figure} ./_figures/Molecular_simulation_process.svg
:alt: Allen Tildesley view on the role of simulations
:width: 300px
:align: center
:name: directive-fig

Flowchart of interplay between experiment, simulation, and theory. Adapted from Allen & Tildesley.

```

A model consists of the equations or rules used to encode the behavior of a system or theory.
A computer simulation is the actual running of the program that perform algorithms which solve those equations.
So, we "design a model" and "run a simulation".{footcite:p}`allen1987computer`

Here, the focus is on **molecular systems**, therefore the models usually describe molecules or atoms.
The simulations are then representative solutions of these molecular models, that can be used to understand experiments, test theories and make predictions ({numref}`directive-fig`).

We will describe both  [Molecular Dyamics Simulations](../molecular-dynamics/index.md)(MD) and [Monte Carlo Simulations](../monte-carlo/index.md) (MC).

## History

The first simulations were of hard spheres using a Monte Carlo algorithm.

> Metropolis, Nicholas, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller, and Edward Teller. "Equation of state calculations by fast computing machines." The journal of chemical physics 21, no. 6 (1953): 1087-1092.

The first molecular dynamics simulations of hard spheres were performed in 1957

> Alder, Berni Julian, and Thomas Everett Wainwright. "Phase transition for a hard sphere system." The Journal of chemical physics 27, no. 5 (1957): 1208.

- Fermi, Pasta, Ulam (1954) experiment on ergodicity
- Alder, Wainwright (1958) liquid-solid transition in hard spheres. “long time tails” (1970)
- Vineyard (1960) radiation damage using MD
- Rahman (1964) liquid argon, water (1971)
- Verlet (1967) correlation functions, algorithms ...
- Andersen, Rahman, Parrinello (1980) constant pressure MD
- Nose, Hoover (1983) constant temperature thermostats.
- Car, Parrinello (1985) ab initio MD.

## Problems That Can be Addressed by Simulations

- Determine properies of materials at conditions where experiments would be challenging or expensive
- Gain microscopic insight into macroscopic behavior
- Investigate phase behavior, transport coefficents, structure-propoerty relationships
- Discovery/Inverse Design: use simulations to screen/discover/"make" new materials

## Additional Resorces & References

- Allen, Michael P., and Dominic J. Tildesley. "Computer simulation of liquids.", Oxford (1987){cite}`allen1987computer`
- “Understanding Molecular Simulation”, Frenkel and Smit {cite}`frenkel1957understanding`
- “Computational Materials Science”, Richard LeSar {cite}`lesar1999computational`
- “A Guide to Monte Carlo Simulations in Statistical Physics”, David P.
Landau, Kurt Binder {cite}`landau2021guide`
