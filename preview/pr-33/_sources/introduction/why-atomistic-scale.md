# Why are we interested in the atomistic scale?

> “The general theory of quantum mechanics is now almost complete. The underlying physical laws necessary for the mathematical theory of a large part of physics and the whole of chemistry are thus completely known, and the difficulty is only that the exact application of these laws leads to equations much too complicated to be soluble.” (P. A. M. Dirac, Proc. R. Soc. Lond. A 1929, pg. 123)

> “A profound joke is that one can measure the progress of physics by the problems that can't be solved. In Newtonian gravity, the three-body problem is difficult, but the two-body problem can be done exactly; in general relativity, two bodies are difficult but one body can be done exactly; in quantum gravity, the vacuum is intractable.” (Frank Wilczek, Physics Today 2003, pg.11)

The atoms are the units or particles of interest (see also [Molecular Models](../molecular-models-and-interactions/molecular-models.md)), and simulation (see also [Simulations](./what-are-simulations.md)) is the technique of interest, where simulation just means an imitation of the operation of a real-world process or system over time.

## General Thoughts

Computational physics per se is interesting and challenging, it is often a good (sometimes the only) way to understand the physics of complex multi-body systems. Experiment is/can be limited and expensive, and simulations can complement the experiment.

But:

- Computational time is limited and expensive (carbon footprint!): few particles for short time
- Systems with many particles and long-time scales are problematic
- Physical and mathematical underpinnings: What approximations come in? Hamiltonian is unknown, until we solve the quantum many-body problem!
- How do we estimate errors? (statistical and systematic)
- How do we manage ever more complex codes? (parallelism, testing)
