# Thermostats

## 1. Generating Canonical Ensemble in MD

The basic MD ensemble is constant energy and constant volume. However, experimentally it is usually more convenient to specify the pressure and temperature. In those variables the phase of the system is unique except precisely at a phase transition. If we input the number of particles and volume near a phase boundary, then it is possible we will be in the two phase region, for example we could have a mixture of ice and water. This is unlikely to occur in a simulation because our system is usually so small. The interface between the two phases would cost too much energy and inhibits the system from moving freely from one phase to the other. Temperature controls and pressure controls allow one to do such simulations more directly.

Molecular dynamics (MD) naturally gives the **NVE ensemble**. To obtain the **NVT ensemble**, apply a **thermostat** (heat reservoir) that drives the system to the correct temperature.

The disadvantage of all thermostatting methods for working at constant temperature is that the dynamics is changed in an artificial way and dynamics is the reason why we do MD and not MC. Real dynamics obey the rules of special relativity (in principle). Effects need to be mediated by the transport of particles since we don't have any photons. Heat is transported at the speed of sound or slower. But if there is a kinetic energy fluctuation, the effect on the other particles with the various temperature thermostats is immediate. All three methods have a coupling constant (e.g. the frequency of rescaling, the friction coefficient or the mass of the N-H variable.) It should be chosen as small possible to alter the dynamics as little as possible. If this is done, the non-physical effects will be order $1/N$ in general. If this is a problem one should use a more physical method to control temperature fluctuations, for example put in a real heat bath at the edge of the physical system. Extremely accurate estimations of dyanmical quantites like the diffusion constants or other transport coefficients should be done in the **NVE** if possible. Often, it is useful to first equilibrate with **NVT**, and then switch to **NVE** for production runs in these cases.

### Stochastic Thermostats

We want to do simulations at constant temperature. How do we do it?

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

The simplest method is to start the simulation with random velocities. If the system is ergodic, the only thing that matters is the total energy. One could give all the extra energy to a single particle and the energy would cascade down to all the particles, and the velocity would have a normal distribution after a few collisions. But to minimize simulation time, you want to start as close as possible to the final true distribution, a normal distribution. In the **constant kinetic energy** or **velocity rescaling method**, every so often one re-scales the velocity, multiplying by a constant chosen so that the kinetic energy is $3/2K T$ per particle. Once the system reaches equilibrium, the scaling is no longer necessary.

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

An approach pioneered in 1984 by Nose adds a single heat bath particle. A new variable with the dimensions of a friction constant is added to the system. This approach gives reversible deterministic dynamics and if the system is ergodic we will be guaranteed to go to the canonical distribution. The approach of adding a new fictitious particle is very common trick in simulation.

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

## Pressure Controls

Pressure controls can be introduced in a similar fashion. The conjugate variable to the pressure is the size of the box, then one can simulate the isothermal–isobaric **NPT ensemble** . Anderson, Parrinello and Rahman (1980-84) introduced a formalism where the size of the box is a dynamical variable. When the box size fluctuates (because the pressure from the virial is not equal to the desired pressure) all the particle positions dilate or contract. In some methods, the box shape also fluctuates; it is allowed to become an arbitrary parallelpiped. Then the system can switch between different crystal structures by itself (for example between FCC and BCC). This method is very useful is studying the transitions between two different crystal phases or the equilibrium lattice constants of different crystals.

Again the dynamics is unrealistic. In addition the size effects can be larger than in a cubic box because fluctuations in the size make the box narrower in some directions. Remember that just because a system can fluctuate from one structure to another does not mean than the probability is high for that to happen.

## References

- [LAMMPS Nose-Hoover thermostat documentation](https://docs.lammps.org/fix_nh.html)
- [HOOMD-blue thermostat documentation](https://hoomd-blue.readthedocs.io/en/stable/hoomd/md/methods/module-thermostats.html)
- [GROMACS thermostat documentation](https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html#temperature-coupling)

- Tuckerman, Mark E., et al. "A Liouville-operator derived measure-preserving integrator for molecular dynamics simulations in the isothermal–isobaric ensemble." Journal of Physics A: Mathematical and General 39.19 (2006): 5629. {cite}`tuckerman2006liouville`

- Tuckerman, Mark E., and Glenn J. Martyna. "Understanding modern molecular dynamics: Techniques and applications." The Journal of Physical Chemistry B 104.2 (2000): 159-178 {cite}`tuckerman2000understanding`

- Martyna, Glenn J., Douglas J. Tobias, and Michael L. Klein. "Constant pressure molecular dynamics algorithms." J. chem. Phys 101.4177 (1994): 10-1063. {cite}`martyna1994constant`

-  Parrinello and Rahman, J Appl Phys, 52, 7182 (1981).{cite}`parrinello1981polymorphic`
