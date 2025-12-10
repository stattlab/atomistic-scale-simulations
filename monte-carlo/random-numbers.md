# Random Numbers

Throughout various aspects of molecular models, random numbers are crucial for everything ranging from creating initial configurations for a system to iterating through steps of a Monte Carlo simulation. However, the generation of such numbers is often not trivial, and different methods exist for accomplishing this task. In order to obtain truly random numbers, one must rely on natural phenomena. Some examples include the time at which a radioactive nucleus decays, as measured by a Geiger counter, or the fluctuations of the voltage across a resistor, which depend on environmental noise. However, it is often inconvenient to implement such processes in simulations due to time constraints and hardware requirements. Instead, pseudorandom numbers, which mimic the behavior of truly random numbers while being much more efficient to generate, are used extensively in various areas, such as molecular modeling.

## Linear Congruential Generator

$$
X_{n + 1} = (a X_n + b) \bmod m
$$

The Linear Congruential Generator (LCG) is one of the simplest and oldest pseudorandom number generators. It produces a sequence of numbers using the formula shown above. Here, $X_n$ is the current number in the sequence, $a$ is the multiplier, $b$ is the increment, and $m$ is the modulus. Given an initial seed $X_0$, all subsequent values can be determined. LCGs are computationally fast and simple to implement, but they can potentially have short periods and correlations between generated numbers, which can negatively affect simulations.

## Mersenne Twister

$$
X_{k + N} = X_{k + M} \oplus AX_k
$$

The Mersenne Twister (MT19937) is another pseudorandom number generator that can produce high-quality random numbers with an extremely long period of $2^{19937} - 1$. It was designed to overcome the limitations of simpler generators, and uses 32-bit integers in binary as inputs and outputs, which can be represented as 32-dimensional vectors denoted by X in the above equation. To start, the algorithm utilizes a large internal state that contains 624 ordered 32-bit integers. In particular, the values N and M shown in the above equation are defined as 624 and 397 respectively. 

In order to find random number $k + N$, number $k + M$ and number $k$ must already have been generated, or are part of the predetermined set. Assuming this is the case, number $k$ can be expressed as a 32-dimensional vector $X_k$, multiplied by a matrix A, and then taken to modulo 2. Next, the each element of the product vector is combined with $X_{k + M}$ as a vector via a piecewise XOR ($\oplus$) operation in order to obtain $X_{k + N}$.

## Inverse Transform Sampling

While pseudorandom number generators like the Linear Congruential Generator and the Mersenne Twister are very good at generating random numbers that are uniform within a range, many tasks related to simulating molecular behavior require more complex distributions, such as a Boltzmann distribution. To start, with the aforementioned generators, one can make uniform distributions over any range, simply by scaling and shifting the values obtained by the appropriate amounts. However, in order to get non-uniform distributions, some more complex techniques are required. Inverse Transform Sampling one such technique. It can produce samples from a probability density function $f(x)$ assuming its associated cumulative distribution function (CDF) can be calculated as: $F(x) = \int_{-\infty}^x f(t)dt$. Samples from $f(x)$ can be obtained by generating a uniform random number $u \in [0,1)$, and computing $F^{-1}(u)$.  

## Rejection Sampling

While inverse transform sampling is useful, it is sometimes inconvenient or not possible to calculate the cumulative distribution function, $F(x) = \int_{-\infty}^x f(t)dt$. In situations like this, a different techniques, such as rejection sampling, must be used. Rejection Sampling is used when the inverse CDF of a target distribution $f(x)$ is difficult or impossible to compute. It can be described as follows:

1. Obtain a probability density $g(x)$ from which sampling can be done.
2. Scale $g(x)$ by a constant M such that $Mg(x) \ge f(x)$ across the entire domain of $f(x)$.
3. Select a sample X from $f(x)$, a sample Y from $g(x)$, and a sample Z from Uniform(0, 1).
4. If $Z \le \frac{f(X)}{Mg(Y)}$, then accept the sample X.
5. Repeat step 4 until enough samples have been drawn.

## Additional Resources

Bradley, T., et al. "Chapter 16-parallelization techniques for random number generators." GPU Computing Gems Emerald Edition: 231-246

Gilks, Walter R., and Pascal Wild. "Adaptive rejection sampling for Gibbs sampling." Journal of the Royal Statistical Society: Series C (Applied Statistics) 41.2 (1992): 337-348.

Olver, Sheehan, and Alex Townsend. "Fast inverse transform sampling in one and two dimensions." arXiv preprint arXiv:1307.1223 (2013).


Tezuka, Shu. "Linear congruential generators." Uniform Random Numbers: Theory and Practice. Boston, MA: Springer US, 1995. 57-82..
