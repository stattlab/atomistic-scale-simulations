
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


Finally, the entire system is orchestrated by a **scheduler** or resource manager, such as SLURM (used on Campus Cluster here at UIUC), PBS, or similar software. Users do not typically start jobs by directly launching programs on compute nodes. Instead, they write a job script specifying the resources they need, such as the number of nodes, the number of CPU cores per node, the number and type of GPUs, memory per node or per task, maximum runtime, and sometimes additional constraints like node features or queue/partition. A minimal SLURM job script illustrating these fields is shown below. The scheduler places the job in a queue, finds an appropriate set of nodes when they become available, and starts the job with the requested resources. It also enforces policies, such as limits per user or project, and can pack small jobs together on the same node to maximize utilization.


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



## 2. Types of Parallelism

The purpose of parallel computing is to take a computation that would normally run as a single stream of instructions and restructure it so that many operations can be carried out concurrently, allowing the work to be split across multiple hardware resources. In practice, most HPC applications combine several kinds of parallelism. They may exploit vector units inside a core, use multiple threads on a CPU socket, and spread work across many nodes in a cluster.

At a high level, we can distinguish between three main execution models. In **serial execution**, one worker performs all tasks in sequence. In **threaded** or **shared-memory parallelism**, multiple workers (threads) on the same node share a single address space and cooperate through common variables in memory. In **distributed-memory parallelism**, multiple processes, each with its own private memory on possibly different nodes, communicate explicitly by sending messages over the network. Modern large-scale codes often use a hybrid MPI +X model, where MPI handles distributed-memory parallelism across nodes and a secondary model (" $X$ ") such as OpenMP or CUDA handles shared-memory or accelerator parallelism on each node.

### 2.1. Serial

In the serial model, the program is executed by a single worker, namely a single operating-system process with a single thread of execution. Instructions are carried out one after another according to the program order, and there is no explicit coordination with other workers because there are no other workers. This model is conceptually simple and is still the starting point for most algorithm development because it is easier to design, debug, and reason about a serial implementation before introducing parallel constructs.

However, serial execution does not scale. Once the algorithm and its implementation are fixed, the only way to make it faster on a single core is to change hardware (e.g., higher clock speed or better microarchitecture) or rely on automatic forms of parallelism such as vectorization. But there is a hard upper bound: the program can never use more than one core at a time. On an HPC cluster with hundreds of thousands of cores available, this means a purely serial code is effectively leaving almost all the machine idle. For problems whose size or desired resolution keeps increasing-larger systems, finer grids, longer trajectories-serial execution quickly becomes a significant bottleneck.

### 2.2. Threaded (Shared Memory)

Threaded or shared-memory parallelism extends the serial model by allowing multiple workers to run concurrently within the same process, all sharing a common address space. These workers are called **threads**. Each thread executes its own sequence of instructions, but they all see the same global variables and can read or write to the same arrays in memory. On a typical HPC node, threads are mapped to CPU cores. On a GPU, threads are mapped to lightweight hardware execution units.

High-level threading frameworks make it relatively easy to express this pattern. On CPUs, a common approach is to use **OpenMP**, which adds compiler directives (such as `#pragma omp parallel for`) that instruct the compiler to split a loop across multiple threads. On GPUs, **CUDA** or similar frameworks allow kernels to be launched with thousands of threads, each handling one or more elements of the data. In both cases, the programmer identifies parts of the code that can be executed independently-often loops over particles, grid points, or matrix rows-and marks them for parallel execution.

Shared-memory parallelism has two appealing properties. First, it can be adopted incrementally. A working serial code can often be accelerated by adding a relatively small number of directives or annotations to its most time-consuming loops. Second, because all threads share memory, passing data between them is conceptually simple. Any thread can access any variable in the process's address space without explicit messages. However, this same feature introduces new challenges. When multiple threads update the same data, the final result can depend on the precise timing and interleaving of their operations, leading to subtle and hard-to-reproduce bugs. Avoiding these issues requires synchronization mechanisms such as locks, barriers, and atomic operations. Poorly designed synchronization can easily erase the benefits of parallelism. Moreover, scalability is limited by the resources of a single node, such as the number of cores, the available memory bandwidth, and the cache hierarchy. Once an application has saturated the cores and memory of a node, further speedup requires a move to distributed-memory parallelism.

### 2.3. Distributed (Distributed Memory)

Distributed-memory parallelism is the dominant model for cluster-scale computing. Instead of a single address space shared by all workers, each worker (an operating system process) has its own private memory, often on its own physical node. Processes cannot directly read or write each other's memory. To exchange data, they must communicate explicitly by sending and receiving messages over the network. The most widely used standard for this model in scientific computing is the **Message Passing Interface (MPI)**.

A typical MPI program begins by launching many processes, often one or several per node. Each process is assigned a unique rank (an integer ID) and runs the same program, but on different portions of the data. For example, in a domain-decomposition scheme, the simulation box is partitioned into spatial subdomains, and each process is responsible for updating the particles or grid points in its subdomain. At each timestep, processes perform local computations, then exchange boundary data with their neighbors so that interactions across subdomain boundaries are correctly accounted for. At the end of a timestep or at output times, processes may send partial results to a designated root process or collectively write to disk.

Because data movement is explicit, distributed-memory programming forces the programmer to think carefully about data layout and communication patterns. The cost of sending messages depends on both latency (how long it takes to initiate a communication) and bandwidth (how many bytes per second can be transferred), both determined by the cluster's network hardware or fabric. When the computation per process becomes small compared to the amount of data that must be exchanged, communication overhead can dominate the runtime. This is the fundamental reason why scalability is not unlimited: as the number of processes grows, maintaining efficient parallel execution increasingly depends on minimizing and overlapping communication.

#### 2.3.1. Communication Patterns

Within MPI and related libraries, communication occurs in a variety of patterns that reflect common algorithmic needs. The simplest is **point-to-point communication**, which occurs when one process sends a message directly to another. This is often used between neighboring subdomains in a spatial decomposition, where each process must exchange halo data (also called ghost data: copies of boundary values from neighboring subdomains needed to compute interactions near the boundary) only with a small set of neighbors.

Many algorithms also require collective operations, where a group of processes cooperates in a higher-level communication pattern. In a **broadcast (point-to-all)**, a single process distributes a piece of data to all others-for example, sending updated parameters or control flags to every process participating in the computation. In a **reduction (all-to-point)**, many processes contribute local values (such as partial sums, minima, or maxima) that are combined and delivered to a single target process. A classic example is computing a global norm or total energy from local contributions. There are also **all-reduce operations**, which combine reduction and broadcast in one step, so that all processes receive the global result, and **all-to-all patterns**, where every process sends potentially different data to every other process.

The performance of these communication patterns depends sensitively on the interconnect. High-bandwidth, low-latency network fabrics-the combination of the interconnect hardware and its topology (how the nodes and switches are connected) -allow collective operations to be implemented efficiently. MPI libraries exploit this by using tree-based or hierarchical algorithms that minimize the number of intermediate links and switches each message must traverse. By shortening these paths and reducing contention on shared links, they help prevent network congestion. On systems with slower or more heavily loaded networks, the same collectives can quickly become bottlenecks. Effective parallel algorithm design therefore involves not only balancing work across processes but also carefully managing how often and how much data is exchanged, and in which pattern.


#### 2.3.2. MPI + X

As HPC systems have evolved, individual nodes have become more powerful and more complex. A single node may have multiple CPU sockets with many cores, several GPUs, and a deep memory hierarchy. To exploit these resources efficiently, most large-scale applications now use a hybrid parallel model, often referred to as "MPI + X." In this approach, MPI provides distributed-memory parallelism across nodes (and sometimes across NUMA domains within a node), while " $X$ " represents an additional on-node parallel programming model such as OpenMP threads, CUDA kernels, HIP, SYCL, or another accelerator-focused framework.

In a simple MPI + OpenMP configuration, a cluster might run one MPI process per node, with that process spawning many OpenMP threads to utilize all the cores on the node. The MPI level is responsible for dividing the global problem into large chunks, one per process, and coordinating communication between them. Within each process, OpenMP is used to parallelize loops and kernels over the local data. Similarly, in an MPI + CUDA setup, each MPI process might drive one or more GPUs on its node, offloading compute-intensive kernels while using MPI to exchange data between nodes.


This hybrid strategy offers several advantages. It reduces the total number of MPI processes, which can mitigate pressure on the MPI implementation and the network, particularly in collectives and all-to-all communications. It also aligns naturally with the hardware hierarchy because it mirrors the two main levels of parallel hardware in a modern cluster: MPI handles communication across nodes over the network fabric, while threads or GPU kernels focus on exploiting the high-bandwidth, low-latency resources within each node (shared memory, caches, and device memory). At the same time, it introduces additional layers of complexity in load balancing, memory placement, and synchronization across and within nodes.


Ultimately, the effectiveness of MPI + X parallelism depends heavily on the characteristics of the underlying network hardware. High-bandwidth, low-latency interconnects make it possible for MPI processes to exchange data frequently without stalling the whole computation. If the network is slow or oversubscribed, communication time can overwhelm any gains from adding more nodes, and strong scaling quickly breaks down.



## 3. Parallelization in Molecular Dynamics (MD)

Molecular dynamics (MD) simulations are a natural fit for HPC because they involve performing very similar computations over and over again on large numbers of particles. At each timestep, the equations of motion are integrated by first computing the forces on every atom, then updating positions and velocities. Among all steps in the algorithm, the force calculation is usually the most expensive. For short-ranged interactions, this means evaluating pairwise forces only for nearby neighbors within a cutoff radius. For long-ranged interactions (e.g., Coulombic forces), additional work is spent on mesh or Ewald-type methods. Either way, the bulk of the runtime is spent in loops that look at many particle pairs and accumulate forces, making them prime targets for parallelization.

Because the same operations are repeated over many atoms or grid points, MD codes can exploit multiple layers of parallelism. At the finest level, vector units and GPU cores handle many pairwise interactions simultaneously. At the next level, multiple CPU cores cooperate via threading on a single node. At the highest level, large simulations are split across many nodes, each responsible for a subregion of the simulation box. Modern production codes typically combine all of these strategies: threaded or GPU kernels accelerate force loops on each node, while distributed-memory parallelism spreads the system across the cluster and coordinates communication between subdomains.



### 3.1. Threaded


In the threaded (shared-memory) approach, an MD simulation running on one node uses multiple CPU cores to evaluate forces and related quantities in parallel. Conceptually, the main loop over atoms or interactions is divided among several threads: each thread is assigned a subset of atoms, neighbor-list entries, or spatial cells, and computes the corresponding contributions to the forces and energies. Because all threads share the same memory, they all see the same arrays of positions, velocities, and forces.

There are different ways to organize this work. One common pattern is to parallelize over atoms: each thread takes a chunk of the atom index range and loops over the neighbors of those atoms. Another pattern parallelizes directly over pair interactions, distributing neighbor-list entries across threads. In both cases, care must be taken when multiple threads update the same force array. Many MD codes avoid these timing-dependent errors by assigning each atom to a "home" thread that accumulates its force, or by using per-thread temporary force buffers that are reduced at the end of the loop.

Threading can deliver substantial speedups on a single node with relatively small changes to a serial code, especially when using OpenMP pragmas or similar directives. However, its scalability is ultimately limited by on-node resources. As the number of threads increases, they compete for the same memory bandwidth and cache hierarchy. At some point, adding more threads produces diminishing returns because the force loop becomes memory-bound rather than compute-bound. Moreover, threading alone cannot extend a simulation beyond the memory capacity of a single node: it can accelerate a given system size but cannot make arbitrarily large systems feasible. For truly large MD simulations, threaded parallelism should be combined with distributed-memory decomposition.



### 3.2. Distributed


To scale MD beyond a single node, most codes use domain decomposition in a distributed-memory (MPI) setting. The basic idea is to partition the simulation box into spatial subdomains and assign each subdomain to a different MPI rank (process). Each process "owns" the atoms whose positions lie inside its subdomain. It stores their positions, velocities, and forces locally and is responsible for updating them in time. In this way, the global system is broken into many smaller chunks that can be advanced largely in parallel.

Interactions near subdomain boundaries require information about atoms in neighboring regions. To handle this, each process maintains a layer of **ghost particles** (also called halo atoms): copies of atoms that are actually owned by neighboring ranks but lie within the interaction cutoff of the local domain. At each timestep (or whenever needed), neighboring processes exchange boundary data: they send the coordinates of atoms near the boundary to their neighbors, which update their ghost layers. The local process can then compute forces involving both its owned atoms and the ghosts, ensuring that pairwise interactions across subdomain boundaries are correctly included.

As the simulation evolves, atoms move and may cross from one subdomain into another. When this happens, ownership of the atom must be transferred: the old process sends the atom's state (position, velocity, identity, etc.) to the new process, which adds it to its own list of owned atoms. This particle migration step keeps the domain decomposition consistent with the physical configuration. In practice, domain decomposition and migration are tightly integrated with neighbor-list construction, so that communication and bookkeeping overhead are minimized.

The efficiency of distributed MD parallelization depends on the balance between computation and communication. Each process spends most of its time computing forces for atoms in its subdomain, which roughly scales with the subdomain volume. Communication scales with the surface area of the subdomain, because only atoms near boundaries need to be exchanged. As the number of processes increases for a fixed global system size (strong scaling), subdomains become smaller and more "surface dominated," and the relative cost of communication grows. Good parallel performance therefore requires both a decomposition that keeps work balanced across ranks and a network fabric with low latency and high bandwidth, so that ghost exchanges and migrations do not dominate the timestep.



## 4.7.4. Parallel Performance

Even with a powerful cluster and a carefully parallelized code, performance is not unlimited. Some parts of a program are inherently serial, some algorithms do not expose enough independent work, and real hardware introduces overheads from communication, synchronization, memory bandwidth limits, and I/O. Understanding parallel performance means understanding both how much of your code can run concurrently and how efficiently your hardware can keep all workers busy.

A simple but useful model for the limits of parallel speedup is **Amdahl's Law**. Suppose a fraction $P$ of your program's runtime can be perfectly parallelized, while the remaining fraction $1-P$ is intrinsically serial. If you run on $N$ processors, the best possible speedup $S$ (compared to a single processor) is

$$
S=\frac{1}{(1-P)+\frac{P}{N}}
$$


Here, $S$ is the ratio of the original serial runtime to the parallel runtime, $P$ is the parallelizable fraction (between 0 and 1), and $N$ is the number of processors. As $N \rightarrow \infty$, the second term $P / N$ tends to zero, and the speedup approaches $1 /(1-P)$. In other words, no matter how many processors you add, the serial fraction of the code $1-P$ sets a hard ceiling. If only $90 \%$ of the code is parallelizable ( $P=0.9$ ), the maximum speedup is about $10 \times$, even on an arbitrarily large machine.

This model is deliberately optimistic because it assumes perfect load balance, no communication costs, and no caches or memory bottlenecks. In real applications, the "effective" serial fraction is often larger because communication, synchronization, and other overheads also scale badly with processor count. Nevertheless, Amdahl's reminds us that parallel performance is limited not just by hardware, but by algorithmic structure and software design. Improving performance often means refactoring the code to reduce serial regions and to restructure communication patterns, not just throwing more cores at the problem.

To reason more concretely about how your code behaves on a given system, two complementary metrics are commonly used: strong scaling and weak scaling. **Strong scaling** asks, "How much faster can I solve this fixed problem if I increase the number of processors?" **Weak scaling** asks, "How large can I make the problem if I grow it together with the processor count, without blowing up the runtime?"




### 4.1. Strong Scaling

Strong scaling measures how the runtime changes when you solve the same problem on increasing numbers of processors. You fix the total problem size-say, the number of atoms in an MD simulation or the number of grid points in a PDE solve-and then run the code with $N=1,2,4,8, \ldots$ processors, recording the time to solution in each case. If parallelization were perfect, doubling the number of processors would halve the runtime, and the speedup $S(N)$ would equal $N$.

A useful quantity here is the parallel **efficiency**, which compares the achieved speedup to the ideal speedup. If we take the _base time_ to be the runtime on a single processor, then the efficiency at $N$ processors is

$$
\text { Efficiency }=\frac{N \times \text { base time }}{\text { actual time }} .
$$


An efficiency of 100\% corresponds to linear speedup, which means that every additional processor contributes fully, and the computation scales perfectly.

In practice, efficiency drops as $N$ increases for several reasons. The serial portion of the code, as captured by Amdahl's law, becomes more prominent. Once the parallel region has been sped up, even a small serial region can dominate the total runtime. Communication and synchronization overheads also grow with processor count, because collective operations, halo exchanges, and global reductions become more frequent and more expensive relative to the purely local work. At the same time, load imbalance can emerge if the work is not distributed evenly, so that some processors finish early and sit idle while others are still computing. Finally, memory bandwidth and latency can become limiting, especially when many cores on a node compete for access to the same memory channels and caches.

In molecular dynamics, strong scaling is often favorable up to a certain number of cores for a fixed system size, after which the efficiency deteriorates sharply. Beyond that point, the cost of communicating ghost particles and performing global operations such as energy reductions no longer shrinks in proportion to the added compute resources. Strong-scaling studies are therefore essential for deciding how many processors to request for a given simulation. Past some threshold, adding more cores increases the allocation cost or queue time more than it reduces the wall-clock time to solution.



### 4.7.4.2. Weak Scaling


Weak scaling takes a different perspective. Instead of fixing the total problem size, you fix the work per processor and ask how the runtime changes as you increase both the problem size and the number of processors together. For instance, you might assign a fixed number of atoms per core in an MD simulation and then run with $N=1,2,4,8, \ldots$ cores, each time increasing the total number of atoms proportionally. In an ideal world, the runtime would remain constant so that each processor does the same amount of local work, and any extra overhead from communication is negligible.

In practice, weak scaling reveals how well an algorithm and implementation handle the overheads that grow with system size, which include the communication volume, the cost of collective operations, the pressure on the network fabric, and the increased load on shared services such as filesystems. If the runtime grows slowly with $N$, you have good weak scaling meaning that the code can handle larger and larger problems without a disastrous increase in time to solution. If the runtime grows rapidly, then some part of the computation-often communication, I/O, or global synchronization-does not scale with problem size as gracefully as the local work.

From the user's point of view, weak scaling answers the question, "How big can I go?" If your application shows good weak scaling up to hundreds or thousands of processors, you can use larger allocations to handle much bigger systems than would fit on a single node, while keeping runtimes within reasonable limits. If weak scaling breaks down beyond a certain point, then the machine may still be capable, but the code or algorithm must be redesigned to reduce global communication, restructure data layouts, or exploit different parallel patterns.



## References

(1) Department of Computer Science, PBR Visvodaya Institute of Science And Technology, India; Sravanthi, G.; Grace, B.; Kamakshamma, V. A Review of High Performance Computing. _IOSRJCE_ **2014**, _16_ (1), 36–43. [https://doi.org/10.9790/0661-16173643](https://doi.org/10.9790/0661-16173643).

(2) Plimpton, S. "Fast Parallel Algorithms for Short-Range Molecular Dyanmics." _J. Comput. Phys._ **1995**, 117, 1-19.

(3) Páll, S.; Zhmurov, A.; Bauer, P.; Abraham, M.; Lundborg, M.; Gray, A.; Hess, B.; Lindahl, E. Heterogeneous Parallelization and Acceleration of Molecular Dynamics Simulations in GROMACS. _The Journal of Chemical Physics_ **2020**, _153_ (13), 134110. [https://doi.org/10.1063/5.0018516](https://doi.org/10.1063/5.0018516).

(4) Hill, M. D.; Marty, M. R. Amdahl’s Law in the Multicore Era.

(5) Lawrence Livermore National Laboratory. **Introduction to Parallel Computing Tutorial;** High Performance Computing.
https://hpc.llnl.gov/documentation/tutorials/introduction-parallel-computing-tutorial?utm_source=chatgpt.com (accessed 2025-12-06)

