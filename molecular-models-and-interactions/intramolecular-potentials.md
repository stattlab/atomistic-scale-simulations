# Intermolecular Potentials

in {numref}`bonds-angles-fig` most typical intermolecular potentials for a molecule are shown.

```{figure} ./_figures/intramolecular-def.png
:alt: Visualization of bonds, angles, and dihedrals in a molecule
:width: 300px
:align: center
:name: bonds-angles-fig

Visualization of bonds, angles, and dihedrals in a molecule with four atoms.

```

The overall energy is given by:

$ U = \sum_{\text{bonds}, {i,j} } U_b(r_{ij}) + \sum_{\text{angles}, {i,j,k}} U_\theta(\theta_{ijk}) + \sum_{\text{dihedrals}, {i,j,k,l} } U_\varphi(\varphi_{ijkl}) $

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

\begin{align*}
 F_i = - \nabla_i U_b(r_{ij}) = - \frac{\partial U_b}{\partial r_i} \nabla_i r_{ij}\quad .
\end{align*}

For this, we need $\nabla_i r_{ij}$, which is
\begin{align*}
\nabla_i r_{ij} &=  \frac{\partial}{\partial x_{i,\alpha}} \left[ \sqrt{(x_{j,\alpha}-x_{i,\alpha})(x_{j,\alpha}-x_{i,\alpha})} \right]\\
&= \frac{1}{2} \frac{-2 x_{j,\alpha}+2x_{i,\alpha}}{\sqrt{(x_{j,\alpha}-x_{i,\alpha})(x_{j,\alpha}-x_{i,\alpha})}}\\
&= - \frac{x_{j,\alpha}-x_{i,\alpha}}{\sqrt{(x_{j,\alpha}-x_{i,\alpha})(x_{j,\alpha}-x_{i,\alpha})}}\\
&= - \frac{r_{ij}}{|r_{ij}|}\\
&= - \hat r_{ij}
\end{align*}

which is the unit vector pointing in the direction of the bond!

The force then is
\begin{align*}
F_i &= - \frac{\partial U_b(r_{ij})}{\delta r_{ij}} (-\hat r_{ij}) \\
&= - F_b(r_{ij}) \hat r_{ij}, \text{ with }
 F_b(r_{ij}) \equiv - \frac{\partial U_b(r_{ij})}{\delta r_{ij}}
\end{align*}

By symmetry we should have $\nabla_j r_{ij}=-\nabla_i r_{ji}$, meaning that
\begin{align*}
F_j = F_b(r_{ij}) \hat r_{ij} \quad.
\end{align*}
This shows that for a bond, $F_i = -F_j$, which illustrates that action has a equal and opposite reaction.

```{tip}
Once can use the action reaction principle to save on computations by only computing either $F_i$ OR $F_j$ and then applying the equal action-reaction principle to save on calculations.
```

### Harmonic

$ U(r) = \frac{1}{2}k(r - r_0)^2 $

This fixes the bond length to fluctuate around an average of $r_0$.

- Watch for factor of 2!
- Typically $ k \sim 10^3 \epsilon/l^2$ for "stiff" bond

```{example} Harmonic bond force
$ U_b = \frac{1}{2}k(r - r_0)^2 $, so

$ F_b = \frac{\partial U_b}{\delta r_{ij}} = -k (r_{ij}-r_0)$, leading to

\begin{align*}
F_i &= + (r_{ij}-r_0) \hat r_{ij}\\
F_j &= - (r_{ij}-r_0) \hat r_{ij} \quad .
\end{align*}
If $r_{ij}>r_0$, the bond is streched past $r_0$ and particle $i$ moves toward $j$, and $j$ toward $i$. If $r_{ij}<r_0$, the bond is compressed below the set point $r_0$ and particle $i$ moves away from $j$, and $j$ away from $i$.
```

### FENE (Finite Extensible Nonlinear Elastic)

$ U(r) = -\frac{1}{2}k r_0^2 \ln\left(1 - \left(\frac{r}{r_0}\right)^2\right) $

Diverges at $r_0$, minimum at 0. This is usually used in conjuction with a repulsive, short-ranged force (WCA = cut LJ at minimum and shift up to get a purely repulsive potential).

Typical parameters:

- k = 30, r_0 = 1.5

## Angle Potentials

The **angle** between three particles $i$, $j$, and $k$ is given by:

$ \cos \theta_{ijk} = \frac{(\vec{r}_{ji} \cdot \vec{r}_{jk})}{|\vec{r}_{ji}||\vec{r}_{jk}|} = - \frac{(\vec{r}_{ij} \cdot \vec{r}_{jk})}{|\vec{r}_{ij}||\vec{r}_{jk}|}$.

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
These two definitions can be easily converted into each other $\theta_{ijk} = \pi - \theta'_{ijk}$.
 ````

To compute the angle potential between three particles, we need to
\begin{align*}
F_i &= -\nabla_i U_\theta (\theta_{ijk}) \\
&=- \frac{\partial U_\theta}{\partial \theta_{ijk}} \nabla_i \theta_{ijk} \\
\text{ where } - \frac{\partial U_\theta}{\partial \theta_{ijk}} = F_\theta \quad .
\end{align*}
Getting $\cos^{-1}$ is computationally expensive, which would be needed above.
Once can try to avoid that by using the chain rule:

\begin{align*}
F_i &= - \frac{\partial U_\theta}{\partial \theta_{ijk}} \nabla_i \theta_{ijk} \\
F_\theta \frac{\partial \theta_{ijk}}{\partial \cos(\theta_{ijk})} \nabla_i \cos\theta_{ijk} \\
-F_\theta \frac{1}{\sin(\theta_{ijk})} \nabla_i \cos\theta_{ijk}\quad .
\end{align*}
For this, we then need $ \nabla_i \cos\theta_{ijk}$. Eq.7 of [J. Chem. Phys. 146, 226101 (2017)](https://doi.org/10.1063/1.4985251) offers a compact form.

```{warning}
$F_i$ is singlular if $\theta_{ijk}=0^\circ$ or $180^\circ$ if $F_\theta$ is not zero at these points!
```

### Harmonic

$U_\theta(\theta) = \frac{k}{2} (\theta - \theta_O)^2$

Fixes average angle around set point of $\theta_0$. Like with the harmonic bond potential, whatch for the factor of two in the spring constant.

### Cosine

$U_\theta(\theta) = k (1 + \cos{theta})$

Minimum is when the particles are in colinear $\theta =180^\circ$ arrangement.

### Cosine squared

$U_\theta(\theta) = \frac{k}{2} (\cos\theta - \cos\theta_O)^2$

```{note}
For specific models and force fields, always check if the angles are given in degree or radians.
```

## Dihedral Potentials

**Torsional** or **dihedral** angles are defined as shown in {numref}`dihedral-def-fig`. One needs to define two planes created by three of the four points each.

```{figure} ./_figures/dihedral.png
:alt: Definition of dihedral or torsional angle.
:width: 200px
:align: center
:name: dihedral-def-fig

Definition of dihedral or torsional angle.

```

Angle between two plane (A,B) normals:

- $ \vec{n}_A = \vec{r}_{ij} \times \vec{r}_{jk} $
- $ \vec{n}_B = \vec{r}_{jk} \times \vec{r}_{kl} $

Then the angle is

$\varphi_{ijkl} = \frac{\vec n_A \cdot \vec n_B}{|n_A||n_B|}$

SImilar to the angle, alternative definitions exist, $\psi = \pi -\varphi$.

To compute dihedral forces on four particles, we need to compute

\begin{align*}
F_i &= -\nabla_i U_\phi(\phi_{ijkl})\\
&= - \frac{\partial U_\phi}{\partial \phi_{ijkl}} \nabla_i \phi_{ijkl} \\
= - \frac{\partial U_\phi}{\partial \phi_{ijkl} } \frac{\partial \phi_{ijkl}}{\partial \cos(\phi_{ijkl})} \nabla_i \cos\phi_{ijkl} \\
= -F_\phi \frac{1}{\sin(\phi_{ijkl})} \nabla_i \cos\phi_{ijkl}\quad .
\end{align*}

This results in some involved computations, see Allen & Tildesley for a step by step derivation in Appendix C.

```{warning}
The same singularities show up at $\phi_{ijkl}=0^\circ$ and $180^\circ$ but one can eliminate them (details in [J. Comput. Chem., 17: 1132-1141, 1996](https://doi.org/10.1002/(SICI)1096-987X(19960715)17:9%3C1132::AID-JCC5%3E3.0.CO;2-T)).

However, $\phi$ becomes also degenerate if $\theta_{ijk}$ or $\theta_{jkl}$ approaches $0^\circ$ or $180^\circ$ because the two planes to define the dihedral cannot be defined in these cases. This is important for models with "soft" interactions, where these configurations are possible, e.g. coarse-grained models.
```

### Periodic

$ V_\phi(\phi_{ijkl}) = k_{\phi}(1 + \cos(n \phi - \phi_s)) $

Used in the CHARMM force field

### Ryckaert-Bellemans

$V_{\phi}(\phi_{ijkl}) = \sum_{n=0}^5 C_n( \cos(\psi ))^n,$ where $\psi = \phi -180^\circ$.

### Fourier

$V_{F} (\phi_{ijkl})= \frac{1}{2} \sum_{n=1}^4 C_n (1-(-1)^n\cos(n\phi))$

Used in the OPLS force field. This can be transformed into the Ryckaert-Bellemans form using trigonometric indentities.

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

## Resources

- Allen & Tildesley, "Simulations of liquids" Appendix C.2 - Calculation of forces and torques
- ["Note: Smooth torsional potentials for degenerate dihedral angles" Michael P. Howard, Antonia Statt, Athanassios Z. Panagiotopoulos, J. Chem. Phys. 146, 226101 (2017)](https://doi.org/10.1063/1.4985251)
- [Blondel, A. and Karplus, M., New formulation for derivatives of torsion angles and improper torsion angles in molecular mechanics: Elimination of singularities. J. Comput. Chem., 17: 1132-1141. (1996)](https://doi.org/10.1002/(SICI)1096-987X(19960715)17:9<1132::AID-JCC5>3.0.CO;2-T)
- [Gromacs Documentation on Intramolecular Potentials](https://manual.gromacs.org/current/reference-manual/functions/bonded-interactions.html)

## Additional Literature
