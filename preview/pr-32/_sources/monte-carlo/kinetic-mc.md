# Kinetic Monte Carlo

## Kinetic Monte Carlo Simulations

(a.k.a. Dynamical Monte Carlo)

## Overview: MD vs. MC

Molecular dynamics (MD) simulations explicitly propogate the equations of motion throught time (e.g., Verlet algorithm) and, thus, they follow the real dynamics of a many-body system. However, time steps must be chosen small enough to address correctly the physics at hand and large enough to span a large time interval (which is often just pico-seconds, far from that to compare to experiments). Such restrictions on computational time limit the scope of dynamical simulations involving interacting particles, molecules, etc. In addition, as system complexity increases, there can be substantial decrease of system sizes and of real time evolution. System complexity can arise from may sources, e.g. gas-surface or condensed phases, which involve direction dependent, many-body interactions. In particular, MD is unable to perform simulations over long times due to the required repeated evaluations of potential and derivatives of potentials (potential-energy surface information). This may be partly overcome by so-called Hyperdynamics methods; nonetheless, it still consititutes a significant limitation.

Note on Time Scales in MD: High-frequency motions will determine the integration time step that must be used. For small time steps, low-frequency events cannot be sampled in reasonable computational time. Thus, MD has difficulty accomodating events that occurs with vastly different probabilities or rates.

Direct Monte Carlo (MC) simulation are a quasi-random, i.e. non-deterministic, approach to time evolution. In other words, MC methods evolve according to a stochastic algorithm, so as to explore the entire phase space (possible accessible states) of the system. Such stochastic attempts at changing the configurations usually have nothing to do with the underlying energy barriers inhibiting (or favoring) change of state (or motion). The MC methods follow a Markov process to evolve a system towards equilibrium, regardless of pathway. For example, the standard Metropolis MC alogrithm makes all transitions of the system to states of lower or equal energy with probability of unity, regardless of the barrier to access this state, the process required or the transition rate. Hence, MC moves based on the Metroplis algorithm cannot be interpreted dynamically as a process that simulates random motion in time! Nonetheless, MC methods do generate states that are correlated - each configuration is correlated because it is produced in a sequential Markov chain process. At present, all practical sampling methods produce correlated configurations (which is also why you use auto-correlation times to remove some clearly wrong correlations during analysis of MC data).

As for the case of diffusion, notice that there is a need for a relation to a real-time
process, which is not necessarily the same as a simulation time, depending on the MC Algorithm used (see later). The real time evolution is required to characterize the system, such as the diffusion constant. Most MC papers report everything in Monte Carlo Step (MCS) being one unit of simulation time. A MCS unit has different values depending on the problem, and it is not necessarily related directly to (real) experimental time.
Note on Time Scales in MC (The BIG Point): If, and only if, the cor- relations between these quasi-random states in the MC can be interpreted as dynamical correlations in a stochastic sense, can a kinetic interpretation of MC be made; that is, states represent actual motion of the system - not just sampling of the ensemble. If this is the case, then the expectation value can be calculated as time averages! And, importantly, a connection can be made between simula- tion time, tsim, and real time, tr, rather than just quoting the simulation time in terms of MC Steps (MCS), as often done. (More on this later.)
Kinetic Monte Carlo (KMC, sometimes called Dynamic MC, and not to be confused with Diffusion MC), in contrast, is meant to address (roughly speaking) materials-related problems whose physical outcomes are very much governed by the energy barriers between various possible states, or local configurations of the system. The rates for these physics-based transitions control the dynamics. KMC is meant to have a direct relationship to real time, rather than MCS. It also follows that KMC does not require potential derivatives, giving it a distinct advantage over MD methods.
Note on Time Scales in KMC: Events with largest rates will dominate the simulation, while low-rate (small probability of occurance) will be rare. Some- times such differences in rates can be overcome by ignoring "fast events"; in which case the KMC simulation will have events of similar order.
Obvious examples where KMC is needed: diffusion of an adatom species at the surface of a crystal or a concentration profile inside a bulk material. Each depends on the diffusion barriers associated with the local bonding (chemical environment) and position of other adatoms, and interaction with the substrate or bulk atoms. In these situations, the transition probabilities must occur so that the transition rates are established in terms of models for the rates of microscopic events comprising the overall process. As discussed by Fichthorn and Weinberg [8], when the transition probabilities are formulated as physical-based rates within a Poisson Process, a defi- nite (or unambiguous) relationship can be established between a MC time-step (MCS) and transition rates, if there is a "dynamical hierarchy" established for the possible transitions. Simply stated, a "dynamical hierarchy" requires that there is a spectrum of transition probabilities (when made relative to the maximum rate process) such that the maximum probability is one. Fichthorn and Weinberg [8] concluded that if

1. a so-called "dynamical hierarchy" is established for the transition probabilities which obeys detailed balance criterion;
2. time increments for each successful event are calculated properly (as we will discuss); and
3. independence of each possible events in system can be achieved,

then MC methods simulate a Poisson Process and both static and dynamic prop- erties of Hamiltonian may be obtained and interpreted consistently. Not all choices of transition probabilities, however, can satisfy these criteria, as exemplified by Kang and Weingberg [12] and Ray and Baetzold [17] (and discussed briefly later).

What is dynamical hierarchy? For example, in a simplistic adsorption- desorption of a "atom" at a surface, which we return to again, a transition rates for adsoprtion at any site i, WA, and for desorption, Wpi, of one type of molecule at a surface will be proportional to the overall rates for these events,  ̃å and ãò and the site-dependent coverage, if for nothing else than intuitively. The prob- abilities for these events would be PA TA/R, where R=rA+TD, and similarly for desorption. An order for these probabilities, or dynamical heirarchy, can be created most easily by defining W1= ri/Tmax. This means, if г > гò, that W1=1 and WD =  ̃D/ ̃A. Thus, WA > WD, a heirarchy exist [8]. This generalizes for more processes. You can be begin to intuit that time will be reflected in these rates, for the more probable the less time passes before the event occurs

Recall that a number of definitions of transition probabilities will give detailed balance. As such, an additional criteria is required so that the transition prob- abilities reflect unique transition rates, and, hence, simulate the dynamical phe- nomena within the model. It is the formulation of a dyamical heirarchy for the transition rates that is the additional criteria, see Ref. [8] for more discussion.

## Synopsis of KMC

Thus, main difference in KMC is to evolve a system using a stochoastic (or random- walk) algorithm that directly takes into account the physical energy barriers that govern the evolution of a system and that translate to a real time scale (t,, rather than just reporting some simulation time (tsim). Importantly, the KMC time for a given step will be scaled by the average time required to observe the particular stochastic event chosen to occur that time step. Thus, each KMC time step will have widely different magnitudes (sometime by orders of magnitude) depending on event, temperatures, barrier changes, and so on. Notably, KMC simulations are usually on a lattice (or ordered mesh) as many problems, such as surface diffusion, can always be mapped to an effective lattice.

Technically, independent events, such as in adhesion within a low-flux atmosphere, can be consider Poisson processes which have certain transition probabilities associ- ated with them. Each of the possible transition probabilities depend upon configu- ration and environment, and evolve as a function of time. It is the up-date per time step of these transition probabilities that become the time consuming portion of any Kinetic Monte Carlo. Basically, three criterion are needed to simulate a Poisson Process:

1. transitions must satisfy detailed balance,
2. there is a proper correspondence between tsim and tr, and
3. the events comprising the sequence of processes are independent.
It can be shown that any set of Poisson Processes, (or, based on a dynamical interpre- tation, any Monte Carlo calculations), are governed by a so-called Master Equation which encompasses all possible transitions allowed from a given set of configurations. As such, KMC allows simulation of non-equilibrium processes, not just simulation of equilibrium averages as typical from Monte Carlo.

## KMC Problems and Algorithms

Generally speaking, every simulation method has two key components: the physical problem and the algorithm (and data structure) to solve the model or equations rep- resenting that problem. It is important to keep in mind that for any simulation the efficiency of the algorithm may be more important than the physical model. For KMC, this is also true and there have been, and continue to be, research into developing efficient algorithms for updates of the stochastic rates each time step. These methods, e.g., "n-fold-way", binary-tree, and K-level search algorithms, and so on, combined with clever organization of data can speed up simulations by orders of magnitude, allowing significant improvement in statistics. We discuss briefly the important algo- rithm and data structures for KMC in a later section. Here we just cursorially state a few example areas that KMC have addressed. (Note that the references are listed in alphabetical order, hence, the references are not labelled sequentially.)
The paper of Fichthorn and Weinberg [8] is a very good intoduction to the fundamental underpinnings to KMC. For the effects within the simulation regarding physical energy barriers and stochoastic-based algorithms, as well as the connection of t, and tsim, see Kang and Weinberg [12]. Clark et al. [5] have discussed a hy- brid method that combines methodologies (MD and KMC) to address processes with substantially varying rates, in their case Chemical Vapor Depositon (CVD).
Probably, although I have performed no exhaustive search, one of the first ma- terials simulations using KMC for studies of surface diffusivity is that by Reed and Ehrlich at the University of Illinois [18]. This paper is probably not as well known because Reed and Ehrlich did not give the method a fancy name, like Kinetic Monte Carlo. Since that time there have been numerous publications in physics, chemistry, biology, surface science, materials science, etc., using the KMC approach. These include topics and physical processes such as:

1. surface diffusion (e.g. [18, 17]),
2. MBE (molecular beam epitaxy) growth (e.g. [15]),
3. CVD (chemical vapor deposition) growth (e.g. [5]),
4. vacancy diffusion in alloys (e.g. [1, 2]),
5. compositional patterning in alloys driven by irraditation (e.g. [6]),
6. polymers: topological constraints vs. entanglements (e.g. [16]),
7. coarsening of domain evolution (e.g.[11]), and
8. dislocation motion (e.g. [14]).

Note that, for instance, in thin-film growth there are multi-events occuring with varying time scales, e.g., deposition~ 1 monolayer/sec or hopping ~ 1 atom/site/sec. Each problem may have multiple processes with different rates, and, you need to know what are the (relative) rates of each. There are difficulties inherent. For reconstruc- tion, one needs to keep track of top atom and its bonding partners, dimer bond energies, dimer-dimer energy (e.g., does it prefer rows, not random?). The basic idea - describe system with a set of equations in terms of rates of reaction; iteratively solve equation in time; and, use data from a few atomistic calculations (or experiment or phenomenology). We will see this in our example problem of adsorption-desorption. Such Kinetic Rate Equation methods provide a simple means to describe a wide va- riety of systems, but one gives up spatial resolution of lattice MC, yet gains ability to model larger systems.
KMC may be used to study non-equilibrium situations, which may perhaps be best developed within a so-called Master-Equation Approach. For example, for studying an order-disorder transition in an Ising-type alloy on a lattice, KMC via a Master Equation approach has been used by Haider, Bellon, and Martin [10]. In this study, a non-equilibrium phase transition were studied where there were two competing pro- cesses: thermally-activated jumps and ballistic jumps, like those that occur under irradiation (which we shall consider for homework). A mean-field approximation was used for the kinetic equations for the evolution of the order parameter of interest, in their case of binary alloy ordering it was long-range order. The validity of KMC for non-equilibrium cases is guarenteed by establishing a "dynamical hierarchy" and transition based on Poisson processes [8].

## The Markovian Master Equation

As stated earlier, MC methods are correlated in that they are generate sequentially in a Markov process. The time evolution of the probability density is given by a Marko- vian Master Equation. This Master Equation for evolution of dynamical processes is quite intuitive and is given by

$$
\frac{\partial P\left(\sigma_f, t\right)}{\partial t}=\sum_{\sigma_i} W\left(\sigma_i \rightarrow \sigma\right) P\left(\sigma_i, t\right)-\sum_{\sigma_i} W\left(\sigma_f \rightarrow \sigma_i\right) P\left(\sigma_f, t\right) \quad .
$$

Here $\sigma$; and of are the successive (e.g., intial and final) states of the system, usually a set of 3-D vector for all M particles. P(o, t) is the probability that the system is in state o at time t, and W(o; → of) is the transition probability per unit time that the system will undergo a transition from state $\sigma$; to of. (Sometime Wij is explicitly given as wT-1, where 7 is a characteristic MCS and is a probability. Note that in Markov processes typically Σj Wij = 1 so that the total probability of doing an event (or not) is 100%). Generally, KMC can be regarded as algorithms that numer- ically solve the Eq. (1) by choosing randomly among various possible transitions and accepting (or rejecting) particular transitions with appropriate probabilities. Upon each successful transition (or, in some cases, each attempted transition), time is in- cremented in varying values 7 (in standard MC these typically are integral values of MCS). The time scale is incorporated via the transition rates (discussed in the next Section). But, importantly, these rates must be determined by some method, such as phenomenological arguments, experiment, or MD simluations, for they are not intrinisic to the KMC method.
It is noteworthy that each possible transition rate for an event depends upon configuration and environment and evolve as a function of time. (For example, the simple adsorption-adsorption model discussed later, the fractional surface coverage evolves in time and affects the rate of adsorption and desorption at each time-step. Hence, the UPDATE per TIME-STEP of the transition rates is the time-consuming portion of KMC. These issues also highlight the importance of data structure, search and update algorithms in the KMC methods, which are discussed later.
Fichthorn and Weinberg [8] have discussed that KMC formulated as a set of (independent) Poisson processes is valid for non-equilibrium Monte Carlo simulations if the transition rates satisfy the "dynamical hierarchy" criterion (or scaled rates, such that maximum probabilities are 1) mentioned earlier and these transition probabilities (based on the rates) obey detailed balance (or microscopic reversibility).

### Detailed Balance

Note that at steady-state (not necessarily equilibrium) the L.H.S. of Eq. (1) is zero and the sum of all transitions into a particular state o equals the sum of all transi- tions out of the state. You must be careful to ensure this if using phenomenological arguments (which can be done by requiring detailed balance). Although not actually guaranteed to give solution of the Master Equation at any given time, detailed-balance criterion, i.e.,

$$
W\left(\sigma_i \rightarrow \sigma_f\right) P\left(\sigma_i, t=\infty\right)=W\left(\sigma_f \rightarrow \sigma_i\right) P\left(\sigma_f, t=\infty\right)
$$

must be imposed so that the MC transition probabilities are consistent with the Boltzmann distribution,

$$
P(\sigma, t=\infty)=\frac{e^{-\beta H(\sigma)}}{Z}
$$

expected at thermal equilibrium (steady state). The detailed-balance criterion is clearly much more strict here than is required. However, as in the Metropolis algo- rithm, it was used in order to require no knowledge of the transition matrix in the Random Walk, and to guarantee Boltzmann-like behavior. There are some cases of driven systems, such as under irradiation, where the detailed-balance criterion cannot be obeyed while solving the Master Equation, see, e.g., the Refs. [1, 2, 10].
So, generally speaking, the choice of transition probabilities in MC simulations can affect the ratio of time scales [12], and gives a temperature dependence for the time scales. Most notably, under non-equilibrium situations the time scales for different transition probabilities (i.e., different types of MC simulations) results in non-linear time scales between these different MC methods. In addition, other important quantities are affected, such as the growth exponents and the diffusion coefficients, especially at low temperatures. For example, using the Kawasaki dynamics within Monte Carlo (where two "atoms" are swapped simultaneously so as to maintain sto- ichiometry, or number of spins), energy barriers are taking into account BUT there can NOT be a correspondence between MC time and real time for most physical processes - not unless there is a single rate operable in the physics under consider- ation [12, 17]. In other words, there can sometimes be a dynamical hierarchy for simple cases; but, the transition probabilities for Kawasaki dynamics cannot be gen- eralized for complex potentials to produce a "dynamical heirarchy", so time (diffusion constants, etc.) must be carefully considered due to the non-linear ratio of time scales.

### Possible Choices for $W(\sigma_i \rightarrow \sigma_ƒ)$

Let $\Delta E = H(\sigma_f) – H(\sigma_i)$. We have mentioned 3 choices, which are representative. (Here we follow ideas discussed by Kang and Weinberg [12].)

#### Metropolis Walk

$$
W_M\left(\sigma_i \rightarrow \sigma_f\right)=\frac{\omega_M\left(\sigma_i \rightarrow \sigma_f\right)}{\tau}=\left\{\begin{array}{ll}
e^{-\beta \Delta E} & \text { for } \Delta E>0 \\
1 & \text { for } \Delta E \leq 0
\end{array},\right.
$$

For Metropolis, 7 is the usual MCS. Note, again, that the acceptance of all states that lower energy is why Metropolis algorithm does not express the real dynamics
of the system. Another way to view this is that, unlike MD which diffuses through phase space based on real potential barriers and transitions, Metropolis based MC samples phase randomly - jumping here and their regardless of barriers required to reach a particular lower-energy minimum. In addition, this algorithm for reaching equilibrium clearly does not allow one to establish a dynamical hierarchy for the transition rates.

#### Kawasaki Dynamics

In Kawasaki dynamics two particles, or two spins, etc., are exchanged simultaneously so as to conserve particle (spin) number, which yields a factor of 2.

$$
W_K\left(\sigma_i \rightarrow \sigma_f\right)=\frac{\omega_K\left(\sigma_i \rightarrow \sigma_f\right)}{\tau}=\frac{e^{-\beta \Delta E / 2}}{e^{-\beta \Delta E / 2}+e^{\beta \Delta E / 2}},
$$

For a surface diffusion, for example, the attempt frequency $\tau = e^{\beta Q(t)/\nu}$, where Q is the average energy barrier a particle must jump and it is T dependent because σ; is. The frequency, v, of frustrated translation motion (parallel) on surface. Typically, in Kawasaki dynamics, 7 is taken as unit of time and the Q dependence is lost.

#### Thermally-Excited Process (barrier controlled)

$$
W_E\left(\sigma_i \rightarrow \sigma_f\right)=\frac{\omega_E\left(\sigma_i \rightarrow \sigma_f\right)}{\tau}=e^{-\beta E_b\left(\sigma_i, \sigma_f\right)}=e^{-\beta(\epsilon+\Delta E)}
$$

where the barrier depends on initial and final positions. That is, it is not symmetric (e.g., WE (of →σ;) = e-ße) but does obey microscopic reversibility or detailed bal- ance. Figure 1 shows the example barrier. Here, 7 is simply 1/v and we is a physical quantity: the probability of success for thermally excited barrier crossing for average time $\tau$.

#### A Comparison of Probabilities

For a single barrier jump, one can show (see Figure 1 for definition of energies) that $WK (i→j) = AWE (i→j)$, where

$$
A=\frac{e^{\beta \Delta E / 2+\beta|\epsilon|}}{e^{\beta \Delta E / 2}+e^{-\beta \Delta E / 2}}
$$

In an interacting lattice-gas model, the difference in energy for each pair of sites will depend on the local configuration around the pair of sites. So, each type of neighborhood will have a specific value of A. When you have no additional interaction in the lattice-gas, i.e. no dependence on other neighbors and so forth, then there is only one value of A. As a result, one can use Kawasaki dynamics and still obtain real time. For Kawasaki dynamics, the real time is t1 = ATS/N; whereas, for kinetic version with excitation barriers, real time is tr TS/N, where S is the number of MCS.


The only reason this may be important is if we consider normalizing the Thermal Excited transition probabilities with respect to hopping forward and backwards. We find that

$$
\frac{\omega_E(i \rightarrow j)}{\omega_E(i \rightarrow j)+\omega_E(j \rightarrow i)}=\omega_K(i \rightarrow j) .
$$

Thus Kawasaki dynamics renormalizes the probabilities of barrier crossings so that wk(i → j)+wk (j → i) = 1. It follows immediately that for barriers where we (i → j)+wE(j → i) < 1 the hopping rates are increased and, where the sum is > 1, the rates are decreased. Because of this renormalization, Kawasaki dynamics requires shorter computational times for processes where we are very small. When we are small, a hop has to be attempted many times before it is successful and computer time can be prohibitive. But, again, this depends also on algorithm used in simulation. For thermally excited KMC case using n-fold-way algorithm, this advantage of Kawasaki dynamics is no longer an issue. On may, however, wish to utilize the advantage of Kawasaki dynamics for maintaining stochiometry because it swaps two things at a time. This may be incorporated into thermal KMC approach too.

### Poisson Processes and Real Time

#### Poisson Statistics

If one adopts a dynamical interpretation of Monte Carlo with a perspective that we will resolve time such that events never occur simultaneously, then our MC algorithm must establish a chronological sequence of distinct events that are separated by various intervening times. Because the microscopic dynamics giving the exact times are not modelled directly, the events and associated times must be constructed from appropriately weighted probability distributions of all possible outcomes. This course- graining of time and events, with its inherent expectations, assumes that each event, i, can be characterized by an average transtion rate, r. Given this, it is assumed that any particular transition which is possible at t can again be possible at some later time t + At with a uniform probability based on its rate and is independent of previous events. This is, by definition, a Poisson process and is given by the Poisson distribution, i.e.

$$
P\left(n_i\right)=\frac{\left(r_i t\right)^{n_i}}{n_{i}!} e^{-r_i t}
$$

where n is a random variable counting the number of events i which have occured within time t. Notice the expected number of events occuring within a time t is <ni >= rit, which recovers the average occurance rate of the process. It can be shown that the Poisson process is consistent with the Master Equation (N.G. van Kampen, Stochastic Processes in Physics and Chemistry (North-Holland, Amsterdam, 1990).
A useful feature of the Poisson process is that an ensemble of independent Poisson processes will behave as one, large Poisson process. Thus, the statistical properties of the ensemble may be formulated in terms of the dynamics of the individual processes. For example, if there are two types of events with rates r1 and r2, then the total number of events of both types (n nin2) that occur in time t is a Poisson distribution with a total rate of R=r1 + r2. (For N types of events, RΣ1r; and n = n;) And, it follows that

$$
P(n)=\frac{(R t)^n}{n!} e^{-R t}
$$

These ideas and developments of Poisson statistics may be found in W. Feller, An Introduction to Probability Theory and Its Applications (Wiley, New York, 1975); E. Cinlar, An Introduction to Stochastic Processes (Prentice-Hall, Englewood Cliffs, 1975); and, H. Stark and J.W. Woods, Probability, Random Processes, and Estimation Theory for Engineers (Prentice-Hall, Englewood Cliffs, 1986).
3.2 Mean Time between Events and Real Time
Mean Time: An important additional attribute of the Poisson process is that the probability density of time t between successive events is
$ P(t) = Re^{-Rt}$

From this probability density, the mean time between successive events is < t >= 1/R. In a non-stationary situation (evolving towards equilibrium) all still holds but the rates are time dependent, see below.
Real Time via MC: If a system with processes under study can be cast as a set of independent events with known rates, then the time between events has an expotential distribution (Eq. 11) that can be sampled to determine the time that it takes for an event to occur. To see this from Eq. (11), note that the time to an event
is

$$
T(\tau)=\int_0^\tau d t^{\prime} R e^{-R t^{\prime}}=1-e^{-R \tau}
$$

which lies between [0,1]. So, a random variable U = e-RT is uniformly distributed between [0,1], and this relation allows us to obtain the real time, 7(in units of MCS), between successive events:

$\tau=-\frac{InU}{R}$, the **Real Time for Event Occurance**.
This random sampling of the Poisson time distribution for each chosen event ensures that a direct and unambiguous relationship between MCS and real time step is established.

Time in the General Case: Note that the basic ideas leading to the Poisson distribution of times and events are equally applicable to systems which are non- stationary and evolving towards equilibrium. The non-stationary Poisson process has overall rates that are a function of time. As a result, if the MC algorithm is made to simulate the Poisson process, then the relationship between MC time and real time can be given a firm basis in both static and dynamic situations. For the general case of N species (e.g. [8]), k events are characterized by the rates {r} = {T1, T2, ..., Tk}, which are consistent with average dynamic barriers arising from the potential energy surface. The N species can partition among various possible transition events as {n} = {n1, N2, ..., n}, where n is the number of species capable of undergoing a transition with a rate r; and N=1 n. If a sufficiently large system is used to achieve independence of the various events, then the MC algorithm effectively simulates the Poisson process and the passage of real time can be maintained in terms of {r} and {n}. For each trial i in which an event is realized, the time should be updated with an increment 7; selected from an exponential distribution with R1 = Σ=1njrj.

## References

- "Theoretical foundations of dynamical Monte Carlo simulations", K.A. Fichthorn and W.H. Weinberg, J. Chem. Phys. 95, 1090 (1991)
