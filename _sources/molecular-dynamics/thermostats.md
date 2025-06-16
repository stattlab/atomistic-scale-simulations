# Thermostats

## 1. Generating Canonical Ensemble in MD

Molecular dynamics (MD) naturally gives the **NVE ensemble**. To obtain the **NVT ensemble**, apply a **thermostat** (heat reservoir) that drives the system to the correct temperature.

### Stochastic Thermostats

- **Andersen**: At random intervals, assign new momenta to particles.
  - ❌ Not momentum conserving.
- **Lowe-Andersen**: Pairwise stochastic velocity changes.
  - ✅ Momentum conserving.
- **Langevin**: Add deterministic friction and random forces.
  - ❌ Not momentum conserving.
- **DPD (Dissipative Particle Dynamics)**: Pairwise friction and random forces.
  - ✅ Momentum conserving.

> ✅ Random thermostats are usually stable.
> ⚠️ They add computational cost due to random number generation.
> ⚠️ Must tune friction strength carefully to avoid distorting dynamics.

### Deterministic Thermostats

- Add a scaling variable acting as a controller.
  - **Isokinetic**: Constant kinetic energy.
  - **Berendsen**: Weak velocity rescaling.
  - **Nosé / Nosé-Hoover / Nosé-Hoover chains**: Canonical (sometimes).

## 2. Isokinetic Thermostat: Constant Kinetic Energy

Use a Lagrange multiplier to constrain kinetic energy:

$$
K = \frac{p^2}{2m} = \text{constant}
$$

Differentiating:

$$
\frac{dK}{dt} = \frac{p \cdot f}{m} = 0
$$

This leads to:

$$
f = \lambda p
$$

The resulting ensemble has probability:

$$
P \propto \delta(K(p) - K_0) \cdot e^{-\beta U(q)}
$$

> ⚠️ Not canonical, but for large systems, it's a good approximation.
> ✅ Configurations have correct distribution.

Can also use velocity rescaling:

$$
p \leftarrow \alpha p, \quad \alpha = \sqrt{\frac{T_0}{T}}
$$

> ⚠️ Discontinuous, but useful for initial equilibration.

## 3. Berendsen Thermostat: Proportional Control

Control temperature via exponential relaxation:

$$
\frac{dT}{dt} = -\gamma (T - T_0)
$$

Velocity rescaling:

$$
p \leftarrow \lambda p, \quad \lambda = \sqrt{1 + \frac{\Delta t}{\tau} \left( \frac{T_0}{T} - 1 \right)}
$$

> ⚠️ Not canonical.
> ✅ Useful for steering system to target temperature.

## 4. Nosé–Hoover Thermostat

Nosé introduced an **extended Hamiltonian**:

$$
\mathcal{H} = \sum \frac{p^2}{2ms^2} + U(q) + \frac{p_s^2}{2Q} + gk_BT \ln s
$$

- \( s \): scaling variable
- \( Q \): thermal mass
- \( g = 3N - 3 \): degrees of freedom

Equations of motion:

$$
\dot{q} = \frac{p}{ms^2}, \quad \dot{p} = f - \frac{p_s}{Q} p, \quad \dot{s} = \frac{p_s}{Q}, \quad \dot{p_s} = \sum \frac{p^2}{ms^3} - gk_BT
$$

> ✅ Extended system is microcanonical
> ✅ Subsystem (q, p) is canonical

Hoover reformulated to avoid time scaling:

$$
\dot{q} = \frac{p}{m}, \quad \dot{p} = f - \zeta p, \quad \dot{\zeta} = \frac{1}{Q} \left( \frac{p^2}{m} - gk_BT \right)
$$

- Generates canonical distribution if ergodic
- Conserves extended energy:

$$
\mathcal{H} = K + U + \frac{Q\zeta^2}{2} + gk_BT \eta
$$

Choose \( Q \) carefully:

$$
Q \sim gk_BT \tau^2
$$

## 5. Nosé–Hoover Chains

Single Nosé–Hoover thermostat may not be ergodic (e.g., harmonic oscillator).

Solution: Add a chain of thermostat variables:

$$
\dot{\zeta}_1 = \frac{1}{Q_1} \left( \frac{p^2}{m} - gk_BT \right), \quad \dot{\zeta}_2 = \frac{1}{Q_2} \left( Q_1 \zeta_1^2 - k_BT \right), \dots
$$

- Improves ergodicity
- Commonly used in modern MD simulations

## 6. Implementation via Operator Splitting

Nosé–Hoover thermostat can be implemented using **operator splitting**:

Split Liouville operator:

$$
e^{\mathcal{L} \Delta t} \approx e^{\mathcal{L}_1 \Delta t/2} e^{\mathcal{L}_2 \Delta t} e^{\mathcal{L}_1 \Delta t/2}
$$

- \(\mathcal{L}_1\): thermostat part
- \(\mathcal{L}_2\): velocity Verlet

Further split thermostat operator for accuracy:

- Use multiple substeps
- See: Martyna et al., Mol. Phys. 87, 1117 (1996)

## Additional Resources

1. Tuckerman et al. (2006) – J. Phys. A: Math. Gen.
This paper presents a novel, measure-preserving, reversible geometric integrator for molecular dynamics simulations in the isothermal–isobaric (NPT) ensemble. The authors develop the integrator using a Liouville-operator-based formalism that ensures phase-space volume conservation, even in non-Hamiltonian systems. They extend the method to handle multiple time scales via r-RESPA and validate it through analytical derivations and numerical simulations, including Lennard-Jones fluids and flexible diatomic molecules. The integrator is shown to outperform previous schemes in stability and accuracy, particularly in preserving the correct ensemble distribution. The work concludes with suggestions for future extensions, including flexible cell dynamics and alternative thermal control methods.

2. Martyna et al. (1996) – Mol. Phys.
This comprehensive study introduces explicit, reversible integrators for extended system dynamics in molecular simulations, targeting canonical (NVT) and isothermal–isobaric (NPT) ensembles. The integrators are derived from the Liouville operator formalism and are designed to be efficient, stable, and suitable for large-scale simulations. The paper details the integration schemes for various ensembles, including full cell fluctuations, and incorporates multiple time step strategies (RESPA) to handle systems with disparate time scales. The authors compare their methods with standard iterative velocity-Verlet schemes and demonstrate improved energy conservation and computational efficiency. The work includes practical implementation guidance, including Fortran code and constraint-handling techniques, making it a foundational reference for molecular dynamics practitioners.

3. Martyna et al. (1992) – J. Chem. Phys.
This seminal paper introduces the Nosé–Hoover chain (NHC) method, a significant advancement in molecular dynamics for generating the canonical ensemble. The authors address the non-ergodicity of traditional Nosé–Hoover dynamics in small or stiff systems by coupling a chain of thermostat variables to the system. They provide a rigorous theoretical foundation, including derivations of the equations of motion, stability analysis, and proofs of phase-space volume conservation. Numerical experiments confirm that NHC dynamics yield accurate canonical distributions and are more robust than previous methods. The paper also discusses practical aspects such as thermostat mass selection, Lyapunov exponent analysis, and efficiency comparisons with Monte Carlo methods, establishing NHC as a reliable tool for simulating thermodynamic ensembles.
