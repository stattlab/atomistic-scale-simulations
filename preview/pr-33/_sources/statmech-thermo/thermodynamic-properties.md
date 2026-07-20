# Thermodyanmics Properties

## Classical Systems

Classical systems have continuous positions and momenta, so sums become integrals:

$$
Q(T, V, N) = \frac{1}{N! h^{3N}} \int d^{3N}q \, d^{3N}p \, e^{-\beta H(q, p)}
$$

- *Indistinguishable particles*
- Prefactor to account for quantum entropy in high T limit where particles are exchanged and are the same.

For classical systems, \( H(q, p) = U(q) + K(p) \) is separable:

- \( U(q) \): potential energy
- \( K(p) = \sum \frac{p^2}{2m} \): kinetic energy

Hence, \( Q \) is separable:

$$
Q(T, V, N) = \frac{1}{N! h^{3N}} \int d^{3N}q \, e^{-\beta U(q)} \int d^{3N}p \, e^{-\beta K(p)}
$$

- Configuration integral:

$$
Z(T, V, N) = \int d^{3N}q \, e^{-\beta U(q)}
$$

- Thermal de Broglie wavelength:

$$
\Lambda = \left( \frac{h^2}{2\pi m k_B T} \right)^{1/2}
$$

Example: Ideal gas \( U(q) = 0 \), so

$$
Z = V^N, \quad Q = \frac{V^N}{N! \Lambda^{3N}}
$$
Free energy:

$$
\beta A = -\ln Q = -\ln \left( \frac{V^N}{N! \Lambda^{3N}} \right) = N \ln \left( \frac{\Lambda^3}{V} \right) + N
$$

## Probability Distributions

Probability density functions are also separable:

$$
f(q, p) = \frac{1}{Q} e^{-\beta H(q, p)} = \frac{1}{Z} e^{-\beta U(q)} \cdot \frac{1}{K} e^{-\beta K(p)}
$$

- Marginal distributions:
  - Maxwell-Boltzmann distribution:

$$
f(p_i) = \left( \frac{\beta}{2\pi m} \right)^{1/2} e^{-\beta p_i^2 / 2m}
$$
Each momentum component is independently Gaussian distributed. The variance increases with temperature.

## Temperature

Using the distribution of \( p \), we can find the average kinetic energy:

$$
\langle K \rangle = \int d^{3N}p \, K(p) f(p) = \frac{3N}{2} k_B T
$$
In the canonical ensemble, \( T \) is fixed but \( K \) fluctuates. We define a "kinetic" temperature:

$$
T = \frac{2 \langle K \rangle}{3N k_B}
$$

In practice, some momenta are constrained. For example, if linear momentum is conserved, only \( N - 1 \) momenta are true variables. So we define:

$$
T = \frac{2 \langle K \rangle}{N_{\text{DOF}} k_B}
$$

Most common form: \( N_{\text{DOF}} = 3(N - 1) \) for linear momentum conservation.

## Pressure

The pressure can be computed from \( Q \):

$$
\beta P = \left( \frac{\partial \ln Q}{\partial V} \right)_{T, N}
$$
Be careful: the integration limits of \( Q \) depend on \( V \)!

Scale the coordinates as \( q' = q / V^{1/3} \), then:

$$
Q = \frac{1}{N! \Lambda^{3N}} V^N \int d^{3N}q' \, e^{-\beta U(V^{1/3} q')}
$$

## Chemical Potential

Also from \( Q \):

$$
\beta \mu = -\left( \frac{\partial \ln Q}{\partial N} \right)_{T, V}
$$

Or:

$$
\mu = -k_B T \ln \left( \frac{Q(N+1)}{Q(N)} \right)
$$
Example:

$$
\mu = -k_B T \ln \left( \frac{V}{(N+1) \Lambda^3} \right)
$$

- Excess chemical potential:

$$
\mu^{\text{ex}} = -k_B T \ln \left\langle e^{-\beta \Delta U} \right\rangle
$$
Where \( \Delta U \) is the energy of a test particle inserted at a random position in the existing ensemble.

> Note: Insertion can fail in dense systems. Methods like thermodynamic integration, fractional insertion, and Bennett’s acceptance ratio can help.

> Note: Defining by deletion (rather than insertion) usually does not work. Pathological case: hard spheres.
