# Random Numbers

>Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin.
> -- <cite>John von Neumann (1951)</cite>

Up to now we have not discussed where the ``random numbers'' come from or indeed what we mean operationally by a random number. First randomness is a property of an infinite sequence xi with i = 1, 2, . . . . It is impossible to tell whether a single number is random or not. Random is a negative property, it is the absence of any order.
Note that there are three types of so-called random numbers.

- Truly Random - numbers exhibiting "true" randomness, such as found by counts of a Geiger measuring radioactive decay.
- Pseudo-Random - PR numbers (PRN) having the appearance of randomness, nevertheless the numbers exhibit a repeatable pattern or period of re-occurance (Hopefully very, very long because for 1024x1024 sites on 2-D lattice using 107 MC sweeps, one needs 1013 RNG!).
- Quasi-Random - numbers that are not random at all really (in fact, Quasi-random is not really a proper name). QR numbers are chosen to fill solution space with maximum distances between points so that "holes" are filled sequentially. An example would be numbers from [0,10], where the numbers could be chosen in any order and all space would be covered with no repeats. Using this with MC techniques for integration can improve variance to 1/N, such as for simple definite integrals. (Does not do so for all.)

In this section we will only discuss the uniform distribution, x, is either uniformly distributed in the range (0, 1) or x is an integer in [1, 2M]. (M is the number of bits). For simplicity, assume the latter representation. Then we can say the sequence is not random if knowing the previous values, allows you to predict something about the next value, (other than it is one of the allowed integers). With a random sequence, the predictions of even a very clever person are not better than average.

## What are some of the desired properties of random numbers?

Uncorrelated, deterministic, long-periods between repeats, uniform converage of range, efficiency of algorithm.

- **Determinism.** This is an odd property for a random sequence to have, since if it is deterministic, one can predict with certainty the next number, if you know the algorithm. However, it is a useful property for debugging since often one needs to check the code. Computers as they are now constructed are deterministic. The only possibilities for randomness are to read an "external" device, say the microsecond clock or a very unreliable memory. This is not done because it is very much too slow and too expensive. Everyone uses pseudo-random number generators (PRNG) instead, perhaps seeding (or initializing) them with the clock. It is likely that the PRNG are as reliable as a hardware version of a random number generator. A perfect pseudo-random number generator appears to be perfectly random, unless you happen to know both the algorithm and its internal state. From now on, we only discuss pseudo-random numbers. Let s be the internal state of the prng. Then a PRNG is a mapping from one state to another: sn+1 = f(sn). The nth random number is then some mapping of the internal state onto the integers or reals.
- **Cycle length.** Any pseudorandom number generator eventually has to repeat or cycle since there are a finite number of internal states. One would like the cycle length to be longer than a typical run. Consider the worst case scenerio, where all a code is doing is generating PRNs. A fast computer now can generate 109 operations/second. If we run it for 1 week we can generate 1015 = 249 PRNs. Hence if the PRNG has the maximal cycle length we should have at least 49 bits in the internal state. The continuing performance increase in computer performance, means that methods that worked in the past, may fail with tomorrow's computers. Luckily, it is easy to make very long cycle lengths.
Uniformity. This property means that if we go through a complete cycle, all the integers occur once. If we make a test with N occurrences of x, the number in the interval (a, b) should be in the range N (b-a) ± ( N (b-a) )-1/2. (This assumes that N ( b - a ) is much greater than 1.) Usually uniformity is easy to guarantee if you go over an entire cycle.
-**Correlation.** We would like our random numbers to be completely uncorrelated with each other. In general this means that any average such as: $< f1(xi+1) f2(xi+2) . . . fk(xi+k) > = < f1(xi+1) > < f2(xi+2) > . . . < fk(xi+k) >$ or for any set of functions f. The average is over all internal states of the random number generator. It turns out that Monte Carlo simulations of statistical mechanics can be sensitive to very long range correlations. Which particular correlations they are sensitive to is not very obvious, so often the only real test to run the code for a case where the exact answer is know or alternatively to try several different PRNGs.

## Pseudorandom Number Generation

- Truly random values must come from a physical source (e.g., radioactive decay, system entropy).
- These are slow to sample, so we use **pseudorandom values** instead.
- Pseudorandom values are generated by deterministic mathematical operations but mimic randomness.

### Example: Linear Congruential Generator (LCG)

This is what is provided on most computers.

$$
X_{n+1} = (aX_n + b) \mod m
$$

The initial (or seed) value to start the PRNG sequence is denoted I0. "mod" denotes modulo, or the remainder after division by m. Prime modulo are the best but 2N work fastest on binary computers. If c not zero, then LCG is called Mixed LCG.

For c=0, the maximum cycle length m= 2M occurs when a = 1 mod 4 and c is odd (often chosen as 1). For c not zero, the maximum cycle length= 2M-2 occurs when a = 3 mod 8 or 5 mod 8 (which is prefered) and initial seed is odd. (Note that low-order bits are not random!) For m = P (prime number), P-1 is the maximum period IFF a = primitive element mod P. There is always one integer that maps to itself, e.g. for c=0, I0 = 0 maps to itself.

Park and Miller recommend the following portable generator: m=p= 231 - 1 (i.e., 2,147,483,647), with a=16,807 and c=0. It is found that the larger M is the better the resulting sequence. Some 48 bit generators are very good. 64 bit are even better.

In general, never use the lower order bits from this type of generator as they are not very random.

Beware of using large groups of PRNs together (i.e. n-tuples). The congruential PRNG have the disadvantage that they are not free of sequential correlations on successive calls. They fall into planes. If k random numbers at a time are used to plot points in k-dimensional space, then the points lie on k-1 dimensional planes rather than filling up all k-space. There are at most m1/k planes, or fewer (which is even worse) if a, c, or M are not well chosen. If you take k numbers together, the correlation can be as high as 2-M/k.

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

A real or float pseudo-pandom number is then obtained by:

$$
Rn = In/ float(m) for [0,1)
Rn = In/ float(m-1) for [0,1]
$$

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

D. Knuth, Art of Computer Programming, Vol2. Seminumerical Algorithms, Second edition. Addison-Wesley, Reading, Massachusetts, 1981.

W.H. Press and S.A. Teukolsky, Numerical Recipes

Portable PRNG: George Marsaglia and Arif Zaman, Comput. Phys. 8, 117 (1994)
(From Physics Resource Link download Computer in Physics Articles)

P. Coddington, Tests of random number generators using Ising model simulations . Int. J. of Mod. Phys. C, 7(3):295-303, 1996.

Srinivasan, A., D. M. Ceperley and M. Mascagni, "Random Number Generators for Parallel Applications" in Monte Carlo Methods in Chemical Physics, Vol. 105, Advances in Chemical Physics, eds. D. M. Ferguson, J. I. Siepmann and D. G. Truhlar,Wiley (1999).
