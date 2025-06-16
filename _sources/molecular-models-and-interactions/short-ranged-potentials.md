# Short-Ranged Intramolecular Potentials

## Features of Interaction

- Applies between **all particles** in the system, pairwise and additive.
- Some force fields **exclude** interactions between certain bonded particles:
  - 1–2 (bonded): ignored
  - 1–3 (two bonds apart): ignored
  - 1–4 (three bonds apart): rescaled (e.g., by 50%)

- Interactions are "**short-ranged**" and can be **truncated** at a **cutoff** $r_c$:
  - $\Delta u = 2\pi \rho \int_{r_c}^{\infty} \underbrace{r^2 \underbrace{u(r)}_{\sim 1/r^6}}_{\sim 1/r^4} dr $ converges
  - In MD, truncate forces: $ F(r > r_c) = 0 $

## Nonbonded Potentials

### Lennard-Jones Potential

 $ u(r) = 4\varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right] $

The most wildely used intramolecular potential. We will focus is on the Lennard-Jones (LJ) potential due to its common use.

```{tip}
Once of the reasons why the LJ potential is so popular, is that one can re-use the $ \left( \frac{\sigma}{r} \right)^6$ term by squaring it - thus reducing computational cost. This is much less important with improved hardware.
```

### Mie Potential

$ u(r) = C \varepsilon \left[ \left( \frac{\sigma}{r} \right)^n - \left( \frac{\sigma}{r} \right)^m \right] $
with $ C = \frac{nm}{n - m} \left( \frac{n}{m} \right)^{\frac{m}{n - m}} $

This is a generaized LJ potential.

### Exponential-6 Potential

$ u(r) = -A e^{-Br} + \frac{C}{r^6} $

## Force Calculation

\begin{align*}
 \vec{F}_{ij} &= -\nabla_i u(r_{ij}) \\
 &= \underbrace{-\frac{du}{dr}}_{=F(r)} \nabla_i {r}_{ij} \\
 & = - F(r)\hat{r}_{ij}
\end{align*}

```{example} Lennard-Jones Force
\begin{align*}
u(r) = 4\varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right]
\end{align*}

\begin{align*}
 F(r) &= -\frac{du}{dr}
 &= -4\varepsilon \left[ -12\frac{\sigma^{12}}{r^{13}} + 6 \frac{\sigma^{6}}{r^{7}}\right]
 & = \frac{24\varepsilon}{r} [2 \left( \frac{\sigma}{r} \right)^{12}  - \left( \frac{\sigma}{r} \right)^{6} ]
 \end{align*}
When written in this form, the  $\left( \frac{\sigma}{r} \right)^6$-term can be reused from the $u(r)$ calculation.
```

```{tip}
Write $F_i= -F(r) \hat{r}_{ij} = - \frac{F(r_{ij})}{r_{ij}} \vec{r}_{ij}$. Then one can write the LJ force in such a way, that only ever $r^2_{ij}$ is needed, not $r_{ij}$, thus avoiding the need for a expensive sqrt operation.
```

## Truncating and Shifting

**Truncate**:
\begin{align*}
u(r) = u_o(r)H(r_c-r) =\begin{cases}  U_o(r)\quad r\leq r_c \\
0 \quad r\ge r_c  \end{cases}
\end{align*}
Note that this means that the force has a "jump" at the cutoff, because $\frac{\partial u}{\partial r}$ now has a $\delta(r_c-r)$ term from the Heaviside function, if $U_o(r_c) \neq 0$.

**Truncate** and **shift**:
\begin{align*}
u(r) = \left[u_o(r)-u_o(r_c)\right]H(r_c-r) =\begin{cases}  U_o(r)-u_o(r_c)\quad r\leq r_c \\
0 \quad r\ge r_c  \end{cases}
\end{align*}

Here $\frac{\partial u}{\partial r}$ is finite but might be discontinous. One can apply **smoothing functions**, e.g. polynominals (xplor).

```{example} Weeks-Chandler-Anderson Potential
Use truncate and shift scheme at $r_c=2^{1/6}\sigma$ for LJ potential. The result is a purely repulsive potential, the WCA potential, often used to model purely excluded volume interactions.
```

For  truncating, truncating and shifting, and or smoothing, **thermodynamic properties** will be influenced by the exact scheme. Those effects can be corrected with long-range integral approximations/corrections.

## Mixing Rules

For unlike atom types $i$ and $j$, use mixing rules on LJ parameters. There are many different ones, falling into two categories, arithmetic ($x_{ij}=(x_j+x_i)/2$) or geometric ($x_{ij}=\sqrt{x_ix_j}$).

Commonly used mixing rules are:

- Lorentz-Berthelot:\
 $\begin{align*}
\sigma_{ij} &= \frac{\sigma_{ii}+\sigma_{jj}}{2}\\
\epsilon_{ij} &= \sqrt{\epsilon_{ii}\epsilon_{jj}}
\end{align*}$
- Kong:\
 $\begin{align*}
\epsilon_{ij}\sigma_{ij}^{6}&=\left(\epsilon _{ii}\sigma_{ii}^{6}\epsilon_{jj}\sigma_{jj}^{6}\right)^{1/2}\\
 \epsilon_{ij}\sigma_{ij}^{12}&=\left[{\frac {(\epsilon_{ii}\sigma_{ii}^{12})^{1/13}+(\epsilon_{jj}\sigma_{jj}^{12})^{1/13}}{2}}\right]^{13}
 \end{align*}$

## Additional Resorces

- more short-ranged potentials, as implemented in:
  - [hoomd-blue](https://hoomd-blue.readthedocs.io/en/v5.2.0/hoomd/md/module-pair.html)
  - [LAMMPS](https://docs.lammps.org/pair_style.html)
  - [GROMACS](https://manual.gromacs.org/current/reference-manual/functions/nonbonded-interactions.html)
- more mixing rules from [Wikipedia](https://en.wikipedia.org/wiki/Combining_rules)
