# Transport Coefficients

## 1. Time Correlation Functions

Let \( X(t) \) be a fluctuating variable sampled at time \( t \). When are two samples "independent"?

- Autocorrelation function:

$$
C(t) = \langle X(0) X(t) \rangle
$$

- Normalized: \( C(0) = \langle X^2 \rangle \), and \( C(t) \to 0 \) as \( t \to \infty \)

An "independent" sample can be taken after a time \( \tau \) has passed, where \( C(\tau) \) is sufficiently small.

To improve averaging, use multiple **independent time origins**:

$$
\langle X(t_0) X(t_0 + t) \rangle
$$

### Example

A random variable \( X \) is chosen every time step from a uniform distribution over \([-1, 1]\).

- \( \langle X^2 \rangle = \int_{-1}^1 x^2 \cdot \frac{1}{2} dx = \frac{1}{3} \)
- For two independent samples: \( \langle X(t_0) X(t_0 + 1) \rangle = 0 \)
- \( \langle X(t_0) X(t_0 + 2) \rangle = 0 \)

## 2. Ways to Compute Autocorrelation

### Methods

- **FFT (Fast Fourier Transform)**: Efficient for computing \( C(t) \) over long times.
- **Brute Force**: Common for short-time correlations.

### Brute Force Steps

1. Choose \( X_i \) in data series as \( t_0 \)
2. For \( j = i \) to \( i + \text{window} \):
   - Accumulate \( C_{j-i} += X_i X_j \)
3. Advance to next origin \( i \) and repeat
4. Normalize: \( C_k = \frac{C_k}{N - k} \)

## 3. Green-Kubo and Einstein Relations

Using **linear response theory** (small perturbations), we can show:

### Green-Kubo Formula

$$
X = \int_0^\infty dt \, \langle A(0) A(t) \rangle
$$

- \( X \): transport coefficient
- \( A(t) \): dynamic observable

### Einstein Relation

$$
X = \lim_{t \to \infty} \frac{1}{2t} \langle [A(t) - A(0)]^2 \rangle
$$

This is a **fluctuation-dissipation relation**.

## 4. Diffusion

### Diffusion Coefficient \( D \)

$$
D = \lim_{t \to \infty} \frac{1}{2d} \frac{d}{dt} \langle [x(t) - x(0)]^2 \rangle
$$
If isotropic:

$$
D = \frac{1}{3} (D_{xx} + D_{yy} + D_{zz})
$$

Or:

$$
D = \lim_{t \to \infty} \frac{1}{2d} \langle \Delta x(t)^2 \rangle
$$

### Random Walker in 1D

- Hop left or right with \( p = \frac{1}{2} \)
- \( \langle \Delta x \rangle = 0 \)
- \( \langle \Delta x^2 \rangle = n l^2 \) (binomial distribution)

Hence:

$$
D = \frac{l^2}{2 \Delta t}
$$
