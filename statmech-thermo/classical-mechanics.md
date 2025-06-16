# Classical Mechanics

## Newtonian Mechanics

Newton's second law:

$$
F = ma = m \ddot{x}
$$

Everything is expressed in terms of force, but:

- Hard to use in non-Cartesian coordinates
- Difficult when there are constraints (which become forces)

In **generalized coordinates**, forces are generally conservative (derived from a potential \( U(q) \)).

This approach works with **energy** (scalars) instead of vectors.

## Lagrangian Mechanics

**Classical Lagrangian**:

$$
\mathcal{L}(x, \dot{x}) = K - U
$$

Where:

- \( K \): kinetic energy
- \( U \): potential energy

The **action** is defined as:

$$
S = \int_{t_1}^{t_2} \mathcal{L}(x, \dot{x}) \, dt
$$

- \( S \) is a **functional**: it depends on the trajectory \( x(t) \) from \( t_1 \) to \( t_2 \)

**Principle of stationary action**: The equations of motion correspond to stationary points of \( S \)

## Euler–Lagrange Equation

To find the stationary point of the action:

$$
\frac{d}{d\epsilon} S[x + \epsilon \eta] \bigg|_{\epsilon=0} = 0
$$

This leads to the **Euler–Lagrange equation**:

$$
\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) - \frac{\partial \mathcal{L}}{\partial x} = 0
$$

Example:

If \( \mathcal{L} = \frac{1}{2} m \dot{x}^2 - U(x) \), then:

$$
\frac{d}{dt}(m \dot{x}) = -\frac{dU}{dx} \Rightarrow F = ma
$$

## Hamiltonian Mechanics

The Euler–Lagrange equation is a second-order differential equation. Can we simplify?

The Lagrangian uses coordinates \( (x, \dot{x}) \). What if we switch to **momentum coordinates** \( (x, p) \), where:

$$
p = \frac{\partial \mathcal{L}}{\partial \dot{x}}
$$

We use a **Legendre transform** to define the **Hamiltonian**:

$$
\mathcal{H}(x, p) = p \dot{x} - \mathcal{L}(x, \dot{x}(p))
$$

### Hamilton's Equations

From the total differential:

$$
d\mathcal{H} = \frac{\partial \mathcal{H}}{\partial x} dx + \frac{\partial \mathcal{H}}{\partial p} dp + \frac{\partial \mathcal{H}}{\partial t} dt
$$

We derive:

$$
\dot{x} = \frac{\partial \mathcal{H}}{\partial p}, \quad \dot{p} = -\frac{\partial \mathcal{H}}{\partial x}
$$

This is a system of **first-order differential equations** with elegant symmetry.

## 5. Energy and Motivation

The classical Hamiltonian is:

$$
\mathcal{H} = \frac{p^2}{2m} + U(x)
$$

Which is the **total energy**:

$$
\mathcal{H} = K + U
$$

Hamilton’s equations reproduce Newtonian mechanics.

## Why Use Hamiltonian Mechanics?

- Needed to analyze **time integrators**
- Leads to **Liouville’s theorem** (coming soon)
