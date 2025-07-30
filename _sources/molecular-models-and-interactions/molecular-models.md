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

# Molecular Models

## Classical Atomistic Models

- One **Atom** is treated as **1 particle**
- Interactions with in a molecule, i.e, **Intramolecular forces** are
**bonded interactions**, **angles** and **dihedrals** (or **torsional angles**) as illustrated in {numref}`bonds-angles`.

```{figure} ./_figures/intramolecular-def.png
:alt: Visualization of bonds, angles, and dihedrals in a molecule
:width: 300px
:align: center
:name: bonds-angles
Visualization of bonds, angles, and dihedrals in a molecule with four atoms.
```

### Non-bonded interactions

- **Van der Waals (dispersion forces)**: induced dipoles

    $ u(r) \sim \frac{1}{r^6} \quad \quad \text{(where } r \text{ = distance between particles)} $
- **Repulsion** (electron cloud overlap)

    $u(r) \sim e^{-r/l}$, which is slow/expensive to evaluate
- Combine Van der Walls and short ranged repulsion, one gets the **Lennard-Jones Potential** (short-ranged):

    $ u(r) = 4\varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right] $

- **Coulomb electrostatics** (long-ranged):

    $ u(r) = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q_1 q_2}{r} $, where $\varepsilon_r = 2.61$ is the relative permeability.

````{note}
The Lennard-Jones potential (as shown in Fig. {numref}`LJ-fig`) is incredibly popular for a whole range of models and is frequently used across fields. It can be used to model simple model liquid systems, predict phase diagrams, and much more.


```{figure} ./_figures/LJ.png
:alt: Sketch of the Lennard-Jones potential
:width: 300px
:align: center
:name: LJ-fig

Lennard-Jones potential $U(r)$ as function of distance $r$. Here, $\sigma$ corresponds to a particle size, and $-\varepsilon$ is the interaction energy at the minimum of the potential, which is located at $r=2^{1/6}\sigma$.
```

````

It is helpful to plot these **non-bonded** interaction potentials with python and matplotlib, vary the parameters to familiarize ourselves with the shapes and the effects of each parameter.

test

```{code-cell} ipython3
:tags: [hide-input]
import matplotlib.pyplot as plt
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

# Plot
fig, axs = plt.subplots(1, 2)
axs[0].plot(r_values, U_values)
axs[0].axvline(x=r0, color='r', linestyle='--', label='Equilibrium Length')
axs[0].set_xlabel('$r$')
axs[0].set_ylabel('$U_{\text{bond}}(r)$')
axs[0].set_title('Harmonic Bond Potential')
axs[0].legend()
axs[1].plot(r_values, F_values)
axs[1].axvline(x=r0, color='r', linestyle='--', label='Equilibrium Length')
axs[1].set_xlabel('$r$')
axs[1].set_ylabel('$F_{\text{bond}}(r)$')
axs[1].set_title('Harmonic Bond Force')
axs[1].legend()
plt.tight_layout()
plt.show()
```

### Bonded, Angle, and Dihedral interactions

## Total potential energy

The total potential engery is the sum of all one-body, two-body, and higher-body interactions. One-body interactions are for example caused by external fields or forces.
Two body interactions are interactions as described above.

$ U = \sum_i u(r_i) + \sum_i \sum_{j>i} u(r_i,r_j) + \sum_i \sum_{j>i} \sum_{k>j} u(r_i,r_j,r_k)+ \ldots $

## Two-Body Approximation

Three-body (and higher) forces are expensive to compute (combinatorics!).
Usually, we truncate at two-body interactions and use an **effective potential** ({numref}`effective-pot-fig`), that reproduces relevant properties.

Other forces (e.g., polar forces) are often neglected.

```{figure} ./_figures/effective-pot.png
:alt: Effective pair potential that incoperates some approximation of three-body effects.
:width: 300px
:align: center
:name: effective-pot-fig

"Effective" pair potential that incoperates some approximation of three-body effects.
```

Atomistic force fields often consists of two-body non-bonded interactions, bonds, angles and dihedrals.

### Additional References

- ["Understanding three-body contributions to coarse-grained force fields" Christoph Scherer and  Denis Andrienko](https://pubs.rsc.org/en/content/articlelanding/2018/cp/c8cp00746b) Phys. Chem. Chem. Phys., 2018,20, 22387-22394

- ["Effective Two-Body Interactions"
Cameron Mackie, Alexander Zech, Martin Head-Gordon](https://pubs-acs-org.proxy2.library.illinois.edu/doi/10.1021/acs.jpca.1c05677), J. Phys. Chem. A 2021, 125, 35, 7750–7758

## Two Complementary Approaches to Designing Models

- Use experimental data, invent a model to mimic the problem
(semi-empirical approach).
**But:** one cannot reliably extrapolate the model away from the empirical data.

- Use foundation of physics (Maxwell, Boltzmann, and Schrödinger) and
numerically solve the mathematical problem,
determine the properties (first-principles/ab initio methods)

## Coarse-Grained Models

- Atomistic resolution may be impractical for large systems.

```{example} Nanoparticles in Water
1 water molecule ≈ 3 Å, 1 nanoparticle ≈ 10 nm results in 1 NP diameter ≈ 30 water molecules. If we compare volume $V_{np}=\frac{4\pi}{3}(5\text{nm})^3$, then we need $\sim 37,000$ water molecules to fill the same space as one nanoparticle. If, additionally, we are interested in dilute situations, the vast majority of the system is comprised of the solvent.
```

In these cases, we study models of the particles we care about with  **effective** interactions that **coarsen** out the pieces of the system we do not care about, i.e the solvent, as illustrated in {numref}`coarse-grain-fig`.

```{figure} ./_figures/coarse-grain.png
:alt: Illustration of coarse-graining by removing solvent.
:width: 300px
:align: center
:name: coarse-grain-fig

Illustration of coarse-graining by removing solvent.  The top shows so-called explicit solvent, e.g. water molecules, and the bottom panel shows the same system where the solvent is replaced with a homogenous "background" that is treated implicitly by modifing the pair interactions. This is called a implicit solvent model.

```

Coarse-graining removes degrees of freedom and is therefore less accurate, and often considered a empirical approach.

- How to get these effective interactions:
  - **Force matching**
  - **Relative entropy minimization**
  - **Inverse Boltzmann iteration**

### Simple Examples for coarse-grained Models

Even though a coarse-grained or simplified model lost some amout of detail and degrees of freedom, they often offer a lot of insights.

- **Hard spheres**:
    $ u(r) = \begin{cases}
    \infty & r < d \\
    0 & r \geq d
    \end{cases} $
- **Lennard-Jones** spheres for liquids
- **Bead-spring polymers**:
  - FENE (Finite Extensible Nonlinear Elastic) Spring model

### Additonal References

## Force Fields

- Parametrized, self-consistent models fit to thermodynamic or structural data.
- Designed for specific systems:
  - **OPLS**: hydrocarbons
  - **SPC/E, TIP4P/2005, OPC, ...**: water
  - **AMBER, CHARMM**: biomolecules
  - **TraPPE**: phase equilibrium
  - **Martini**: coarse-grained lipids and biomolecules in water
- **Machine Learning (ML)** models trained on quantum mechanics data are becoming popular.
- You can create or refit your own force field, however **validation is crucial**.

- How to get the parameters and functional forms for these force fields:
  - experimental information to parameterize model parameters
  - ab-initio calculations from Density Functional Theory (DFT) or other quantum methods

## Reduced Units

- SI units are too small and often inconvinient for atomic systems.
- Use **reduced units** where quantities are of order 1. This also helps with numerical stability and readability of simulation code.

### Unit Systems

Traditional unit systems can be looked at as follows:

| Quantity | SI | CGS | Imperial |
|----------|----|-----|----------|
| length   | m  | cm  |    ft    |
| mass     | kg | g   |    lb    |
| time     | s  | s   |     s    |

Other units follow from the base units defined abve in the table.

```{example} Unit Consistency
Energy: $ E = \frac{[\text{mass}] [\text{length}]^2}{[\text{time}]^2} = \frac{m l^2 }{ t^2} \rightarrow J = \frac{kg \cdot m^2}{s^2}$ ✅
```

- For **reduced** units, choose $ l, m, E $ based on the problem:
  - $l =  $ length =  diameter of atom (LJ $\sigma$, Å)
  - $ m = $ mass =  mass of atom (10s amu)
  - $ E = $ energy = interaction energy or thermal energy at reference temperature ($k_B T$) (LJ $\varepsilon$)

This then leads to **derived units** from your base reduced units:

| Derived unit | Relation to base units |
|--------------|--------------|
| area | $[\mathrm{length}]^2$ |
| volume |  $[\mathrm{length}]^3$ |
| time |  $[\mathrm{energy}]^{-1/2} \cdot [\mathrm{length}] \cdot [\mathrm{mass}]^{1/2}$ |
| velocity | $[\mathrm{energy}]^{1/2} \cdot [\mathrm{mass}]^{-1/2}$ |
|force | $[\mathrm{energy}] \cdot [\mathrm{length}]^{-1}$ |
| pressure | $[\mathrm{energy}] \cdot [\mathrm{length}]^{-3}$ |
| charge  | $`\left(4 \pi \epsilon_{0} \cdot [\mathrm{energy}] \cdot [\mathrm{length}] \right)^{1/2}$ |

Here, $\epsilon_{0}$ is permittivity of free space.

 Note that for example **time**, often called $\tau$, is a
derived unit in reduced unit systems, where it is a base unit in traditional unit systems.
We can do that because we can choose $ l, m, E $ sutiable for the system of interest.

### GROMACS Units

| Quantity  |   | Unit         |
|-----------|--|--------------|
| Length |$l$      | nm           |
| Mass   | $m$     | amu (g/mol)  |
| Energy |  $\varepsilon$    | kJ/mol       |
| Charge  | $q$    | e ($=1.602 \cdot 10^{-19}$ coulombs)      |

| Quantity  |   | Derived Unit         |
|-----------|---|--------------|
| Time   |  $\tau  = \sqrt{\frac{m \cdot \sigma^2 }{ \varepsilon}}$    | ps           |
| Velocity| $l/\tau$   | nm/ps        |
| Force    | $\varepsilon/l$   | kJ/mol/nm    |
| Pressure |  $\varepsilon/l^3$  | kJ/mol/nm³   |
| Viscosity | $\varepsilon \tau/l^3$  | kJ/mol·ps/nm³|
| Diffusivity |$l^2/\tau$ | nm²/ps       |

- Temperature is either in its own units or derived via Boltzmann constant:
  $ T = \frac{E}{k_B} $

```{example} Time Units
Time in reduced units: $ \tau = \sqrt{\frac{[\text{mass}] [\text{length}]^2 }{ [\text{energy}]}} \rightarrow \tau = \sqrt{\frac{m \cdot \sigma^2 }{ \varepsilon}}$.

Time in GROMACS units: $\tau = \sqrt{(10^{-3}kg/mol\cdot (10^{-9}m)^2)/(10^3 J/mol)} = 10^{-12}s$ = ps.  ✅
```

### LAMMPS Units

 LAMMPS offers many different [unit systems](https://docs.lammps.org/units.html) to use.

```{warning}
 Simulation software may use inconsistent units (e.g., LAMMPS "real" units). Always convert carefully.
```

**Arbitrary units** are useful for generalizing results to new problems &rarr;**Corresponding states principle**.

## Resources

- Allen & Tildesley, "Simulations of liquids" Appendix B - Reduced Units
