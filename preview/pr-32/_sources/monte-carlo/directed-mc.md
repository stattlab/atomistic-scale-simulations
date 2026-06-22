# Directed Monte Carlo

Last chapter, we discussed the concept of a random walk. This chapter we will discuss some methods for continuum systems that can move through phase space faster. These are discussed in Allen and Tildesley.

## Preferential Monte Carlo

The idea here is that in an inhomogenous or multi-component system we preferentially sample variables which are more interesting or which control the dynamics.

As an example, suppose we wish to sample several layers of molecules absorbed on a surface. Usually the first layer is rather firmly stuck to the surface. That first layer is important because it covers the surface but it doesn't move around very much. The dynamics of the upper layers are much more interesting. Let the direction away from the surface be the $z$ direction. Then we can sample a particle with label $i$ with probability proportional to $h\left(z_{i}\right) / H$ where $h(z)$ is some adjustable sampling probability and $H=\sum_{j} h\left(z_{j}\right)$. For an attempted move from $z$ to $z^{\prime}$, the acceptance ratio ratio will contain the factors $\left[h\left(z_{i}\right)\left(H+h\left(z^{\prime}\right)-h\left(z_{i}\right)\right)\right] /\left[h\left(z^{\prime}\right) H\right]$ in addition to the change in potential energy factor. The acceptance ratio is not necessarily better, but you can fine tune which particles you think are important to move and not waste time sampling particles which never move or are not interesting. You must regularly sample all the particles, but you can choose the relative time the computer spends on various parts of the system.

Two component example; say we have particles of type $1,2, \ldots$, for example, big, slowly moving particles and small, quickly moving particles. We can choose which of them to move according to a probability $\gamma_{i}$ with $\gamma_{1}+\gamma_{2} \ldots=1$. In this case, one does not have to modify the acceptance probability since the $\gamma$ 's cancel out of the ratio.

## Force-Bias Monte Carlo

Suppose we want to sample the Boltzmann distribution of particles $\exp [-\beta V(R)]$. Using the "classic" Metropolis procedure, we choose a neighborhood for a particle centered around the old position and move uniformly in a cube centered on the old position with side $\Delta$. Keeping the same neighborhood, let us try to approximate the heat-bath transition. To do so expand the potential to first order,

$$
\pi\left(\mathbf{r}^{\prime}\right) \propto \exp \left[-\beta V\left(\mathbf{r}^{\prime}\right)\right] \approx \exp \left[-\beta V(\mathbf{r})+\beta \mathbf{F}(r) \cdot\left(\mathbf{r}^{\prime}-\mathbf{r}\right) \ldots\right]
$$

where $\mathbf{F}(\mathbf{r})$ is the force evaluated at the old position. Let us sample a transition probability from:

$$
T\left(r \rightarrow \mathbf{r}^{\prime}\right)=C(\mathbf{r}) \exp \left[\alpha \mathbf{F}(\mathbf{r})\left(\mathbf{r}^{\prime}-\mathbf{r}\right)\right],
$$

where $C(\mathbf{r})$ is the normalization constant:

$$
C(\mathbf{r})=\alpha \mathbf{F} /(2 \sinh (b))
$$

$b=\alpha \mathbf{F} \Delta / 2$, and $\alpha$ is some adjustable constant.

To sample this probability distribution we can use the mapping idea that we discussed a few weeks ago. Let $\mathbf{u}$ be a uniformly distributed random 3 -vector in the unit cube ( 0,1 ). Then the new displacement in the force-bias method is :

$$
\mathbf{r}^{\prime}=\mathbf{r}+1 /(\alpha \mathbf{F}) \ln [\mathbf{u} \alpha \mathbf{F} / c+\exp (-b)]
$$

and the trial move is accepted according to:

$$
\left.\min \left[1, \exp \left[-\beta\left(V\left(\mathbf{r}^{\prime}\right)-V(\mathbf{r})\right)+\alpha\left(\mathbf{F}\left(\mathbf{r}^{\prime}\right)+\mathbf{F}(\mathbf{r})\right) \cdot\left(\mathbf{r}-\mathbf{r}^{\prime}\right)\right)\right]\left(C_{x}^{\prime} C_{y}^{\prime} C_{z}^{\prime}\right) /\left(C_{x} C_{y} C_{z}\right)\right]
$$

We need both the force and the potential at the old and new point.
So far we have let $\alpha$ be arbitrary. If we choose $\alpha=0$ we get the classical Metropolis method. Suppose the force is slowly varying inside the moving cube. Then we can make the acceptance ratio unity by setting $\alpha=\beta / 2$. This is an improvement if the additional expense in computing the force pays off in much larger average steps.

## Smart Monte Carlo

I introduced ideas of the Smoluchowksi equation in class. You can also look at pages 257-269 in Allen and Tildesley. I am discussing this method in somewhat more detail because we will use it for Brownian dynamics, Smart Monte Carlo, and (later) quantum Monte Carlo. The Smoluchowski equation is the unique "master" equation which is:

1. local
2. goes to the Boltzmann distribution
3. is Markovian:

$$
-d \pi(R, t) / d t=-\nabla D[R](\nabla \pi-\beta \mathbf{F}(R) \pi)
$$

where $D(R)$ is in general a many-body tensor but is usually taken to be a constant diagonal tensor. $\mathbf{F}$ is the force.

The asymptotic solution of $\pi(R, t)$ will be $\pi(R) \propto \exp (-\beta V(R))$. It is easy to see that this distribution satisfies $d \pi / d t=0$. If we assume ergodicity since the process is Markovian, this must be the only solution.

Let us define the Green's function as the solution $G\left(R, R_{0} ; t\right)$ to the above equation. with the boundary condition at zero time: $G\left(R, R_{0} ; 0\right)=\delta\left(R-R_{0}\right)$. One can prove that the Green's function satisfies detailed balance:

$$
\pi(R) G\left(R \rightarrow R^{\prime} ; t\right)=\pi\left(R^{\prime}\right) G\left(R^{\prime} \rightarrow R ; t\right)
$$

for any value of $t$. To do that one writes the evolution equation for the symmetrized Green's function: $\left(\pi(R) / \pi\left(R^{\prime}\right)\right)^{1 / 2} G\left(R \rightarrow R^{\prime} ; t\right)$, and sees the right hand side of the master equation is an Hermitian operator which implies that the symmetrized Green's function is symmetric in $R$ and $R^{\prime}$. Then $G$ can be used for a transition probability and it will always give an acceptance probability of unity. Also, it gives interesting dynamics (not MD but dynamics of viscous particles always in contact with a very light heat bath).

However, we can only calculate $G$ in the short-time limit. To do this let us calculate the first three moments of $G$,

$$
I_{n}\left(R_{0}, t\right)=\int d R\left(R-R_{0}\right)^{n} G\left(R_{0} \rightarrow R ; t\right)
$$

Take the time derivative of this equation, use the master equation on the r.h.s., and Green's theorem to get a simple integral over $G$ on the r.h.s (we interpret this as an average $<\ldots>$ ). We assume there are no absorbing surfaces of the random walks. Then,

$$
d I_{0} / d t=0
$$

This implies the normalization of $G$ is always one so the evolution describes a process which neither creates nor destroys walks. The next moment is:

$$
d I_{1} / d t=<\beta D \mathbf{F}+\nabla D>
$$

Let us assume that $\mathbf{F}$ and $\nabla D$ are slowly varying. Then we can replace them by the values at the initial points and integrate:

$$
<R_{t}>=R_{0}+t\left[\beta \mathbf{F}\left(R_{0}\right)+\nabla D\left(R_{0}\right)\right]+\mathcal{O}\left[t^{2}\right] .
$$

The equation for the second moment (in general a second rank tensor) is:

$$
d I_{2} / d t=2<D>+2<\left(R-R_{0}\right)(\beta \mathbf{F}+\nabla D)>
$$

Integrating,

$$
<\left(R-R_{0}\right)^{2}>=2 D\left(R_{0}\right) t+\mathcal{O}\left[t^{2}\right] .
$$

The solution at small time is a Gaussian distribution with the above mean and covariance.

$$
G_{g}\left(R, R_{0} ; t\right)=\exp \left[-\left(R-R_{t}\right)\left(2 D\left(R_{0}\right) t\right)^{-1}\left(R-R_{t}\right)\right]\left[2 \pi t \operatorname{det}\left(D\left(R_{0}\right)\right)\right]^{-1 / 2}
$$

According to the central limit theorem, Eqs. 11-13 are all that is needed to simulate the random walk if the time step $t$ is sufficiently small.

We have not yet discussed the diffusion tensor. For simplicity, one normally assumes that $D(R)=$ $D_{0} \mathcal{I}$ is a constant, unit tensor. Physically more complicated tensors are related to "hydrodynamic" interactions and will lead to different dynamics but the same static properties.

Then the acceptance probability for the simple case of a constant diffusion is given by:

$$
A=\min \left[1, \exp \left(-\beta\left(V\left(\mathbf{r}^{\prime}\right)-V(\mathbf{r})\right)-\beta\left(F(\mathbf{r})+F\left(\mathbf{r}^{\prime}\right)\right)\left(2\left(\mathbf{r}^{\prime}-\mathbf{r}\right)-\beta D\left(F^{\prime}-F\right)\right) / 4\right)\right] .
$$

As with force-bias Monte Carlo, the acceptance ratio goes to unity at small t. It differs because the sampled points are not bounded. Also, as mentioned above, the dynamics are interesting in themselves. Finally one can possibly make more accurate schemes by including off-diagonal components in the second moment. We can choose for a transition probability the most general correlated Gaussian in $3 n$ variables,

$$
T_{S}(R)=\sqrt{(2 \pi)^{3 m} \operatorname{det}(\mathbf{A})} e^{-(R-\bar{R})(2 \mathbf{A})^{-1}(R-\bar{R})}
$$

where the $3 \times 3$ positive-definite covariance matrix A and the mean position vector $\bar{R}$ can be arbitrary. Suppose we solve equation (12) to one higher order:

$$
\mathbf{A}=2 \mathcal{I} t-t^{2} \nabla \nabla V\left(R_{0}\right) .
$$

We can sample the multivariate Gaussian distribution. One Cholesky-factorizes the covariance matrix as $\mathbf{A}=\mathbf{S S}^{T}$, where $\mathbf{S}$ is an upper triangular matrix. Then if $\chi$ is a vector of Gaussian random numbers with zero mean and unit variance, $\mathrm{S} \chi+\bar{R}$ has the desired mean and variance. The diagonal divisors in the Cholesky decomposition of $\mathbf{A}$ are needed to find the actual value of $T\left(R \rightarrow R^{\prime}\right)$ and the acceptance probability for a move. The effect of interactions is to push the mean position of an atom away from its current position if other particles are nearby. Similarly, the covariance is changed by interactions with neighboring particles. In directions where the curvature of the potential is positive, the cage of surrounding atoms results in a narrower Gaussian's being sampled.
