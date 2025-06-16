# Initialization and Neighbor Searching

## Initialization

How to place particles in a box initially?
Want to avoid too many overlaps or the simulation will likely blow up.

- If density is low enough, **random sequential addition** may work:
  1. Choose a random position.
  2. Check if there are overlaps with existing particles (subject to PBCs).
  3. Accept if no overlaps; otherwise, choose a new location.

> This procedure becomes inefficient once there are too many particles.
> A dense solid is an extreme case, but most liquids also cannot be initialized this way.

- If density is very high or structure is ordered (e.g., crystal), use a **lattice**:
  - Examples:
    - Simple cubic
    - Face-centered cubic (FCC)
    - Body-centered cubic (BCC)
    - Hexagonal close-packed (HCP)
  - Choose lattice spacing so that:
    1. Particles don't overlap.
    2. Lattice fits a periodic box.

- If density is intermediate:
  - Use a lattice but randomly fill sites in it.
  - This strategy is effective for speeding up equilibration when:
    - Density is fairly high.
    - There are multiple particle types or sizes (e.g., fill big to small on different lattices).

- Or, use a tool like **Packmol**:
  - Places particles at random.
  - Solves a large optimization problem to eliminate overlaps.

## Neighbor Search

When placing particles or doing pair force calculations, you need to find distances between particles that are close (within a cutoff).

- Naively checking all pairs:
  - Number of unique pairs:
    $$ \frac{N(N-1)}{2} $$
  - This is expensive, especially since most pairs are beyond the cutoff.

### Solution: Accelerate search using a cheap data structure

- **Cell list (uniform grid)**:
  - Bin particles into cells (~O(N) operation).
  - For each particle, only look in nearby cells.
  - Hence, total cost becomes **O(N)** instead of **O(N²)**.
  - Distance checks become spatially localized.

### Other approaches

- **Bounding volume hierarchies**
- **Octrees**
- **k-d trees** (implemented in `scipy`)

> Be careful with PBCs when using trees.
> These methods can be very fast, especially for sparse systems or with multiple particle types.

## Additional Resorces
