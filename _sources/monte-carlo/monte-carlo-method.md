# Monte Carlo Methods

(sec:MC)=
## Introduction to Monte Carlo

## What is Monte Carlo?

Monte Carlo is a way of solving problems using "random numbers" in some essential way. All Monte Carlo calculations can be viewed as a multidimensional integration, although that may not always be the most useful point of view. Consider the following multidimensional integral:

$$
I=\int_{0}^{1} d^{D} x f(x)
$$

With MC, we sample randomly in the "cube" and take the average value.

$$
I=\lim _{M \rightarrow \infty} \frac{1}{M} \sum_{i=1}^{M} f\left(x_{i}\right)
$$

We will see in a minute that the (statistical) error $\epsilon$ of our estimate of $I$ converges like $\epsilon \propto M^{-1 / 2}$. Hence, the computer time $T$, needed to get an accuracy $\epsilon$ goes like

$$
T_{M C} \propto \epsilon^{-2}
$$

One order of magnitude in accuracy requires a 100 times longer run! This is true in all stochastic or Monte Carlo methods.

Why do we then use Monte Carlo? Consider the alternatives. Suppose we use the trapezoidal rule. There we find the error is $\epsilon \propto d x^{2} f^{\prime \prime}(x)$. The improved Simpson's rule gives an error $\epsilon \propto d x^{4} f^{(4)}(x)$ where $f^{(4)}$ is the fourth derivative and $d x$ is the grid spacing. In general we can write that the error is proportional to:

$$
\epsilon \propto d x^{\alpha} c_{\alpha}
$$

for an integration rule good to order $\alpha$ where $c_{\alpha}$ is proportional to the maximum $\alpha^{\text {th }}$ derivative of the function in the integration region. But here is the problem: the computer time will scale with the number of points: $d x^{-D}$. Hence we find that the time to do a "traditional" integration goes as:

$$
T_{i n t} \propto \epsilon^{-D / \alpha}
$$

Hence in the limit of small $\epsilon$, Monte Carlo will be more efficient if $D>2 \alpha$.\\
Why is this? It simply takes too long to fill an D-dimensional space uniformly with points. To get a reasonable value for the integrand, the grid spacing $d x$ must be smaller than the natural variation in $f(x)$. Typically hundreds of grid points in each dimension are required. If one raises one hundred to some high power, one cannot complete the integration.

Why can't we use very high order integration schemes, that is, take $\alpha$ large? The order of the scheme $\alpha$ is controlled by the smoothness of the function. Typical functions that we use in science become nasty if you differentiate, them too often. This means that higher order schemes\\
are less accurate than low order schemes unless $d x$ is exceedingly small. Hence one gets best results for $2 \leq \alpha \leq 4$. That means that MC is preferred once you get above 6 dimensions or so. This is borne out by experience.

The other reasons for doing MC are its conceptual simplicity and the fact that it comes with built in error bars. But the scaling behavior is the crucial difference.

Later we will discuss an alternative integration method which is between MC and grid based methods called "quasi-random numbers."

## Monte Carlo Terminology

First let us review some terms from probability theory.
A probability distribution function $p(x) d x$ is the probability of $x$ being in a small interval $(x, x+d x)$. This means than $p(x) \geq 0$ and $\int d x p(x)=1$. I will not particularly worry about what $x$ is, a real number or an integer (e.g. the state of a thrown die.) The cumulative distribution is better defined mathematically. $F(x)$ is the probability that $y \leq x$. Hence $F(x)=\int_{-\infty}^{x} d y p(y)$.

The expectation value of some function $f(x)$ with respect to $p$ is $I=<f>=\bar{f}=\int d x f(x) p(x)$. With an estimator we sample a set of $N$ values $\left\{x_{i}\right\}$ from $p$ and use those to estimate the value of $I$. The best estimator for the simple integral above is:

$$
f_{N}=\frac{\sum_{i=1}^{N} f\left(x_{i}\right)}{N}
$$

Now $f_{N}$ is distributed according to some probability distribution $p_{f_{N}}$. Of course, by construction $\left\langle f_{N}\right\rangle=I$. But we can ask, what are the fluctuations of $f_{N}$ about its mean value? This is the variance of $f_{N}$.

The central limit theorem is the foundation on which MC is built. The estimator, Eq.(6) will converge to the value of the integral, if the variance of $f(x)$ exists. Furthermore, we will know exactly the probability distribution of $f_{N}$ in the limit of large $N$; it is the normal distribution:

$$
p\left(f_{N}\right)=\left(2 \pi \sigma_{N}^{2}\right)^{-1 / 2} \exp \left[-\left(f_{N}-I\right)^{2} /\left(2 \sigma_{N}^{2}\right)\right]
$$

Since the successive values of $x_{i}$ are uncorrelated we have the variance of the mean is

$$
\sigma_{N}^{2}=\frac{1}{N} \sigma^{2}=\frac{1}{N}\left\langle[f(x)-I]^{2}\right\rangle=\frac{1}{N} \int d x p[x](f(x)-I)^{2}
$$

Traditionally in MC, one quotes $1 \sigma$ deviations as the error. Since we know it is a normal distribution, this means that $33 \%$ of the time one expects the value to exceed $1 \sigma, 5 \%$, a $2 \sigma$ deviation etc. A $2 \sigma$ error should not concern you too much, it happens fairly often.

Of crucial importance in any MC work is to prove (analytically) that the variance $\sigma$ exists. Only then you can talk about reliably about estimating errors. Usually the variance (of $f_{N}$ ) is estimated itself from the data with the formula:

$$
\sigma^{2}=\int d x(f(x)-I)^{2}=\frac{1}{N-1} \sum_{i=1}^{N}\left[f\left(x_{i}\right)-f_{N}\right]^{2}
$$

with the $F_{N}$ estimated from eq. (6). The $N-1$ appears because both the mean and variance are estimated from the same data. This formula is only correct if the data points are uncorrelated; otherwise one has to do blocking to eliminate the correlation. Then the estimate of the error of the mean is $\sigma_{N}=\sqrt{\sigma^{2} / N}$.

## Multidimensional distributions

Up to now we have been discussing a single variable ( x or f ). Often the output of a MC simulation is several variables (e.g. the energy and the pressure). We will write the $M$ output variables as a vector $\mathbf{x}=\left(x_{1}, \ldots, x_{M}\right)$. Then there is a p.d.f. in that M-dimensional space, $p(\mathbf{x}) d \mathbf{x}$. One can generalize the central limit theorem for that case. Define the covariance matrix:

$$
\nu_{i, j}=\left\langle\left(x_{i}-<x_{i}>\right)\left(x_{j}-<x_{j}>\right)\right\rangle
$$

The covariance matrix is a positive symmetric matrix. This means that it can be diagonalized and has positive eigenvalues.

Assume $p(\mathbf{x}) d \mathbf{x}$ is such that all elements of $\nu_{i, j}$ are finite, the various variances exist. Then the central limit theorem says that the estimate of the mean:

$$
\mathbf{x}_{N}=\frac{\sum_{k=1}^{N} \mathbf{x}_{k}}{N}
$$

for sufficiently large $N$ will obey the multidimensional normal (Gaussian) distribution:

$$
p_{N}\left(\mathbf{x}_{N}\right)=[2 \pi \operatorname{det}(\nu) / N]^{-1 / 2} \exp \left[-\left(\mathbf{x}_{N}-<\mathbf{x}_{N}>\right) \frac{N \nu^{-1}}{2}\left(\mathbf{x}_{N}-<\mathbf{x}_{N}>\right)\right]
$$

where the matrix inverse and determinant are meant. Unless $\nu$ is diagonal, the various values of $\nu$ are correlated positively if $\nu_{i, j}>0$, negatively otherwise. The covariance matrix can be estimated from applying its definition (Eq. (10) to a sequence of $\mathbf{x}_{i}$ 's. One note of caution: it takes at least ( $M+3) / 2$ vectors of data to fully specify the covariance matrix. Many more usually are needed.

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

## Comparison between MC and MD

Which is better for simulations, Monte Carlo or Molecular Dynamics?

1. MD can compute Newtonian dynamics. MC has a dynamics (often called kinetics) but it is under user control, through the transition probability. MC dynamics is useful for studying long-term diffusive process, if one sticks to local transition rules.
2. MC is simpler: no forces, no time step errors. (direct simulation of the canonical ensemble. It relies on a good source of pseudorandom numbers. Luckily this has not been a major problem.
3. MC is more general. In MD you can only work on how to make the CPUtime/physical time faster. If the system remains in a metastable state for a long physical time you are stuck. In MC you can invent better transition rules.
4. MD is sometimes very effective in highly constrained systems compared with classic Metropolis.
5. MD requires some extra effort for constant temperature and that messes up the dynamics. MC is naturally formulate at constant T .
6. MC can handle discrete degrees of freedom (e. g. spin models) while MD is limited to models that only have continuous degrees of freedom.

So you need both! The best is to have both in the same code so you can use MC to warm up the dynamics.

## Additional Resorces
