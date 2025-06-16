# Monte Carlo Methods

## History

- **Origin**: Von Neumann, Ulam & Metropolis (1947) — neutron diffusion in fissionable material.
- **Term**: "Monte Carlo" coined.
- **First MC simulation**: Metropolis, Rosenbluth, Teller (1953) — equilibrium statistical mechanics.

## Monte Carlo Integration

### Example: Estimating Area

- Throw rocks randomly into a bounding rectangle.
- Estimate area of a pond:

  $$
  \text{Area} = W \times L \times \frac{\text{hits in pond}}{\text{total throws}}
  $$

- Can be used to estimate π via quarter-circle area.

### Accuracy

- Accuracy improves slowly: 1 decimal digit per 10× more samples.
- For low-dimensional problems, deterministic methods (e.g., Simpson’s Rule) are better.

## Multidimensional Integrals

- Example: Canonical partition function for N = 20 particles with 25 positions each:

  $$
  25^{20} \approx 10^{28} \text{ evaluations needed}
  $$

- Most configurations contribute little to the integral.
- Random sampling often generates invalid configurations (e.g., overlapping particles).

## Importance Sampling

- **Problem**: Uniform sampling inefficient in high-dimensional phase space.
- **Solution**: Sample from a distribution proportional to the function of interest.

### Definitions

- Uniform sampling:

  $$
  \langle P \rangle = \frac{1}{n} \sum P_i
  $$

- Importance sampling:

  $$
  \langle P \rangle = \sum P_i \cdot w_i
  $$

Where \( w_i \) is the weight from the desired distribution.

## Generating States with Correct Probability

- Consider 20 particles in 25 positions → \( 25^{20} \) states.
- In a large sample, the number of times a state appears is proportional to:

  $$
  N(i) \propto \exp(-\beta U(i))
  $$

- To ensure correct sampling, transitions must satisfy **detailed balance**:

  $$
  N(o) \cdot M(o \rightarrow n) = N(n) \cdot M(n \rightarrow o)
  $$

## Transition Probabilities

- Transition probability has two parts:

  $$
  M(o \rightarrow n) = x(o \rightarrow n) \cdot \text{acc}(o \rightarrow n)
  $$

  - \( x(o \rightarrow n) \): probability of proposing the move.
  - \( \text{acc}(o \rightarrow n) \): probability of accepting the move.

- Best choice for \( x \): satisfies **microscopic reversibility**:

  $$
  x(o \rightarrow n) = x(n \rightarrow o)
  $$

## Acceptance Rules

### Metropolis Rule

- If \( U(n) < U(o) \): accept
- Else: accept with probability

  $$
  \exp(-\beta [U(n) - U(o)])
  $$

### Barker Rule

  $$
  \text{acc}(o \rightarrow n) = \frac{\exp(-\beta U(n))}{\exp(-\beta U(o)) + \exp(-\beta U(n))}
  $$

## Example: 10-State System

- States: 1 to 10
- Probabilities: proportional to state index
- Partition function:

  $$
  Z = \sum_{j=1}^{10} j = 55
  $$
- Equilibrium probability of state \( j \):

  $$
  P(j) = \frac{j}{55}
  $$

- Transition rule: \( x(o \rightarrow n) = \frac{1}{10} \) for all pairs

## Convergence Comparison

- **Metropolis** converges faster than **Barker**.
- Example: Starting from state 3, track probability distribution over trials.
- Metropolis reaches equilibrium faster due to higher acceptance of favorable moves.

## Summary

- Monte Carlo methods are powerful for high-dimensional integrals.
- Importance sampling and detailed balance are key to efficient and correct simulations.
- Metropolis algorithm is widely used due to its simplicity and effectiveness.

## Additional Resorces
