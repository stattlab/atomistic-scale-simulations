# Entropy and Temperature

Entropy and Temperature arise from the algebra of "big" numbers. The logarithm of the number of accessible states of the system is the entropy and of great importance to the thermal properties of a system. (This follows Kittel "Thermal Physics")

Consider two systems only in thermal contact. The systems have particle number, $\mathrm{N}_{1}$ and $\mathrm{N}_{2}$, and energy, $\mathrm{E}_{1}$ and $\mathrm{E}_{2}$. When in thermal contact the combined "new system" now has $\mathrm{N}=\mathrm{N}_{1}+\mathrm{N}_{2}$ particles and total energy $E_{1}+E_{2}=E_{1}^{\prime}+E_{2}^{\prime}=E$.

What is the degeneracy of states that are accessible? The degeneracy function is $\mathrm{g}(\mathrm{N}, \mathrm{E})$. For the combined system,

$$
g(N, E)=\sum_{E_{1}}^{\leq E} g_{1}\left(N_{1}, E_{1}\right) g_{2}\left(N_{2}, E-E_{1}\right)
$$

Sum is over all possible accessible states $E_{1}$. The product $g_{1} g_{2}$ is the number of accessible state for the combined systems for energy $E_{1}$.

For statistical mechanics, a very important feature of this product is that it must have a maximum for some value $E_{1}=\bar{E}$, the most likely energy. It is an extremely sharply peaked. (Consider $g_{1}(x)=e^{-x^{2}}$ and $g_{2}(x)=e^{(8-x)^{2}}$. The product is basically zero except for a narrow region around $\mathrm{x}=4$, and it is $10^{13}$ smaller than $g_{1}(0)$ and $\left.g_{2}(8)!!\right)$

Consider the extremal properties of this distribution.

$$
0=d g=\left(\frac{\delta g_{1}}{\delta E_{1}}\right)_{N_{1}} g_{2} d E_{1}+g_{1}\left(\frac{\delta g_{2}}{\delta E_{2}}\right)_{N_{2}} d E_{2}
$$

and we have $d E_{1}+d E_{2}=0$. (We shall assume here that this is a maximum, which can be proved.) Then, the most probable configuration of the combined system (using $d E_{1}=-d E_{2}$ ) gives

$$
\frac{1}{g_{1}}\left(\frac{\delta g_{1}}{\delta E_{1}}\right)_{N_{1}}=\frac{1}{g_{2}}\left(\frac{\delta g_{2}}{\delta E_{2}}\right)_{N_{2}}
$$

or

$$
\left(\frac{\delta \ln g_{1}}{\delta E_{1}}\right)_{N_{1}}=\left(\frac{\delta \ln g_{2}}{\delta E_{2}}\right)_{N_{2}}
$$

Let us define ENTROPY as $S(N, E)=\ln g(N, E)$ and INVERSE TEMPERATURE as $\left(\frac{\delta \ln g}{\delta E}\right)_{N}=T^{-1}$. We have for the maximal probability and equilibrium configuration the $T_{1}=T_{2}$, the temperatures must be equal.

Note also that equilibrium is reach only when the number of accessible states are a maximum.
Note also that, in this maximal state, $S=\ln g_{1} g_{2}=\ln g_{1}+\ln g_{2}$ and the Entropy is Additive.

For Statistical Mechanics or our simulation, we are interested in properties where one of the systems in contact is a very large thermal reservoir, i.e. $N_{R} \gg N_{s}$ and $E_{R} \gg E_{s}$. Let us even suppose that the systems are now in thermal and diffusive contact, so they exchange energy and particles.

What are the statistical properties of the system? We consider an ensemble consisting of indentical copies of the "system + reservoir" having accessible states only.

What is the probability to find the system with N particles and in the state $s$ of energy $\epsilon_{s}$ ? Clearly the probability $P\left(N_{s}, \epsilon_{s}\right)$ proportional to the number of accessible states of the RESERVOIR. Because when we specify the state of the system, i.e. N and $\epsilon_{s}$, the number of accessible states can only arise from the reservoir: $g($ sys + res $)=g($ sys $) g($ res $)=g($ res $)$ as $g($ sys $)=1$ (for it was specified). Therefore,

$$
P\left(N_{s}, \epsilon_{s}\right) \propto g\left(N-N_{s}, E-E_{s}\right)
$$

where $\mathrm{g}(\mathrm{N}, \mathrm{E})$ depends only on the reservoir. Notice that this relation is for the probability of the system, yet is appears to depend on the make up of the reservoir (strange indeed), but only (as we shall see) on the temperature, T , and chemical potential, $\mu$, of the reservoir.

As we do not know the proportionality constant, let us consider the ratio of probabilities of two states:

$$
\frac{P\left(N_{1}, \epsilon_{1}\right)}{P\left(N_{2}, \epsilon_{2}\right)}=\frac{g\left(N-N_{1}, E-E_{1}\right)}{g\left(N-N_{2}, E-E_{2}\right)}
$$

Notice that $N-N_{i} \ggg N_{i}$ and the $\mathrm{g}(\mathrm{N}, \mathrm{E})$ are extremely large numbers arsing from the reservoir. So, to avoid big numbers we can define the Entropy as $S(N, E)=\ln g(N, E)$ and work with the logarithms.

$$
\frac{P\left(N_{1}, \epsilon_{1}\right)}{P\left(N_{2}, \epsilon_{2}\right)}=e^{S\left(N-N_{1}, E-E_{1}\right)-S\left(N-N_{2}, E-E_{2}\right)}
$$

Because the reservoir is very large compared to the system, we may expand to first-order (this can be verified as OK) to get $\Delta S$ in the exponent using Taylor's Series expansion.

$$
\Delta S=-\left(N_{1}-N_{2}\right)\left(\frac{\delta S}{\delta N}\right)_{E}-\left(E_{1}-E_{2}\right)\left(\frac{\delta S}{\delta E}\right)_{N}
$$

By defining

$$
\frac{1}{T}=\left(\frac{\delta S}{\delta E}\right)_{N} \quad-\frac{\mu}{T}=\left(\frac{\delta S}{\delta N}\right)_{E}
$$

We immediately get that

$$
\frac{P\left(N_{1}, \epsilon_{1}\right)}{P\left(N_{2}, \epsilon_{2}\right)}=\frac{e^{-\left(E_{1}-\mu N_{1}\right) / T}}{e^{-\left(E_{2}-\mu N_{2}\right) / T}}
$$

The numerator is the Gibbs' probability distribution for canonical ensemble, whereas for constant N the $\mu N$ drops out and we have the Boltzmann distribution.

Gibbs was actually more clever. He introduced the "index of probability" defined as $\ln g_{N}$ and its ensemble average $S=\int d V_{\Gamma} g_{N} \ln g_{N}$. Under the condition that $\langle E\rangle=\int d V_{\Gamma} E g_{N}$, microcanonical contraint, Gibbs showed that S was a maximum when $g_{N}=g_{N}^{0}=e^{\beta(F-E)}=e^{S}$, so that $S=\ln g_{N}^{0}$ for equilibrium.

This is, in effect, Gibbs' principle of maximum entropy, a Laplacian-like view of probability (not a frequency or counting-occurances-type viewpoint). Essentially, given any constraint, such as constant E, and the fact that the probability must sum to one, you can maximize the "entropy" $S=-K \sum_{i} P_{i} \ln P_{i}$ and obtain any of the distribution that we know, such as microcanonical for constant E, etc. The distributions such as Fermi-Dirac and Bose-Einstein occur because of how the states $\epsilon_{i}$ are occupied, like 1 or 0 for Fermions and $1,2, \ldots$ infinty for Bosons.

More generally, this entropy $S=-K \sum_{i} P_{i} \ln P_{i}$ is called the Shannon Informational Entropy. With this general entropy and utilizing Maximum Entropy Method, you may find the most probable state for anything that has informational entropy: encryption, image analysis, etc. As an example, using the astronomical data provided by a friend, Laplace predict that Jupiter had to have an additional moon (not yet observed) to explain the deviation in the observed data. He even predicted it mass, being only off about $10 \%$ from today's value. (Ah, to be as amazing as Laplace!)\\
"Entropy" again results from the algebra of large numbers and what it means to be the most probable or average, whether it is thermodynamic state or something else. Using this Principle of Maximum Entropy and a few results from Probability Theory regarding correlated variables, most all of Statistical Mechanics can be derived in a few lines. While less straightforward, such an approach can also be used for non-equilibrium Statistical Mechanics (see "Introduction to Statistical Mechanics, vol 1: Equilibrium", Grandy, Jr. 1987)

An outstanding discussion of all these points, as well as Erogdicity, see "The Principle of Statistical Mechanics", R.C. Tolman, 1937.

Most importantly for simulation class is that if we pick the correct distribution function for our problem then we have gone quite far into be able to obtain averages via simulation. It is our concern later to learn how to choose the probability distribution for our ensemble cleverly.

## Useful Formulas

The Boltzman constant $k_{B}$ is used to express temperature in units of energy, $k_{B} T$. The inverse of $k_{B} T$ is often needed and is notated $\beta=1 /\left(k_{B} T\right)$, which has units of inverse energy. Note that $\beta \rightarrow \infty$ is the (absolute) zero temperature limit, and $\beta \rightarrow 0$ it the high-temperature limit.

For a Boltzman distribution at temperature $T$, the probablility of a state $i$ being occupied is

$$
P_{i}=\frac{1}{Z} \mathrm{e}^{-\beta E_{i}}
$$ (eq1)

where the normalizing factor, $Z$, is the partition function, defined as the sum over all states:

$$
Z & =\sum_{i} \mathrm{e}^{-\beta E_{i}} \\
& =\operatorname{Tr}\left[\mathrm{e}^{-\beta H}\right] \text{ (QM definition, H is the Hamiltonian) }  \\
& =\mathrm{e}^{-\beta F} \text{ (Defines the free energy F). }
$$

Using Eq. {eq}`eq1`, the average value of an observable can be written as

$$
\langle A\rangle & =\frac{1}{Z} \sum_{i} A_{i} \mathrm{e}^{-\beta E_{i}} \\
& =\frac{1}{Z} \operatorname{Tr}\left[A \mathrm{e}^{-\beta H}\right] ; \quad(\mathrm{QM}),
$$

where $A_{i}$ is the value of $A$ for the state $i$ in the ensemble. In the QM case, $A$ is an operator.\\
A state of a classical system of $N$ particles is a point in phase space, described by $2 \times 3 N$ coordinates: $\left(\mathbf{r}_{1}, \mathbf{r}_{2}, \ldots \mathbf{r}_{\mathbf{N}}, \mathbf{p}_{1}, \mathbf{p}_{\mathbf{2}}, \ldots, \mathbf{p}_{\mathbf{N}},\right)=(\mathbf{R}, \mathbf{P})$. (Note: $\mathbf{p}_{i}=m \mathbf{v}_{i}$ is the momentum of particle $i$.) A classical state is defined as having as volume $h^{3 N}$ in phase space.

The probability of a state ( $\mathbf{R}, \mathbf{P}$ ) with energy $E$ being occupied in the canonical ensemble is

$$
P(R, P) d R d P=\frac{1}{Z} \frac{\mathrm{e}^{-\beta E} d R d P}{N!h^{3 N}}
$$

where the energy is

$$
E=V(R)+\sum_{i} \frac{p_{i}^{2}}{2 m_{i}}
$$

Since the details of the system only enter in the interactions $V(R)$, the momentum part can be solved to give some general results for any classical system (gas, solid or liquid),

\begin{array}{rlr}
\left\langle\frac{p^{2}}{2 m}\right\rangle=\frac{3}{2} N k_{B} T & & (\text { Equipartion of KE }), \\
P(v) d v & =\sqrt{\frac{2}{\pi}}\left(\frac{m}{k_{B} T}\right)^{\frac{3}{2}} v^{2} \mathrm{e}^{-\frac{m v^{2}}{2 k_{B} t}} d v & (\text { Maxwell Velocity Distribution }), \\
Z & =\frac{f^{3 N}}{N!} \int d R \mathbf{e}^{-\beta V(R)} ; & f=\left(\frac{2 \pi m \beta}{h^{2}}\right)^{\frac{1}{2}} .
\end{array}

The last line, Eq. (11), shows that only the configurational part of the partion funciton is needed classically.
