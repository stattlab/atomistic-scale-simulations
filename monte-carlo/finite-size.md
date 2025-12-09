
# 1. Phase Transitions, Finite-Size Scaling and Renormalization Group


## 1. Phase Transitions and Correlations

Phase transitions mark abrupt or qualitative changes in the macroscopic state of matter when one or more thermodynamic control parameters are varied. These control parameters include temperature $T$, pressure $P$, density $\rho$, and, for magnetic systems, and external magnetic field $H$. A **critical point** is a special point in this parameter space–typically denoted by ($P_{c}$, $\rho_{c}$, $T_{c}$) for fluids or ($H_{c}$, $M_{c}$, $T_{c}$) for magnets–at which the distinction between two phases disappears and fluctuations underlying microscopic degrees of freedom become long-ranged. Near such points, systems exhibit characteristic singular behavior that is largely independent of microscopic details.


A convenient way to characterize a phase transition is through an **order parameter**, a macroscopic quantity that distinguishes one phase from another and often vanishes continuously at a continuous (second-order) transition. In a ferromagnet, for instance, the order parameter is the spontaneous magnetization $M(T)$ in zero external field. Below the Curie temperature $T_c$, the spins align collectively and $M(T) \neq 0$. Above $T_c$, thermal agitation destroys long-range order and $M(T)=0$. The graph of $M(T)$ versus $T$ thus shows a continuous loss of magnetization as the system is heated through the critical temperature.


An analogous example appears in the liquid-gas transition of a simple fluid. At temperatures below the liquid-gas critical temperature $T_c$, the coexistence of liquid and gas phases is characterized by a density difference $\rho_L-\rho_G$, where $\rho_L$ and $\rho_G$ denote the equilibrium densities of the liquid and gas, respectively. This difference plays the role of an order parameter: it is nonzero along the coexistence curve and tends to zero as the critical point is approached. Exactly at the critical point, the liquid and gas become indistinguishable, and $\rho_L=\rho_G=\rho_c$.


Order parameters can also be defined in more complex systems. In binary alloys, one natural order parameter is the deviation of the local composition from its average value,

$$
c(\mathbf{r})-c_0,
$$

where $c(\mathbf{r})$ is the local concentration of one species (say, A atoms in an A-B alloy) and $c_0$ is the overall composition. Below an ordering temperature, the alloy may develop long-range compositional order (for example, alternating A and B on a lattice), and the fluctuations of $c(\mathbf{r})-c_0$ reflect the emergence of ordered domains. Such composition fluctuations are routinely probed by scattering experiments using x rays, electrons, or neutrons. The resulting structure factor encodes spatial correlations of $c(\mathbf{r})$, which grow in range and magnitude as the system approaches an ordering transition.


A particularly striking manifestation of critical behavior is **critical opalescence**, historically observed in fluids such as carbon dioxide near their liquid-gas critical point. As $T$ approaches $T_c$ from above at fixed pressure, the fluid becomes milky and strongly scatters visible light. Microscopically, this phenomenon arises because density fluctuations become both large in amplitude and long-ranged. Droplets of high- and low-density regions form and grow to sizes comparable to the wavelength of visible light. These density inhomogeneities act as efficient scatterers, leading to the observed opalescent appearance. Critical opalescence provided some of the earliest direct visual evidence that something singular occurs at the critical point.


A central quantity in understanding these phenomena is the correlation length $\xi$, which measures the typical distance over which fluctuations of a local thermodynamic variable–such as the spin orientation in a magnet or the density of a fluid–remain significantly correlated. Far above the critical temperature, correlations decay rapidly and $\xi$ is microscopic, corresponding to short-range order. As the critical point is approached, however, $\xi$ grows rapidly, reflecting the emergence of large correlated regions like fluctuating high-and low density domains responsible for critical opalescence. In the two-dimensional Ising model, for example, the spin-spin correlation function decays exponentially with a characteristic length $\xi(T)$ for $T>T_c$, while below $T_c$ the system develops true long-range order and the correlations become effectively infinite in range due to the nonzero spontaneous magnetization. In numerical simulations with finite linear size $L$, this growth of $\xi$ is eventually cut off when $\xi(T)$ becomes comparable to or larger than $L$, so that the divergence of the correlation length that would occur at $T_{c}$ in an infinite system is rounded off and replaced by pronounced finite-size effects once $\xi \gtrsim L$.


Generally speaking, three closely related signatures appear as a system approaches a critical point. First, density fluctuations grow dramatically. As $T$ -> $T_{c}$ at fixed pressure, correlated regions of high and low density become comparable in size to the wavelength of visible light, so these inhomogeneities scatter light strongly and give rise to critical opalescence. Second, the isothermal compressibility $K_{T}$ increases sharply and, in the thermodynamic limit, diverges according to

$$K_T \rightarrow \infty \quad \text{as} \quad T \rightarrow T_c$$


Physically, this means that an arbitrarily small change in pressure produces a very large change in volume or density near the critical point. Third, the range of density-density correlations grows without bound: the correlation length $\xi$, which measures the typical size of correlated density fluctuations, also diverges,

$$\xi \rightarrow \infty \ \ \text{as} \ \ T \rightarrow T_{c}$$

The divergence of $\xi$ underlies both the enhanced density fluctuations and the anomalous compressibility. All three reflect the same underlying fact that, at criticality, fluctuations are correlated over all length scales.


To make the connection between these macroscopic signatures and microscopic structure more explicit, it is useful to introduce the **density-density pair correlation function**. In a fluid, fluctuations of the local density can be written as $\delta \rho(\mathbf{r})=\rho(\mathbf{r})- \langle\rho\rangle$, and the pair correlation function is defined as $G\left(\mathbf{r}-\mathbf{r}^{\prime}\right)=\left\langle\delta \rho(\mathbf{r}) \delta \rho\left(\mathbf{r}^{\prime}\right)\right\rangle$. This quantity measures how a fluctuation at one point is correlated with a fluctuation at another. Thermodynamic response functions such as the isothermal compressibility $K_{T}$ are not independent of these microscopic correlations. Rather, they can be expressed in terms of the integrated pair correlations. For an ideal gas, the compressibility is $K_T^0=\langle N\rangle k T / V$, while more generally one has the fluctuation relation

$$
\frac{K_T}{K_T^0}=\frac{\left\langle(N-\langle N\rangle)^2\right\rangle}{\langle N\rangle},
$$
which tells us that the compressibility of a fluid, compared to an ideal gas at the same condition, is determined by how large the particle the particle-number fluctuations are compared to the average number of particles. Here, the variance of the particle number in a volume $V$ can be written as

$$
\left\langle(N-\langle N\rangle)^2\right\rangle=\int d \mathbf{r} \int d \mathbf{r}^{\prime} G\left(\mathbf{r}-\mathbf{r}^{\prime}\right)=V \int d \mathbf{r} G(\mathbf{r}) .
$$

As the critical temperature is approached, the divergence $K_T \rightarrow \infty$ in the thermodynamic limit therefore implies that the integral of $G(\mathbf{r})$ diverges. This can only occur if the density-density correlations become very long-ranged, so that $G(\mathbf{r})$ decays only slowly for $|\mathbf{r}| \gg 1$. In other words, the divergence of the compressibility is a direct consequence of the divergence of the correlation length $\xi$ that characterizes the range of $G(\mathbf{r})$. This growing correlation length, together with the associated singular behavior of thermodynamic quantities, motivates the use of scaling ideas in finite-sized simulations. When $\xi$ becomes comparable to the system size $L$, finite-size effects encode how observables depend on the ratio $L / \xi$, and these finite-size scaling relations can be used to estimate the true critical point and critical exponents from data obtained in systems of limited size.




## Finite-size Scaling

**Reduced Coordinates** are often convenient to define when discussing scaling of thermodynamic quantities. For example, reduced temperature t = (T - TC)/TC, which is a temperature relative to the critical point. You can define reduced densities. Or, in percolation problems, reduced units would be x = (p - pC)/pC. Its use in what follows should be apparent.

**Experimental Evidence for Scaling --** When measured coexistence curves of numerous **fluids**, e.g., are plotted as T/TC vs. $\rho/ \rho_C$, a single curve is found (see, e.g. E. Stanley, pg. 10). A fit to this curve reveals that $\rho - \rho_C ~ (-t)\beta$, and $\beta=0.33$. However, it is generally found that there is a range: 0.33 < \beta < 0.37. For example, in Helium, $\beta=0.354$. Measurements for other quantities, such as susceptibilities, also lend themselves to this type of scaling analysis.

Whether talking of magnetic systems, fluids, or percolation problems, the order parameters (pair-correlations, correlation lengths, and so on) exhibit this type of scaling behavior. Here we only discuss the named quantities in the magnetic case, (i) Magnetization, M(T), (ii) the isothermal susceptibility, \chi(T), and (iii) the correlation length, \xi(T), and (iv) the zero-field specific heat, C(T). For percolation, they would be the (i) spanning probability, pinf, (ii) the mean cluster size, S(p), and (iii) the correlation length, \xi(p).

**Scaling Properties and Critical Exponents***   **Magnetization**
    M(T) ~ (-t)\beta           0.33 < \beta < 0.37.           (for T < TC)

- **Magnetic Susceptibility**
    \chi(T) ~ |t|\-\gamma           1.3 < \gamma < 1.4.
- **Correlation Length**
    \xi(T) ~ |t|\-\nu           \nu depends on dimension of problem.
- **Zero-field Specific Heat**
    C(T) ~ |t|\-\alpha           \alpha ~ 0.1.

The coefficients defining the power law behavior (i.e., \beta, \gamma, \nu, etc.) are referred to as **critical exponents**

### Scaling with Finite System Size

Consider a simulation system with linear dimension L.

**Scaling revealed from behavior of Correlation Length***   If \xi(T) < < L, power law behavior is expected because the correlations are local and do not exceed L.

- If \xi(T) ~ L, however, \xi cannot change appreciably and M(T) ~ (-t)\beta is no longer applicable.
- For \xi(T) ~ L ~ |t|\-\nu, a quantitative change will occur in the system.
- **This last relation obviously implies (for a given L) that**

    **|T - TC(L)| ~ L\-1/\nu.         Scaling Relation of TC**

Note that for a 2-dimensional system, like the square lattice, \nu\=1. Thus, TC(L) should scale linearly with L and the final TC should be (within error bars) close to the exact 2-D square lattice in zero field, 2.269. To determine TC(L), CV(L,T) vs. T is calculated for various L = (4, 8, 16, 32, ...) and the maximum CV(L,T) is used to indicate TC(L). Recall CV(T) = (<E2\> - <E>2)/kT2, which reveals the energy fluctuations of the system and the distribution of configurations over energy, i.e. the more possible configurations, the higher the specific heat.

**Why not use E vs. T plots to reveal the transition temperature, instead of CV?**

**Determining the Critical Exponents***   From TC scaling relation (when \xi(T) ~ L as L \rightarrow\infty),         **M(T=TC(L)) ~ L\-\beta/\nu** .

- A similar analysis may be made for susceptibility or specific heats.
- Or, for order paramters in other problems, such as percolation, **pinf(T=TC) ~ L\-\beta/\nu** .
- Hence, the critical exponents can be determined through scaling analysis. ### A Preliminary: Scaling Law for Homogeneous Functions

**A function, f(r), is said to scale if for all values of \lambda, f(\lambda r) = g(\lambda) f(r)**.
A function with this property is **homogeneous**, e.g., f(r)= Br2 \rightarrow f(\lambda r)= \lambda2f(r), and g(\lambda)= \lambda2.
For a homogeneous function, if we know f(r=r0) and we know g(\lambda), then we know f(r) everywhere!

**The scaling function is not arbitrary. It must be g(\lambda) = \lambdaP.**
P is the degree of homogeneity.
See Stanley, pg 176 for "proof".

**A generalized homogeneous function is given by f(\lambdaa x, \lambdab y) = \lambda f(x,y).**
There is no \lambdaP on R.H.S. because you could always re-scale with \lambda1/P and change a'=a/P and b'=b/P, without loss of generality.
Notice this is NOT f(\lambda x, \lambda y) = \lambdaP f(x,y), as you might suspect, because functions can be scaled differently in different directions. ### Static Scaling Hypothesis for Thermodynamic Functions

**The (ad hoc) static scaling hypothesis asserts that G(t,H) is a generalized homogeneous function.** Hence, G(\lambdaat t, \lambdaaH H) = \lambda G(t,H).

**If G(t,H) is a generalized homogeneous function, then so are all other forms of Free Energy, as they are just Legendre transforms of G.**

**Relations amongst critical exponents may be obtained by application of thermodynamic relations, e.g., M(t,H) = -dG(t,H)/dH.** Taking this derivative, we find (try it!):

\lambdaaH M(\lambdaat t, \lambdaaH H) = \lambda M(t,H).

**For zero field, M(t,0) = \lambdaaH\-1 M(\lambdaat t, 0).**

- Letting \lambda = (- t\-1)1/at yields the scaling **M(t,0) = (-t)(1-aH)/at M(-1,0)**
- And, because we know M(t,0) ~ (-t)\beta, then **\beta = (1-aH)/at** .
- The same can be done for all observables which are derivatives of G(t,H).
- e.g. \chiT ~ (-t)\-\gamma' from below TC, **\gamma' = (2 - aH)/at**.
- e.g. \chiT ~ (t)\-\gamma from above TC, **\gamma = (2 - aH)/at** , and \gamma' = \gamma.

**From SCALING of the thermodynamic functions, the critical exponents can be determined in terms of ratios of only 2 quantities, aH and at.** Hence, by plotting the thermodynamic functions according to the derived scaling relations, both aH and at can be determined.

You can perform the same type of analysis for other Thermodynamic functions or quantities to derive the scaling equalities, which from another analysis are given as inequalities (but you must remember that the scaling hypothesis was, in fact, an ad hoc idea -- but seems to be born out).

### Renormalization Group

Because the correlation length diverges, and various fluctuation grow (along with the associated pair correlations), as TC is approached from above, it shows that long-range fluctuations control the phase transition and the critical point. This also suggests that the phase transition (or fluctuations) is associated with the _degree of connectivity_ of the system. Recall that there is no _connectivity_ in 1-D and, hence, no phase transition. (You may have connectivity but in combination with frustration due, say, to geometry of lattice and competing interactions which results in no phase transition, as with the triangular lattice and AFM interactions. But this is because there is no unique ground-state, not becuase of non-connectivity.)

The results of **scaling**, as discussed above, is that the important fluctuations and their range can be _scaled up_ to the appropriate lenght scale, and the local effects (which do not control the phase transition) can be ignored. Such scaling ideas were developed by Leo Kadanoff in the 60's in real space, which provided a very intuitive insight. However, these ideas were still only approximate and not complete. Nonetheless, the ideas of **_fixed points, Kadanoff transformations, etc._** extend directly into many areas of physics, chemistry, and engineering (although perhaps not obvious at first glance).

Based on the work of Kadanoff, Ken G. Wilson in the early 70's proposed a formal mathematical approach (based in reciprocal-space (or k-space)) solvable with large-scale computing, now known as the **Renormalization Group (RNG) Theory**. For this work he was awarded the Nobel Prize in Physics in 1982. It has less intuitive nature than the so-called **Real-space Renormalization Group** ideas of Kadanoff, but carries the principals out exactly, in principle. Two good references for an overview of these ideas are in _Problems in Physics with Many Scales of Length_, Sci. Am. 241, 158 (1979) and Rev. Mod. Phys. 55, 583 (1983) by K.G. Wilson.

A **good introduction** to the concepts of RNG can be found in **D. Chandler's _Introduction to Modern Statistical Mechanics_**, pg. 139. For statistical mechanics problems, the key issues is how to re-scale the partition function such that it (i) retains the same symmetry and ground-state given by the original partition function, (ii) can re-scale the so-called _coupling constant_, i.e. K = J/kT in the nearest-neighbor model, and (iii) the partition function can be re-cast in terms of partially summed original partition function such that it look the same as original, with different spins and (perhaps) with different coupling constant. If this re-scale is possible, then we can develop a **Recursion Relation** to compute the partition function from a system with another coupling (e.g., zero, non-interacting system). An iterative solution of this Recursion Relation for the partition function yields "roots" or **fixed points** of the solution space. The fixed points reveal the possible critical behavior expected.

This development of the RNG ideas and their solution is straightforward, but a little long, in 1-D (see Chandler). Nonetheless, the solution is exact and show there is no critical point in 1-D. In 2-D, which is even more difficult, the model can be also managed by **real-space renormalization** and the **fixed point** is found to be KC = J/kTC = 0.50698, whereas Onsager's (or Yang's) exact solution is KC = 0.44069. The specific heat is found to be C ~ |T - TC|\-\alpha where \alpha = 0.131, which is a weak singularity reminiscient of the exact solution C ~ - ln|T - TC|. Notice the results of Real-space RNG are very good, much better than mean-field theory which ignores correlations (or at least the important long-range ones).

**Important Physics** (think Ising for simplicity)

In re-scaling the partition function, there are partial summations performed of spin (in the Ising case). In integrating (or summing) out some spins means we have a Boltzmann samples fluctuations of those spins (see the scaled partition fct. in Chandler's book -- but you at least know in statisitical mechanics the partition function is the Boltzmann weighting and remains so upon re-scaling). Since each spin is indirectly coupled to the non-nearest neighbor through fluctuations, even though remaining spin are not nearest-neighbors after summation, they contain remnant interactions through the fluctuations. And, each new coupling is intrinsic to the degree of connectivity of the lattice. With no connectivity, there can be no phase transition, just a sin 1-D Ising model.

**Concrete Example** (peroclation in real-space)

Scaling of Hamiltonian and Partition Function is not as easy as for percolation in real space. Hence, **percolation** is best example to reveal **the ideas** and how a **recursion relation** is found, giving the **fixed point** solutions.

Consider an L= 16 x 16 percolation simulation lattice in 2-D. Shaded squares are occupied sites and un-shaded are unoccupied sites. Sites are occupied with probability **p = 0.5**. Here we will consider a percolation of the lattice (i.e. a connectivity across the lattice) **from bottom to top**.


For Renormalization one must consider what size of renormalization you are going to perform. Let us consider a b=2 type RNG, where a you half the size of square under consideration each RNG.
As such we must consider all 2 x 2 clusters and how they span (or occupy) in the bottom to top direction to obtain percolation. They each have a **Total occupation probability** given by **the product of the individual site occupations**.

The **pertinent vertically spanning clusters** that renormalizes to a **single shaded square** (and produced the first RNG image from L=16 to L=8) are obvious, i.e.


First cluster has probability of **p4** ,
second set of clusters have **4 p3(1 - p)** ,
last set of clusters have **2 p2(1 - p)2** ,
in order to span from bottom to top.
The new (renormalized) cell dimension is obvious reduced by a factor of **b**. For example, beginning with L=16 and with one renormalization, the new cell is L=8, which is shown in first image.

**The renormalization transformation** between p' and p must reflect the **connectedness**, i.e. formation of the spanning path which percolates from top to bottom, and we define a cell to be occupied if it spans the cell vertically. This is how the L=8 square was found. Such an RNG can be performed until we get to L=2, as the final two RNG process are shown in next image.


**The Renormalization Group Equation**

Hence, if sites are occupied with probability **p**, then the cells are occupied with probability **p'**. As a result, the **RG Equation is p' = R(p)**. Hence, for the above vertically spanning clusters we have

**p' = R(p) = p4 + 4 p3(1 - p) + 2 p2(1 - p)2**.

**The Trivial Fixed Points**

Let p= p0 = 0.5, as in the images.*   One application of RG Equation gives p1 = R(0.5) = 0.44.

- Second application gives p2 = R(p1) = 0.35.
- Continued application of RG yields p = 0.

Let p= p0 = 0.7.*   Succussive RG applications gives p = 1.

These two solutions of RG Equation are called **Trivial Fixed Points** because starting with anything above (or below) the p\* percolation threshhold (yet to be found) leads to these two un-interesting values. Recall p=0 is no sites are occupied and p=1 is fully occupied. By the way, it should be clear from the last image for p = 0.5 RNG that there is no percolation because the last renormalization from L=2 to L=1 yields an empty site. **What is p\*?**

**The Non-Trivial Fixed Point**

We want the non-trivial fixed point such that **p\* = R(p\*)**. In the present case, it is a fourth-degree polynomial, as seen from above. Realize this depends on the size, b, of the renormalization. Solution of this polynomial root equation yields p\* = 0 and 1 (the trivial fixed points) and **p\* = 0.61804** . Try it! We now associate the non-trivial fixed point, p\*, with pC the critical point. The best know value for pC = 0.5927. So, with such a simple b=2 RG, we find a very good estimate (4% error) of the critical point. Similar results may be found in the thermodynamic version of RNG.

For an introduction into a thermodynamic version of RNG, where the partition function is renormalized to obtain a scaled interaction (so-called coupling constant) and the RG Equation for the partition function, see **R.J. Creswick, H.A. Farach, C.P. Poole, Jr., _Introduction to Renormalization Group Methods in Physics_**. The algebra is straightforward in the nearest-neighbor Ising case for a 1 and 2 Dimension, but grungy.
