
# HPC (High-Performance Computing)

## 1. What is High-Performance Computing (HPC)?

High-performance computing (HPC) refers to the use of supercomputers and large compute clusters to solve problems that are too big, too slow, or too data-intensive for a typical desktop or laptop. Instead of running on a single machine with a handful of cores, HPC workloads run across tens, hundreds, or even thousands of processors working together on the same task. The performance of these systems is usually measured in **floating-point operations per second (FLOPS)**. A modern laptop might sustain billions of FLOPS (gigaflops), while even a modest HPC cluster can reach trillions of FLOPS (teraflops), and nationalscale systems operate in the petaflop or exaflop range.

Conceptually, an HPC system is just a large number of ordinary computers connected by a high-speed network and managed as a single machine. These individual computers-called nodes-each have their own processors, memory, and local storage. When you submit a job to the cluster, you are asking the system to reserve some number of these nodes (or CPU cores on them) for a certain amount of time, run your program there, and then return the results. From the user's point of view, this looks like logging into a login node, writing a job script, and handing that script to a scheduler. Behind the scenes, the cluster's software stack figures out where and when your job can run.

The key reason to use HPC is that many scientific and engineering problems are naturally parallel. This means that different parts of the computation can be carried out at the same time. For example, you might simulate different spatial regions of a material on different processors, or evaluate forces on different atoms in parallel. To benefit from HPC, your code must be written to exploit this concurrency. A purely serial program-one that uses only one core-will not suddenly become dramatically faster just because it is launched on a supercomputer. At best, it will use a slightly newer CPU. Effective use of HPC therefore requires both appropriate algorithms and explicit parallelization strategies.

Another hallmark of HPC is its emphasis on throughput and scalability rather than user interactivity. Jobs are typically run in batch mode, often for hours or days, and many users share the same cluster. Fair access and efficient utilization are handled by a job scheduler, which queues jobs, allocates resources, and enforces limits. As a result, the workflows and tools used in HPC (batch scripts, modules, environment management, parallel I/O) look very different from those in everyday desktop computing, even though the underlying hardware components are recognizable.




### 1.1. Components


Although HPC systems can vary in size and architecture, they share a common set of building blocks. At the heart of the system are the **compute nodes**, the machines that actually execute user jobs. Each node contains one or more **CPUs**, and each CPU provides multiple cores. These **cores** run the main program logic and many parallel threads. In addition to CPUs, many modern nodes also provide accelerators such as GPUs. GPUs contain thousands of simpler cores optimized for massively parallel arithmetic, making them extremely effective for certain workloads that apply the same operations to many independent data elements, have high arithmetic intensity (many floating-point operations per byte moved), and exhibit regular control flow and memory access patterns.


Each node has its own pool of RAM, which serves as local working memory for that node's processes. The amount of RAM available per node (and per core) places practical limits on the size of problems that can be handled efficiently. If a computation exceeds the memory capacity of a single node, the problem must be distributed across multiple nodes, and the program must explicitly manage the communication of data between them. A common pattern, for example, is to use MPI-based domain decomposition where each process holds only a subregion of a large array (such as a part of a mesh or subset of atoms) and, at each timestep or iteration, exchange ghost or halo data with neighboring processes via message passing so that boundary interactions are correctly updated. Nodes also have **local disk storage** (either hard drives or SSDs), which can be used for temporary files or caching but is usually not the main place where users store data, especially on shared systems.


To support many users and jobs, clusters rely on a **networked file system** that is visible from all nodes. This is typically implemented using a parallel or distributed filesystem such as Lustre, GPFS, or a similar technology. On many systems, users see distinct logical areas. A **home directory** (`/home` ) is usually relatively small, backed up regularly, and intended for scripts, source code, and small configuration files. In contrast, a **scratch directory** (`/scratch` ) is much larger and designed for high-throughput I/O. Scratch storage is fast but not backed up, and files there are often purged periodically. The intended workflow is to run large, I/O-intensive jobs from /scratch , keep only essential results, and move important data back to a more permanent location when the job is finished.


All of these nodes and filesystems are tied together by a high-speed interconnect, the specialized network that lets nodes exchange data with low latency and high bandwidth. This network fabric is critical for distributed parallel applications, where the cost of communication can dominate the overall runtime if the interconnect is slow or congested. High-quality interconnects enable codes to scale to hundreds or thousands of nodes without being completely bottlenecked by communication overhead.


Finally, the entire system is orchestrated by a **scheduler** or resource manager, such as SLURM (used on the Campus Cluster here at UIUC), PBS, or similar software. Users do not typically start jobs by directly launching programs on compute nodes. Instead, they write a job script specifying the resources they need, such as the number of nodes, the number of CPU cores per node, the number and type of GPUs, memory per node or per task, maximum runtime, and sometimes additional constraints like node features or queue/partition. A minimal SLURM job script illustrating these fields is shown below. The scheduler places the job in a queue, finds an appropriate set of nodes when they become available, and starts the job with the requested resources. It also enforces policies, such as limits per user or project, and can pack small jobs together on the same node to maximize utilization.


```
#!/usr/bin/env bash

#SBATCH -J md_example              # Job name
#SBATCH -p compute                 # Partition / queue
#SBATCH -A my_project_account      # Account / project
#SBATCH -N 2                       # Number of nodes
#SBATCH --ntasks-per-node=32       # MPI tasks per node
#SBATCH --gres=gpu:1               # GPUs per node (if needed)
#SBATCH -t 02:00:00                # Time limit (hh:mm:ss)
#SBATCH -o md_example_%j.out       # Standard output (%j = job ID)

# Load any required modules
module load my-md-code/1.0

# Run the parallel program
srun my_md_executable input.in
```



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

