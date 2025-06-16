# Monte Carlo: NVT, NPT, and Grand Canonical Ensembles

## Trial Moves

- Should be:
  - (a) Microscopically reversible
  - (b) Ergodic
  - (c) Efficient

- **Single-particle moves** are preferred due to:
  - Cost ∝ number of particles moved (N)
  - Acceptance ∝ probability (p)

- **Displacement rule**:

  ```text
  x_i = x_i + dr_max * (rand() - 0.5)
  y_i = y_i + dr_max * (rand() - 0.5)
  z_i = z_i + dr_max * (rand() - 0.5)
  ```

x := x + drmax *(rand - 0.5) y := y + drmax* (rand - 0.5) z := z + drmax * (rand - 0.5)

- How do we select `drmax`?
- Low `drmax` → high acceptance, but small movement
- Common recipe: select `drmax` for 50% acceptance
- Some studies suggest 20% is better

## CPU Cost and Acceptance

- CPU cost of a successful move: `ts`
- CPU cost of an unsuccessful move: `tu`
- Actual displacement per step ∝ `p(1 - p)`
- CPU time per step: `p * ts + (1 - p) * tu`
- Optimal acceptance probability `p_opt = 0.5`

## Initial Configuration

- Random placement:
- Requires repeated attempts to avoid overlaps
- Place particle 1 randomly
- Place particle 2 randomly, check overlaps with existing particles

## Energy Calculation

Two types:

1. **From scratch**:

- All interactions: \( \frac{N(N-1)}{2} \) pairs

2. **Changed interactions**:

- Only 2 × (N - 1) interactions (old and new positions)

- Acceptance:
ΔU = U_new - U_old Accept if exp(-βΔU) > rand

## NPT Monte Carlo (Isothermal-Isobaric Ensemble)

- Useful for simulating constant pressure and temperature
- Microstate probability ∝ exp(-βU - βPV)
- Volume fluctuations must be sampled
- Volume change:
- Scale positions for continuous potentials
- No scaling for lattice models

## Volume Change Acceptance

- Coordinate scaling:
P_new ∝ V^N *exp(-βU_new - βPV_new) P_old ∝ V^N* exp(-βU_old - βPV_old) Acceptance = min(1, P_new / P_old)

- For volume creation/annihilation (no particle movement):
Acceptance = min(1, exp(-βΔU - βPΔV))

- Test: Equation of state for non-interacting particles

## Implementation Issues

- Multiple move types:
- Choose with fixed probabilities
- Example: 99% displacements (cheap), 1% volume changes (expensive)
- Rule of thumb: equalize CPU cost per move type

## Selecting `dVmax`

- Target acceptance: 20–30%
- Sampling in `V` or `lnV`:
- Sampling in `lnV` better at low densities
- Modify acceptance criterion accordingly

- Overall algorithm:

```fortran
do istep = 1, nsteps
  if (rand() < p_displ) then
    call displace(N, u, ...)
  else
    call V_change(N, u, V, ...)
  endif
  if (mod(istep, sample_interval) == 0) call sample()
enddo
```

Grand Canonical Monte Carlo (GCMC)
Simulations at constant chemical potential

Useful for phase equilibrium calculations

Fundamental equation:

dU = TdS - PdV + μdN
Microstate probability ∝ exp(-βU + βμN)

Fluctuations:

⟨(ΔN)^2⟩ = kT^2 / (∂μ/∂N)
Particle Addition/Removal
Attempt 50% additions, 50% removals

Addition:

Accept(N → N+1) = min(1, (V / (N+1)) * exp(-βΔU + βμ))
Removal:

Accept(N → N-1) = min(1, (N / V) * exp(-βΔU - βμ))
For ideal gas:

exp(-βμ) = 1 / (N+1) *V
μ = kT* ln(ρ)
Implementation Details
Insertion:

Increase array size
N = N + 1
Deletion:

Patch hole in array
x(m) = x(N)
N = N - 1
Metastable States
At high T: density converges regardless of initial state

At low T: hysteresis observed

Density jumps at certain pressure
Remains high even if pressure decreases
Associated with phase transitions

Seen in experiments (e.g., bubble chambers)

Phase Transition and EOS
Nucleation barrier prevents transition

Barrier higher at lower T

Present in van der Waals EOS:

P = RT / (v - b) - a / v^2
Maxwell construction needed for equilibrium

Combine NPT and GCMC to find correct transition densities

## Additional Resorces
