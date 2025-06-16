# Verlet Integration

## 1. Liouville's Theorem

How does the probability distribution evolve?

Define \( \Gamma = (q, p) \) to be the phase space coordinate.

Probability is a conserved quantity, so:

$$
\frac{df}{dt} = 0
$$

This is analogous to:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0
$$

Apply the product rule and Hamilton’s equations:

$$
\frac{\partial f}{\partial t} + \sum_i \left( \frac{\partial f}{\partial q_i} \frac{\partial H}{\partial p_i} - \frac{\partial f}{\partial p_i} \frac{\partial H}{\partial q_i} \right) = 0
$$

Therefore:

$$
\frac{df}{dt} = 0
$$

This means **phase space is incompressible**.

**Liouville’s Theorem**: The phase-space distribution is constant along trajectories of the system.

Alternative form using **Poisson bracket**:

$$
\frac{df}{dt} = \{f, H\} = 0
$$

The Liouville operator is:

$$
\mathcal{L} = \{., H\}
$$

This operator is **Hermitian** (important property).

## 2. Propagators: Symplectic, Time Reversible

The phase-space trajectories follow from Hamilton’s equations and have a formal solution:

$$
\Gamma(t) = e^{t \mathcal{L}} \Gamma(0)
$$

The exponential of the operator is a **Taylor series** and acts as a **propagator**.

This propagator is:

- **Unitary**: \( e^{-t \mathcal{L}} = (e^{t \mathcal{L}})^{-1} \)
- **Volume-preserving**: Jacobian of transformation is identity
- **Symplectic**: Canonical transformation
- **Time reversible**

### Not all integrators are symplectic or reversible

#### Example: Explicit Euler

- \( x(t + \Delta t) = x(t) + \Delta t \cdot p(t) \)
- \( p(t + \Delta t) = p(t) + \Delta t \cdot f(x(t)) \)

Not symplectic or reversible.

## 3. Trotter Decomposition

Split the Liouville operator:

$$
\mathcal{L} = \mathcal{L}_1 + \mathcal{L}_2
$$

Where:

- \( \mathcal{L}_1 = \sum_i \frac{\partial H}{\partial p_i} \frac{\partial}{\partial q_i} \)
- \( \mathcal{L}_2 = -\sum_i \frac{\partial H}{\partial q_i} \frac{\partial}{\partial p_i} \)

In general, \( \mathcal{L}_1 \) and \( \mathcal{L}_2 \) do not commute.

Using **Trotter decomposition**:

$$
e^{(\mathcal{L}_1 + \mathcal{L}_2) \Delta t} \approx e^{\frac{1}{2} \mathcal{L}_1 \Delta t} e^{\mathcal{L}_2 \Delta t} e^{\frac{1}{2} \mathcal{L}_1 \Delta t} + \mathcal{O}(\Delta t^3)
$$

This gives a **single-step propagator**:

- **Symplectic**: Each sub-propagator is unitary
- **Reversible**: Symmetric operator sequence
Higher-order integrators exist but are more complex.

## 4. Velocity Verlet Algorithm

Apply Trotter decomposition to derive **Velocity Verlet**:

### Steps

1. **Half-step velocity update**:

   $$
   v(t + \frac{\Delta t}{2}) = v(t) + \frac{\Delta t}{2m} F(t)
   $$

2. **Full-step position update**:

   $$
   x(t + \Delta t) = x(t) + \Delta t \cdot v(t + \frac{\Delta t}{2})
   $$

3. **Half-step velocity update with new force**:

   $$
   v(t + \Delta t) = v(t + \frac{\Delta t}{2}) + \frac{\Delta t}{2m} F(t + \Delta t)
   $$

### Equivalent form

$$
x(t + \Delta t) = x(t) + \Delta t \cdot v(t) + \frac{\Delta t^2}{2m} F(t)
$$

- **Symplectic**
- **Time reversible**
- **Widely used in MD packages**

Other variants: basic Verlet, leapfrog — less convenient than Velocity Verlet.

## Additional resources

The 1992 paper by Tuckerman, Berne, and Martyna introduces a class of reversible molecular dynamics integrators based on the Trotter factorization of the Liouville propagator. These integrators, known as reversible reference system propagator algorithms (RESPA), are designed to efficiently simulate systems with multiple time scales or long-range interactions by separating fast and slow forces or motions. The authors derive several new integrators, including the velocity and position Verlet schemes, and demonstrate their superior stability and energy conservation compared to traditional methods. They show how these reversible integrators can be applied to systems with disparate masses, stiff oscillators in soft environments, and systems under constant temperature using Nosé dynamics. The paper emphasizes the advantages of time-reversibility for numerical stability and compatibility with hybrid Monte Carlo methods, and provides both theoretical foundations and practical implementation strategies, including FORTRAN code examples.
