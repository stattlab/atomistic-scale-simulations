# Gibbs Ensemble and Phase Coexistence

## 1. Phase Coexistence

- Total system is closed, sum of two phases:
  - \( E = E_A + E_B \)
  - \( S = S_A + S_B \)
  - \( V = V_A + V_B \)
  - \( N = N_A + N_B \)

- Since the total system is closed, \( E, V, N \) are constant:
  - \( dE = 0 = dE_A + dE_B \Rightarrow dE_A = -dE_B \)
  - \( dV = 0 = dV_A + dV_B \Rightarrow dV_A = -dV_B \)
  - \( dN = 0 = dN_A + dN_B \Rightarrow dN_A = -dN_B \)

- Entropy differential:
  \[
  dS = dS_A + dS_B = \left( \frac{1}{T_A} - \frac{1}{T_B} \right) dE_A + \left( \frac{P_A}{T_A} - \frac{P_B}{T_B} \right) dV_A - \left( \frac{\mu_A}{T_A} - \frac{\mu_B}{T_B} \right) dN_A
  \]

- At equilibrium, entropy is maximized \( \Rightarrow dS = 0 \), so:
  - \( T_A = T_B \)
  - \( P_A = P_B \)
  - \( \mu_A = \mu_B \)

## 2. Simulating Phase Coexistence

- **Direct (interfacial) coexistence**: two phases in one box
- **GCMC + NPT**: simulate \( S(P), \mu(P) \); find coexistence where \( P \) and \( \mu \) match
- **GCMC with histogram reweighting**: accurate but expensive

## 3. Gibbs Ensemble

- Idea: couple two systems to generate equal \( P \) and \( \mu \)
- Boxes represent bulk phases, no true interface
- Probability of observing both systems in a state:
  \[
  \propto \frac{V_A^{N_A} V_B^{N_B}}{N_A! N_B!} \exp[-\beta(U_A + U_B)]
  \]

### Move Set

- **Displacement** (NVT move):
  \[
  P_{\text{accept}} = \min\left(1, e^{-\beta \Delta U}\right)
  \]

- **Volume change** (move \( \Delta V \) from box B to A):
  \[
  P_{\text{accept}} = \min\left(1, \left(\frac{V_A + \Delta V}{V_A}\right)^{N_A} \left(\frac{V_B - \Delta V}{V_B}\right)^{N_B} e^{-\beta \Delta U}\right)
  \]

- **Particle transfer** (move particle from B to A):
  \[
  P_{\text{accept}} = \min\left(1, \frac{V_A}{V_B} \frac{N_B}{N_A + 1} e^{-\beta \Delta U}\right)
  \]

- Typical move set: 100 displacements : 1 volume change : 200 transfers

## 4. Gibbs–Duhem Integration

- If one coexistence point is known, use thermodynamics to integrate:
  \[
  -S_A dT + V_A dP - N_A d\mu_A = 0
  \]
  \[
  -S_B dT + V_B dP - N_B d\mu_B = 0
  \]

- Subtracting:
  \[
  d(\mu_B - \mu_A) = -(S_B - S_A) dT + (V_B - V_A) dP
  \]

- At coexistence:
  \[
  \frac{dP}{dT} = \frac{S_B - S_A}{V_B - V_A} = \frac{\Delta H}{T \Delta V}
  \]

- This is the **Clapeyron equation** (or Clausius–Clapeyron if ideal gas)

- Most useful for solids where other techniques are harder or fail

## Additional Resorces
