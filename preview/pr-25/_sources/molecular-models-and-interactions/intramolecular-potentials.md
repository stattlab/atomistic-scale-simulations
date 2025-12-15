---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Intermolecular Potentials

In addition to nonbonded interactions (e.g. Lennard--Jones and Coulomb), molecular simulations must describe the *internal* geometry of molecules:
how atoms are held together by covalent bonds and how those bonds can bend and twist. These "bonded" or "intramolecular" interactions are usually written in terms of: 

- bond lengths between pairs of atoms $i$ and $j$,
- bond angles between triplets $i,j,k$, and
- dihedral (torsional) angles between quadruplets $i,j,k,\ell$,

in {numref}`bonds-angles-fig` most typical intermolecular potentials for a molecule are shown.

```{figure} ./_figures/intramolecular-def.png
:alt: Visualization of bonds, angles, and dihedrals in a molecule
:width: 300px
:align: center
:name: bonds-angles-fig

Visualization of bonds, angles, and dihedrals in a molecule with four atoms.

```

The total bonded **intramolecular** energy is conventionally written as:

$$
 U = \sum_{\text{bonds}, {i,j} } U_b(r_{ij}) + \sum_{\text{angles}, {i,j,k}} U_\theta(\theta_{ijk}) + \sum_{\text{dihedrals}, {i,j,k,l} } U_\varphi(\varphi_{ijkl})
 $$

where:

- $r_{ij} = \lVert \mathbf r_i - \mathbf r_j \rVert$ is the bond length,

- $\theta_{ijk}$ is the angle at atom $j$ between bonds $ij$ and $jk$, and

- $\varphi_{ijkl}$ is the dihedral angle defined by the two planes
$(i,j,k)$ and $(j,k,\ell)$.

For molecular dynamics, we do not only need energies but also forces. For any potential $U({\mathbf r_i})$ the force on atom $i$ is given by:

$$
\mathbf F_i = - \nabla_i U
= - \left(
    \frac{\partial U}{\partial x_i},
    \frac{\partial U}{\partial y_i},
    \frac{\partial U}{\partial z_i}
  \right) .
$$

For bonded terms this is slightly more involved than for a simple pair potential, because we must use the chain rule:

we differentiate $U$ with respect to $r_{ij}$, $\theta_{ijk}$, or $\phi_{ijkl}$,
and then differentiate those geometric quantities with respect to the atomic coordinates.

In actual simulations under periodic boundary conditions, distances such as $r_{ij}$ are almost always computed with a ``minimum image'' distance function, so that a bond crossing a periodic boundary still has the correct length.


To compute a conservative force in general:
$ \vec{F}_i = -\nabla_i U $ where $\nabla_i = \frac{\partial}{\partial r_i}$ is
the gradient with respect to $r_i$.

## Bond Potentials

As shown in {numref}`bond-def-fig`, the **bond length** between particle $i$ and $j$ is given by

$ r_{ij} = \| \vec{r}_i - \vec{r}_j \| = \sqrt{(x_j-x_i)^2 + (y_j-y_i)^2 + (z_j-z_i)^2}$.

The **bond vector** is $ \vec r_{ij} =  \vec{r}_i - \vec{r}_j $.

```{figure} ./_figures/bond.png
:alt: Definition of bond distance.
:width: 200px
:align: center
:name: bond-def-fig

Definition of bond distance.

```

To obtain the force on a bond we need to compute

$$
 F_i = - \nabla_i U_b(r_{ij}) = - \frac{\partial U_b}{\partial r_i} \nabla_i r_{ij}\quad .
$$

For this, we need $\nabla_i r_{ij}$, which is

$$
\begin{aligned}
\nabla_i r_{ij} 
&= \frac{\partial}{\partial x_{i,\alpha}} \left[ \sqrt{(x_{j,\alpha}-x_{i,\alpha})(x_{j,\alpha}-x_{i,\alpha})} \right]\\
&= \frac{1}{2} \frac{-2 x_{j,\alpha}+2x_{i,\alpha}}{\sqrt{(x_{j,\alpha}-x_{i,\alpha})(x_{j,\alpha}-x_{i,\alpha})}}\\
&= - \frac{x_{j,\alpha}-x_{i,\alpha}}{\sqrt{(x_{j,\alpha}-x_{i,\alpha})(x_{j,\alpha}-x_{i,\alpha})}}\\
&= - \frac{r_{ij}}{|r_{ij}|}\\
&= - \hat r_{ij} \, .
\end{aligned}
$$


which is the unit vector pointing in the direction of the bond!

The force then is

$$
\begin{aligned}
F_i &= - \frac{\partial U_b(r_{ij})}{\partial r_{ij}} \, (-\hat r_{ij}) \\
    &= - F_b(r_{ij}) \hat r_{ij}, \quad 
       F_b(r_{ij}) \equiv - \frac{\partial U_b(r_{ij})}{\partial r_{ij}} \, .
\end{aligned}
$$


By symmetry we should have $\nabla_j r_{ij}=-\nabla_i r_{ji}$, meaning that

$$
F_j = F_b(r_{ij}) \hat r_{ij} \quad.
$$
This shows that for a bond, $F_i = -F_j$, which illustrates that action has a equal and opposite reaction.

Thus the bond force is always collinear with the bond and equal and opposite on the two atoms --- a direct manifestation of Newton's third law. In code, one can compute the force once and apply $\mathbf F_i$ and $-\mathbf F_i$ to save work.


```{tip}
Once can use the action reaction principle to save on computations by only computing either $F_i$ OR $F_j$ and then applying the equal action-reaction principle to save on calculations.
```

### Harmonic

$ U(r) = \frac{1}{2}k(r - r_0)^2 $

Here:

- $r_0$ is the equilibrium bond length,

- $k_b$ is the force constant (spring constant) with units of
energy / length$^2$.

This fixes the bond length to fluctuate around an average of $r_0$.

- Watch for factor of 2!
- Typically $ k \sim 10^3 \epsilon/l^2$ for "stiff" bond

This potential has a single minimum at $r_{ij} = r_0$ and grows quadratically as the bond is stretched or compressed. The factor of $1/2$ is conventional and very convenient: when we differentiate to obtain the force, the factor $2$ from the exponent cancels the $1/2$ in front, so $k_b$ directly controls the strength of the force.

```{code-cell} ipython3
:tags: [hide-cell]
from myst_nb import glue
import matplotlib.pyplot as plt
plt.style.use(['../_matplotlib/book.mplstyle'])
import numpy as np

# Harmonic bond potential
def harmonic_bond_potential(r, k, r0):
    return 0.5 * k * (r - r0)**2

# Harmonic bond force
def harmonic_bond_force(r, k, r0):
    return -k * (r - r0)

# Parameters
k = 1.0
r0 = 1.0
r_values = np.linspace(0.5, 1.5, 100)
U_values = harmonic_bond_potential(r_values, k, r0)
F_values = harmonic_bond_force(r_values, k, r0)

fig, axs = plt.subplots(1, 2, figsize=(6,3.5))

axs[0].plot(r_values, U_values,c='lightcoral')
axs[0].axvline(x=r0, linestyle='--',c='dodgerblue', label='$r_0$')
axs[0].set_xlabel('$r$')
axs[0].set_ylabel('$U_{\mathrm{bond}}(r)$')
axs[0].set_title('Harmonic Bond Potential')
axs[0].legend(frameon=False)

axs[1].plot(r_values, F_values,c='seagreen')
axs[1].axvline(x=r0, linestyle='--',c='dodgerblue', label='$r_0$')
axs[1].set_xlabel('$r$')
axs[1].set_ylabel('$F_{\mathrm{bond}}(r)$')
axs[1].set_title('Harmonic Bond Force')
axs[1].legend(frameon=False)

plt.savefig('./_figures/harmonic_bond.png')
```

````{example} Harmonic bond force
$ U_b = \frac{1}{2}k(r - r_0)^2 $, so

$ F_b = \frac{\partial U_b}{\delta r_{ij}} = -k (r_{ij}-r_0)$, leading to

$$
F_i &= + (r_{ij}-r_0) \hat r_{ij}\\
F_j &= - (r_{ij}-r_0) \hat r_{ij} \quad .
$$

If $r_{ij}>r_0$, the bond is streched past $r_0$ and particle $i$ moves toward $j$, and $j$ toward $i$. If $r_{ij}<r_0$, the bond is compressed below the set point $r_0$ and particle $i$ moves away from $j$, and $j$ away from $i$.

```{figure} ./_figures/harmonic_bond.png
:alt: Plot of the harmonic bond potential and force
:width: 400px
:align: center
:name: bond-fig

Bond potential and force as function of bond length $r$.
```
````
**Physical picture**.

- If $r_{ij} > r_0$, the bond is stretched:
$r_{ij} - r_0 > 0$, so $F_b < 0$ and the force pulls the atoms
\emph{toward} each other to restore the equilibrium distance.

- If $r_{ij} < r_0$, the bond is compressed:
$r_{ij} - r_0 < 0$, so $F_b > 0$ and the force pushes the atoms
\emph{apart}.

**Example**.

In an all-atom force field, a typical stiff covalent bond might use
$k_b \sim 10^3$ (in reduced units) so that the bond length fluctuates only
slightly around $r_0$ during the simulation.


### FENE (Finite Extensible Nonlinear Elastic)

For polymers and coarse-grained models it is often desirable to prevent bonds from stretching arbitrarily far. The FENE potential does exactly this:

$ U(r) = -\frac{1}{2}k r_0^2 \ln\left(1 - \left(\frac{r}{r_0}\right)^2\right) $

Diverges at $r_0$, minimum at 0. This is usually used in conjuction with a repulsive, short-ranged force (WCA = cut LJ at minimum and shift up to get a purely repulsive potential).{cite}`weeks1971`

with parameters:

- $k_f$ --- FENE spring constant,

- $R_0$ --- maximum bond extension.

Key properties:

- $U_b^{\text{FENE}}$ has a minimum at $r_{ij}=0$.

- As $r_{ij} \to R_0$, the logarithm diverges and the potential
goes to $+\infty$:
the bond cannot extend beyond $R_0$ (*finite extensibility*).

- For moderate extensions ($r_{ij} \ll R_0$), the potential is roughly
quadratic and behaves similarly to a harmonic spring.

In practice FENE bonds are almost always combined with a short-range repulsive nonbonded potential (e.g.\ a Weeks--Chandler--Andersen or purely repulsive Lennard--Jones) so that the overall interaction has a finite minimum at a nonzero distance. A widely used parameter set in coarse-grained polymer
simulations is :

$k_f = 30$, $r_0 = 1.5$

(in reduced Lennard--Jones units), which allows bonds to stretch up to about 1.5 times their typical length before the potential diverges.

**Example.**
In the Kremer--Grest polymer model, beads connected by FENE+WCA bonds behave like flexible springs that can fluctuate but never break, making them ideal for studying polymer melts and entangled chains.{cite}`kremer1990`


```{code-cell} ipython3
:tags: [hide-cell]
from myst_nb import glue
import matplotlib.pyplot as plt
plt.style.use(['../_matplotlib/book.mplstyle'])
import numpy as np

# Define parameters for the potentials
k_harmonic = 850.0  # Harmonic bond constant
r0_harmonic = 0.96  # Harmonic equilibrium bond length

k_fene = 30.0      # FENE bond constant
R0_fene = 1.5      # FENE maximum bond extension
epsilon = 1.0
sigma = 1.0

# Define the range of bond distances (r)
r = np.linspace(0.9, 1.1, 500) # Adjust range based on potential parameters

V_harmonic = 0.5 * k_harmonic * (r - r0_harmonic)**2
arg_fene = 1 - (r / R0_fene)**2
V_fene =  -0.5 * k_fene * R0_fene**2 * np.log(arg_fene)

V_fene_wca = V_fene
r_rep = r[r<2**(1/6)]
V_fene_wca[r<2**(1/6)] += 4*epsilon*((sigma/r_rep)**12-(sigma/r_rep)**6)+ epsilon

fig, axs = plt.subplots(1, 1)

axs.plot(r, V_harmonic-np.min(V_harmonic),label='harmonic')
axs.plot(r, V_fene_wca-np.min(V_fene_wca), label='FENE+WCA')
axs.set_xlabel('$r$')
axs.set_ylabel('$U_{\mathrm{bond}}(r)-U_\mathrm{min}$')
axs.legend()

axs.set_ylim(0,6)

plt.savefig('./_figures/FENE_bond.png')
```


```{figure} ./_figures/FENE_bond.png
:alt: Plot of the harmonic bond potential and force
:width: 400px
:align: center
:name: fene-bond-fig

FENE+WCA bond potential with standard parameters $R_0=1.5$ and $k=30$ compared to a harmonic bond potential with $r_0=0.96$ and $k=850$.
```

## Angle Potentials

The **angle** between three particles $i$, $j$, and $k$ is given by:

$$
\cos \theta_{ijk} = \frac{(\vec{r}_{ji} \cdot \vec{r}_{jk})}{|\vec{r}_{ji}||\vec{r}_{jk}|} = - \frac{(\vec{r}_{ij} \cdot \vec{r}_{jk})}{|\vec{r}_{ij}||\vec{r}_{jk}|}\quad .
$$

```{figure} ./_figures/angle.png
:alt: Definition of angle .
:width: 200px
:align: center
:name: angle-def-fig
Definition of angle.
```

Note the negative sign, i.e the two bond vectors point out from the middle particle $j$.

````{note}
 In polymers, angle θ is sometimes defined as the outer angle. This is less common in atomistic models, but be careful!

 ```{figure} ./_figures/outer-angle.png
:alt: Definition of angle.
:width: 200px
:align: center
:name: angle2-def-fig
Alternative definition of angle as the outer angle.
```
These two definitions can be easily converted into each other     $\theta_{ijk} = \pi - \theta'_{ijk}$. This is just a different convention, but it matters when specifying equilibrium
angles and when interpreting the potential. Computing $\theta_{ijk}$ explicitly requires an $\arccos$ operation, which is relatively expensive. Many force fields therefore write angle potentials
directly in terms of $\cos\theta_{ijk}$ to avoid calling $\arccos$ inside tight inner loops.
 ````

To compute the angle potential between three particles, we need to:

$$
\begin{aligned}
F_i &= -\nabla_i U_\theta (\theta_{ijk}) \\
    &= - \frac{\partial U_\theta}{\partial \theta_{ijk}} \,\nabla_i \theta_{ijk}, \\
\text{where } - \frac{\partial U_\theta}{\partial \theta_{ijk}} &= F_\theta \, .
\end{aligned}
$$


Getting $\cos^{-1}$ is computationally expensive, which would be needed above.
Once can try to avoid that by using the chain rule:

$$
\begin{aligned}
F_i &= - \frac{\partial U_\theta}{\partial \theta_{ijk}} \nabla_i \theta_{ijk} \\
    &= F_\theta \frac{\partial \theta_{ijk}}{\partial \cos(\theta_{ijk})} \nabla_i \cos\theta_{ijk} \\
    &= -F_\theta \frac{1}{\sin(\theta_{ijk})} \nabla_i \cos\theta_{ijk} \, .
\end{aligned}
$$


with $F_\theta = -\partial U_\theta / \partial \theta_{ijk}$.
The explicit expression for $\nabla_i \cos\theta_{ijk}$ is algebraically long, so in practice one reuses known formulas from the literature or trusted implementations.

One must also be careful with units: some force fields use *degrees* in the input files and convert internally to radians when evaluating the potential.

For this, we then need $ \nabla_i \cos\theta_{ijk}$. Eq. 7 of [J. Chem. Phys. 146, 226101 (2017)](https://doi.org/10.1063/1.4985251){cite}`howard2017note` offers a compact form.


```{warning}
$F_i$ is singlular if $\theta_{ijk}=0^\circ$ or $180^\circ$ if $F_\theta$ is not zero at these points!
```

### Harmonic
The harmonic angle potential mirrors the harmonic bond:

$$
U_\theta(\theta) = \frac{k}{2} (\theta - \theta_O)^2
$$

Here:

- $\theta_0$ is the equilibrium angle (straight line: $180^\circ$,
tetrahedral: $\approx 109.5^\circ$, etc.),

- $k_\theta$ is the angle force constant, controlling how stiffly the molecule resists bending away from $\theta_0$

Harmonic angle potentia fixes average angle around set point of $\theta_0$. Like with the harmonic bond potential, whatch for the factor of two in the spring constant.


**Interpretation.**

- Near $\theta_0$ the distribution of angles is approximately Gaussian.

- Larger $k_\theta$ means narrower fluctuations (stiffer angle).

- The same "factor of $1/2$" remark as for harmonic bonds applies here:
  check whether your simulation package includes it in the definition of
  $k_\theta$ or not.

### Cosine
A common alternative that avoids computing $\arccos$ is a cosine angle potential. One simple form is:

$$
U_\theta(\theta) = k (1 + \cos{\theta})
$$

Minimum is when the particles are in colinear $\theta =180^\circ$ arrangement. There are forms with a set angle different from that, by using $k (1 - \cos{(\theta - \theta_0)}) $ as functional form.


More generally, we can allow an arbitrary equilibrium angle by shifting:

$$
U_\theta^{\cos}(\theta)
= k_\theta \left[ 1 - \cos(\theta - \theta_0) \right].
$$

Here the minimum is located at $\theta = \theta_0$.
In both cases the potential depends smoothly on $\cos\theta$, which is
straightforward to compute from the dot product of bond vectors.

**Practical point.**
Cosine angle forms are often preferred in coarse-grained models because the force expressions are simpler and cheaper than those obtained from a harmonic potential written in terms of $\theta$ itself.

### Cosine squared
A third popular choice is the cosine-squared potential:

$$
U_\theta(\theta) = \frac{k}{2} (\cos\theta - \cos\theta_O)^2
$$

This form has several nice properties:

- It has a minimum at $\theta = \theta_0$.

- The potential is symmetric around $\theta_0$ when expressed in terms of
$\cos\theta$.

- In some cases it naturally produces two symmetric minima (e.g.\ near $\theta_0$ and $\pi-\theta_0$) when combined with other constraints.

Cosine-squared forms appear in various coarse-grained force fields where the
angle potential is expressed entirely in terms of $\cos\theta$.

Watch out for the exact definition of the parameters, sometimes $1/2$ is included in the definition of $k$.

```{note}
For specific models and force fields, always check if the angles are given in degree or radians.
```

```{code-cell} ipython3
:tags: [hide-cell]
from myst_nb import glue
import matplotlib.pyplot as plt
plt.style.use(['../_matplotlib/book.mplstyle'])
import numpy as np

# Define the range of angles (in radians)
theta = np.linspace(0, np.pi, 500)  # From 0 to pi radians

# Define potential parameters (example values)
k_harmonic = 1.0  # Force constant for harmonic potential
theta_0_harmonic = np.pi / 2  # Equilibrium angle for harmonic potential

k_cosine = 1.0  # Pre-factor for cosine potential
theta_0_cosine = np.pi / 2 # Equilibrium angle for cosine potential

k_cosine_squared = 1.0  # Pre-factor for cosine-squared potential
theta_0_cosine_squared = np.pi / 2 # Equilibrium angle for cosine-squared potential

# Calculate the potentials
harmonic_potential = 0.5 * k_harmonic * (theta - theta_0_harmonic)**2
cosine_potential = k_cosine * (1 - np.cos(theta - theta_0_cosine)) # Often defined as 1-cos(theta) for a minimum at theta=theta_0
cosine_squared_potential = k_cosine_squared * (1 - np.cos(theta - theta_0_cosine_squared)**2) # Often defined as 1-cos^2(theta) for a minimum at theta=theta_0

# Plotting
plt.figure()
plt.plot(theta, harmonic_potential, label='Harmonic Potential')
plt.plot(theta, cosine_potential, label='Cosine Potential')
plt.plot(theta, cosine_squared_potential, label='Cosine Squared Potential')

plt.xlabel('Angle (radians)')
plt.ylabel('Potential Energy')
plt.title('Comparison of Angle Potentials')
plt.legend()

plt.savefig('./_figures/angle_potentials.png')
```

```{figure} ./_figures/angle_potentials.png
:alt: Plot of different angle potentials
:width: 400px
:align: center
:name: angle-comp-fig
Comparison of harmonic, cosine, and cosine-squared angle potentials, all with an angle constant $k=1$ and a set angle $\theta_0$ of $\pi/2$.
```

## Dihedral Potentials

**Torsional** or **dihedral** angles are defined as shown in {numref}`dihedral-def-fig`. Dihedral (torsional) angles involve four atoms $i,j,k,\ell$. They are defined via the angle between the two planes spanned by $(i,j,k)$ and $(j,k,\ell)$ (see Fig.~{numref}`dihedral-def-fig`). Equivalently, one can ``look down'' the central bond $j$--$k$ and measure the rotation of atom $i$ relative to atom $\ell$.

```{figure} ./_figures/dihedral.png
:alt: Definition of dihedral or torsional angle.
:width: 250px
:align: center
:name: dihedral-def-fig

Definition of dihedral or torsional angle.

```

Angle between two plane (A,B) normals:

- $ \vec{n}_A = \vec{r}_{ij} \times \vec{r}_{jk} $
- $ \vec{n}_B = \vec{r}_{jk} \times \vec{r}_{kl} $

Then the angle is

$\varphi_{ijkl} = \frac{\vec n_A \cdot \vec n_B}{|n_A||n_B|}$

Similar to the angle, alternative definitions exist, $\psi = \pi -\varphi$.

To compute dihedral forces on four particles, we need to compute

$$
\begin{aligned}
F_i &= -\nabla_i U_\phi(\phi_{ijkl})\\
    &= - \frac{\partial U_\phi}{\partial \phi_{ijkl}} \nabla_i \phi_{ijkl} \\
    &= - \frac{\partial U_\phi}{\partial \phi_{ijkl}} 
       \frac{\partial \phi_{ijkl}}{\partial \cos(\phi_{ijkl})} \nabla_i \cos\phi_{ijkl} \\
    &= -F_\phi \frac{1}{\sin(\phi_{ijkl})} \nabla_i \cos\phi_{ijkl} \, .
\end{aligned}
$$


with: $F_\phi = -\partial U_\phi / \partial \phi_{ijkl}$.


The explicit expressions for the gradients are rather involved and are usually
taken from standard references rather than derived from scratch each time.

**Singular configurations.**
Because of the $1 / \sin\phi_{ijkl}$ factor, dihedral forces can become
singular at $\phi_{ijkl}=0^\circ$ or $180^\circ$ if $F_\phi$ is nonzero there. Similarly, if either of the adjacent bond angles $\theta_{ijk}$ or $\theta_{jk\ell}$ becomes $0^\circ$ or $180^\circ$, the two planes become ill-defined and the dihedral angle is degenerate. Realistic force fields and simulation conditions are chosen to avoid such problematic configurations or to make the potential smooth as these limits are approached.

This results in some involved computations, see Allen & Tildesley{cite}`allen1987computer` for a step by step derivation in Appendix C.

```{warning}
The same singularities as for the angle forces show up at $\phi_{ijkl}=0^\circ$ and $180^\circ$ but one can eliminate them (details in [Bondel, Karplus, J. Comput. Chem., 17: 1132-1141, 1996](https://doi.org/10.1002/(SICI)1096-987X(19960715)17:9%3C1132::AID-JCC5%3E3.0.CO;2-T)){cite}`blondel1996new`.

However, $\phi$ becomes also degenerate if $\theta_{ijk}$ or $\theta_{jkl}$ approaches $0^\circ$ or $180^\circ$ because the two planes to define the dihedral cannot be defined in these cases. This is important for models with "soft" interactions, where these configurations are possible, e.g. coarse-grained models.
```

### Periodic
A very common torsional form is the simple periodic function:

$$
V_\phi(\phi_{ijkl}) = k_{\phi}(1 + \cos(n \phi - \phi_s)) \quad .
$$
Used in the CHARMM force field

where:

- $k_\phi$ controls the barrier height,

- $n$ is the multiplicity (number of minima per $360^\circ$),

- $\delta$ is a phase shift that moves the minima to the desired
dihedral angles.

This form is used, for example, in the CHARMM force field.

**Example.**
For a simple alkane C--C--C--C dihedral, one often chooses $n=3$ to generate three minima (one \emph{trans} and two \emph{gauche}) over $360^\circ$. The phase shift $\delta$ is then chosen so that the global minimum corresponds to the chemically preferred conformation.

### Ryckaert-Bellemans
The Ryckaert--Bellemans (RB) form is widely used for alkanes and other chain molecules:

$$
V_{\phi}(\phi_{ijkl}) = \sum_{n=0}^5 C_n( \cos(\psi ))^n, \text{ where } \psi = \phi -180^\circ\quad .
$$

The coefficients $C_n$ are parameters fitted so that the torsion potential reproduces quantum chemistry data or experimental observables.

**Interpretation.**

- This is effectively a polynomial in $\cos\psi$ and can approximate
fairly complicated periodic shapes.

- Shifting by $\pi$ (using $\psi$) is convenient for alkanes where
the \emph{trans} conformation near $180^\circ$ is often of special
interest.

The RB form is mathematically closely related to a truncated Fourier series, as we will see next.


### Fourier

$$
V_{F} (\phi_{ijkl})= \frac{1}{2} \sum_{n=1}^4 C_n (1-(-1)^n\cos(n\phi))
$$

- Used in the OPLS force field. Each term with index $n$ contributes a periodic component with $n$ minima or maxima per $360^\circ$, and the $(-1)^n$ factor flips the sign of the contribution depending on $n$.

- There is a direct mapping between the Fourier coefficients $C_n$ and the Ryckaert--Bellemans coefficients via trigonometric identities. In practice, force fields may be parameterized in one representation and converted to the other depending on the software.

## Improper Dihedrals

In addition to the dihedrals defined between four bounded particles in a row, there are also
so called **improper** dihedrals, that can be applied to keep planar groups planar, or prevent flipping into mirror images. These are commonly applied between four points in configurations as sketched in {numref}`improper-dihedral-fig`.

```{figure} ./_figures/improper_dihedral.png
:alt: Improper dihedral configuration.
:width: 100px
:align: center
:name: improper-dihedral-fig

Configuration to which an improper dihedral can be applied to.

```

The functional form is often a simple harmonic potential in the improper dihedral angle $\xi$:

$$
U_{\text{imp}}(\xi)
= \frac{1}{2} k_{\text{imp}} (\xi - \xi_0)^2 ,
$$

where $\xi_0$ is usually $0^\circ$ (to enforce planarity) or some other
target angle.



**Typical uses.**

- Keeping aromatic rings or peptide planes planar.

- Preventing a stereocenter from flipping into its mirror image.

- Stabilizing certain local geometries that are underdetermined by
normal bonds and angles alone.

Mathematically, the computation of improper dihedral forces is very similar to that for proper dihedrals; only the connectivity pattern of the four atoms differs.

## References

## References

- Allen, Michael P., and Dominic J. Tildesley. *Computer Simulation of Liquids*. Clarendon Press, Oxford (1987). Appendix C.2: “Calculation of forces and torques.” {cite}`allen1987computer`  
- Howard, Michael P., Antonia Statt, and Athanassios Z. Panagiotopoulos. “Note: Smooth torsional potentials for degenerate dihedral angles.” *The Journal of Chemical Physics* 146, 226101 (2017). {cite}`howard2017note`  
- Blondel, Arnaud, and Martin Karplus. “New formulation for derivatives of torsion angles and improper torsion angles in molecular mechanics: Elimination of singularities.” *Journal of Computational Chemistry* 17, 1132–1141 (1996). {cite}`blondel1996new`  
- Weeks, John D., David Chandler, and Hans C. Andersen. “Role of repulsive forces in determining the equilibrium structure of simple liquids.” *The Journal of Chemical Physics* 54, 5237–5247 (1971). {cite}`weeks1971`  
- Kremer, Kurt, and Gary S. Grest. “Dynamics of entangled linear polymer melts: A molecular-dynamics simulation.” *The Journal of Chemical Physics* 92, 5057–5086 (1990). {cite}`kremer1990`  
- GROMACS development team. *GROMACS Reference Manual*: “Bonded interactions” section. (Accessed 2025.) {cite}`gromacs_bonded`

