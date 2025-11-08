# Langevin Dynamics

## Implicit-Solvent Models

An implicit-solvent model represents average solvent molecules using the idea of “effective potentials”.

In previous discussions, we defined the forcefield and captured all molecular interactions using a microcanonical ensemble (NVE). However, when switching to the practical canonical ensemble (NVT), the computational cost increases with the thermostat dynamics. Especially for a large system, simulating non-target solvent molecules is neither meaningful nor necessary.

Example: Simulate nanoparticles in a solvent.
If we use an explicit solvent model, our system looks like this.

```{figure} ./_figures/Explicit_solvent_model_example.png
:alt: Visualization of explicit solvent model with Au nanoparticles in water.
:width: 200px
:align: center
:name: explicit_solvent_model_example

Schematic of the visualization for a modeling of Au nanoparticles in water by explicit solvent model.

```

- While we need to define the detailed atomic arrangements in Au  Nanoparticles, we also need to model the structure of water molecules.

- The slowest part of an MD simulation is calculating the distances and forces of all particles. In this case, we need to calculate these parameters at each timestep for each NPs and water molecule. 

- Note that in an actual simulation, there will be more than the number of water molecules drawn in the schematic (approximately $10^6$ depending on the system).

An implicit solvent model treats solvent molecules as a “bath”, which transfers the molecular interactions to averaged, continuum effects with the frictional drag and stochastic force. 

- Frictional drag: Energy dissipation into the surrounding implicit solvent.

- Stochastic force: A random kick from the solvent that simulates the collisions of solvent molecules and keeps the system at constant temperature.

Example: Simulate nanoparticles in a solvent.
```{figure} ./_figures/Implicit_solvent_model_example.png
:alt: Visualization of implicit solvent model with Au nanoparticles in water.
:width: 200px
:align: center
:name: implicit_solvent_model_example

Schematic of the visualization for a modeling of Au nanoparticles in water by implicit solvent model.

```

- The system only contains the Au nanoparticles. But the frictional drag and stochastic force are added in the force term.

- The thermal bath can exchange heat with Au nanoparticles. Essentially, the Au nanoparticles can “feel” the solvent molecules.

## Langevin Dynamics

The bridge connecting the explicit molecular interactions with the implicit forces is called the Langevin dynamics, as the “thermal bath” above.

## Fluctuation-dissipation theorem

“When there is a process that dissipates energy, turning into heat, then there is a reverse process related to thermal fluctuations.”

Example: 
- The Au nanoparticles experience the drag (fluid resistance) from solvent molecules. Then, the drag dissipates kinetic energy, turning it into heat. (Kinetic energy to heat)
- Conversely, the Au nanoparticles move around with a change in velocity when molecules collide based on the Brownian motion. (Heat to kinetic energy)

Conceptually, Langevin dynamics can be split into 2 parts:
- Thermodynamics: Random thermal noise and dissipative processes (friction, damping) are not independent. Balancing the energy distribution ensures constant T.
- Dynamics: Drag force from viscous friction is balanced with thermal kicks in damping. Allow the simulation of Brownian motion.

## Langevin Equation
Mathematically, the Langevin dynamics can be defined in the same logic.

- Balancing the stochastic thermal noise with the viscous drag modify the momentum of the system.

**Langevin Equation**
$$
mdv = \big(F(x) - \gamma v\big)\,dt + \sigma\,dW_t
$$

$F(x)$: Conservative forces originate from the system, such as intermolecular potentials.
$\gamma$: Friction coefficient, $$ represents the viscous drag force.
$\sigma$: Strength of fluctuations, $$ represents the stochastic thermal force.
$W_t$ is the Wiener process, which is the cumulative Brownian random motion. $d W_t$ is the Wiener increment as the infinitesimal step of the Brownian motion with $\langle dW_t \rangle = 0, \,\,\langle dW_t^2 \rangle = dt$.

- To show the conservation of T for the canonical ensemble can be realized by linking thermal fluctuation and viscous drag, Itô’s lemma is used to capture the stochastic relationship.

$$
mdv = \big(F(x) - \gamma v\big)\,dt + \sigma\,dW_t \,\, \rightarrow \,\, dv = A(v,t) \,dt + B(v, t) \, dW_t
$$

Similar to the transformation of thermodynamic variables, for a given function $f = f(v, t)$, it can be expressed with the above equation.

$$
df = \frac{\partial f}{\partial t}\, dt + \frac{\partial f}{\partial v}\, dv \,\, \rightarrow \,\, df = f_t \, dt + f_v \, dv
$$

As $\langle dW_t \rangle = 0, \,\, \langle dW_t^2 \rangle = dt$, substituting $dv$ with $A(v,t) \,dt + B(v, t) \, dW_t$. Since $d W_t$ is a stochastic term, it is expanded and considered up to 2nd order.

$$
df = f_t \, dt + f_v \, dv + \frac{1}{2} f_{vv} \, (dv)^2 =f_t \, dt + f_v \, (A(v,t) \,dt + B(v, t) \, dW_t) + f_{vv} \, (A(v,t) \,dt + B(v, t) \, dW_t)^2
$$

Using Itô’s lemma, $(dt)^2 = 0,\, dt dW_t = 0, \, (d W_t)^2 = dt$.

$$
df = (f_t + A f_v + \frac{1}{2} B^2 f_{vv}) \ dt + B f_v \, dW_t
$$

The first part $(f_t + A f_v + \frac{1}{2} B^2 f_{vv}) \ dt$ describes the drift of the function $f(v, t)$, and the second part $B f_v \, dW_t$ describes the random fluctuations. Taking the average using Itô’s lemma, we identify the relationship with the stochastic term average to 0.

$$
\frac{d}{dt} \langle f \rangle = \langle A f_v + \frac{1}{2} B^2 f_{vv} \rangle
$$

To investigate thermal equilibrium, $f(v, t)$ can be set as the kinetic energy and say $f \propto v^2$. Since $$ only describes the potential energy, it will not be included in the discussion of kinetic energy dissipation and injection. With $A(v,t) = \frac{F(x)}{m} - \frac{\gamma}{m}v, \, \, B(v,t) = \frac{\sigma}{m}$.

$$
\frac{d}{dt} \langle v^2 \rangle  = - \frac{2 \gamma}{m} \langle v^2 \rangle + \frac{\sigma^2}{m^2}
$$

At constant temperature, the Maxwell-Boltzmann distribution suggests that the velocity variance is no longer changed.

$$
0  = - \frac{2 \gamma}{m} \langle v^2 \rangle + \frac{\sigma^2}{m^2} \,\, \rightarrow \,\, \langle v^2 \rangle = \frac{\sigma^2}{2m\gamma}
$$

From thermodynamics, the average kinetic energy per degree of freedom is:

$$
\frac{1}{2} m \langle v^2 \rangle = \frac{1}{2} k_B T \,\, \rightarrow \,\, \frac{1}{2} m (\frac{\sigma^2}{2m\gamma}) = \frac{1}{2} k_B T
$$

**Fluctuation-dissipation relation**
$$
\sigma^2 = 2\gamma k_B T
$$

Therefore, the strength of fluctuations $\sigma$ is dependent on the friction coefficient $\gamma$ under this stochastic process. Intuitively, large friction between molecules requires larger thermal fluctuations to maintain the same T.

This coupling verifies that the Langevin dynamics is a valid thermostat, which maintains the correct thermal distribution.

To integrate the Langevin dynamics, one way is to add the viscous drag and thermal fluctuation directly to the Velocity Verlet algorithm.

**Example: Velocity Verlet**

1. Half-step velocity update:

$$
v\!\left(t+\frac{\Delta t}{2}\right)
= v(t) + \frac{\Delta t}{2m} F(t) \,\, \rightarrow \,\, v\!\left(t+\frac{\Delta t}{2}\right)
= v(t) + \frac{\Delta t}{2m} F(t)
- \frac{\gamma \Delta t}{2}v(t)
+ \frac{\sigma}{2m}G_1\sqrt{\Delta t}
$$

2. Full-step position update, note that the velocity includes drag and noise:

$$
x(t+\Delta t)
= x(t) + \Delta t \, v\!\left(t+\frac{\Delta t}{2}\right)
$$

3. Half-step velocity update:

$$
v(t+\Delta t)
= v\!\left(t+\frac{\Delta t}{2}\right)
+ \frac{\Delta t}{2m} F(t+\Delta t)
\,\, \rightarrow \,\,
v(t+\Delta t)
= v\!\left(t+\frac{\Delta t}{2}\right)
+ \frac{\Delta t}{2m} F(t+\Delta t)
- \frac{\gamma \Delta t}{2}v\!\left(t+\frac{\Delta t}{2}\right)
+ \frac{\sigma}{2m}G_2\sqrt{\Delta t}
$$

Note that $G_1 G_2$ are random standardized Gaussian variables, they represent the thermal noise and are independent of each other so $\langle G_1 G_2\rangle = 0$.

However, to retain symplectic properties, sophisticated schemes are highly recommended (BAOAB, G-JF).

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

## References
