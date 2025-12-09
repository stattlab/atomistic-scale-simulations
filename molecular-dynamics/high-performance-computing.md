
# HPC (High-Performance Computing)

## What is High-Performance Computing (HPC)?

High-performance computing (HPC) refers to the use of supercomputers and large compute clusters to solve problems that are too big, too slow, or too data-intensive for a typical desktop or laptop. Instead of running on a single machine with a handful of cores, HPC workloads run across tens, hundreds, or even thousands of processors working together on the same task. The performance of these systems is usually measured in floating-point operations per second (FLOPS). A modern laptop might sustain billions of FLOPS (gigaflops), while even a modest HPC cluster can reach trillions of FLOPS (teraflops), and nationalscale systems operate in the petaflop or exaflop range.

Conceptually, an HPC system is just a large number of ordinary computers connected by a high-speed network and managed as a single machine. These individual computers-called nodes-each have their own processors, memory, and local storage. When you submit a job to the cluster, you are asking the system to reserve some number of these nodes (or CPU cores on them) for a certain amount of time, run your program there, and then return the results. From the user's point of view, this looks like logging into a login node, writing a job script, and handing that script to a scheduler. Behind the scenes, the cluster's software stack figures out where and when your job can run.

The key reason to use HPC is that many scientific and engineering problems are naturally parallel. This means that different parts of the computation can be carried out at the same time. For example, you might simulate different spatial regions of a material on different processors, or evaluate forces on different atoms in parallel. To benefit from HPC, your code must be written to exploit this concurrency. A purely serial program-one that uses only one core-will not suddenly become dramatically faster just because it is launched on a supercomputer. At best, it will use a slightly newer CPU. Effective use of HPC therefore requires both appropriate algorithms and explicit parallelization strategies.

Another hallmark of HPC is its emphasis on throughput and scalability rather than user interactivity. Jobs are typically run in batch mode, often for hours or days, and many users share the same cluster. Fair access and efficient utilization are handled by a job scheduler, which queues jobs, allocates resources, and enforces limits. As a result, the workflows and tools used in HPC (batch scripts, modules, environment management, parallel I/O) look very different from those in everyday desktop computing, even though the underlying hardware components are recognizable.



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

## References

