
# Using MD Packages

## Anatomy of an MD Simulation Workflow

A molecular dynamics (MD) simulation typically proceeds through four major stages:

1. Initialization — Define the starting configuration and parameters.

2. Equilibration — Remove overlaps and unphysical forces and bring the system to the desired thermodynamic state.

3. Production — Collect statistically meaningful simulation data after the system has equilibrated.

4. Post-processing — Analyze and visualize trajectories to obtain physical insights.

## Initialization

Initialization defines the starting point of the simulation. It often provides the easiest place to modify system size, composition, force fields, and other parameters before running MD. Several tools are commonly used for system setup.

### Packmol

Packmol builds the initial coordinates of a system while enforcing minimum-distance constraints so that molecules do not overlap. It handles only geometry, not force fields. You must combine it with another package (Foyer, AmberTools, etc.) to assign force-field parameters.

Documentation:
https://m3g.github.io/packmol/userguide.shtml

To apply the Packmol, you need to firstly create or insert a particle file (pdb format). Then, a Packmol input script needs to be set so that it can be used to run the initialization. You can restrain a part of the molecule to be in a specified region of the space. This is useful for building vesicles where the hydrophilic part of the surfactants must be pointing to the aqueous environment.

### mBuild and Foyer

mBuild is a molecular builder that constructs polymers, solvents, nanoparticles, and other structures.
Foyer assigns classical force-field parameters (Lennard–Jones, bond/angle/dihedral terms, charges, etc.).

Documentation:
mBuild: https://mbuild.mosdef.org/en/stable/
Foyer: https://foyer.mosdef.org/en/stable/

First step is to use mBuild in order to build molecular components in mBuild (monomers, solvents, nanoparticles, polymer chains). Then assemble them into a simulation box using fill_box or Packmol. For the next move, you can use Foyer to assign atom types in order to apply force-field parameters. The output can be used to export to LAMMPS, OpenMM XML, or GSD for simulation.


### AmberTools

AmberTools specializes in biomolecular system preparation (proteins, DNA/RNA, ligands).

Documentation:
https://ambermd.org/AmberTools.php

AmberTools provides workflows for generating chemically accurate biomolecular topologies for assigning AMBER and GAFF force fields. In this method, you can add hydrogens, water, and ions to the system.




## Equilibration

After the initialization process, the next stage of the molecular
dynamics workflow is equilibration. The goal of equilibration is to remove
unfavorable contacts, stabilize the system, and bring it to the desired
thermodynamic state. This process typically includes energy minimization
followed by simulations in the NVT and NPT ensembles.

### Energy minimization

The equilibration process begins with an energy minimization step. This step
removes steric clashes and relaxes any distorted geometries created during
packing or system construction. Common minimization algorithms include
steepest descent, conjugate gradient, L-BFGS, and the FIRE algorithm. By
reducing the forces acting on atoms, minimization ensures that the system is
numerically stable when molecular dynamics integration starts.

### NVT/NPT equilibration

Once the system is minimized, an NVT (canonical ensemble) equilibration stage
sets the system to the target temperature. A thermostat—such as Langevin,
Berendsen, or an isokinetic thermostat—controls the kinetic energy and helps
the system reach the correct thermal distribution. It is important to
initialize velocities properly, since starting with zero velocities can cause
divide-by-zero errors in temperature calculations. During this stage, atomic
velocities relax toward a Maxwell--Boltzmann distribution. Another way is to use NPT (isothermal--isobaric ensemble)
simulation. The barostat generally
responds more slowly than the thermostat, so this phase often requires longer
simulation times. When switching from thermostats that do not conserve
momentum, the center-of-mass momentum should be removed before beginning NPT.
Volume, density, and internal pressure gradually stabilize during this stage.

### Monitoring equilibration

Throughout equilibration, several observables help indicate whether the
The system has reached steady behavior. These include the potential energy $U$,
system density, and the radial distribution function $g(r)$. Depending on
the system, transport properties such as the diffusion coefficient may also
guide decisions about the required equilibration time. Once these properties
stop drifting and fluctuate around stable values, the system is ready for
production molecular dynamics.

### Assessment of equilibration

Equilibration was monitored by tracking macroscopic observables, including
the potential energy $U$, system density, and the radial distribution
function $g(r)$. Transport coefficients, such as diffusion constants, were
used when appropriate to estimate the timescales required for the system to
relax. Production simulations were initiated only after these quantities had
reached stationary behavior.


The following packages are the commonly used MD packages for equilibrium.
Typically used for general-purpose physics simulations.
- LAMMPS: https://docs.lammps.org/
- HOOMD-blue: https://hoomd-blue.readthedocs.io/en/v6.0.0/

Typically used for biophysics
- GROMACS: https://manual.gromacs.org/current/index.html
- NAMD, OpenMM, AMBER 

## Production

- Run long enough to gather statistically independent samples of quantities of interest.
- Trajectory dumping can be disk-intensive—choose frequency wisely.
- Use **checkpointing** (saving restart files) to recover from hardware failures.

## Post-processing

- Write scripts to compute properties, averages, etc., from simulation outputs.
- Can be done on HPC clusters or downloaded to local machines.
- Use existing tools and methods when possible—avoid reinventing the wheel.

## Tips

- Choose the largest time step (Δt) that still ensures accurate integration—test this.
- Tune hyperparameters for performance using representative simulations.
- Run multiple simulation copies to improve statistics and estimate errors.
- Organize files clearly during parameter sweeps. Example structure:

data/ ├── T-1.0/ │ ├── V-20/ │ │ └── input.sh │ ├── V-30/ │ │ └── input.sh ├── T-1.5/ │ ├── V-205/ │ └── V-301/

- Consider using tools to manage simulation campaigns.

## Recommended MD Packages

- **GROMACS, NAMD, OpenMM, AMBER** – widely used in biophysics.
- **LAMMPS, HOOMD-blue** – general-purpose physics simulations.

Always read the documentation for your chosen tool carefully!

## References

- [LAMMPS documentation](https://docs.lammps.org)
- [HOOMD-blue documentation](https://hoomd-blue.readthedocs.io)
- [GROMACS documentation](https://manual.gromacs.org/current/index.html)

- "Simulations: The Dark Side," Daan Frenkel, 2013 {cite}`frenkel2013simulations`

- Braun, E., Gilmer, J., Mayes, H. B., Mobley, D. L. ., Monroe, J. I., Prasad, S., & Zuckerman, D. M. . (2018). Best Practices for Foundations in Molecular Simulations [Article v1.0]. Living Journal of Computational Molecular Science, 1(1), 5957. {cite}`prasad2018best`

- In general, the Journal [Living Journal of Computational Molecular Science](https://livecomsjournal.org/index.php/livecoms/index) has excellent how to articles, tutorials, and best practices.
