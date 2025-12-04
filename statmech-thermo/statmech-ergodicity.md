# Statistical Mechanics: Ensembles, Ergodicity, and Other Stuff

The physical foundation of molecular simulations is *statistical mechanics*. Without it, it would be impossible to connect small systems (at most $10^3$--$10^7$ particles, simulated for nanoseconds to microseconds) to macroscopic thermodynamic quantities like pressure, temperature, or heat capacities that we measure in the lab. Statistical mechanics provides the bridge between:

* **Microscopic variables:** positions and momenta of all particles in a simulation box.
* **Macroscopic variables:** $N$, $V$, $E$, $T$, $p$, $\mu$, etc.

In simulations we always control a small, model system, often with periodic boundary conditions, and ask: *If we sample microscopic states in the right ensemble, can we recover correct thermodynamic averages?* In other words, can we use a few hundred or thousand atoms as a faithful representative of a macroscopic material containing Avogadro's number of atoms?

## Microstates, macrostates, and phase space

Consider a classical system of $N$ particles. The complete microscopic state is specified by all positions and all momenta:

$$
\Gamma = (\underbrace{\mathbf{r}_1,\dots,\mathbf{r}_N}_{3N\ \text{coordinates}};\, \underbrace{\mathbf{p}_1,\dots,\mathbf{p}_N}_{3N\ \text{momenta}}),
$$

so the phase space has dimension $6N$. A single point $\Gamma$ in this phase space is a **microstate**.

A **macrostate** is defined by a few thermodynamic constraints, e.g.

$$
(N,V,E) \quad \text{or} \quad (N,V,T), \quad \text{etc.}
$$

Many different microstates $\Gamma$ are compatible with the same macrostate. For example, keeping $(N,V,E)$ fixed, we can rearrange particles and redistribute momenta in many ways while keeping the total energy unchanged. All such microstates belong to the same *ensemble*.

#### Example: gas in a box
Imagine $N$ argon atoms in a cubic box of volume $V$ with perfectly reflecting walls. Specifying the total energy $E$ and the number of atoms $N$ defines a macrostate $(N,V,E)$. One microstate might have half the atoms on the left side and half on the right; another microstate might have a different spatial arrangement and momentum distribution, but as long as the total energy is $E$, both microstates correspond to the same macrostate.

#### Ensemble
An ensemble is a (conceptual) collection of all microstates consistent with a specified set of macroscopic constraints (e.g. fixed $N$, $V$, $E$ in the microcanonical ensemble). In a simulation, we aim to *sample* microstates from the correct ensemble, either by deterministic dynamics (MD) or stochastic algorithms (Monte Carlo, Langevin, etc.). The ensemble perspective is powerful because it allows us to replace complicated, history-dependent dynamics by simpler probabilistic descriptions.

## Density of states, entropy, and temperature

For a system with fixed $N$ and $V$, the **density of states** (or number of states) at energy $E$ is usually denoted by $\Omega(E)$:

$$
\Omega(E) \equiv \sum_{\Gamma} \delta\bigl(E(\Gamma) - E\bigr),
$$

where the sum is over all microstates $\Gamma$ and $\delta$ is a Dirac delta (or a Kronecker delta for discrete spectra). In words, $\Omega(E)$ counts how many microstates have total energy $E$.

The **microcanonical entropy** is then defined as

$$
S(E,N,V) = k_{\mathrm{B}} \ln \Omega(E,N,V),
$$

where $k_{\mathrm{B}}$ is Boltzmann's constant. From this, the **temperature** $T$ follows as

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{N,V}.
$$

Intuitively:
* $\Omega(E)$ measures *how many* microstates are compatible with the macroscopic constraints.
* $S(E)$ measures *how much uncertainty* we have about the microscopic configuration if we only know $E$, $N$, and $V$.

#### Example: ideal gas (very briefly)
For a monatomic ideal gas, $\Omega(E)$ can be computed analytically and grows roughly like $E^{3N/2}$. Plugging this into $S(E) = k_{\mathrm{B}}\ln\Omega(E)$ and differentiating with respect to $E$ directly gives the familiar relation

$$
U = \langle E \rangle = \frac{3}{2} N k_{\mathrm{B}} T,
$$

which is the equipartition result for an ideal gas.

## The microcanonical (NVE) ensemble

The simplest ensemble, and the easiest one to simulate, is the microcanonical or NVE ensemble:

$$
N = \text{const}, \quad V = \text{const}, \quad E = \text{const}.
$$

Think of an isolated system: fixed number of particles, fixed volume, and fixed energy. At thermodynamic equilibrium, *all accessible microstates with the same total energy are (assumed to be) equally likely*. This is the fundamental postulate of the microcanonical ensemble.

Mathematically, the microcanonical partition function (often denoted $\Omega$) is

$$
\Omega(E,N,V) = \sum_{\Gamma} \delta\bigl(E(\Gamma) - E\bigr),
$$

and the probability of a microstate $\Gamma$ is

$$
P(\Gamma) = 
\begin{cases}
  \dfrac{1}{\Omega(E,N,V)}, & \text{if } E(\Gamma) = E,\\[6pt]
  0, & \text{otherwise}.
\end{cases}
$$

An ensemble average of an observable $A(\Gamma)$ is then

$$
\langle A \rangle_{\mathrm{NVE}} 
= \frac{1}{\Omega(E,N,V)}\sum_{\Gamma} A(\Gamma)\,\delta\bigl(E(\Gamma) - E\bigr).
$$

In molecular dynamics, a pure NVE simulation corresponds to integrating Newton’s equations of motion with no thermostat or barostat, so that total energy is (up to numerical error) conserved.

#### Example: NVE MD of a Lennard--Jones fluid
A standard textbook example is a box of particles interacting via the Lennard--Jones potential. After an initial equilibration, one can switch to an NVE run and monitor the total energy $E = K + U$:
* The kinetic energy $K$ and potential energy $U$ fluctuate in time.
* The *sum* $E$ remains constant, showing that the dynamics stays on the constant-energy surface in phase space.
* Time averages of observables (pressure, structure factor, etc.) estimate microcanonical ensemble averages.

## The canonical (NVT) ensemble and the partition function

Most real systems are not isolated; they are in contact with a *heat bath* that can exchange energy, but not particles, with the system. This motivates the canonical (NVT) ensemble:

$$
N = \text{const}, \quad V = \text{const}, \quad T = \text{const}.
$$

Consider a small system (our simulation box) weakly coupled to a large heat bath. If the total energy is $E_{\mathrm{tot}} = E_{\mathrm{sys}} + E_{\mathrm{bath}}$, then the probability that the system is in a microstate $i$ with energy $E_i$ is proportional to the number of bath states compatible with $E_{\mathrm{bath}} = E_{\mathrm{tot}} - E_i$. Maximizing the total entropy of system + bath leads to the **Boltzmann distribution**:

$$
P_i = \frac{\exp(-\beta E_i)}{Z},
$$

where

$$
\beta = \frac{1}{k_{\mathrm{B}}T}, 
\qquad 
Z = \sum_{i} \exp(-\beta E_i)
$$

is the **canonical partition function**.

The partition function $Z$ plays several roles:

* It is a *normalization constant*:
    $$
    \sum_i P_i = 1.
    $$
* It encodes the density of states and the Boltzmann weights of all microstates.
* From $Z$, one can compute almost all thermodynamic properties.

For an observable $A$ that takes the value $A_i$ in microstate $i$, the canonical ensemble average is

$$
\langle A \rangle_{\mathrm{NVT}}
= \sum_{i} P_i A_i
= \frac{1}{Z}\sum_{i} A_i \exp(-\beta E_i).
$$

It is often more convenient to work with the **Helmholtz free energy**

$$
F(N,V,T) = -k_{\mathrm{B}} T \ln Z,
$$

which is an *extensive* quantity (scales with system size) and is directly related to $Z$. Thermodynamic quantities follow from derivatives of $F$, e.g.

$$
\begin{aligned}
p &= -\left(\frac{\partial F}{\partial V}\right)_{N,T},\\
S &= -\left(\frac{\partial F}{\partial T}\right)_{N,V},\\
\mu &= \left(\frac{\partial F}{\partial N}\right)_{V,T}.
\end{aligned}
$$

#### Example: ideal gas in the canonical ensemble
For a monatomic ideal gas of identical particles with mass $m$, the canonical partition function factorizes into momentum and configuration parts. One finds

$$
Z_{\text{ideal}}(N,V,T)
= \frac{1}{N!}\left(\frac{V}{\Lambda^3}\right)^N,
\qquad
\Lambda = \frac{h}{\sqrt{2\pi m k_{\mathrm{B}}T}}
$$

where $\Lambda$ is the thermal de~Broglie wavelength. From this:

$$
\begin{aligned}
F &= -k_{\mathrm{B}}T \ln Z_{\text{ideal}}
  = -Nk_{\mathrm{B}}T \left[\ln\left(\frac{V}{N\Lambda^3}\right) + 1\right],\\
p &= -\left(\frac{\partial F}{\partial V}\right)_{N,T}
   = \frac{Nk_{\mathrm{B}}T}{V},\\
U &= -\frac{\partial}{\partial \beta}\ln Z_{\text{ideal}}
   = \frac{3}{2}Nk_{\mathrm{B}}T,\\
C_V &= \left(\frac{\partial U}{\partial T}\right)_{V}
     = \frac{3}{2}Nk_{\mathrm{B}}.
\end{aligned}
$$

This reproduces the ideal gas law and the equipartition theorem directly from the canonical partition function.

#### Energy fluctuations in the canonical ensemble
In the canonical ensemble the energy is not fixed but fluctuates around its mean value $\langle E\rangle$. The variance of the energy can be expressed as

$$
\mathrm{Var}(E) = \langle E^2\rangle - \langle E\rangle^2
= k_{\mathrm{B}}T^2 C_V,
$$

where $C_V$ is the heat capacity at constant volume. The *relative* fluctuations scale as

$$
\frac{\sqrt{\mathrm{Var}(E)}}{\langle E\rangle} \sim \frac{1}{\sqrt{N}},
$$

so for macroscopic systems (very large $N$) these fluctuations are negligible, but for simulations with modest $N$ they are visible and physically important.

#### NVT in practice: thermostats
In MD, we construct dynamics whose invariant probability distribution is the canonical one, $P(\Gamma)\propto e^{-\beta H(\Gamma)}$. Popular examples include:
* Nosé--Hoover and Nosé--Hoover chains (deterministic thermostats).
* Langevin dynamics (stochastic thermostat; see below).
* Stochastic velocity rescaling and related schemes.

These methods modify the equations of motion so that time-averaged observables converge to canonical ensemble averages.

## Other standard ensembles

Real simulations often use other ensembles, depending on what is held fixed and what is allowed to fluctuate:

* **Isothermal--isobaric (NPT):** $N$, $p$, $T$ fixed; $V$ fluctuates.
* **Grand canonical ($\mu$VT):** chemical potential $\mu$, $V$, $T$ fixed; $N$ fluctuates.

Formally, these ensembles have their own partition functions (e.g. $Z_{NPT}$, $\Xi_{\mu VT}$) obtained by summing over the appropriate variables. In practice, MD codes implement NPT or $\mu$VT via barostats and particle-insertion/removal schemes that are designed to sample the correct distribution.

#### Isothermal--isobaric (NPT) ensemble
In the NPT ensemble we imagine our system in contact with:
* a large heat bath at temperature $T$, and
* a mechanical reservoir that fixes the external pressure $p$ but allows the volume $V$ to fluctuate.

The NPT partition function is

$$
\Delta(N,p,T)
= \int_0^{\infty} \mathrm{d}V\, e^{-\beta pV}\, Z(N,V,T),
$$

where $Z(N,V,T)$ is the canonical partition function at fixed $N,V,T$. The equilibrium probability density of observing a particular volume $V$ and microstate $i$ (with energy $E_i(V)$) is then

$$
P(i,V) = \frac{1}{\Delta(N,p,T)} e^{-\beta\bigl(E_i(V) + pV\bigr)}.
$$

The corresponding thermodynamic potential is the **Gibbs free energy**,

$$
G(N,p,T) = -k_{\mathrm{B}}T \ln \Delta(N,p,T).
$$

From $G$ we obtain:

$$
\begin{aligned}
\langle V \rangle &= \left(\frac{\partial G}{\partial p}\right)_{N,T},\\
\kappa_T &\equiv -\frac{1}{\langle V\rangle}
\left(\frac{\partial \langle V\rangle}{\partial p}\right)_{N,T}
= \frac{\beta}{\langle V\rangle}\bigl(\langle V^2\rangle - \langle V\rangle^2\bigr),
\end{aligned}
$$

where $\kappa_T$ is the isothermal compressibility. Thus, volume fluctuations in an NPT simulation are directly related to the material's compressibility.

#### NPT in practice: barostats
To realize the NPT ensemble in MD, we introduce a *barostat* that allows the box volume (and sometimes shape) to fluctuate. Standard algorithms include:
* Berendsen barostat (simple, but does not sample the correct distribution exactly).
* Andersen, Parrinello--Rahman, or Martyna--Tobias--Klein (MTK) barostats, which are more rigorous.

These methods, when combined with a thermostat, generate dynamics whose stationary distribution is the NPT distribution. In an MD input file, this typically appears as a directive like `use barostat = NPT` with target pressure and temperature.

#### Grand canonical ($\mu$VT) ensemble (very briefly)
In the grand canonical ensemble the system is allowed to exchange particles with a reservoir at fixed chemical potential $\mu$:

$$
\Xi(\mu,V,T) = \sum_{N=0}^{\infty} e^{\beta \mu N} Z(N,V,T),
$$

and

$$
P(N,i) = \frac{1}{\Xi(\mu,V,T)} e^{-\beta\bigl(E_i(N,V) - \mu N\bigr)}.
$$

Here $N$ fluctuates, which is useful when studying adsorption, phase coexistence, or open systems. In simulations this is usually realized via Monte Carlo particle insertions and deletions rather than pure MD.

## Classical limit and Maxwell--Boltzmann distribution

In the classical limit, the canonical partition function can be written as an integral over phase space:

$$
Z = \frac{1}{h^{3N}N!}
    \int \mathrm{d}^{3N}q\,\mathrm{d}^{3N}p\;
    \exp\bigl[-\beta H(\mathbf{q},\mathbf{p})\bigr],
$$

where $H = K + U$ is the Hamiltonian (kinetic plus potential energy). If $H(\mathbf{q},\mathbf{p}) = K(\mathbf{p}) + U(\mathbf{q})$, then the integrals factor:

$$
Z = \frac{1}{h^{3N}N!}
    \left(\int \mathrm{d}^{3N}p\,\exp[-\beta K(\mathbf{p})]\right)
    \left(\int \mathrm{d}^{3N}q\,\exp[-\beta U(\mathbf{q})]\right).
$$

The momentum integral produces the familiar Maxwell--Boltzmann (Gaussian) distribution of momenta:

$$
P(\mathbf{p}) \propto \exp\!\left(-\beta \sum_{i=1}^N \frac{\mathbf{p}_i^2}{2m_i}\right),
$$

with the equipartition result

$$
\langle K \rangle = \frac{3}{2} N k_{\mathrm{B}}T.
$$

The remaining configuration integral defines the *configurational* partition function used in many simulation contexts.

#### One-particle velocity distribution
For a single particle of mass $m$ in three dimensions, the Maxwell--Boltzmann velocity distribution is

$$
P(\mathbf{v}) = \left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}
\exp\!\left(-\frac{m v^2}{2k_{\mathrm{B}}T}\right),
$$

where $v = |\mathbf{v}|$. This is the distribution that many MD codes use to assign initial velocities when "velocity rescaling" or "temperature initialization" is requested.

## Time averages vs ensemble averages

In real experiments, we typically observe a single macroscopic system over time and take time averages. In statistical mechanics, ensemble averages are defined as averages over many copies (replicas) of the system, each in a different microstate consistent with the ensemble.

#### Ensemble average
For an observable $A$ with values $A_i$ in microstate $i$:

$$
\langle A \rangle_{\text{ens}} = \sum_i P_i A_i.
$$

#### Time average
For a single system evolving in time, we can define a time average:

$$
\langle A \rangle_{\text{time}}
= \frac{1}{\tau}\int_0^{\tau} A\bigl(\Gamma(t)\bigr)\,\mathrm{d}t
\;\approx\; \frac{1}{M}\sum_{m=1}^M A\bigl(\Gamma(t_m)\bigr),
$$

where $\Gamma(t)$ is the trajectory in phase space.

In molecular dynamics, we simulate *one trajectory* and compute time-averaged quantities. The central assumption (to be discussed next) is that, under suitable conditions, time averages converge to ensemble averages.

#### Example: pressure from MD
Suppose we are running an NVT simulation and we want the average pressure. We can compute the instantaneous pressure $p(t)$ at each time step using the virial formula and then form a time average,

$$
\bar{p} = \frac{1}{M} \sum_{m=1}^M p(t_m).
$$

If the simulation is equilibrated and sufficiently long, $\bar{p}$ is our estimate of the canonical ensemble average $\langle p \rangle_{\text{NVT}}$.

## The ergodic hypothesis

The **ergodic hypothesis** states that, for an isolated system at fixed energy, a single trajectory in phase space will eventually come arbitrarily close to every accessible microstate compatible with the conserved quantities (energy, momentum, etc.). In that case,

$$
\langle A \rangle_{\text{time}} = \langle A \rangle_{\text{ens}},
$$

for all "reasonable" observables $A$.

Roughly speaking:
* The system relaxes from many different initial conditions to the same equilibrium macroscopic state.
* Time correlations decay, and the trajectory explores the energy surface in a complicated, effectively random way.
* A long, single MD run is "as good as" sampling many independent microstates from the equilibrium distribution.

This hypothesis underpins the common practice in MD: we run one (or a few) trajectories and treat time averages as estimates of equilibrium ensemble averages.

#### Mixing and decorrelation
Ergodicity is closely related to the idea of *mixing*: initial information about the microstate is gradually lost as the system evolves, and observables decorrelate in time. In practice we often estimate the *correlation time* $\tau_c$ of an observable $A$ and use it to determine how long we need to simulate to obtain statistically independent samples.

## Non-ergodic behavior and glasses

Real systems are often *not* perfectly ergodic, or at least not on accessible simulation timescales. Non-ergodic behavior means that the system fails to explore all of phase space compatible with its energy and constraints, either because:

* There are very high barriers in the energy landscape (metastable states).
* The dynamics are nearly integrable or regular.
* The timescale to cross barriers is astronomically large compared to our simulation time.

A classical example is the Fermi--Pasta--Ulam (FPU) problem: a chain of particles connected by weakly anharmonic springs. Instead of energy spreading evenly among all modes (as equipartition would suggest), energy remains trapped in a few modes for a very long time, revealing non-ergodic dynamics.

Amorphous solids and structural glasses are another important example. If we cool a liquid too fast, it may fall out of equilibrium and get stuck in a disordered, metastable configuration. In such systems:

* The observed structure and dynamics depend sensitively on the *preparation protocol* (e.g. cooling rate).
* There is no unique thermodynamic "glass transition temperature" independent of protocol.
* Time averages depend on the history of the sample and are not equal to equilibrium ensemble averages.

In simulations of glassy, non-ergodic systems, you can still measure useful quantities (structure factors, relaxation times, dynamic correlation functions), but you must always specify:
* How the system was prepared (cooling rate, initial configuration).
* Over what time window quantities were averaged.
* Whether results change if you modify the protocol.

#### Toy example: double-well potential
Even a single particle in a one-dimensional double-well potential can show non-ergodic behavior on finite timescales. If the barrier between wells is large compared to $k_{\mathrm{B}}T$, a trajectory starting in the left well may never cross to the right well during the simulation time, so the time average does not reflect the true equilibrium distribution over both wells.

## Contact with a heat bath: thermostats and Monte Carlo

In the lab, systems are rarely perfectly isolated: they exchange energy, momentum, and sometimes particles with their environment. In simulations we mimic this contact with a "bath" by modifying the equations of motion or using stochastic algorithms. Common approaches include:

* **Deterministic Molecular Dynamics (MD):**
    Integrates Newton’s equations of motion:
    $$
    m_i \frac{\mathrm{d}^2 \mathbf{r}_i}{\mathrm{d}t^2} = \mathbf{F}_i = -\nabla_{\mathbf{r}_i} U(\mathbf{r}_1,\dots,\mathbf{r}_N),
    $$
    usually sampling (approximately) the NVE ensemble. When combined with additional dynamical variables (e.g. Nosé--Hoover thermostat, barostat degrees of freedom), MD can also sample NVT or NPT ensembles.

* **Langevin Dynamics:**
    Adds friction and random forces to mimic a thermal bath:
    $$
    m_i \frac{\mathrm{d}^2 \mathbf{r}_i}{\mathrm{d}t^2}
    = -\nabla_{\mathbf{r}_i} U
      - \gamma m_i \frac{\mathrm{d}\mathbf{r}_i}{\mathrm{d}t}
      + \mathbf{R}_i(t),
    $$
    where $\gamma$ is a friction coefficient and $\mathbf{R}_i(t)$ is a random force satisfying fluctuation--dissipation relations. This samples the canonical (NVT) ensemble.

    More precisely, the random forces are chosen to have:
    $$
    \begin{aligned}
    \langle \mathbf{R}_i(t) \rangle &= \mathbf{0},\\
    \langle R_{i\alpha}(t) R_{j\beta}(t') \rangle
    &= 2\gamma m_i k_{\mathrm{B}}T\,\delta_{ij}\,\delta_{\alpha\beta}\,\delta(t-t'),
    \end{aligned}
    $$
    where $\alpha,\beta$ label Cartesian components. These conditions ensure that, in equilibrium, momenta follow the Maxwell--Boltzmann distribution at temperature $T$.

    **Example: diffusion from Langevin dynamics.**
    Consider a single Brownian particle (e.g. a colloid) in a solvent modeled via Langevin dynamics. In the limit of long times, its mean-squared displacement grows linearly with time:
    $$
    \langle [\mathbf{r}(t) - \mathbf{r}(0)]^2 \rangle \approx 6 D t,
    $$
    with diffusion constant
    $$
    D = \frac{k_{\mathrm{B}}T}{\zeta}, \qquad \zeta = \gamma m,
    $$
    consistent with the Einstein relation. By tuning $\gamma$, we can interpolate between nearly Hamiltonian dynamics (small friction) and strongly damped Brownian motion (large friction).

    **Langevin thermostats in MD codes.**
    In practice, Langevin thermostats are implemented using discrete-time integrators (e.g. BAOAB, OBABO, velocity Verlet with noise). Users typically choose a damping time $\tau_{\mathrm{damp}} = 1/\gamma$ on the order of a fraction of a picosecond to a few picoseconds. Too small $\tau_{\mathrm{damp}}$ (large friction) overdamps the dynamics and can slow down sampling of collective modes; too large $\tau_{\mathrm{damp}}$ (weak coupling) leads to slow temperature control.

* **Brownian Dynamics:**
    Overdamped limit where inertial terms are negligible compared to friction. The equation of motion reads
    $$
    \gamma \frac{\mathrm{d}\mathbf{r}_i}{\mathrm{d}t}
    = -\nabla_{\mathbf{r}_i} U + \mathbf{R}_i(t),
    $$
    and velocities are not explicitly followed. This is useful for simulations of large particles in viscous environments where momentum relaxes very quickly (e.g. coarse-grained polymer or colloid models).

* **Monte Carlo (MC):**
    Random moves in configuration space accepted or rejected with a rule that ensures detailed balance, e.g. Metropolis MC. For the canonical ensemble, a trial move from microstate $i$ to $j$ with energy change $\Delta E = E_j - E_i$ is accepted with probability
    $$
    P_{\text{acc}}(i\to j) = \min\bigl[1,\exp(-\beta\Delta E)\bigr].
    $$
    Repeated moves generate configurations distributed according to $P_i \propto e^{-\beta E_i}$. MC algorithms can be designed to sample NVT, NPT, or other ensembles by including volume-change moves, particle insertions/deletions, etc.

Once any randomness is introduced (Langevin, MC, etc.), ergodicity is usually improved, and convergence towards the canonical distribution is more robust—although for complex systems, equilibration can still be extremely slow.

## Practical issues: equilibration, windowing, and diagnostics

In practice, to obtain meaningful averages from simulations:

1.  **Equilibration:**
    Start from some initial configuration (often artificial, e.g. a lattice or random packing). The early part of the trajectory is usually far from equilibrium. You should:
    * Let the system evolve until observables (e.g. energy, pressure, structure) fluctuate around a steady mean.
    * Discard this initial *equilibration* segment from your averages.

2.  **Check stationarity:**
    Always plot the observable of interest $A(t)$ versus time. Ask:
    * Does $A(t)$ fluctuate around a constant mean?
    * Or does it drift slowly (still evolving)?
    * How long does it take before the drift disappears?

3.  **Time-window averaging:**
    For non-stationary or slowly relaxing systems (e.g. glasses), be explicit about:
    * The time window over which you averaged.
    * How the average changes if you use a different time window.
    * Whether results depend on when you start collecting data (early vs late segments).

4.  **Block averaging and error estimates:**
    Consecutive MD frames are correlated, so naive estimates of the standard error can be misleading. A common approach is *block averaging*:
    * Split the production trajectory into $M$ blocks of duration $\tau_{\text{block}}$.
    * Compute the block average $A_k$ in each block $k = 1,\dots,M$.
    * Treat the $A_k$ as approximately independent samples and estimate the mean and standard error from them:
        $$
        \begin{aligned}
        \bar{A} &= \frac{1}{M}\sum_{k=1}^M A_k,\\
        \sigma_{\bar{A}} &= \sqrt{\frac{1}{M(M-1)} \sum_{k=1}^M (A_k - \bar{A})^2}.
        \end{aligned}
        $$
    * Choosing $\tau_{\text{block}}$ several times larger than the correlation time of $A$ improves the reliability of these error estimates.

5.  **Protocol dependence:**
    If your results depend on preparation protocol (cooling rate, compression rate, etc.), then you are *not* measuring equilibrium ensemble averages, but still something physically meaningful. You must report the protocol clearly.

## Summary

* Statistical mechanics connects microscopic variables from simulations to macroscopic thermodynamic quantities.
* Microstates are points in a $6N$-dimensional phase space; macrostates are defined by a small set of constraints (e.g. $N,V,E$).
* The density of states $\Omega(E)$ and the partition function $Z$ encode the structure of phase space and allow us to compute thermodynamic properties.
* Different ensembles (NVE, NVT, NPT, $\mu$VT) correspond to different physical constraints and are implemented in simulations via thermostats, barostats, and MC schemes.
* The ergodic hypothesis justifies using time averages from MD trajectories as approximations to ensemble averages.
* Non-ergodic behavior (e.g. glasses, metastable states) is common and must be treated carefully; results are often protocol-dependent.
* Good simulation practice always includes checking equilibration, estimating statistical errors, and carefully defining the ensemble and preparation protocol.

## References

* D. Chandler, *Introduction to Modern Statistical Mechanics*.
* M. E. Tuckerman, *Statistical Mechanics: Theory and Molecular Simulation*.
* Course notes on statistical mechanics and ensembles (MSE 485 / atomistic-scale simulations).