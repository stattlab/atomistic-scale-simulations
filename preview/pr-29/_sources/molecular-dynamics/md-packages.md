
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

After the system completes equilibration, the simulation enters the production
phase. The goal of this stage is to generate statistically meaningful data
for analysis. Unlike equilibration, where system properties evolve toward
steady values, production simulations assume that the system is already in
a stable thermodynamic state.

### Sampling and simulation length

The production run must be long enough to collect statistically independent
samples of the quantities of interest. Correlations between configurations
mean that successive frames are not fully independent, so the effective
number of samples depends on the autocorrelation time of the observable.
Longer simulations generally improve statistical accuracy but also increase
computational cost.

### Trajectory output

Trajectory files record particle positions and other observables over time.
Because storing full trajectories can be disk-intensive, the output
frequency should be chosen carefully. Writing too frequently produces large
files without adding meaningful information, while writing too infrequently
may miss important dynamics. A common strategy is to save frames at intervals
longer than the decorrelation time of fast molecular motions.


### Checkpointing and reproducibility

To ensure robustness and recoverability, checkpoint files (or restart files)
are saved periodically during the production run. These files store the
complete simulation state, allowing the run to be resumed after hardware
failures, queue interruptions, or unexpected shutdowns. Checkpointing also
supports reproducibility, since it records exact system coordinates,
velocities, and random-number states at specific points in the simulation.


The following packages are common used MD packages for production. Note that they are the same as the packages used for equilibrium.
Typically used for general-purpose physics simulations.
- LAMMPS: https://docs.lammps.org/
- HOOMD-blue: https://hoomd-blue.readthedocs.io/en/v6.0.0/

Typically used for biophysics
- GROMACS: https://manual.gromacs.org/current/index.html
- NAMD, OpenMM, AMBER 

## Post-processing

Post-processing refers to the analysis performed after the production
simulation completes. At this stage, the goal is to extract meaningful
physical quantities from the raw trajectory data and to interpret the
results in terms of the underlying molecular behavior.

### Computing properties

Custom analysis scripts are often written to compute observables such as
energies, radial distribution functions, diffusion coefficients, structural
order parameters, or time-averaged quantities. These scripts typically use
analysis libraries such as \texttt{MDTraj}, \texttt{MDAnalysis}, or
\texttt{hoomd}’s built-in readers. Post-processing enables the conversion of
large raw trajectories into quantitative results suitable for comparison
with theory or experiment.

### Where analysis is performed

Post-processing can be performed directly on high-performance computing
(HPC) clusters, especially when trajectories are large or many simulations
need to be analyzed. Alternatively, trajectory files can be transferred to a
local workstation for interactive or exploratory analysis. The choice depends
on storage, bandwidth, and computational requirements.

### Using existing tools

The most common tools to use will be through Python packages. Packages such as Matplotlib, which is a package for creating graphs, allows for students and researchers to focus on the scientific interpretation rather than data handling. 

An additional tool for post processing is OVTIO. This can visualize trajectory data in the form of a 3D model. This tool allows for frame by frame visualization to visualize how the particles move. More documentation can be found here: https://www.ovito.org/docs/current/

## Tips

The following guidelines help improve efficiency, stability, and
reproducibility when running molecular dynamics simulations in an educational
or research setting.

### Choose an appropriate time step

Select the largest time step $\Delta t$ that still produces accurate and
stable integration. A time step that is too small wastes computational
resources, while one that is too large can cause numerical instability.
Testing several values during a short trial run is an effective strategy for
finding the optimal choice.

### Tune simulation parameters

Hyperparameters such as neighbor-list update frequency, thermostat and
barostat relaxation times, and cutoff distances should be tuned using
representative systems rather than default settings. Well-chosen parameters
reduce simulation time while maintaining accuracy.

### Use multiple simulation replicas

Running several independent copies of the same simulation improves the
statistical quality of measured quantities. Independent trajectories allow
students to compute error bars and assess reproducibility, which is important
when comparing results or performing parameter sweeps.

### Maintain clear file organization

Simulations often involve variations in temperature, pressure, interaction
strength, or other parameters. To avoid confusion, maintain a consistent and
hierarchical file structure. Below is an example layout for a parameter sweep
over temperature ($T$) and interaction strength ($V$):

```
data/
├── T-1.0/
│   ├── V-20/
│   │   └── input.sh
│   ├── V-30/
│   │   └── input.sh
├── T-1.5/
│   ├── V-205/
│   └── V-301/
```


Clear organization makes it easier to track simulation conditions, automate
workflows, and analyze results across parameter sets.

### Use tools to manage simulation campaigns

Large MD projects often involve many simulations with different parameters,
replicas, or initial configurations. Workflow managers and job-launching
tools—such as \texttt{signac-flow}, \texttt{Snakemake}, or simple shell
scripts—help automate job submission, monitor progress, handle restart files,
and ensure that all simulations follow a consistent protocol. These tools
reduce human error and make large simulation campaigns more repeatable and
scalable.


## Recommended MD Packages

A wide range of molecular dynamics (MD) engines is available, each with its
own strengths, target applications, and user community. Selecting an
appropriate package depends on the system being studied, the desired level of
detail, and available computational resources.

### Biophysics and atomistic simulations

Several MD packages are widely used for biomolecular systems such as
proteins, nucleic acids, and membranes:

1. GROMACS — optimized for speed and highly efficient on both CPUs and GPUs.
2. NAMD — scalable to very large systems and supercomputing architectures.
3. OpenMM — flexible, Python-driven, and ideal for custom workflows.
4. AMBER — traditionally used for biomolecular force fields and free-energy methods.


### General-purpose and materials-focused simulations

Other MD engines support a broad range of classical and coarse-grained
models, making them suitable for soft matter, polymers, and materials
science:

1. LAMMPS — extremely versatile, with support for many force fields and custom potentials.
2. HOOMD-blue — highly efficient for GPU-accelerated simulations of soft-matter and coarse-grained systems.


## References

- [LAMMPS documentation](https://docs.lammps.org)
- [HOOMD-blue documentation](https://hoomd-blue.readthedocs.io)
- [GROMACS documentation](https://manual.gromacs.org/current/index.html)
- [NAMD documentation](https://www.ks.uiuc.edu/Research/namd/documentation.html)
- [OpenMM](https://docs.openmm.org/latest/userguide/)
- [AMBER](https://ambermd.org/Manuals.php)

- [Packmol](https://m3g.github.io/packmol/userguide.shtml)
- [mBuild](https://mbuild.mosdef.org/en/stable/)
- [Foyer](https://foyer.mosdef.org/en/stable/)
- [AmberTools](https://ambermd.org/AmberTools.php)

- [OVITO](https://www.ovito.org/docs/current/)

- "Simulations: The Dark Side," Daan Frenkel, 2013 {cite}`frenkel2013simulations`

- Braun, E., Gilmer, J., Mayes, H. B., Mobley, D. L. ., Monroe, J. I., Prasad, S., & Zuckerman, D. M. . (2018). Best Practices for Foundations in Molecular Simulations [Article v1.0]. Living Journal of Computational Molecular Science, 1(1), 5957. {cite}`prasad2018best`

- In general, the Journal [Living Journal of Computational Molecular Science](https://livecomsjournal.org/index.php/livecoms/index) has excellent how to articles, tutorials, and best practices.
