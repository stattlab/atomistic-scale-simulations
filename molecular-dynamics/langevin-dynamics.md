# Langevin Dynamics

## Implicit-Solvent Models

Sometimes, it's too expensive to simulate all the solvent around a large solute like a nanoparticle or protein.

- Treat effects "implicitly"

## Langevin Dynamics

- Thermodynamics → (effective potential)
- Dynamics → drag forces, thermal "kicks"

**Momentum equation:**
P = mv = { -rx + ow }
T = 2βkT by fluctuation-dissipation theorem

- Conservative drag force
- Force: "free drawing" — Conua around a sphere
- Properly, W is a Wiener process and is not well defined
  - dw = w w(o) = at G
  - Gaussian with zero mean, unit variance, independent for each particle
  - "White noise": uncorrelated in time (vs. colored noise)

**Langevin Equation:**
mdv = (f - xv) dt + σ dw

To integrate, some people just add drag and random forces to normal Verlet integration. However, more sophisticated schemes (BAOAB, G-JF) are recommended to retain symplectic properties.

**Example: BAOAB Scheme**

- Δx(1/2) = p(0) + (Δt/2m) f(0)
- p(Δt/2) = p(0) + (Δt/2) f
- p(Δt/2) = exp(-γΔt/2) p(Δt/2) + √(1 - exp(-2γΔt)) √(mkT) G
- x(Δt) = x(Δt/2) + (Δt/2m) p'(Δt/2)
- p(Δt) = p'(Δt/2) + (Δt/2) f(Δt)

## Brownian Dynamics

In the "overdamped" limit, friction dominates inertia so p ≈ 0 and:

**Equation:**
dx = f dt + σ dw

It can be shown that the update rule is:
x(Δt) = x(0) + (f(0)/γ) Δt + √(2kT/γ) Δt G

By the Einstein relation, we can define a diffusion coefficient:
D = kT / γ

If f = 0,
⟨Δx²⟩ = 2DΔt
⟨G_i G_j⟩ = 2DΔt δ_ij

## Hydrodynamic Interactions in BD

Previous equations used free drainage. In real systems, hydrodynamics give rise to drag forces induced by flows from other particles.

From Ermak and McCammon, *J. Chem. Phys.*, 69, 1352 (1978):

**Equation:**
x(Δt) = x(0) + (M·f + kT ∇·M) Δt + B

- M: mobility tensor, D = kBT M (3N × 3N)
- B: random displacements
- ⟨B Bᵀ⟩ = 2kT M Δt

M captures hydrodynamics, e.g., pairwise approximation:
M = [M₁₁ M₁₂ ... M₁N]
    [M₂₁ M₂₂ ... M₂N]
    [...]
    [MN₁ MN₂ ... MNN]

**Free drawing:**

- M_ij = 0
- Rotne-Prager: M_ij ≠ 0

Both these tensors are divergence-free (i.e., ∇·M = 0), so this term can be ignored.
Not true if there are walls, etc.

- Drawing B is hard! Need to draw with appropriate covariance matrix, which involves a square root. This places some numerical restrictions.
- Tensors can be long-ranged → need Ewald sums
  - Positively Split Ewald technique [Fiore et al., *J. Chem. Phys.*, 146, 12416 (2019)]

## Langevin Thermostat

By making γ small, can use Langevin Dynamics as a thermostat without significantly perturbing the system.

- A value γ ≈ 0.1 m/Å is usually considered "weak" coupling and good for thermostating.
- Beware: Langevin thermostat does not conserve momentum (forces do not sum to zero). Hence, there are no zero degrees of freedom.
- Hydrodynamics of an explicit solvent with Langevin thermostat may also get screened due to lack of momentum conservation.

## Additional Resorces
