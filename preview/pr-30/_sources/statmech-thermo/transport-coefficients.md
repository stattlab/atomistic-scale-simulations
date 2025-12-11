# Transport Coefficients

## Correlation Functions for Dynamical Response

This section continues the discussion of the calculation of properties, in particular the calculation of dynamical properties and the response to perturbation. For static properties it would probably be more convenient to use Monte Carlo methods since they are more robust. Dynamics is the reason that we do MD.

### Linear-Response Functions

The simplest dynamical properties are the linear response to an external perturbation. Most macroscopic measurements are in the linear regime because macroscopic perturbations are very small on the scale of microscopic forces.

Onsager's made a well known conjecture (1935), called the Regression Hypothesis. (also known as the fluctuation-dissipation theorem.) It states that the linear response of the system to a time-varying perturbation is the same as fluctuations that naturally occur in statistical equilibrium. So there are 2 basic ways to calculate response: either wait for the system to fluctuate by itself or apply a perturbation and see what happens. (the first is often referred to as the Kubo method.)

### Static perturbation

First let us consider static perturbations. Suppose our total Hamiltonian has the form:

$$
H = H_0 + c A
$$

where $H_0$ is the unperturbed Hamiltonian, $A$ is a perturbation and $c$ is the coupling constant. As shown on the formula page, one can write the free energy as a power series in $c$. The linear response is simply the expectation of A in the unperturbed system. The second order term is the fluctuation about the mean. In fact if we neglect all terms above the first order we always get an upper bound to the free energy. Finally to calculate the free energy difference between the system at $c=0$ and $c=1$ we just need to integrate the average $A$ over ensembles for various values of $c$ between 0 and 1.

We can also find the response of some property $B$ to the perturbation; it equals the correlation between $A$ and $B$.

In class I did the application of cutting off the potential. Generally one expects that if the neglected potential is smooth it is pretty much independent of the phase space point $R$, and hence terms higher order than first can be neglected.

A second example is to apply a sinusoidal potential and look at the response of the density. It is simply $S_k$, the structure factor. That is essentially how neutrons and X-rays measure the structure factor.

### Diffusion Constant

Now consider the simplest dynamical experiment, mix two types of atoms and see how quickly diffusion makes the system a homogeneous mixture. The diffusion constant $D$, together with the diffusion equation, governs this process on a macroscopic scale. The Green's function for the diffusion equation is a spreading Gaussian with the mean squared displacement equal to $6 D t$. A little thought shows that a way to microscopically calculate $D$ is to study the diffusion of a single atom. Again the equation is on the formula page. One can easily transform this expression to the integral of the velocity autocorrelation function.

The transformation assumes that one is using the _unwound or unwrapped coordinates_; the positions of the atoms such that:

$$
r(t+h) = r(t) + h v(t) + ...
$$

Don't use periodic boundary conditions to put particles back in the central cell.

One of the key discoveries in the early days of computer simulation was the long-time tails on the $v-v$ function by Alder and Wainwright. The $v-v$ correlation functions decay algebraically in time (as $t^{-d/2}$ where $d$ is the spatial dimension). This implies that diffusion may not really exist in 2D. This is not Markovian (random) behavior which would decay exponentially in time. The momentum of a fast moving particle gets stored in the nearby liquid as a vortex and helps to keep it moving in the same direction for a very long time.{cite}`alder_decay_1970`

### Response to a time varying perturbation

If we measure the response to $A$ of a perturbation $B$ it is the correlation between $A$ and the time derivative of $B$ (or vice versa) which enters. The coefficent ($\chi$) or the susceptibility is the linear response, or transport coefficient. Some examples are the electrical and thermal conductivity, the bulk and shear viscosity, the mass diffusion coefficient and the dynamical structure factor. In linear response the perturbation and the response are at the same frequency and wavelength. Macroscopically one is often interested in only the zero-frequency, zero-wavelength limit of the response. A peak at finite frequency shows the presence of a collective mode, for example a sound wave. The derivation of the fluctuation dissipation theorem is in many textbooks. The general result for a perturbation is:

$$
\chi(\omega)=\beta \int_0^{\infty} d t e^{i t \omega}\left\langle B(t) \frac{d A(0)}{d t}\right\rangle
$$

The dynamic structure factor is a key quantity (also known as the density-density response function). If you push the system at time and place ($r$,$t$) how does it respond at ($r'$,$t'$)? This is what neutron scattering does. It is not hard to see that sound waves of various kinds will show up as prominent features of $S_k(\omega)$. The book *The Theory of Simple Liquids* by Hansen and MacDonald contains a thorough treatment of the theoretical properties of this function.{cite}`hansen_theory_2013`

### Some Details on Time Correlation Functions

The time correlation function is given by:

$$
C_{AB}(\tau)=\langle A(t)B(t+\tau) \rangle
$$

As this is an equilibrium property and it depends only on the time delay $\tau$, this must be independent of time origin, $t$. This means that the function $C(\tau)$ is stationary with respect to time origin, or $\frac{d}{dt}C(\tau) = 0$ . This time-origin invariance can be seen as:

$$
C(\tau)= \langle A(t) B(t + \tau)\rangle = \langle A(t + s) B(t + s + \tau)\rangle
$$

Let $s = -\tau$, then:

$$
C(\tau)= \langle A(t - \tau) B(t)\rangle
$$

In other words, either shifting $B$ forward by $\tau$, or $A$ backwards by $\tau$, gives the same average.

For $\tau=0$, $C(0) = \langle A(t)B(t)\rangle$, and this is the time-averaged pair-correlation that we normally calculated for thermodynamic quantities, etc. Here it is important to note that for **non-periodic** or **chaotic** functions, $\lim _{t \rightarrow \infty} C(0)=\langle A\rangle \langle B\rangle $, whereas for periodic functions (which are not ergodic) this is not true. Typically, we choose to normalized the time correlation functions by $C(0)$, i.e. $c(\tau)= C(\tau)/C(0)$, so that $c(\tau)$ ranges from 1 to its uncorrelated value $\langle A\rangle \langle B\rangle /\langle A(0)B(0)\rangle$. Clearly, in cases where either $\langle A\rangle$ or $\langle B\rangle$ are zero, such as for a non-flowing (or a stationary center-of-mass) system of particles where $A=v=velocity$ and $\langle v\rangle=0$, $c(\tau)$ varies from 1 at time zero to 0 at long times. It can be negative in between.

One of the most important correlations is the **auto-correlation** function, which is defined as $\langle A(t) A(t + \tau)\rangle$, the time correlation of a function with itself. By considering $\langle (A(t + \tau) - A(t))^2\rangle$ which is always positive definite, we may expand and find that it equals $2\langle A^2(t)\rangle - 2\langle A(t)A(t + \tau)\rangle$. Hence, the normalized auto-correlation function is bounded, i.e. $|c(\tau)| \le 1$. For dynamics, one example is the **velocity-velocity autocorrelation function** $C_{vv}(\tau)=\langle \mathbf{v_i}(\tau) \cdot \mathbf{v_i}(0)\rangle$, which is related to the diffusion coefficient. So $C_{vv}(\tau)$ is 1 at $\tau=0$ (from normalization) and $\langle v_i\rangle^2$ at long times (the average velocity squared of the system). **Importantly, for indistinguishable particles, statistical precision is improved greatly if one considers the average over all particles in the simulation** , i.e.

$$
\frac{1}{N} \sum_i \mathbf{v_i}(\tau) \cdot \mathbf{v_i}(0)
$$

## 1. Time Correlation Functions

Let $X (t)$ be a fluctuating variable sampled at time $t$. When are two samples "independent"?

- Autocorrelation function:

$$
C(t) = \langle X(0) X(t) \rangle
$$

- Normalized: $C(0) = \langle X^2 \rangle$ and $ C(t) \to 0 $ as $ t \to \infty$

An "independent" sample can be taken after a time $ \tau $ has passed, where $ C(\tau) $ is sufficiently small.

To improve averaging, use multiple **independent time origins**:

$$
\langle X(t_0) X(t_0 + t) \rangle
$$

### Example 
A random variable $ X $ is chosen every time step from a uniform distribution over $[-1, 1]$.

- $ \langle X^2 \rangle = \int_{-1}^1 x^2 \cdot \frac{1}{2} dx = \frac{1}{3} $
- For two independent samples: $ \langle X(t_0) X(t_0 + 1) \rangle = 0 $
- $ \langle X(t_0) X(t_0 + 2) \rangle = 0 $

## 2. Ways to Compute Autocorrelation

### Methods

- **FFT (Fast Fourier Transform)**: Efficient for computing $ C(t) $ over long times but beyond the scope of this course.
- **Brute Force**: Common for short-time correlations.

### Brute Force Steps

1. Choose $ X_i $ in data series as $ t_0 $
2. For $ j = i  \to  i + \text{window} $:
   - Accumulate $ C_{j-i}$ += $X_i *X_j $
3. Advance to next origin $ i $ and repeat
4. Normalize: $ C_k = \frac{C_k}{N - k} $

## 3. Green-Kubo and Einstein Relations


The **Green-Kubo expression** links a transport coefficient $X$ to a related dynamic observable $A(t)$. 

$$
X = \int_0^\infty dt \, \langle A(0) A(t) \rangle
$$

It is derived by using **linear response theory** to link the response of the system to small perturbations.

Associated with the Green-Kubo expression is a generic **Einstein relation**:

$$
X = \lim_{t \to \infty} \frac{1}{2t} \langle [A(t) - A(0)]^2 \rangle
$$

This can be derived from the Green-Kubo expression with integration by parts. Note that this is a **fluctuation-dissipation relation**. The Einstein relation can be used to calculate transport coefficients from dynamic observables in a simulation.
More details about the Green-Kubo expression and Einstein relation can be found in chapter 2 of Allen and Tildesley.{cite}`allen1987computer`

## 4. Diffusion

### Diffusion Coefficient $ D $

One of the most common transport coefficients calculated from simulations is the diffusion coefficient $D$. It can be calculated from the dynamic observable displacement by following the Einstein relation above. The explicit formula is:

$$
D = \lim_{t \to \infty} \frac{1}{2d} \frac{d}{dt} \langle [x(t) - x(0)]^2 \rangle
$$

If the system is isotropic:

$$
D = \frac{1}{3} (D_{xx} + D_{yy} + D_{zz})
$$

Or:

$$
D = \lim_{t \to \infty} \frac{1}{2d}\frac{1}{t} \langle \Delta x(t)^2 \rangle
$$

### Random Walk in 1D

A random walk is a simple demonstration used to demonstrate the diffusion coefficient. The simplest case is a 1D random walk in which a particle can hop a distance $l$ left or right each with a specific probability.

As an example, take a system in which a particle hops left or right with $ p = \frac{1}{2} $ (equal in each direction). It is straightforward to see that after $n$ hops and a sufficiently large $t$, the mean displacement $ \langle \Delta x \rangle$ will be 0 because of the equal probability for each direction. Furthermore the mean squared displacement (MSD), $ \langle \Delta x^2 \rangle$ will be $n l^2$ (a binomial distribution) since the $l$ gets squared each hop. For a discrete timestep for a hop $\Delta t$, $t=n\Delta t$.

Plugging all of this into the isotropic Einstein relation above with $d=1$ (1 dimension) we can calculate the diffusion coefficient of this particle:

$$
D = \frac{l^2}{2 \Delta t}
$$
