
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



## 2. Finite-Size Scaling

Reduced coordinates are often convenient when discussing the scaling of thermodynamic quantities near a critical point. A standard example is the reduced temperature,

$$
t=\frac{T-T_c}{T_c},
$$

which measures the temperature relative to the critical temperature $T_c$. One can similarly introduce reduced densities, such as $\rho / \rho_c$, or, in percolation problems, a reduced occupation probability,

$$
x=\frac{p-p_c}{p_c},
$$

where $p$ is the site (or bond) occupation probability and $p_c$ is its critical value. These reduced variables provide convenient, dimensionless measures of distance from criticality and will be used repeatedly in what follows.

### 2.1.1 Experimental Evidence for Scaling

There is compelling experimental evidence that thermodynamic quantities exhibit such scaling behavior. When measured coexistence curves for a wide variety of simple fluids are plotted in reduced variables $T / T_c$ versus $\rho / \rho_c$, the data collapse onto a single universal curve (see, for example, E. Stanley, p. 10). Fitting the coexistence density difference $\rho-\rho_c$ along this curve shows that

$$
\rho-\rho_c \sim(-t)^\beta \quad \text { for } \quad T<T_c
$$

with $\beta \approx 0.33$. More careful analyses reveal a range $0.33<\beta<0.37$; for instance, in liquid helium one finds $\beta=0.354$. Similar scaling laws are observed for other response functions, such as susceptibilities, which can also be analyzed in terms of appropriate power laws in the reduced temperature.


Whether one is dealing with magnetic systems, ordinary fluids, or percolation models, the relevant order parameters and correlation measures-magnetization, density differences, pair-correlation functions, correlation lengths, and related quantities-all display analogous scaling behavior near their respective critical points. In the magnetic case, central quantities include (i) the magnetization $M(T)$, (ii) the isothermal susceptibility $\chi(T)$, (iii) the correlation length $\xi(T)$, and (iv) the zero-field specific heat $C(T)$. For percolation, the analogous set would consist of (i) the spanning probability $p_{\infty}$ (which plays the role of an order parameter), (ii) the mean cluster size $S(p)$, and (iii) the correlation length $\xi(p)$ that characterizes the typical size of connected clusters.


### 2.1.2 Scaling Properties

More quantitatively, these observables obey power-law scaling near the critical point.
The magnetization behaves as

$$
M(T) \sim(-t)^\beta, \quad 0.33<\beta<0.37, \quad\left(T<T_c\right),
$$

vanishing continuously as $T \rightarrow T_c^{-}$. The magnetic susceptibility diverges as

$$
\chi(T) \sim|t|^{-\gamma}, \quad 1.3<\gamma<1.4
$$

reflecting the growth of the response to an applied field. The correlation length scales as

$$
\xi(T) \sim|t|^{-\nu},
$$

where the exponent $\nu$ depends on the spatial dimension of the system and controls how rapidly the range of correlations diverges. Finally, the zero-field specific heat exhibits a (typically weak) singularity,

$$
C(T) \sim|t|^{-\alpha}
$$

with $\alpha \approx 0.1$ in many three-dimensional systems. The coefficients $\beta, \gamma, \nu, \alpha$, and their analogues for other observables are known as **critical exponents**, and they encapsulate the universal scaling properties of systems near continuous phase transitions.



### 2.1.3 Scaling with Finite System Size


Consider a simulation system with linear dimension $L$. Finite-size scaling can be understood by examining how the correlation length $\xi(T)$ compares with $L$. When $\xi(T) \ll L$, the system behaves essentially as if it were infinite. In this case, correlations remain local, do not "feel" the boundaries, and bulk power laws such as $M(T) \sim (-t)^\beta$ (for $T<T_c$ ) are expected to hold. As the temperature approaches the critical region, however, $\xi(T)$ grows. Once $\xi(T)$ becomes comparable to $L$, the correlation length can no longer increase significantly. In this case, its growth is effectively cut off by the system size. In this regime, the simple infinite-system law $M(T) \sim (-t)^\beta$ is no longer applicable, because the would-be divergence of $\xi$ is replaced by saturation at $\xi \sim L$, and observables acquire a nontrivial dependence on $L$.

Near criticality, the correlation length follows the power law

$$
\xi(T) \sim|t|^{-\nu},
$$

where $t=\left(T-T_c\right) / T_c$ is the reduced temperature and $\nu$ is the correlation-length exponent. The condition $\xi(T) \sim L$ therefore implies

$$
L \sim|t|^{-\nu} \quad \Longrightarrow \quad|t| \sim L^{-1 / \nu}.
$$


Equivalently, for a system of finite size $L$, the apparent critical temperature $T_c(L)$ -for example, the temperature at which some response function is maximal-shifts away from the infinite-system value $T_c(\infty)$ according to the finite-size scaling relation

$$
\left|T_c(L)-T_c(\infty)\right| \sim L^{-1 / \nu}
$$


This is often referred to as the scaling relation for $T_c(L)$. For a two-dimensional system such as the square-lattice Ising model, one has $\nu=1$, so $1 / \nu=1$. In that case the shift scales as

$$
T_c(L)-T_c(\infty) \sim \frac{1}{L},
$$

and an extrapolation of $T_c(L)$ versus $1 / L$ should converge, within error bars, to the exact critical temperature $T_c(\infty) \approx 2.269$.

In practice, one convenient way to determine $T_c(L)$ from simulations is to compute the specific heat per site $C_V(L, T)$ as a function of temperature for various system sizes $L=4,8,16,32, \ldots$. For each $L$, the temperature $T$ at which $C_V(L, T)$ attains its maximum is taken as the finite-size critical temperature $T_c(L)$. The specific heat can be expressed in terms of energy fluctuations as

$$
C_V(T)=\frac{\left\langle E^2\right\rangle-\langle E\rangle^2}{k_B T^2},
$$

which makes clear that $C_V$ measures how broadly the system's energy is distributed among accessible configurations. The larger the fluctuations $\left\langle E^2\right\rangle- \langle E\rangle^2$, the higher the specific heat and the richer the ensemble of thermally accessible states.


One might ask why not simply plot $\langle E\rangle$ versus $T$ to locate the transition, instead of examining $C_V(T)$. The reason is that for a continuous (second-order) phase transition, $\langle E\rangle(T)$ remains a smooth function of temperature (the singularity appears in its derivative with respect to $T$). The specific heat $C_V=\partial\langle E\rangle / \partial T$ exhibits a pronounced peak that sharpens and grows with system size, and in the thermodynamic limit this peak becomes a true divergence (when $\alpha>0$ ) or at least a cusp-like singularity. Thus $C_V(L, T)$, rather than $\langle E\rangle(T)$, is a much more sensitive diagnostic for pinpointing the location of the critical region and extracting $T_c(L)$.

Once $T_c(L)$ is known as a function of $L$, finite-size scaling can also be used to determine the critical exponents. At the critical point of the infinite system, the order parameter and other observables obey power laws such as

$$
M(T) \sim(-t)^\beta, \quad \chi(T) \sim|t|^{-\gamma}, \quad \xi(T) \sim|t|^{-\nu}, \quad C(T) \sim|t|^{-\alpha} .
$$


For a finite system, a standard finite-size scaling ansatz shows that at the (size-dependent) critical temperature $T=T_c(L)$, the order parameter scales with system size as

$$
M\left(T_c(L)\right) \sim L^{-\beta / \nu} .
$$


Thus, plotting $M\left(T_c(L)\right)$ versus $L$ on a log-log scale yields a straight line whose slope is $-\beta / \nu$. A similar analysis applies to other quantities. For example, the susceptibility at $T_c(L)$ scales as

$$
\chi\left(T_c(L)\right) \sim L^{\gamma / \nu},
$$

and, when $\alpha>0$, the specific heat peak typically scales as

$$
C_V^{\max }(L) \sim L^{\alpha / \nu} .
$$


In problems where the order parameter is of a different type-for instance, in percolation-the same logic holds. The spanning probability $p_{\infty}$ at the percolation threshold $p=p_c$ plays the role of an order parameter and obeys

$$
p_{\infty}\left(p_c, L\right) \sim L^{-\beta / \nu},
$$

while the mean cluster size $S(p)$ and the percolation correlation length $\xi(p)$ exhibit their own characteristic finite-size scaling forms. In all these cases, the critical exponents can be extracted from how observables depend on $L$ at or near the finite-size critical point, providing a route to determining $\beta, \gamma, \nu_{\text {, and }}$ related exponents.



### 2.1.4 Scaling Law for Homogeneous Functions


To formalize the notion of scaling, it is helpful to recall the concept of homogeneous and generalized homogeneous functions. A function $f(r)$ is said to scale (or to be homogeneous) if, for all values of $\lambda$,

$$
f(\lambda r)=g(\lambda) f(r) .
$$


An example is $f(r)=B r^2$, for which

$$
f(\lambda r)=B(\lambda r)^2=\lambda^2 f(r),
$$

so $g(\lambda)=\lambda^2$. In general, for a homogeneous function, the scaling function $g(\lambda)$ cannot be arbitrary. It must be a pure power,

$$
g(\lambda)=\lambda^p,
$$

where $p$ is called the degree of homogeneity. Once $f\left(r_0\right)$ and $g(\lambda)$ are known, the value of $f(r)$ at any $r$ can be obtained by choosing an appropriate scaling factor $\lambda=r / r_0$.

A generalized homogeneous function involves more than one variable and can be written in the form

$$
f\left(\lambda^a x, \lambda^b y\right)=\lambda f(x, y) .
$$


Here the variables $x$ and $y$ scale with possibly different exponents $a$ and $b$, but the function as a whole is homogeneous of degree 1 with respect to the transformation. There is no extra factor $\lambda^p$ on the right-hand side because one can always rescale $\lambda$ by $\lambda^{1 / p}$ and redefine the exponents as $a^{\prime}=a / p$ and $b^{\prime}= b / p$ without loss of generality. The important point is that generalized homogeneous functions allow different directions in the $(x, y)$ space to scale with different exponents, while preserving an overall scaling form.




### 2.1.5 Static Scaling Hypothesis for Thermodynamic Functions


The (ad hoc) static scaling hypothesis asserts that the thermodynamic potential $G(t, H)$ near a continuous phase transition is a generalized homogeneous function of the reduced temperature $t$ and magnetic field $H$. More precisely, one postulates that there exist exponents $a_t$ and $a_H$ such that

$$
G\left(\lambda^{a_t} t, \lambda^{a_H} H\right)=\lambda G(t, H)
$$

for all $\lambda>0$. If $G(t, H)$ has this property, then all other free-energy representations (Helmholtz, Gibbs, etc.) obtained by Legendre transforms will also be generalized homogeneous, since Legendre transforms preserve homogeneity.

Thermodynamic observables are derivatives of $G(t, H)$ and therefore inherit corresponding scaling forms. For instance, the magnetization is given by

$$
M(t, H)=-\frac{\partial G(t, H)}{\partial H} .
$$


Differentiating the scaling form of $G$ with respect to $H$ and using the chain rule (try it!), one finds that

$$
\lambda^{a_H} M\left(\lambda^{a_t} t, \lambda^{a_H} H\right)=\lambda M(t, H) .
$$


This implies that, at zero field $H=0$, the magnetization satisfies

$$
M(t, 0)=\lambda^{1-a_H} M\left(\lambda^{a_t} t, 0\right) .
$$


Choosing $\lambda=(-t)^{-1 / a_t}$ for $t<0$ gives

$$
M(t, 0)=(-t)^{\left(1-a_H\right) / a_t} M(-1,0) .
$$


Since we already know from standard critical behavior that

$$
M(t, 0) \sim(-t)^\beta \quad \text { as } \quad t \rightarrow 0^{-},
$$


we can identify the order-parameter exponent as

$$
\beta=\frac{1-a_H}{a_t} .
$$


The same procedure applies to other observables that are derivatives of $G(t, H)$. For example, the isothermal susceptibility $\chi_T(t, H)$ is given by

$$
\chi_T(t, H)=\frac{\partial M(t, H)}{\partial H},
$$

and its scaling form implies power laws of the form

$$
\chi_T(t, 0) \sim(-t)^{-\gamma^{\prime}} \quad \text { for } t \rightarrow 0^{-}, \quad \chi_T(t, 0) \sim t^{-\gamma} \quad \text { for } t \rightarrow 0^{+},
$$

with

$$
\gamma^{\prime}=\frac{2-a_H}{a_t}, \quad \gamma=\frac{2-a_H}{a_t},
$$

so that $\gamma^{\prime}=\gamma$ in this simple scaling picture. Analogous relations can be derived for the specific heat, correlation length, and other thermodynamic quantities, all expressed in terms of the two basic scaling exponents $a_t$ and $a_H$.

Thus, from the scaling form of the thermodynamic functions, all critical exponents can be written as ratios of just two quantities, $a_t$ and $a_H$. By plotting thermodynamic observables according to the scaling relations implied by the generalized homogeneity of $G(t, H)$, one can in principle determine $a_t$ and $a_H$, and hence obtain the full set of critical exponents. The same style of analysis can be extended to other thermodynamic functions or order parameters, yielding a network of scaling equalities among exponents-relations that, in more rigorous treatments, often appear as inequalities. It is important to remember that the static scaling hypothesis is an assumption rather than a theorem, but it is strongly supported by experimental data, simulations, and renormalization-group theory, and forms the conceptual backbone of the modern theory of critical phenomena.



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
