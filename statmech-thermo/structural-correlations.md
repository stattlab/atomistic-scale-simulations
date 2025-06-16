# Structural Correlations

## Distribution Functions

What if we only care about the distribution of some particles in a given portion?

Let:

$$
f^{(2)}(r_1, r_2) = \frac{N!}{(N-2)!} \int \cdots \int e^{-\beta U(r^N)} \, dr_3 \cdots dr_N
$$

This is for two specific particles, but what if we don't care which ones?

There are:

- \( N \) ways to choose particle 1,
- \( N - 1 \) ways to choose particle 2, etc.

These functions measure probabilities, which must depend on the overall density.

Example: Ideal gas

$$
f^{(2)}(r_1, r_2) = \rho^2
$$

We define the **two-body correlation function** \( g(r) \) to measure correlations relative to a completely uncorrelated ideal gas:

$$
g(r) = \frac{f^{(2)}(r_1, r_2)}{\rho^2}
$$

## Radial Distribution Function (Pair Correlation Function)

If the system is:

- **Homogeneous**: \( g(r_1, r_2) \) depends only on the relative position.
- **Isotropic**: \( g(r_1, r_2) = g(|r_1 - r_2|) = g(r) \)

### Features of \( g(r) \)

- First peak: nearest neighbor shell
- Second peak: second shell
- \( g(r) \to 1 \) as \( r \to \infty \)
- \( g(r) = 0 \) at very small \( r \) due to core repulsion

### Interpretation

- \( g(r) \) is a **conditional probability**:

  $$
  p(r_2 | r_1) = \frac{p(r_1, r_2)}{p(r_1)} = \rho g(r)
  $$

- \( \rho g(r) \): average density at distance \( r \) from a particle at the origin

## Pairwise Properties

To compute an average pairwise property \( \langle a \rangle \):

$$
\langle a \rangle = \frac{1}{2} \rho^2 \int d\vec{r} \, g(r) a(r)
$$

For example, potential energy:

$$
U = \frac{1}{2} \rho^2 \int d\vec{r} \, g(r) u(r)
$$

In spherical coordinates:

$$
U = 2\pi \rho^2 \int_0^\infty dr \, r^2 g(r) u(r)
$$

## Tail Correction

To account for interactions beyond a cutoff \( r_c \):

$$
\Delta U/N = 2\pi \rho \int_{r_c}^\infty dr \, r^2 g(r) u(r)
$$

For Lennard-Jones potential:

$$
u(r) = 4\epsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right]
$$

## How to Compute \( g(r) \)

1. Choose a particle \( i \)
2. Compute distances to all other particles \( j \)
3. Count (histogram) distances into bins of width \( \Delta r \)
4. Repeat for all particles
5. Normalize histogram:

   $$
   g_k = \frac{n_k}{N \cdot V_k \cdot \rho}
   $$

   where:
   - \( n_k \): number of particles in bin \( k \)
   - \( V_k = 4\pi r_k^2 \Delta r \): volume of spherical shell

Typically define \( g(r_k) \) at \( r_k + \Delta r / 2 \)

## Structure Factor

The **structure factor** \( S(k) \) is obtained in scattering experiments and is related to \( g(r) \) via Fourier transform:

$$
S(k) = 1 + \rho \int d\vec{r} \, e^{i \vec{k} \cdot \vec{r}} [g(r) - 1]
$$

> Note: We will not discuss this in detail in this class due to subtleties, but you should be aware of it.
