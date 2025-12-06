# Short-Ranged Intramolecular Potentials

## Features of Interaction

- Applies between **all particles** in the system, pairwise and additive.
- Some force fields **exclude** interactions between certain bonded particles:
  - 1–2 (bonded): ignored
  - 1–3 (two bonds apart): ignored
  - 1–4 (three bonds apart): rescaled (e.g., by 50%)

- Interactions are "**short-ranged**" and can be **truncated** at a **cutoff** $r_c$:
  - $\Delta u = 2\pi \rho \int_{r_c}^{\infty} \underbrace{r^2 \underbrace{u(r)}_{\sim 1/r^6}}_{\sim 1/r^4} dr $ converges
  - In MD, truncate forces: $ F(r > r_c) = 0 $

The non-zero range of the short-ranged potential should not be greater than half of the smallest simulation box, otherwise the atom would "feel" itself if [periodic boundary conditions](./periodic-boundary-conditions.md) are imposed.

## Nonbonded Potentials

### Lennard-Jones Potential

 $ u(r) = 4\varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right] $

Here,
$\epsilon$ is maximal well-depth of the attractive part of the potential. It is related to the cohesive energy.
Here, $\sigma$ is an effective radius where the "hard core" repulsion is starting to be felt. (Note that $\sigma$ is about 0.34 nm and $$\varepsilon/k_B$ is about 120 K for liquid Argon. Warning: these are not properties arising from isolated pairs of Argon atoms.)

It is worth mentioning that the L-J potential has been used to study dynamics in super-cooled liquids, in an effort to understand glass transitions, to study packing of hard-spheres of varying radii, and many other situations. Regarding L-J, as well as many of those to follow, there is a nice review of classical systems if interested (see, Caccamo, "Integral Equation Theory Description of Phase Equilibria in Classical Fluids," Physics Reports 274, 1 (1996)).

LJ is by far the most widely used intremolecular potential. We will focus on the Lennard-Jones (LJ) potential due to its common use.

```{tip}
One of the reasons why the LJ potential is so popular, is that one can re-use the $ \left( \frac{\sigma}{r} \right)^6$ term by squaring it - thus reducing computational cost. This is much less important with improved hardware.
```

### Mie Potential

$ u(r) = C \varepsilon \left[ \left( \frac{\sigma}{r} \right)^n - \left( \frac{\sigma}{r} \right)^m \right] $
with $ C = \frac{nm}{n - m} \left( \frac{n}{m} \right)^{\frac{m}{n - m}} $

This is a generalized LJ potential.

### Morse Potential

$ u(r)=D_{e}\left(1-e^{-a(r-r_{e})}\right)^{2}$

Here $r$ is the distance between the atoms, $r_{e}$ is the equilibrium distance,
$D_{e}$ is the well depth (defined relative to  dissociated atoms at $r \rightarrow \infty$), and
$a$ controls the 'width' of the potential (the smaller  $a$ is, the larger the well).

The Morse potential offers the same properties as Lennard-Jones, however, it allows more intermediate range of interaction and it is more of a bonding-type potential. Most elements, esp. metals, that form solids in the Periodic Table can be fit with this type of potential, at least locally near their equilibrium lattice constant, by choosing the lattice constant, s, the bulk moduli, and the cohesive energy. This is the basis for the so-called Rose Equation of State and the way the Effective Medium Theory chooses to reduce parameters in the potential.


```{note} LJ vs Morse
Generally: the Morse potential is well suited for modeling diatomic molecules that are bonded together. On the other hand, the Lennard-Jones potential is better suited for modeling inter-molecular forces between atoms that are not bonded together.
```

### Exponential-6 Potential

$ u(r) = -A e^{-Br} + \frac{C}{r^6} $

### Yukawa

Single Yukawa
$ u(r)=A{\frac {e^{-\alpha r}}{r}}$

Double Yukawa
$ u(r)=A{\frac {e^{-B r} + e^{-C r}}{r}}$

For those in Physics, you may have come across this potential in regards to nuclear physics, in fact interactions within the nucleus, a field in which Yukawa was honored with a Nobel Prize.  Nonetheless, this is a potential with a functional form which has some appealing properties (see Caccamo, for example).

For Soft-sphere-like interactions, the Yukawa offers advantages over the Soft-sphere potential for analytic investigations of thermodynamics. In addition, it can be shown that the Double-Yukawa form adequately reproduces the L-J spatial behavior, however, it offers the ability to perform useful analytic proceedures to study free-energy variationally in some restricted systems (e.g., "Variational Theory of Phase Separation in Binary Liquids," Foiles and Ashcroft, J. Chem. Phys. 75 3594 (1981)).

### Hard Sphere

$$
u(r) =\begin{cases}0&{\text{if}}\quad  r\geq \sigma \\
\infty &{\text{if}}\quad r <\sigma \end{cases}
$$

This "wall-like" potential is very useful in some contexts.  Also a systems of hard spheres is a very nice idealized problem.  And, Percus and Yevik offered an exact solution of the thermodynamic properties for this potential, obtained using Laplace Transforms, which use exponentials like exp(-ar) rather than exp(ikr) like Fourier Transforms. In fact, the Hard-Sphere free energy is purely entropic, because of the potential. Later Liebowitz (1964) provided exact solution for a systems with varying hard-sphere radii, i.e. a mixed system, such as Ar-Kr. The Hard-Sphere pair-correlation functions have also been shown to be exact for systems with potentials not too different from Hard-Sphere (Foiles and Ashcroft, Phys. Rev. A 24, 424 (1981)).
Hard spheres are obviously short-ranged and non-bonding, leading only to entropic behavior.

### Soft Sphere

$u(r) = (r/\sigma)^{-n}$

Again, $\sigma$ and $n$ can vary: $n \approx 1$ is soft and the larger $n$ the harder the repulsion. Also, this offers the useful analytic form for some mathematic investigations into properties.

## Force Calculation

$$
 \vec{F}_{ij} &= -\nabla_i u(r_{ij}) \\
 &= \underbrace{-\frac{du}{dr}}_{=F(r)} \nabla_i {r}_{ij} \\
 &= - F(r)\hat{r}_{ij}
$$

```{example} Lennard-Jones Force
$$
u(r) = 4\varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right]
$$

$$
 F(r) &= -\frac{du}{dr}\\
 &= -4\varepsilon \left[ -12\frac{\sigma^{12}}{r^{13}} + 6 \frac{\sigma^{6}}{r^{7}}\right]\\
 &= \frac{24\varepsilon}{r} [2 \left( \frac{\sigma}{r} \right)^{12}  - \left( \frac{\sigma}{r} \right)^{6} ]
 $$
When written in this form, the  $\left( \frac{\sigma}{r} \right)^6$-term can be reused from the $u(r)$ calculation.
```

```{tip}
Write $F_i= -F(r) \hat{r}_{ij} = - \frac{F(r_{ij})}{r_{ij}} \vec{r}_{ij}$. Then one can write the LJ force in such a way, that only ever $r^2_{ij}$ is needed, not $r_{ij}$, thus avoiding the need for an expensive sqrt operation.
```

## Truncating and Shifting

Energy ($E= T+V$) conservation is impacted by the way how a short-ranged potential is cut, or cut and shifted.

**Truncate**:

$$
u(r) = u_o(r)\theta(r_c-r) = \begin{cases}  &u_o(r)\quad r\leq r_c \\
&0 \quad r\ge r_c  \end{cases}
$$

Note that this means that the force has a "jump" at the cutoff, because $\frac{\partial u}{\partial r}$ now has a $\delta(r_c-r)$ term from the Heaviside function $\theta$, if $U_o(r_c) \neq 0$. These jumps contribute to the energy and can compromise energy $E=U+T$ conservation.

**Truncate** and **shift**:

$$
u(r) = \left[u_o(r)-u_o(r_c)\right]\theta(r_c-r) =\begin{cases}  u_o(r)-u_o(r_c)\quad r\leq r_c \\
0 \quad r\ge r_c  \end{cases}
$$

Here $\frac{\partial u}{\partial r}$ is finite but might be discontinous.
Shifted potentials do contribute, i.e. technically their Hamiltonian and phase space is not identical to the original potential anymore. This means that properties like their phase boundaries and critical points will be changed as well.  Moreover, the force is discontinous at $r_c$. (e.g. for L-J, the discontinuity is $0.039 \epsilon/\sigma$ for $r_c=2.5$.) This discontinuity can cause numerical instabilities, which may be eliminated using a **shifted-force potential**, for example. One can apply **smoothing functions**, e.g. polynominals (xplor).

```{admonition} Derivative of the Heaviside function
:class: dropdown

$$
\frac{d}{d x}\left[f(x) \theta\left(x-x_0\right)\right]=f^{\prime}(x) \theta\left(x-x_0\right)+f\left(x_0\right) \delta\left(x-x_0\right)
$$

where $\theta$
$$
\theta\left(x-x_0\right)= \begin{cases}1, & x \geqslant x_0 \\ 0, & x<x_0\end{cases}
$$
is the Heaviside function.

Define a test function $\phi(x)$ that goes to 0 sufficiently quickly as $x \rightarrow \pm \infty$.
$$
\int_{-\infty}^{\infty} dx \left[f(x) \theta\left(x-x_0\right)\right]^{\prime} \phi(x) =f\left(\left.x\left|\theta_{x-x_0}\right| \phi(x)\right|_{-\infty}^{\infty}-\int_{-\infty}^{\infty} d x f(x) \theta\left(x-x_0\right) \phi^{\prime}(x)\right. \\
$$

by parts, $\phi$ vanishes at $\infty$.

$$
 =-\int_{x_0}^{\infty} dx f(x) \phi^{\prime}(x) \\
 =-\left[\left.f(x) \phi(x)\right|_{x_0} ^{\infty}-\int_{x_0}^{\infty} dx f^{\prime}(x) \phi(x)\right]
 $$
 Then,

 $$
=-\left[-f\left(x_0\right) \phi\left(x_0\right)-\int_{x_0}^{\infty} d x f^{\prime}(x) \phi(x)\right] \\
$$

$\phi$ vansles at $\infty$

$$
 =f\left(x_0\right) \phi\left(x_0\right)+\int_{x_0}^{\infty} dx f^{\prime}(x) \phi(x)
$$

with $\int_{-\infty}^{\infty} d x f(x) \delta\left(x-x_0\right)=f\left(x_0\right)$.

$$
=\int_{-\infty}^{\infty} d x f\left(x_0\right) \delta\left(x-x_0\right) \phi(x)+\int_{-\infty}^{\infty} d x f^{\prime}(x) \theta\left(x-x_0\right) \phi(x) \\
=\int_{-\infty}^{\infty} d x \underbrace{\left[f\left(x_0\right) \delta\left(x-x_0\right)+f^{\prime}(x) \theta\left(x-x_0\right)\right]} \phi(x)
$$

combine terms.

Note that could also choose $f(x)$ rater them $f\left(x_0\right)$. Since $\delta\left(x-x_0\right)$ "cicks on" only at $x_0$, it doesn't really care about the other values of $x$.

This is a "product rule" for Heaviside function.
```

**Shifted-force Potential**:

$$
V^{s f}(r)=V(r)-V\left(\mathbf{r}_c\right)-\nabla V\left(\mathbf{r}_c\right)\left(\mathbf{r}-\mathbf{r}_c\right) \quad \text { for } r \leq r_c \text { and } 0 \text { for } r \gt r_c
$$

The gradient term now makes force continuous and zero beyond the cut-off. Note that this really is a different potential now and extra care must be taken to either recover original thermodynamics, or be statisified with current model. Recovering of thermodynamics can be done in some cases by perturbation theory or long-range corrections.

**Smoothing**:

Instead of cutting and shifting smoothing functions can be employed to ensure that both the
energy and the force go smoothly to zero at the desired cutoff distance. Polynominal interpolations or splines can be used.

```{example} Weeks-Chandler-Anderson Potential
Use truncate and shift scheme at $r_c=2^{1/6}\sigma$ for LJ potential. The result is a purely repulsive potential, the WCA potential, often used to model purely excluded volume interactions.
```

For  truncating, truncating and shifting, and or smoothing, **thermodynamic properties** will be influenced by the exact scheme. Those effects can be corrected with long-range integral approximations/corrections.

## Mixing Rules

For unlike atom types $i$ and $j$, use mixing rules on LJ parameters. There are many different ones, falling into two categories, arithmetic $x_{ij}=(x_j+x_i)/2$ or geometric $x_{ij}=\sqrt{x_i\cdot x_j}$.

Commonly used mixing rules are:

**Lorentz-Berthelot**:
test

$
\sigma_{ij} = \frac{\sigma_{ii}+\sigma_{jj}}{2}
\epsilon_{ij} = \sqrt{\epsilon_{ii}\epsilon_{jj}}
$

**Kong**:
test

$
\epsilon_{ij}\sigma_{ij}^{6} = \left(\epsilon _{ii}\sigma_{ii}^{6}\epsilon_{jj}\sigma_{jj}^{6}\right)^{1/2}
 \epsilon_{ij}\sigma_{ij}^{12} = \left[{\frac {(\epsilon_{ii}\sigma_{ii}^{12})^{1/13}+(\epsilon_{jj}\sigma_{jj}^{12})^{1/13}}{2}}\right]^{13}
$

### Criteria for Choosing a Potential

What science are you wanting to address?  What does it require, as far as accuracy of forces or energetics, and so on?
The three main criteria for choosing a potential are:

- Accuracy: Reproduce properties of interest as closely as possible.
- Transferability: Applicable to more situations for which the potential was NOT fit.
- Computational Speed: Force calculations are the most time consuming part of simulation, e.g., so they should be as fast as possible (meaning potentials should be as simple as possible). A 2-body potential $V(rij)$  depends only on distance between atoms, i.e., $|ri-rj|$; whereas a 3-body potential will depend on orientation which will require more computation.

Typical emphasis for various disciplines include:

- Chemistry:    Accuracy
    Rate constants, for example, require very accurate reaction barriers.
- Statistical Mechanics:    Computational Speed
    Complexity can result from simple potentials (e.g., the near-neighbor Ising Model).
- Materials Science:    Computational Speed   (due to complexity; in some case all 3)
    Calculation of equilibrium positions of atoms around defects, etc., for comparison to
    EXAFS or LEED signals, or High-resolution TEM.
- Biochemistry:    Perhaps all 3
    Protein structures with different conformations using approximate forces.

Finding the actual parameterizations for the analytic functions one has chosen is an important but perhaps difficult task. It can be technically elaborate and an "art form" in itself.
Many applications use no more than 3-body terms, which implicitly assumes higher-order terms are negligible to the energy and forces. This is equivalent to assuming a rapidly convergent interaction series.  Basically, a general 3-body equation is not known and forms are chosen for particular interest, e.g. Si (3-body with angular bonding information required) vs. Au (metallic 2-body that is density dependent). Notably, convergence of many-body interactions really may not converge very rapidly (if at all).

Therefore, what do you want to model, how accurate must you be, and how long/much are you willing to spend calculating?

### Commonly Used Potentials

Here are some common approaches, with various levels of sophistication, to obtaining V(r) which in turn determines the forces:

- Analytic potential based on functional forms, built-in physics, and assumptions.
- Potentials derived from concepts from quantum-mechanical bonding arguments, e.g., EAM, EMT, Bond-order, Finnis-Sinclair.
- Forces obtained directly via electronic-structure (quantum-mechanical-based) calculations, e.g., Carr-Parrinello Phys. Rev. Lett. 55, 2471 (1985).
- Force-Field Methods (used widely in chemistry) are tremendously valuable, but often not transferable.  Usually, these are much simpler in form and can be parameterized to achieve very good molecular structures.
For example, to model Polyethylene, one requires a potential to deal with   bond-stretching (2-body), angular bending (3-body), stretch-stretch and stretch-bend (3-body + higher), bend-bend (4-body + higher). Such potentials may be composed of pieces: (1) intramolecular (Valence Force Field with bonded atoms in molecule) and (2) intermolecular (L-J + Coulomb interaction for non-bonding interaction).
-Combination of approaches 2 and 3 are being used in order to increase system sizes yet provide more realistic representations of the systems. (See, for example, multiscale scale materials science modeling.)

Approaches 1 and 2 fit parameters from chosen functional form via some restricted data base of physical properties of the system (or sub-systems) of interest.  For molecules, e.g., bond length, cohesive energies, vibrational energies, etc., could be used. For solids, lattice constants, elastic moduli, configurational or defect energies could be used, which may be also modified to include molecular data, or lower-symmetry data of interested in surfaces.  Based on electronic-structure methods, approach 3 requires a large computational effort and restricts system sizes, so while important it has limited application to large simulations.  (See Review, A.E. Carlsson, Solid State Physics 43, 1 (1990).)

## Three Common Situations: Noble Gases, Metals, Covalently-bonded Molecules

Let us now discuss some of the theoretical ideas that go into determining potentials. Looking at the periodic table, there are three common situations.

### Noble Gases

These are the non-bonding, rare gases (e.g., Kr and Ar) where the electronic shells are closed. Thus means they are spherically symmetric, with rather weak, but long-ranged, van der Waals type interactions. They were the first systems to be simulated and pair potentials work best for them. For this case, a commonly used pair potentials is the Lennard-Jones (6-12) potential.

At large distances (r >> r0, the equilibrium distance) one can undestand the interaction by considering how two oscillators would interact, giving an r-6 attraction, where the coefficient is determined by the atomic polarizibility (arising due to correlations between electron clouds surrounding atoms and give van der Waals (dipole-dipole) interactions.) On the other hand, at short distances (r << r0), the potentials are strongly repulsive because of the Pauli exclusion principle (electrons are fermions). Lennard-Jones assumed a stronger inverse power law, conveniently r-12. One should not think the Lennard-Jones (L-J) potential as anything more fundamental than this.

Even for Argon it is only accurate to 10% or so. And three-body potentials can be significant at the 10% level (more in case of polarizable species). An example of the difference between the simple L-J 6-12 potential and one that has been constructed using a large quantity of experimental data is on pg. 8 of A&T. The potentials that are fit to bulk data are really effective potentials and could be somewhat different than the real 2-body potential that would be determined from gas-phase data because they include corrections for three- and higher-body interactions, for, in effect, the two-body potential is obtained by averaging over the third spatial coordinate:

$$
V(r) = \frac{1}{2} \sum_{i\neq j} V_2(r_{ij})，\qquad
V_2(r_{ij})=\frac{1}{V} \int d\mathbf{r}_k\, V_3(\mathbf{r}_i,\mathbf{r}_j,\mathbf{r}_k)
$$

Hence, the effective potentials can be dependent upon density and less so on temperature.

## Metals: Other problems with 2-body interactions

How about metals? Metals are characterized by a rare gas shell plus a number of valence electrons. Pair potentials do not work terribly well, because the electrons will be delocalized. If one does use a pair potential, it must be softer than the Lennard-Jones form, for example a Morse potential (sum of exponentials.) The Morse potential is often fit by choosing equilibrium lattice constant, the bulk moduli, and the cohesive energy. This is the basis for the so-called Rose equation of state and is the form used in Effective Medium Theory (see below).

The major problem with pair potentials for solid metals is that they have no environmental dependence so the a bulk atom is too much like a surface atom. For metals, the strength of the individual bonds decrease as the local environment becomes more crowded, corresponding to the behavior expected from Pauli's "exclusion principle."  In contrast, with 2-body potentials the "strength" of the individual bonds does not depend on environment. Thus, capturing the environmental dependence of bonding is crucial for metallic systems.

Failure:  An example of how 2-body interactions like L-J fail is the relaxation of a surface layer of atoms in a metallic system, like Cu. Pair potentials predicted expansion of surface layer, whereas, most metals contract inward to increase the charge density and, therefore, the metallic bonding.
In the formula page we show the potential used in the Embedded Atom Method (EAM) for metals. The basic idea is that metallic bonding involves ions in an electron sea so the total potential energy is the sum of direct ion-ion interactions (e.g., to keep ion cores from overlapping) and the interactions between ion and the electron sea. One assumes that locally there is an electroni charge density coming from the postive charge of the ion and nearby ions and that the interaction is some function of this density. This latter term is then a true many-body potential. The EAM works well for spherically symmetric atoms (close-packed solids) such as Cu, Al, and Pb.

References and other related concepts, derived from Quantum Mechanics, are:

- Embedded Atom Method [EAM] - Daw and Baskes, Phys. Rev. B 29, 6443 (1984); Foiles, Baskes, and Daw, Phys. Rev. B 33, 7983 (1986)
- bond-order potential - e.g., Horsfield, J. Phase Equil. 18, 573 (1997); Aoki et al., ibid. 614; and applications, e.g.: Lagana et al., J. Chem. Phys. 108, 3886 (1998); Girshick et al, Phil. Mag. A77, 981 (1998)},
- Effective Medium Theory [EMT] - Jacobsen, Norskov, Puska, Phys. Rev. B35, 7423 (1987).
- Finnis-Sinclair (FS)- Phil. Mag A50, 45 (1985); Tersoff Phys. Rev. B37 6991 (1988).
- Glue Model - e.g., Ercolessi et al., Phil Mag. A58, 23 (1988)

These methods have very different parameterizations and functions. In addition, while they usually appear composed of 2-body-type potentials, all really are cleverly disguised MANY-body potentials.

## Covalently-bonded Molecules

When molecules form bonds it is best to put that in directly. Silicon has been studied extensively since it is so important for the semiconductor industry. Silicon forms bonds with the nearest 4 atoms with a local tetrahedron structure. This is very unlikely to ever come out of a pair potential so it has to be put in.

In the formula page we give the well-known potential function for silicon: the Stillinger-Weber potential. It contains an explicit term which forces the angle between nearby triples to stay close to 109 degrees and has been adjusted to giving roughly the lattice constant, the cohesive energy, the melting point and liquid structure. Unfortunately, this does not work well for other polytypes found under pressure, e.g., for there is no bond coordination changes or bending allowed: NO TRANSFERABILITY. There is a recent review article Balamane, Phys. Rev. 46, 2250 (1992) describing how well various potentials work on silicon. They conclude that the potentials, even if they have been carefully tuned, do not really describe all aspects of pure silicon terribly well. That is why the Car-Parrinello technique is viewed as an advance (even though it is slow). One gets a better (but still not perfect) potential, without have to adjust lots of parameters.

For other systems there are extensive codes which handle real biomolecular systems (GROMOS, CHARM, AMBER ...). They use an experimental data base and put in specific terms for bond lengths, bond angles torsion angles. etc. They are really quite complicated because they have to distinguish between many local bonding arrangements. Even so, one should never trust the accuracy of the empirical potentials. The errors can still be quite large even if a lot of data has been put in. This is because the potential surface is so highly dimensional and there are so many different possible combinations of atoms that experiment can only hope to sample a very few of them.

## Additional Resorces

- more short-ranged potentials, as implemented in:
  - [hoomd-blue](https://hoomd-blue.readthedocs.io/en/v5.2.0/hoomd/md/module-pair.html)
  - [LAMMPS](https://docs.lammps.org/pair_style.html)
  - [GROMACS](https://manual.gromacs.org/current/reference-manual/functions/nonbonded-interactions.html)
- more mixing rules from [Wikipedia](https://en.wikipedia.org/wiki/Combining_rules)

test
