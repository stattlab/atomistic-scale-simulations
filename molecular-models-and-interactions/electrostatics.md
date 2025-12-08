# Long-Range Potentials

A potential is **long-ranged** if its decay is slower than $r^{-d}$, where $ d$ is dimensionality.

```{note}
The formal definition is given over the integral

$$
I(R) = \int_R^\infty dr\, r^{D-1}\,\frac{A}{r^n}
      = \begin{cases} \infty &\text{ for } n \le D\\
    \text{finite} &\text{ for } n > D
    \end{cases}
$$

where $D$ is the dimension. I.e we look at the potential $u(r)$ as $r \rightarrow \infty$. This integral then contains $\frac{r^{D-1}}{r^n}$. In 3D, a potential is short-ranged if it converges faster than $r^{-3}$. In 2D,  a potential is short-ranged if it converges faster than $r^{-2}$.
```

**Coulomb potential** for charges:

  $$
  u(r) = \frac{q_i q_j}{4\pi \varepsilon_0 r}
  $$

where $q_i,q_j$ are the charges, and  $\varepsilon_0$ is the permittivity of free space. Sometimes the factor of $4\pi$ is not written.

Other long range forces include dipoles, low Reynolds number hydrodynamics, etc.

Interaction can extend much further than the simulation box. **How to deal with this?**

- Use a bigger box (expensive!)
- Include more than one image of each particle in the calculation

## Electrostatics

Most common example for long-range potentials that need to be considered in particle based simulations.

## Ewald Sums

- Developed by Ewald (1921), Madelung (1918)

For the calculation of the electric potential $U$ of an ion at position $r_i$ due to all other ions of the lattice, we need to compute a sum like this:
$$
U = \frac{1}{2} \sum_{\vec m\in\mathbb Z^3}
    \sum_{i=1}^N \sum_{\substack{j=1\\ j\neq i}}^N
    \frac{q_i q_j}{4\pi\varepsilon_0 |\vec r_i - \vec r_j + \vec m L|}
$$
where $\vec{m}$ are the image vectors, and $L$ is the box size.

This sum is conditionally convergent!{cite}`widomShapeAdapted`

```{figure} ./_figures/mandelung-sum.png
:alt: Illustration of the summation of charges on a simple lattice.
:width: 200px
:align: center
:name: madelung-const-fig

Illustration of the summation of charges on a simple lattice (NaCl). The particle in the center, $0$, indicates $i$, and the others are labeled by a possible order of how they could be summed.

```

 {numref}`madelung-const-fig` shows a simple NaCl crystal. Here, the nearest neighbors contribute $-\frac{e^2}{4\pi\epsilon_0}\frac{6}{a}$, then the second nearest neighbors contribute $+\frac{e^2}{4\pi\epsilon_0}\frac{12}{a\sqrt{2}}$, the third $-\frac{e^2}{4\pi\epsilon_0}\frac{8}{a\sqrt{3}}$, and so on. This doesn't obviously converge without some math tricks and rearranging. This general challenge exist for any system with long range interactions, in various lattice types.

**Solution:** Add and subtract a Gaussian charge at each point charge source:

- Point charge:$ \rho(\vec{r}) = q_i\delta(\vec{r}-\vec{r}_i)$
- Gaussian:$ \rho(\vec{r})^G = \frac{q_i}{(2 \pi \sigma^2)^{3/2}} e^{-\lvert\vec{r}-\vec{r}_i\rvert^2/2\sigma^2}$. Note that $\rho(\vec{r})^G  \rightarrow \rho(\vec{r})$ as $\sigma \rightarrow 0$.

This scheme is illustrated in {numref}`ewald-split-fig`.

```{figure} ./_figures/ewald-split.png
:alt: Illustration of the summation of charges on a simple lattice.
:width: 200px
:align: center
:name: ewald-split-fig

Illustration of the summation of charges on a simple lattice (NaCl). The particle in the center, $0$, indicates $i$, and the others are labeled by a possible order of how they could be summed.

```

**How Does This Help?**

- The Gaussian charge screens the point charge, making the sum converge faster.
- The cancelling Gaussian charge can also be summed.
- The problem is therefore split into two solvable parts.

For doing this, we do need the **electric potential of a Gaussian charge**.
We use Poisson's equation

$$
\begin{aligned}
\nabla^2 \phi^G(r)
 & = - \frac{\rho^G(r)}{\varepsilon_0} \\
 & = - \frac{q_i}{\varepsilon_0 (2\pi\sigma^2)^{3/2}} e^{-r^2/2\sigma^2} \\[4pt]
\frac{1}{r}\,\frac{d^2}{dr^2}\!\bigl(r\,\phi^G(r)\bigr)
 & = - \frac{q_i}{\varepsilon_0 (2\pi\sigma^2)^{3/2}} e^{-r^2/2\sigma^2} \\[4pt]
\int_{\infty}^{r} \!dr'\, \frac{d^2}{dr'^2}\!\bigl(r'\,\phi^G(r')\bigr)
 & = - \frac{q_i}{\varepsilon_0 (2\pi\sigma^2)^{3/2}} \int_{\infty}^{r} \!dr'\, e^{-r'^2/2\sigma^2} \\[4pt]
\frac{d}{dr}\!\bigl(r\,\phi^G(r)\bigr)
 & = \frac{q_i\,\sigma^2}{\varepsilon_0 (2\pi\sigma^2)^{3/2}} e^{-r^2/2\sigma^2} \\[4pt]
\int_{0}^{r} d\!\bigl(r'\,\phi^G(r')\bigr)
 & = \frac{q_i\,\sigma^2}{\varepsilon_0 (2\pi\sigma^2)^{3/2}} \int_{0}^{r} dr'\, e^{-r'^2/2\sigma^2} \\[4pt]
 & \dots \\
\phi^G(r)
 & = \frac{q_i}{4\pi\varepsilon_0 r}\, \mathrm{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)\,.
\end{aligned}
$$

For a simple point charge, we get

$$
\phi(r) = \frac{q_i}{4\pi\epsilon_0 r} \quad .
$$

Using this, we can split the sum, called **Ewald summation**, which we will derive below.

$$
\begin{aligned}
\phi(\vec{r}) &= \frac{1}{4 \pi \varepsilon_0}
  \sum_{\vec{m}} \sum_{j=1}^N \frac{q_j}{\lvert \vec{r}_j - \vec{r} + \vec{m}L\rvert} \\
\rightarrow\; u &= \frac{1}{2} \sum_{i=1}^N
  q_i\!\left[\phi(\vec{r}_i) - \underbrace{\phi_i(\vec{r}_i)}_{\substack{\text{exclude self interactions}\\ \text{where } \vec{m}=0}}\right]
\end{aligned}
$$

```{note}
We exclude self-interactions, but they can be kept in principle. In the final equation in the summary below, we list them explicitly, but commonly they are excluded or set to zero.
```

Now we split the sum:

$$
\begin{aligned}
\phi_i(r) &= \underbrace{\phi_i(r)-\phi^G_i(r)}_{\text{short}} + \underbrace{\phi^G_i(r)}_{\text{long}}\\
&= \frac{q_i}{4 \pi \varepsilon_0 r}-\frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)+\frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)\\
&= \frac{q_i}{4 \pi \varepsilon_0 r}\!\left[1-\operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)\right]+\frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)\\
&= \frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erfc}\!\left(\frac{r}{\sqrt{2}\sigma}\right)+\frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)\\
&= \frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erfc}\!\left(\kappa r\right)+\frac{q_i}{4 \pi \varepsilon_0 r} \operatorname{erf}\!\left(\kappa r\right)
\end{aligned}
$$


Where we have defined an inverse screening length $\kappa = \frac{1}{\sqrt{2}\sigma}$ in the last step.

Now we define a short ranged $\phi_i^S(r)$ and a long ranged $\phi_i^L(r)$,

$$
\begin{aligned}
\phi_i^S(r) &= \frac{q_i}{4 \pi \varepsilon_0 r}\,\operatorname{erfc}\!\left(\frac{r}{\sqrt{2}\sigma}\right) \\
\phi_i^L(r) &= \frac{q_i}{4 \pi \varepsilon_0 r}\,\operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma}\right)
\end{aligned}
$$

so that we get

$$
\begin{aligned}
\phi(r) &= \sum_{\vec{m}} \sum_{j=1}^N \phi_j\!\left(\lvert\vec{r}_i-\vec{r}+\vec{m}L\rvert\right) \\
&= \sum_{\vec{m}} \sum_{j=1}^N \phi_j^S + \phi_j^L\\
&= \sum_{\vec{m}} \sum_{j=1}^N \phi_j^S + \sum_{\vec{m}} \sum_{j=1}^N \phi_j^L\\
&= \phi^S + \phi^L \quad ,
\end{aligned}
$$

and

$$
\begin{aligned}
u &= \frac{1}{2} \sum_{i=1}^N q_i\!\left[\phi^S(r_i)-\phi_i^S(r_i)\right]
   + \frac{1}{2} \sum_{i=1}^N q_i\!\left[\phi^L(r_i)-\phi_i^L(r_i)\right] \\
&= \frac{1}{2} \sum_{\vec{m}} \sum_{i=1}^N \sum_{\substack{j=1\\ j\neq i}}^N
   u^S\!\left(\lvert r_j-r_i+\vec{m}L\rvert\right)
   + \frac{1}{2} \sum_{i=1}^N q_i \phi^L(r_i)
   - \frac{1}{2} \sum_{i=1}^N q_i \phi_i^L(r_i)
\end{aligned}
$$


For the last sum, we can now look at the limit:

$$
\lim_{r \rightarrow 0} \frac{q_i}{4 \pi \varepsilon_0 r}
  \operatorname{erf}\!\left(\frac{r}{\sqrt{2} \sigma}\right)
= \frac{q_i}{4 \pi \varepsilon_0}\,\frac{1}{\sigma}\,\sqrt{\frac{2}{\pi}}
$$

This results in

$$
u =\underbrace{\frac{1}{2} \sum_{\vec{m}} \sum_{i=1}^N \sum_{j=1, i\neq j}^N u^S\left(\lvert r_j-r_i+\vec{m}L\rvert \right)}_{u^S(r)=\frac{q_i q_j}{4\pi\varepsilon_0r}\operatorname{erfc}\left(\frac{r}{\sqrt{2}\sigma}\right)}+
\frac{1}{2} \sum_{i=1}^N q_i \phi^L\left(r_i\right)
-\frac{1}{4 \pi \varepsilon_0} \frac{1}{\sqrt{2}\sigma} \frac{1}{\sqrt{\pi}}  \sum_{i=1}^N q_i^2
$$

The first term, turns into a normal pairwise sum, if $\operatorname{erfc}$  decays quickly. The middle term still needs to be evaluated.

Long-ranged part is convieniently summed in Fourier space.{cite}`stern2008mesh`
**Fourier transform**:

$$
\begin{aligned}
\hat f(\vec{k}) &= \int_V d\vec{r}\, f(\vec{r})\, e^{-i\vec{k}\cdot\vec{r}} \quad \text{for finite volumes} \\
\hat f(\vec{r}) &= \frac{1}{L^3} \sum_{\vec{k}} \hat f(\vec{k})\, e^{i\vec{k}\cdot\vec{r}} \quad \text{with } \vec{k}=\frac{2\pi \vec{n}}{L}\, .
\end{aligned}
$$


We need to Fourier transform Poisson's equation for Gaussian charge (periodic array).

$$
\nabla^2 \phi^G=-\frac{\rho^G}{\varepsilon_0} \rightarrow -k^2 \hat{\phi}^G=-\frac{\hat{\rho}^G}{\varepsilon_0} \rightarrow \hat{\phi}^G=\frac{1}{k^2 \varepsilon_0} \hat{\rho}^G
$$

Now we can compute the Fourier transform of the Gaussian charge distribution.
First, we recognize that summing over all lattice vectors $\vec{m}$ effectively extends the domain of integration from the finite volume $V$ to the entire space $\mathbb{R}^3$. This allows us to remove the sum and integrate over infinity:

$$
\begin{aligned}
\hat{\rho}^G(\vec{k})
 & = \int_V d\vec{r}\, \sum_{\vec{m}} \frac{q_i}{(2 \pi \sigma^2)^{3/2}}
 e^{-\lvert \vec{r}-\vec{r}_i+\vec{m}L\rvert^2 / 2 \sigma^2}
 e^{-i \vec{k} \cdot \vec{r}} \\
 & = \int_{\mathbb{R}^3} d\vec{r}\, \frac{q_i}{(2 \pi \sigma^2)^{3/2}}
 e^{-\lvert\vec{r}-\vec{r}_i\rvert^2 / 2 \sigma^2}
 e^{-i \vec{k} \cdot \vec{r}}
\end{aligned}
$$

Next, we perform a change of variables by substituting $\vec{r}' = \vec{r} - \vec{r}_i$. This shifts the origin to the particle position $\vec{r}_i$, pulling a phase factor $e^{-i \vec{k} \cdot \vec{r}_i}$ out of the integral:

$$
\begin{aligned}
\hat{\rho}^G(\vec{k})
 & = \int_{\mathbb{R}^3} d\vec{r}'\, \frac{q_i}{(2 \pi \sigma^2)^{3/2}}
 e^{-r'^2 / 2 \sigma^2} e^{-i \vec{k} \cdot(\vec{r}'+\vec{r}_i)} \\
 & = e^{-i \vec{k} \cdot \vec{r}_i}
 \int_{\mathbb{R}^3} d\vec{r}'\, \frac{q_i}{(2 \pi \sigma^2)^{3/2}}
 e^{-r'^2 / 2\sigma^2} e^{-i \vec{k} \cdot \vec{r}'}
\end{aligned}
$$

To solve the remaining integral, we switch to spherical coordinates $(r', \theta, \phi)$. We align the $z$-axis with the wavevector $\vec{k}$ so that $\vec{k} \cdot \vec{r}' = k r' \cos\theta$:

$$
\begin{aligned}
\hat{\rho}^G(\vec{k})
 & = e^{-i \vec{k} \cdot \vec{r}_i}
 \int_0^{\infty} dr'\, r'^2
 \int_0^{2\pi} d\phi \int_{-1}^{1} d(\cos\theta)\,
 \frac{q_i}{(2 \pi \sigma^2)^{3/2}}
 e^{-r'^2 / 2\sigma^2} e^{-i k r' \cos\theta} \\
 & = e^{-i \vec{k} \cdot \vec{r}_i} \frac{q_i}{(2 \pi \sigma^2)^{3/2}} \int_0^{\infty} dr'\, r'^2 e^{-r'^2 / 2\sigma^2} \underbrace{\left[ \int_0^{2\pi} d\phi \int_{-1}^{1} d(\cos\theta)\, e^{-i k r' \cos\theta} \right]}_{\text{Angular integration}}
\end{aligned}
$$

The angular integral yields $4\pi \frac{\sin(kr')}{kr'}$. Substituting this back and solving the radial Gaussian integral gives the final result:

$$
\begin{aligned}
\hat{\rho}^G(\vec{k})
 & = e^{-i \vec{k} \cdot \vec{r}_i} \frac{q_i}{(2 \pi \sigma^2)^{3/2}} \frac{4\pi}{k} \int_0^{\infty} dr'\, r' e^{-r'^2 / 2\sigma^2} \sin(k r') \\
 & = \mathbf{q_i e^{-\sigma^2 k^2/2} e^{-i\vec{k}\cdot\vec{r}_i}}
\end{aligned}
$$

Hence, $\hat{\phi}_i^G(k)=\frac{q_i}{\varepsilon_0 k^2} e^{-k^2 \sigma^2 / 2} e^{-i \vec{k} \cdot \vec{r}_i}$.

Last, invert

$$
\phi^L(\vec{r}) = \frac{1}{L^3} \sum_{\vec{k}\neq 0} \sum_{j=1}^N \frac{q_j}{\varepsilon_0 k^2} e^{-k^2 \sigma^2 / 2} e^{-i \vec{k} \cdot (\vec{r}_j - \vec{r})}
$$

and

$$
U^L = \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N
       \sum_{\vec{k} \neq 0}
       \frac{q_i q_j}{\varepsilon_0 k^2 L^3}
       e^{-k^2 \sigma^2 / 2} e^{-i \vec{k} \cdot \vec{r}_{ij}}
$$

### Boundary Effects

The lattice needs to be truncated somewhere, so it is effectively embedded in some medium.
At this boundary, there is a depolarizing field counteracting the fluctuatin dipole moment of the main cell.

$$
U^{BC} = \frac{1}{2(2\varepsilon_r+1)\,\varepsilon_0 L^3}
  \left\lvert\sum_{i=1}^N q_i \vec{r}_i\right\rvert^2
$$

For so called "tin foil" BCs used in most simulations, set $\varepsilon_r=\infty$.

### Summary

In summary,

$$
u = \underbrace{
      \frac{1}{2}
      \sum_{\vec{m}} \sum_{i\neq j}
      \frac{q_i q_j}{4\pi \varepsilon_0 \,\lvert \vec{r}_{ij} + \vec{m}L\rvert}
      \operatorname{erfc}\!\bigl(\kappa \lvert \vec{r}_{ij} + \vec{m}L\rvert\bigr)
    }_{\text{short}} \\
\qquad
  + \underbrace{
      \frac{1}{2} \sum_{\vec{k} \neq 0} \sum_{i=1}^N \sum_{j=1}^N \frac{q_i q_j}{\varepsilon_0 k^2 L^3} e^{-k^2 / 4 \kappa^2} e^{-i \vec{k} \cdot \vec{r}_{ij}}
    }_{\text{long}} \\
\qquad
  \underbrace{
    - \frac{\kappa}{4\pi^{3/2} \varepsilon_0}
      \sum_{i=1}^{N} q_i^{2}
  }_{\text{self}}
  \;+\;
  \underbrace{
    \frac{1}{2(2\varepsilon_r + 1)\,\varepsilon_0 L^{3}}
    \left\lvert \sum_{i=1}^{N} q_i \vec{r}_i \right\rvert^{2}
  }_{\text{BC}}
$$

- Real space: efficient for short-range potentials
- Reciprocal space: efficient way to treat smooth periodic functions
- Ewald: efficient way to sum a divergent and long-range interaction by summing part in real space and part in reciprocal space{cite}`toukmaji199`

Choose $k=\frac{1}{\sqrt{2}\sigma}$, the inverse screening length, and the number of wavevectors to be accurate and efficient. 

- Self-interactions are commonly excluded.

## Alternative Methods

- Direct summation, Laplace, 1820, $\mathcal{O}(N^2)$
- Ewald summation, Ewald, 1921  (with adjusted E and neighbor tables)  $\mathcal{O}(N^{3/2})$
- Multigrid summation, Brandt, 1977, $\mathcal{O}(N)$
- Barnes-Hut Treecode, Barnes, Hut, 1986, $\mathcal{O}(N \log N)$
- Fast Multipole Method, Greengard, Rokhlin, 1987, $\mathcal{O}(N)$
- **Particle-Particle Particle-Mesh**, Hockney, Eastwood, 1988,$\mathcal{O}(N \log N)$
- **Particle Mesh Ewald**, Darden, 1993,
$\mathcal{O}(N \log N)$

## References

- ["On mesh-based Ewald methods: Optimal parameters for two differentiation schemes"
Harry A. Stern; Keith G. Calkins
J. Chem. Phys. 128, 214106 (2008)](https://doi.org/10.1063/1.2932253){cite}`stern2008mesh`

- [Shape-Adapted Ewald Summation,
M. Widom](https://euler.phys.cmu.edu/widom/pubs/drafts/Dipole/dip.pdf){cite}`widomShapeAdapted`

- [Ewald summation techniques in perspective: a survey, Toukmaji, A. Y. and Board, J. A.](https://doi.org/10.1016/0010-4655(96)00016-1){cite}`toukmaji199`