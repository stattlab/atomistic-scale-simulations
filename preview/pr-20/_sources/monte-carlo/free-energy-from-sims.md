# Free Energy Estimation in Simulations

Free energy differences are needed to determine phase stability. Direct simulation is too expensive and unreliable due to size effects, critical slowing down, and hysteresis. Free energy is determined by integrating over a reversible path, not directly measured.

## Overview

This is a brief overview of free energy estimation, much of which can be found in the article by D. Frenkel: \emph{Free-Energy Computation and First-Order Phase Transitions}, in \emph{MD simulation of Statistical Mechanical Systems}, edited by Ciccotti and Hoover. Generic remarks are given in A\&T on pg. 40. Specific methods refer to various relevant pages.

The free energy is related to the partition function by:
\begin{equation}
    e^{-\beta F} = \frac{1}{N! \Lambda^{dN}} \int dR\, e^{-\beta V(R)} = Z
\end{equation}
where $N$ is the number of particles, $d$ is the dimension, $\beta = (k_B T)^{-1}$, and $\Lambda = (4 \pi \lambda \beta)^{-3/2}$ is the classical thermal de Broglie wavelength.

The Gibbs free energy is
\begin{equation}
    G = \mu N = F + PV
\end{equation}
where $\mu$ is the chemical potential per particle.

The entropy can be obtained from the free energy.
Free energy differences are needed to determine phase stability. Direct simulation of stability of a given phase is too expensive and unreliable. For example the different phases may have different size effects, there can be critical slowing down and hysteris effects. In experiment, the free energy is determined experimentally
by integrating over a reversible path; one cannot measure it directly.

## Methods for Free-Energy Estimation

We will briefly describe seven methods that may be used in order to calculate the free energies. Each method has its own difficulties and, therefore, the choice of method for a particular problem should be chosen with the specific application in mind. Careful checks and analysis are required to have trustworthy results.
For lattice Hamiltonians some of the methods described are not applicable because many ground states may compete at finite temperature, depending on the range and types (i.e., pair, triplet, etc.) of interactions. Therefore you usually need to know which and how many Free Energies are needed a priori via simulation to construct the temperature versus composition phase diagram, beyond simply performing the simulation

## Thermodynamic Integration

With this method one establishes the free energy in a reference state and then integrates the derivative of the free energy (which we can calculate) along a path from the reference state to the desired state with respect to the density or the temperature or even with respect to an artificial parameter. To integrate with respect to the density we have:

$$
    \left( \frac{dF}{dV} \right)_{N,T} = -P \Rightarrow F(V) = F_0(V) + \int_0^\rho \frac{d\rho'}{N\beta \rho'} \left( \beta P/\rho' - 1 \right)
$$
Here, F0 is the free particle free energy, which is known exactly. For a fluid one is performing a density integration from ρ = 0 to the density of interest.

$$
    \left( \frac{d(F\beta)}{d\beta} \right)_{N,V} = E \Rightarrow F(T) = F_0(T) + \beta^{-1} \int_0^\beta d\beta' \left( E(\beta') - E_0(\beta') \right)
$$

Here, F0 and E0 are the free energy and energy of a reference system, which must be known exactly. For a solid, a temperature integration is performed from $\beta = \infty$ to the temperature of interest.
When performing these thermal integrations, you must not cross a phase boundary, since the derivatives needed will depend very sensitively on the size of system and may be subject to critical slowing down. Notice that many careful simulations are required but this method always works! Clever choices of the path can save much computer time.

## Direct Methods

**Hit or Miss Method** Sample some probability distribution $p(R)$ with $R dRp(R) = 1$

$$
e^{-\beta F} = \frac{1}{N! \Lambda^{3N}} \int dR\, p(R) \frac{e^{-\beta V(R)}}{p(R)} = e^{-\beta F_0} \left\langle \frac{e^{-\beta V(R)}}{p(R)} \right\rangle_p
$$
For non-trivial problems, this method gives a very large variance since it is very difficult to make p(R) large where V(R) is small.

**Sample $e^{-\beta V}Z$ Method**: Calculate the following estimator.
\begin{equation}
    Z^{-1} = \left\langle e^{-\beta H} \right\rangle
\end{equation}
However, this has a very large variance unless V(R) is very weak.

## Particle Insertion/Deletion Methods

Calculate the following average to obtain directly the chemical potential relative to the ideal gas:
$$
    \mu = \mu_{\text{ideal}} - k_B T \ln \left\langle e^{-\beta(V_N(r_N) - V_{N-1}(r))} \right\rangle_{N-1}
$$
Here we sample $e^{−\beta V_{N−1}} , a N-1 particle system, and add a particle uniformly at random and find the change in energy, VN - VN−1. Recall, $μ_\text{ideal} = k_BT ln(\Lambda^{cl}\rho)$. This method becomes very difficult as density increases and impossible for a solid. Also random deletion has infinite variance for hardcore systems.

## Grand Canonical Ensemble Method

Given the Grand Canonical Ensemble of constant μ, T, V, one may calculate from the Gibbs’ Free Energy the Free Energy as

$$
    \frac{F}{N} = \mu - \frac{\langle P \rangle V}{\langle N \rangle}
$$

This technique had very slow convergence at high densities (i.e., solids) and roughly only good for $\rho < \rho_\text{critical}$. In addition, there is a large size dependence.

## Artificial Thermodynamic Integration

Here one must sample from an artificial distribution $(R, \lambda)$ such that $\Pi(R, \lambda)$ interpolates between two distributions:

$$
    \Pi(R, 0) &= \text{known reference state} \\
    \Pi(R, 1) &= \frac{e^{-\beta V}}{Z}
$$

Here $\lambda$ is an adjustable parameter to “turn on” the interactions: $H(\lambda) = H_0 + \lambda H_1$, where we know how to obtain the free energy, etc., for H0. The partition function may be obtained as follows:

$$
Z(\lambda) = \int d\vec{R} \Pi(R,\lambda)\\
    Z = Z_0 \exp\left[ \int_0^1 d\lambda \left\langle \ln \left( \frac{\Pi(R, 1)}{\Pi(R, 0)} \right) \right\rangle_\lambda \right]
$$

Care must be taken when using this method.

1. Carefully pick a reference state $\Pi(R, 0)$ as close to $\Pi(R, 1)$ as possible.
2. Make sure there are no Phase Boundaries between $\Pi(R, 0)$  and $\Pi(R, 1)$ .
3. $ \ln(\Pi(R, \lambda)) = \ln(\Pi(R, 0)) + \lambda \ln\left(\frac{\Pi(R,1)}{ \Pi(R,0)}\right) $
4. simulate $\Pi(R, λ)$ for several λ’s.

We now obtain the Free Energy of system by

$$
F=F_0+\beta^{-1} \int_0^1 d \lambda\left\langle\ln \left(\frac{\Pi(R, 1)}{\Pi(R, 0)}\right)\right\rangle_\lambda
$$

Beware of any non-analytic behavior as a function of λ. Also choose CPU time ($\propto \lambda's$) so that uncertainties are independent of λ.

Let us consider the case where only the potential matters. Here V(λ) = V0 + λ V1, and, therefore, λ=0 we have V(λ) = V0 with known F0, whereas, for λ=1 we have V(λ). Generally, then

$$
    F(\lambda) = -k_B T \ln \left[ \frac{1}{N! \Lambda^{3N}} \int d^N q\, e^{-\beta V(\lambda)} \right]
$$
With F0 known,
$$
    \frac{dF(\lambda)}{d\lambda} = \left\langle \frac{dV(\lambda)}{d\lambda} \right\rangle_\lambda
$$

Notice that $\langle dV (λ)/d\lambda \rangle$, a canonical average of a mechanical quantity for a system with H(λ), can be obtained by a computer simulation, just as we have done for all other mechanical properties!

Examples of Artificial Integrations

- Map a complicated liquid into a simple liquid (e.g., Car-Parinello Si $\rightarrow$ empirical force filed for Si).
- Realistic solid $\rightarrow$ Einstein solid, so as to use $V_E = K \sum(r_i − r_{0,i})^2$.
- Perfect crystal $\rightarrow$ defective crystal, e.g., turn off one atom.
- Bcc crystal $\rightarrow$ Fcc crystal, via distortion of simulation box.
- Coiled protein $\rightarrow$ straight protein, by applying end-to-end force.

## Acceptance Ratio Method (Bennett)

Suppose you want to calculate the free energy distribution between Π0(R) and Π1(R), where Zk = R Πk for k=0,1. We then are considering an enlarged sample space, i.e. (R,k). System is allowed to hop from 0 to 1. Thus, there are two types of moves: 1) usual R → R’, and 2) transition between k → k’, given by T. Here, Pk = probability that system is in state k (irrespective of R).

$$
\Pi(R,k) &=
\begin{cases}
    \Pi_0(R) & k=0 \\
    c\, \Pi_1(R) & k=1
\end{cases}
$$

and “c” is the importance sampling parameter. Therefore, we find that

$$
\frac{P_0}{P_1} &= \frac{Z_0}{cZ_1}
$$

which is how we can calculate Z0/Z1. The optimal value of the importance sampling parameter is usually
c≈ Z0/Z1. Let T0→1 and T1→0 be the transition rates of hopping from 0 → 1, or vice-versa. We then have

$$
\frac{P_0}{P_1} = \frac{\langle T_{1 \rightarrow 0} \rangle_1}{\langle T_{0 \rightarrow 1} \rangle_0}
$$

Use a heat bath for T:
$$
T_{1 \rightarrow 0} = \frac{c \Pi_1}{\Pi_0 + c \Pi_1} = \frac{1}{1 + \Pi_0 / (c \Pi_1)}
$$

Finally, we see that

$$
   \frac{Z_0}{Z_1} &= c \frac{ \left\langle \left(1 + \frac{\Pi_0}{c\Pi_1} \right)^{-1} \right\rangle_0 }{ \left\langle \left(1 + \frac{c\Pi_1}{\Pi_0} \right) \right\rangle_1 }
$$

whose variance will be large unless we can hop from 0 ↔ 1. Notice that by introducing more states 0 ≤ λi ≤ 1 leads to a continuous transition and, therefore, to exact thermodynamic integration.

## Umbrella Sampling / Histogram Method

Within this approach one applies importance sampling to
$$
\frac{Z_1}{Z_0}=\frac{\int d \mathbf{R} \Pi_1(R)}{\int d \mathbf{R} \Pi_0(R)}
$$

Sample R from $\Pi^*$ within Metropolis Algorithm, thereby giving the estimator
$$
\frac{Z_1}{Z_0}=\frac{\left\langle\Pi_1 / \Pi^*\right\rangle_{\Pi^*}}{\left\langle\Pi_0 / \Pi^*\right\rangle_{\Pi^*}}
$$

Here is an example with $\Pi^*=\sqrt{\Pi_0 \Pi_1}$. In this case,
$$
\frac{Z_1}{Z_0}=\frac{\left\langle\sqrt{\Pi_1 / \Pi_0}\right\rangle_{\Pi^*}}{\left\langle\sqrt{\Pi_0 / \Pi_1}\right\rangle_{\Pi^*}}
$$

Thus, the optimal $\Pi^*$ is found by usual method:

$$
\Pi^* & \propto \sqrt{\Pi_0 \Pi_1}\left|f(R)-f(R)^{-1}\right| \\
& =\left|\Pi_0 / Z_0-\Pi_1 / Z_1\right|
$$

where $f=\sqrt{\left(\Pi_1 Z_0\right) /\left(\Pi_0 Z_1\right)}$. We can introduce an uncertainty in $Z_1 / Z_0$ as

$$
\Pi^* \approx \sqrt{\left(\Pi_0-c \Pi_1\right)^2+\epsilon c \Pi_0 \Pi_1}
$$

where c is an estimator of $Z_0 / Z_1$ and $\epsilon$ is chosen to minimize variance (arising from undersampling and convergence).

In lattice models this method is know as the histogram method.

## References

- D. Frenkel, ``Free-Energy Computation and First-Order Phase Transitions'' in \textit{MD Simulation of Statistical Mechanical Systems}, ed. Ciccotti and Hoover.
- Allen and Tildesley
