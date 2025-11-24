# The Ising Model

As an illustration of the heat bath method we discuss the Ising model, the "fruit-fly" of the study of phase transitions. The Ising model consists of a lattice with a single spin $1 / 2$ particle on each lattice site interacting only with nearest neighbors. On a square lattice the neighbors are a single unit away in either the north-south-east-west direction. On each site $i$ the spin $\sigma_{i}$ is either up $\sigma_{i}=+1$ or down $\sigma_{i}=-1$. Then the classical energy of a given spin arrangement is $s=\left\{\sigma_{1}, \sigma_{2} \ldots, \sigma_{N}\right\}$ :

$$
E=-J \sum_{(i, j)} \sigma_{i} \sigma_{j}-\mu H \sum_{i} \sigma_{i}
$$

where $J>0$ is ferromagnetic and $J<0$ is antiferromagnetic and the second term describes the coupling to an external magnetic field. The first sum is only over nearest-neighbor pairs. We need to sample spin arrangements for the Boltzmann distribution $\exp (-\beta E(s))$. At low temperatures, the spins like to line up pointing the same direction (for the ferromagnetic case). At high temperatures the spins assume a random distribution.

Here, we shall only talk about the Lenz (1920) or Ising (1925) type model (rather than a vector-type, or Heisenburg, model) in which si are the thermodynamic "spin variables" which can take the values ±1. Here, J can be (Ferromagentic) FM-like interactions tending to cluster like spins together, or (Anti-ferromagnetic) AFM tending to order spins periodically (e.g., ...up...dn...up...dn). (Ising only studied this model in 1-D, where there is no phase transition.) For generality, I have included an external magnetic field (in fact, I have made it site dependent which for mathematical convienience allows one to take derivatives with respect to field, useful for getting susceptibilities).

Onsager (1944) evaluated the partition function exactly for the 2D Ising model on a square lattice and in so doing proved that there is a phase transition between the oriented and random arrangements. For $\beta$ larger than $0.4407 / J$ the spins like to line up, either in the up or down direction. It is in the same universality class of the liquid-gas phase transition. This means near the critical point, the behavior should have the same exponents.

Now consider two different choices for transition moves.

- Single Flip moves

The Classic Metropolis algorithm would be to choose a spin at random and try to flip it. That is: $\sigma^{\prime}=-\sigma$. Then the acceptance probability would be $q=\exp \left(-2 \beta J \sigma_{i} M_{i}\right)$ where $M_{i}$ is the magnetization of the neighborhood of $i: M_{i}=\sum_{j:|i-j|=1} \sigma_{j}$. We compare $q$ to a uniform random number and decide whether or not to flip. One time-saving trick: one can tabulate powers of $\exp (-2 \beta J)$ and avoid having to do any exponentials once the random walk starts.

- Heat Bath

As before choose a spin at random (or sweep through the lattice systematically). In heat bath, we also compute the site magnetization but we disregard the current value of $\sigma_{i}$. Its new state will be $\sigma_{i}=+1$ if $u<f\left(x_{i}\right)$ and $\sigma_{i}=-1$ otherwise. Here $f(x)=\exp (x) /(\exp (x)+\exp (-x))$ and $x=\beta J M_{i}$. As before, needed values of $f(x)$ can be tabulated for the possible magnetization states, $(-Z,-Z+1 \ldots Z-1, Z)$. In heat bath there is no acceptance needed.

There are many more variations on Ising methods. Some use the bit structure of the problem more directly. There is also the Swendson-Wang cluster algorithm.

## Nearest-Neighbor Model and Simulation of Averages

The so-called Nearest-Neighbor Ising model is one in which Jij = J if i and j are nearest neighbors, and 0 otherwise.  Even for this very simple interaction the statistical mechanics and phase transformation can be very interesting depending on the type of Bravais lattice and dimensionality of lattice. In other words, you do not need complexity of potential to get complex phase behavior.
For the Nearest-Neighbor Ising Model, the interesting thermal averages are the Energy, E, and the Magnetization, M, and perhaps also the pair correlations (or susceptibility). The site Magnetization, Mi, is < si >. Hence, using Eqs. 1-4, you can show that

$$
Mi = < si > = < tanh B( \sum_j Jij sj + hj) >
$$

where the thermal average <...> is over the remaining spin variables not on site i. Let us explore a Mean-Field Theory approximation to this where where the average has been moved through the TANH function, or equivalently, we have ignored correlations in the variables, or, in other words, rather than handle si sj we suppose that site i "feels" the average effect of all other sites, so si < sj >. In this approximation the statistical averages can be performed because correlations between specific sites have been ignored. In any case,

$$
Mi = < si > = tanh B( \sum_j Jij < sj > + hj) .
$$

This is a transcendental equation whose solution may be found graphically. The R.H.S. TANH function is a slanted s-like curve and the L.H.S. is a straight line. Their intersection is a solution. We find two types. For temperatures above a certain TCritical, the solution is at M=0, whereas at some lower T there are two solution ±M. These two solutions are the two possible ground states of the Ising model: all +1 spins, or all -1 spins (both have same E). We find that there is then a phase transition that can occur, i.e. a TCritical where above M=0 and below M is finite.
In 1-D, however, there is no phase transition. The fully-correlated state with all spins up can be easily destroyed by just moving one spin down. Hence only at T=0 K, are all spins aligned.
In 2-D, there is finite phase transition, along with usual latent heat, etc. This has been solved exactly by Onsager, but only for h=0. The critical behavior also depends on type of lattice. On a square lattice with n.n. only, the spins align when (kBT)-1 > 0.4407/J, in zero field.
In 3-D there is no analytic solution, and it may be impossible to do so. Hence the importance of simulation.
Above TCritical, there is short-range order arising from the correlations that form, and indicated by the pair correlations. Below TCritical, there is long-range order that forms due to these correlations becoming infinite ranged, indicated by the appropriate order parameter, which is M for the Ising model.
So based on intuition from MFT, we at least can expect some interesting critical behavior associated with the numerical investigation of the Ising Model.

## Relation to Physical Systems

The Ising model appears to be a simple model of little relevance to most physical problems. The closest physical problem is a magnetic phase transformation for a simple ferromagnet. However, it is a good model also for:

- Liquid-Vapor transformation, where clustering of si= 1 represents condensation of the gas molecules due to their attractive intereaction. As gas molecules interact and no longer behave as non-interacting gas (i.e., PV=nRT), then there can be transition to liquid phase.
- Liquid Mixtures.  "Critical opalescence" arises from the short-range correlation of disordered (mixed) phase and there is scattering of light (sample is opaque) and below transition there is long-range correlation in the single phase mixture and sample is transparent because light does not scatter.
- An Alloy, if one considers up=A atoms and down=B atoms. In this case, we have a binary alloy and the magnetic field, h, is the chemical potential (for h=0, we have 50-50 alloy). Nonetheless, non-zero field (finite chemical potential difference) is important generally. The solution of this finite-field problem is not even known in 2-D. Hence, numerical simulations are required.
- Liquid Crystal and Polymers in some instances can also be modeled via lattices. For example, molecules that rotate (as with polarization of liquid crystals) but more-or-less form on a lattice are treated this way
