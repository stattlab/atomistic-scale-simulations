
# HPC (High-Performance Computing)

## What is High-Performance Computing (HPC)?

- **HPC** uses "supercomputers" or "clusters" to solve advanced computing problems.
- Typically measured in **teraflops** or more (FLOPS = floating point operations per second).
- Involves multiple computers connected via a network working together.

### Components

- **Compute nodes**: Perform calculations.
- **CPU cores**: Traditional processors.
- **GPU/Accelerators**: Optimized for number crunching and machine learning.
- **RAM**: Local memory.
- **Local disk space**: HDD or SSD.
- **Network file system**: Shared storage (e.g., APFS, Lustre).
  - `/home`: Smaller, slower, backed-up.
  - `/scratch`: Larger, faster, not backed-up, purged regularly (used for I/O intensive jobs).
- **Scheduler** (e.g., SLURM): Manages job distribution.
  - Specifies number of nodes, cores, accelerators, memory, runtime, and resource sharing.

> To utilize HPC effectively, code must be **parallelized**.

## Types of Parallelism

### **Serial**

- One worker does all tasks.
- Easy to implement but doesn't scale.

### **Threaded (Shared Memory)**

- Multiple workers on one node/accelerator.
- All share memory.
- Examples:
  - **OpenMP**: `#pragma omp`
  - **CUDA**: GPU parallel programming
- Easy to use, but not all code parallelizes well.

### **Distributed (Distributed Memory)**

- Multiple nodes, each with its own memory.
- Workers communicate over a network using **MPI** (Message Passing Interface).
- Example: Split data, each node processes part, then results are combined.

#### Communication Patterns

- Point-to-point
- Point-to-all (broadcast)
- All-to-point (reduction)
- All-to-all

#### **MPI + X**

- Combines distributed and threaded parallelism for large-scale computing.

> Performance depends on network hardware (fabric) for high bandwidth and low latency.

## Parallelization in Molecular Dynamics (MD)

- **Force calculation** is the most expensive part.

### Threaded

- Use multiple cores to evaluate pairwise forces.
- Works, but limited scalability.

### Distributed

- **Domain decomposition**: Split simulation box among processors.
- Each processor "owns" particles in its domain.
- **Ghost particles**: Shared across boundaries for interactions.
- Particles migrate between domains as they move.

## Parallel Performance

- Not all code or problems parallelize well.
- **Amdahl’s Law**: Speedup is limited by the non-parallel portion.

$$
S = \frac{1}{(1 - P) + \frac{P}{N}}
$$

Where:

- \( P \) = fraction of code that can be parallelized
- \( N \) = number of processors

### **Strong Scaling**

- Measures speedup for a fixed problem size as resources increase.

$$
\text{Efficiency} = \frac{N \times \text{base time}}{\text{actual time}} \quad (\text{Ideal} = 100\%)
$$

> How fast can I go?

### **Weak Scaling**

- Measures how runtime changes when both problem size and resources increase proportionally.

> How big can I go?

## Additional Resorces

 test
