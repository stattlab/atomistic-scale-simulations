# Structural Correlations

## Scalar Properties, Static Correlations and Order Parameters

### Scalar Properties

Today we discuss the basic properties we can calculate with simulation and also can be compared to experiment. What we can calculate with MD are microcanonical averages but to within factors of order (1/N) these should equal canonical averages. Later we will calculate the same things with Monte Carlo. The main scalar properties are:

* The Potential Energy, V\(R\).
* The Kinetic energy (to estimate the temperature).
* The Total energy (to test for energy conservation)
* The Pressure using virial theorem.
* The Specific Heat: The fluctuations in the potential energy can be used to estimate the specific heat. Danger: the canonical formula cannot be directly used since energy is conserved. See the discussion in A&T
* See A&T for more thermodynamic quantities.

It would also be possible to estimate the specific heat as the difference in energy with runs at two different temperatures. The disadvantage of this approach is that the statistical errors are amplified as the temperatures get close together and that separate runs are required.

````{exercise} Specific Heat Error

Write the formula for the statistical error of the specific heat versus difference in the temperature dT.

1. How does the systematic error depend on dT?
2. Given a fixed amount of computer time, chose dT to make the **''statistical error'' = ''systematic error''**.
    (Equating errors is legitimate, and easier, because we do not want one type of error to dominate).
3. Finally how does this error (now actually dT) depend on computer time (or sample data points)?


```{solution}
Here's what's inside!
```
````

It is not easy to calculate the free energy directly. We will discuss special methods to calculate it later.  Scalar quantities themselves are not usually very enlightening on the state of the system (e.g. liquid or solid). It is better to look at what is known as order parameters"; this is one of the main advantages of computer simulation over experiment. We will discuss correlation function in real and k-space next time.

## Static Correlations and Order Parameters

The most important information that comes from simulations are the static correlation functions. You should develop a habit of looking at these quantities routinely since they tell you basic information about what the particles are doing, namely where they are and how they arrange themselves.  The homework and exams require you to understand basic properties and relations of the static correlation functions. By static we mean properties that depend on properties computed with single "snapshot" or time step.  This is contrasted with "dynamical properties" which depend on how properties change in time.

The types of static correlations can generally be divided into

* One body quantities: the density and its Fourier transform. Another example is the RMS deviation from lattice sites for a solid, this is called Lindeman's ratio or in Fourier space the Debye-Waller factor.
* Two body quantities: the pair correlation and its Fourier transform: the structure factor.
* Higher body correlations such as angular correlations and three-body correlations.

### The Density

The density (&rho;) tells you where the particles are (or have been). In a translationally invariant system it will be constant except for noise if you average long enough.

You find it by histogramming, that is subdividing the total volume into a set of subvolumes. How to histogram:

* After the particles have been moved, take each particle and map the particle coordinate into an integer.
* Add one to that memory location corresponding to that integer. You have a 'hit' in that 'bin' .
* At end of run normalize the hits by total number of passes and volume element of bin.

How do we set the histogramming size? By balancing the statistical error with the systematic error. The statistical error goes inversely as the square root of the volume size times the length of the run. It blows up for radial functions on a uniform mesh since the volume size goes at r<sup>2</sup>. The systematic error depends on the physical system, if the system is spread out, the density is pretty smooth, only a few bins will be needed.

````{exercise} Density of Inhomogeneous System

Assume that you are computing the density in an inhomogenous system with _N particles_ and _M independent samples_ and the average density f\(r\) depends only on the radius r from the origin. Set up a radial grid with spacing dr. (This is a 3D system!)

1. What is the estimator for f\(r\)?
2. Assuming the particle postitions are uncorrelated, what is the statistical error of the estimate of f\(r\)?
    * Hint: Hits form a bitstream for a particular bin with NM uncorrelated bits.
    * Hint: Probability for any single particle ini a particular bin is **estimator for p = f\(r\) dV/N**, which is clearly correct for f\(r\)= constant = N/V.
    * Hint: Probability for any single trial hitting a bin is proportional to the size of the bin, i.e. p = dV/V. For the NM trials, the **estimator for p = (# of hits)/NM**.
3. How does the systematic error depend on dr and f\(r\)?
    * Hint: How much does f\(r\) vary within 1 bin?
    * Hint: Assume that dr is small, i.e. dr << 1.
4. What is the value of dr which minimizes the total error? How does it scale with M and r?
    * Again, rather than minimize total error, equate the systemmatic statistical error so that one does not dominate the error.

```{solution}
Here's what's inside!
```
````
Three dimensional histograms are a problem because, first the number of hits/bin is low so noise level is high, second they are hard to visualize, third they take alot of memory. You might want to use symmetry or projections to reduce a 3d function to 1 or 2 dimensional densities.

It is also good to examine the density in Fourier space. In periodic boundary conditions  the allowed K-vectors are on a grid. The Fourier density can be used to either: 1) smooth out the real space part by setting to zero the FT density larger than some value and fourier transforming back. (Disadvantage: the resulting density might go negative.) 2) look for periodic structures.

### Pair correlations

The pair correlation function (also called the radial distribution function or g\(r\)) is the density of other particles around a given particle. Its first peak occurs around &rho;<sup>-1/3</sup>. Normalization is usually defined such that at large r, g\(r\)=1. The theory of liquids is based on pair correlations because you can calculate the energy, pressure etc if you know g\(r\) (as long as the only potential is a pair potential.)  In a liquid or gas, g\(r\) depends only on the distance between two particles, not on the angle. Actually PBCs break isotropy, g\(r\) could be different between the box axis and the body diagonal. Usually one ignores this to obtain a spherically symmetric g\(r\) for r less than half the box side. The pair correlation function is needed to apply 'tail' corrections to the potential energy and pressure coming about because of the truncation at the edge of the box.

The Fourier transform of g\(r\) is called the static structure function S\(k\). It is important to calculate because it can be compared directly with experiment, either neutron or X-ray scattering can measure it. There are very expensive instruments at Argonne, Grenoble, Brookhaven that are dedicated to measuring S\(k\) and its time dependent generalization. If the agreement is good it gives a lot of confidence concerning the potential model. But don't be carried away; agreement to 5% is typical if the potential is at all reasonable.

The first peak of S\(k\) is around &rho;<sup>1/3</sup>. Normalization is such that at large k: S\(k\)\=1. It can be computed in two different ways, either as a FT of g\(r\) or the direct way. The direct way is slower but better at low k-values or as reciprocal lattice vectors of a possible solid structure because there are not the systematic errors of ignoring anisotropic correlations and histogram effects. Also g\(r\) must be extended to large r to do the FT.

One should use the peak of S\(k\) to decide is a system is solid. For a liquid S\(k\) is smooth and order 1 everywhere. A solid shows delta functions with peak high a fraction of the number of particles at the reciprocal lattice of the solid. Solid structure shows up in g(r) in a more subtle way: instead of a nice damped oscillations, there are bumps at the nearest neighbor, next-nearest neighbor, etc. (Where they are depends on the type of lattice).

The structure factor also signals separation in a two phase region. An example is the formation of droplets such as occurs when the number of particles corresponds to neither a stable liquid of gas, but a mixture of liquid and gas. In that case the structure function will diverge at low wave vectors. The value at zero ($S(0)$) equals N by definition (in the canonical ensemble) but this can be different than $\lim_{k \to 0} S(k)$  which is proportional to the compressibility of the system.

### Order parameters

A key concept from the theory of phase transitions is the idea of an "order parameter" which characterizes a phase. For the moment we will just explain how this works for the two most common phase transitions: liquid-gas and liquid-solid.

**_The liquid-gas transition:_** the order parameter is the density. a liquid and gas are identical except a liquid has higher density. At the critical point the difference disappears. There is a first order phase transition between liquid and solid so it is quite possible to do a simulation in the two phase region. What will happen? Liquid droplets will form assuming 1) the surface tension allows it and 2) the simulation is long enough. When this happens S\(k\) will have a characteristic behavior.

**_The liquid-solid transition:_** A solid is characterized by a periodic density. For example the Fourier transform of the density will be very large for certain wavevectors (the reciprocal lattice vectors).

## Distribution Functions

What if we only care about the distribution of some particles in a given portion?

Let:

$$
f^{(2)}(r_1, r_2) = \frac{N!}{(N-2)!} \int \cdots \int e^{-\beta U(r^N)} \, dr_3 \cdots dr_N
$$

This is for two specific particles, but what if we don't care which ones?

There are:

* \( N \) ways to choose particle 1,
* \( N - 1 \) ways to choose particle 2, etc.

These functions measure probabilities, which must depend on the overall density.

Example: Ideal gas

$$
f^{(2)}(r_1, r_2) = \rho^2
$$

We define the **two-body correlation function** \( $g(r)$ \) to measure correlations relative to a completely uncorrelated ideal gas:

$$
g(r) = \frac{f^{(2)}(r_1, r_2)}{\rho^2}
$$

## Radial Distribution Function (Pair Correlation Function)

If the system is:

* **Homogeneous**:  $g(r_1, r_2)$  depends only on the relative position.
* **Isotropic**:  $g(r_1, r_2) = g(|r_1 - r_2|) = g(r)$

### Features of $g(r)$
The radial distribution function has several key features which are visualized in 
* First peak: nearest neighbor shell
* Second peak: second shell
* \( g(r) \to 1 \) as \( r \to \infty \)
* \( g(r) = 0 \) at very small \( r \) due to core repulsion

<figure style="background: white; display: inline-block; margin: 0; text-align: center;">
  <img src="statmech-thermo/_figures/Lennard-Jones_Radial_Distribution_Function.svg" 
       alt="Lennard-Jones Radial Distribution Function" 
       style="max-width: 400px; display: block; margin: 0 auto;">
  <figcaption style="font-size: 0.9em; color: #555; margin-top: 4px;">Figure 1: Lennard-Jones Radial Distribution Function</figcaption>
</figure>



### Interpretation

* \( g(r) \) is a **conditional probability**:

  $$
  p(r_2 | r_1) = \frac{p(r_1, r_2)}{p(r_1)} = \rho g(r)
  $$

* \( \rho g(r) \): average density at distance \( r \) from a particle at the origin

## Pairwise Properties

To compute an average pairwise property \( $\langle a \rangle$ \):

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

To account for interactions beyond a cutoff \( $r_c $ \):

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
   * \( n_k \): number of particles in bin \( k \)
   * \( V_k = 4\pi r_k^2 \Delta r \): volume of spherical shell

Typically define \( g(r_k) \) at \( r_k + \Delta r / 2 \)

## Structure Factor

The **structure factor** \( S(k) \) is obtained in scattering experiments and is related to \( g(r) \) via Fourier transform:

$$
S(k) = 1 + \rho \int d\vec{r} \, e^{i \vec{k} \cdot \vec{r}} [g(r) - 1]
$$

> Note: We will not discuss this in detail in this class due to subtleties, but you should be aware of it.

## Thermodynamic Estimators

```{list-table} Thermodynamic Estimators
:header-rows: 1
:name: tab-thermodynamic estimators

* - Name
  - Symbol
  - Formula
* - Kinetic Energy
  - $K$
  -  $\frac{1}{2} \sum_{i} m_{i} v_{i}^{2} \quad=\frac{1}{2} k_{B} T(\text{degrees of freedom})$
* - Potential Energy
  - $U$
  - $\sum_{i<j} \phi\left(r_{i j}\right) \quad=\frac{N}{2} \rho \int d^{3} r \phi(r) g(r)$
* - Pressure
  - $P=-\frac{\partial F}{\partial \Omega}$
  -  $\frac{1}{3 \Omega}\left[2 K-\sum_{i<j} r_{i j} \frac{d \phi}{d r}\right]=\rho k_{B} T-\frac{\rho^{2}}{6} \int d^{3} r g(r) r \frac{d \phi}{d r}$
* - Specific Heat
  - $C_{V}=\frac{\partial F}{\partial T}$
  - $\frac{1}{\left(k_{B} T\right)^{2}}\left\langle(E-\langle E\rangle)^{2}\right\rangle=(3 / 2) N+\frac{1}{\left(k_{B} T\right)^{2}}\left[\left\langle V^{2}\right\rangle-\langle V\rangle^{2}\right]$
```

## Physical Structure Estimators

## Density

### Real Space, $\rho(\vec{r})$

$$
\rho(\vec{r}) & =\sum_{i=1}^{N}\left\langle\left(\delta\left(\vec{r}_{i}-\vec{r}\right)\right\rangle=\sum_{i=1}^{N} \frac{\left\langle\Theta\left(\vec{r}_{i} \in \operatorname{Bin}_{\vec{r}_{i}}\right)\right\rangle}{\text { Vol. of } \operatorname{Bin}_{\vec{r}_{i}}}\right. \\
& =\rho, \quad \text { (for uniform system) }
$$

In a crystal, the mean-squared deviation from a set of lattice sites $\left\{\mathbf{Z}_{\mathbf{i}}\right\}$ is important.

$$
u^{2}=<\left(\mathbf{r}_{\mathbf{i}}-\mathbf{z}_{\mathbf{i}}\right)^{2}>
$$

A classical solid melts when $u^{2}>0.15 d_{n n}^{2}$ (Lindemann's ratio)

### $\vec{k}$ - Space, $\rho_{\vec{k}}$

$$
\rho(\vec{k}) & =\int d^{3} r e^{i \vec{k} \cdot \vec{r}} \rho(\vec{r})=\sum_{i=1}^{N} e^{i \vec{k} \cdot \vec{r}_{i}} \\
\rho_{0} & =N \\
\rho_{\vec{k} \neq 0} & =0, \quad \text { (for uniform system) }
$$

Note: In rectangular periodic boundary conditions, $\vec{k}=\left(\frac{2 \pi}{L_{x}} n_{x}, \frac{2 \pi}{L_{z}} n_{z}, \frac{2 \pi}{L_{z}} n_{z}\right)$.\\
Fourier smoothing is done by removing terms that have $k>k_{\text {cutof } f}$,

$$
\tilde{\rho}(\vec{r})=\frac{1}{\Omega} \sum_{|\vec{k}| \leq k_{\text {cutoff }}} \rho_{\vec{k}} e^{-\vec{k} \cdot \vec{r}}
$$

## Pair Correlation

### Pair Correlation Function, $g(\vec{r})$

In the following formulas, realize the definitions may only make sense for $|\vec{r}| \leq L / 2$.

$$
g(\vec{r})=\frac{2 \Omega}{N^{2}} \sum_{i<j}\left\langle\delta\left(\vec{r}_{i}-\vec{r}_{j}-\vec{r}\right)\right\rangle
$$

For free particles, $g(r)=1-1 / N$.\\
Sum rule is $\int d^{3} r g(r)=(1-1 / N) \Omega$.\\
The potential energy and the pressure estimator can be written in terms of $g(r)$,

$$
V=\left\langle\sum_{i<j} \phi\left(r_{i j}\right)\right\rangle=\frac{N \rho}{2} \int d^{3} r \phi(\vec{r}) g(\vec{r}) \\
P=\rho k_{B} T-\frac{\rho^{2}}{6} \int d^{3} r g(r) r \frac{d \phi}{d r}
$$

The tail correction for a shifted potential is:

$$
\Delta V=2 \pi N \rho\left[\phi\left(r_{c}\right) \int_{0}^{r_{c}} r^{2} d r g(r)+\int_{r_{c}}^{\infty} r^{2} d r \phi(r)\right]
$$

assuming $g(r)=1$ for $r>r_{c}$.

### Structure Factor, $S_{k}$

$$
S_{\vec{k}} & =\frac{1}{N}\left\langle\rho_{\vec{k}} \rho_{-\vec{k}}\right\rangle \\
S_{0} & =N
$$

For a perfect crystal $S_{k}$ will be zero almost everywhere, except for some well-defined spikes. In particular, for a bravais lattice the spikes are located at reciprocal lattice points,

$$
S_{k}=N \sum_{G} \delta_{k, G} .
$$

In general

$$
S_{k}=1+(N-1) \sum_{G} \delta_{k, G} e^{-k^{2} u^{2} / 3}
$$

where the Debye-Waller factor $u$ is defined in Eq. (3).
For a non-perfect crystal, the spikes will soften, and in the limit $k \rightarrow \infty, S_{k} \rightarrow 1$.
For free particles, $S_{k}=1+(N-1) \delta_{k, 0}$.
The short-wavelength behavior of the structure factor is related to the compressibility, $\chi_{T}=$ $(\rho d P / d \rho)^{-1}$ by the relation

$$
\lim _{k \rightarrow \infty} S_{k}=\rho k_{B} T \chi_{T}
$$

### Relation between $g(r)$ and $S_{k}$

Exact formulas for periodic boundaries:

$$} r e^{i \vec{k} \cdot \vec{r}}(g(\vec{r})-1) \\
g(\vec{r}) &= \frac{1}{N} \sum_{k} e^{i \vec{k} \cdot \vec{r}}\left(S_{\vec{k}}-1\right)
$$
S_{\vec{k}} &= 1+N \delta_{\vec{k}, 0}+\rho \int_{\Omega} d^{3

Formulas assuming a large box and isotropic correlations in 3D:

$$
S_{k} & =1+N \delta_{k, 0}+\frac{4 \pi \rho}{k} \int_{0}^{\infty} d r \sin (k r)(g(r)-1) \\
g(r) & =1+\frac{1}{2 \pi^{2} \rho r} \int_{0}^{\infty} k d k \sin (k r)\left(S_{\vec{k}}-1\right)
$$

Formulas assuming a large box and isotropic correlations in 2D:

$$
S_{k} & =1+N \delta_{k, 0}+2 \pi \rho \int_{0}^{\infty} d r J_{0}(k r)(g(r)-1) \\
g(r) & =1+\frac{1}{2 \pi \rho} \int_{0}^{\infty} k d k J_{0}(k r)\left(S_{\vec{k}}-1\right)
$$
