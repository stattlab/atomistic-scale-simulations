# Random Numbers

## Pseudorandom Number Generation

- Truly random values must come from a physical source (e.g., radioactive decay, system entropy).
- These are slow to sample, so we use **pseudorandom values** instead.
- Pseudorandom values are generated by deterministic mathematical operations but mimic randomness.

### Example: Linear Congruential Generator (LCG)

$$
X_{n+1} = (aX_n + b) \mod m
$$

- **Parameters**:
  - Multiplier \( a \)
  - Increment \( b \)
  - Modulus \( m \)
- Example values:
  - \( m = 2^{31} - 1 \)
  - \( a = 48271 \)
  - \( b = 0 \)
- \( X_0 \): seed, \( 0 < X_0 < m \)

- **Period**: How long it takes for the sequence to repeat.

#### Evaluating PRNG Quality

- Use statistical tests:
  - **Diehard / Dieharder**
  - **TestU01** (Small Crush, Crush, Big Crush)

> ⚠️ Do not use default PRNGs unless you know the algorithm.

#### Recommended PRNGs

- **Mersenne Twister**
- **Permuted Congruential Generator (PCG)**
- **Philox** (from Random123 library)

## Random Uniform Values

- We often want **uniform floating-point values**, but PRNGs generate integers.

### How to Generate \( U(0,1) \)

1. Generate a random integer (e.g., 32-bit or 64-bit).
2. Divide by the maximum possible value to get a float in \([0, 1)\).

> ⚠️ Be careful to avoid bias.
> The "bits of mantissa" matter since floating-point values have limited precision.

## Other Types of Random Variables

### Inverse Transform Sampling

Let \( X \) be a random variable with probability density \( f(x) \).
The cumulative distribution function (CDF) is:

$$
F(x) = \int_{-\infty}^{x} f(t) \, dt = P(X \leq x)
$$

**Steps**:

1. Draw \( u \sim U(0,1) \)
2. Compute \( x = F^{-1}(u) \)

> Since \( P(U \leq u) = u \), then \( P(X \leq x) = F(x) \)

#### Example: Exponential Distribution

- \( f(x) = 2e^{-2x} \)
- \( F(x) = 1 - e^{-2x} \)
- Inverse: \( x = -\frac{1}{2} \ln(1 - u) \)

## Special Algorithms

- **Box-Muller**: Generates normal (Gaussian) random values.
- **Sphere-point picking**: For uniform sampling on a sphere.

## Additional Resorces
