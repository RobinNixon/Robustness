# Basin of Attraction as Organizing Principle

## Synthesis Claim 2

> **Basin of attraction is the organizing principle.** The geometry of phase space—where basins exist, how deep they are, what their periods are—determines self-maintenance, survival, and visibility.

---

## Basin Fundamentals

### Definition
A **basin of attraction** is a region of phase space from which all trajectories converge to a common attractor.

Types of attractors:
| Attractor Type | Phase Space Structure | Example |
|----------------|----------------------|---------|
| Point (fixed point) | All trajectories → single state | Still life in GoL |
| Cycle (limit cycle) | All trajectories → periodic orbit | Oscillator (blinker) |
| Strange (chaotic) | Bounded but non-periodic | Lorenz attractor |

### Basin Depth
Informally, basin "depth" refers to how strongly states are attracted:
- **Deep basin:** Strong attraction, perturbations quickly corrected
- **Shallow basin:** Weak attraction, perturbations may escape

Under stickiness, the confirmation counter provides a quantitative measure of depth.

---

## Role in Self-Maintenance (Axis 2)

### Stability Mechanisms Are Basin Mechanisms

Paper 3 identifies two stability mechanisms:
1. **Absorption:** Perturbations absorbed without state change
2. **Repair:** Active return to prior state

Both are basin-related:
- **Absorption:** The basin is so deep that perturbations don't reach the edge
- **Repair:** The basin actively pulls states back to the attractor

### Quantitative Thresholds (Paper 3)
| Mechanism | Threshold | Basin Interpretation |
|-----------|-----------|---------------------|
| Absorption | > 0.5 | Basin depth > perturbation amplitude |
| Repair | > 0.7 | Basin slope steep enough for return |

### Life-Like Classification
The 83.7% of ECA rules that become life-like under stickiness are precisely those where stickiness creates or deepens basins.

**Source:** Paper 3 (Section 3)

---

## Role in Survival (Axis 3)

### The Basin Criterion

Paper 5 establishes:
> "What survives is not what computes, but what repairs."

Survival under temporal filtering is determined by basin strength:

| Structure | Basin | Survival |
|-----------|-------|----------|
| Still life | Point attractor | 100% |
| Oscillator | Limit cycle | 100% |
| Glider | No basin (trajectory) | <5% |
| Chaos | Trivial (entire space) | 100% |

### Intrinsicality Theorem

**Theorem (Paper 5):** Basins are intrinsic and non-transferable.

Proximity to a basin-possessing structure does not stabilize a structure without a basin.

**Proof sketch:** A glider near an oscillator experiences the oscillator's basin only if it enters the oscillator's phase space region. But a glider, by definition, moves through phase space. Its trajectory may pass near the oscillator's attractor but does not converge to it.

**Implication:** You cannot "borrow" stability. Each structure must possess its own basin to survive.

**Source:** Paper 5 (Section 4)

---

## Role in Visibility (Axis 4)

### Carrier Oscillation as Basin Cycle

The anti-resonance effect (Paper 6) requires an oscillatory carrier. An oscillator is a limit cycle—a periodic basin.

| Carrier Property | Basin Interpretation |
|------------------|---------------------|
| Period P | Cycle length of limit cycle |
| Phase | Position within the cycle |
| Stability | Basin depth around the cycle |

### Anti-Resonance Mechanism

When sampling depth d ≡ 0 (mod P):
- Sampling always occurs at the same phase
- The carrier appears uniform (same phase everywhere)
- Defects are hidden in the uniform background

When d ≢ 0 (mod P):
- Sampling occurs at different phases
- The carrier shows phase variation
- Defects create contrast against varying background

**Source:** Paper 6 (Section 3)

---

## Why Computation Is the Exception

### Trajectories vs. Basins

Computation requires **trajectories**:
- Signals must propagate (move through space)
- Collisions must transform states
- Information must flow

Basins are the opposite:
- Attractors are stationary or periodic
- Nearby states converge, not diverge
- Information is absorbed, not transmitted

### The Structural Incompatibility

A structure cannot simultaneously be:
1. A trajectory (for computation)
2. A basin (for robustness)

This is not a design limitation but a **mathematical constraint**:
- Trajectory: f(x) ≠ x (state changes)
- Fixed point: f(x) = x (state unchanged)
- These are mutually exclusive for the same x

### The Computation-Robustness Tradeoff

| Property | Requires | Structural Form |
|----------|----------|-----------------|
| Computation | State change, propagation | Trajectory |
| Robustness | Stability, return to attractor | Basin |

**Resolution:** Temporal segregation. "Compute briefly, then crystallize."
1. Use fragile computational elements for logic
2. Convert results immediately to robust storage
3. Accept that computation and persistence alternate

**Source:** Paper 5 (Section 6)

---

## Basin Geometry and the Four Axes

### Summary Table

| Axis | Basin Role | What Basin Property Matters |
|------|------------|----------------------------|
| Computation | Exception (needs trajectories) | — |
| Self-Maintenance | Stability mechanisms | Basin depth, repair strength |
| Survival | THE criterion | Basin existence, size |
| Visibility | Carrier oscillation | Basin period P |

### The Unified View

Three of four axes are organized by basins:

```
                    BASIN OF ATTRACTION
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    SELF-MAINTENANCE    SURVIVAL      VISIBILITY
    (basin depth)       (basin        (basin period)
                        existence)
```

Computation stands apart—it requires the opposite structure (trajectories).

---

## Design Implications

### Principle: Build on Basins

To achieve self-maintenance and survival:
1. **Identify basin-possessing structures** in your substrate
2. **Recognize intrinsicality:** Basins cannot be borrowed
3. **Design for repair:** Active return to attractor, not just passive resistance

### Principle: Segregate Computation

Since computation requires trajectories:
1. Accept that computational elements are fragile
2. Convert results to basin-possessing storage immediately
3. Use temporal alternation: compute → store → compute → store

### Engineering Checklist

| Goal | Basin Requirement | Design Action |
|------|-------------------|---------------|
| Self-maintenance | Deep basins | Increase absorption/repair |
| Survival | Any basin | Use oscillators/still lifes |
| Visibility | Avoid period multiples | Sample at d ≢ 0 (mod P) |
| Computation | Accept no basin | Use fragile elements, convert outputs |

---

## Connection to Temporal Filtering

### How Filtering Creates Basins

Temporal filtering (stickiness) creates basin-like structure even in systems without native basins:

1. **Confirmation counters** act as "depth"
2. States with high confirmation are "deep" (stable)
3. States with low confirmation are "shallow" (vulnerable)

This is why:
- 83.7% of ECA rules become life-like under stickiness
- Rules that are chaotic natively acquire structure
- Filtering reveals latent basin potential

### Synthesis Claim 3 Connection

> "Temporal filtering is a diagnostic probe that reveals intrinsic properties."

Filtering reveals basin potential—the latent capacity for basin-like behavior. Some substrates (low leakiness, high capacity) have high potential; others have low potential.

**Source:** Paper 4 (Section 4), Paper 5 (Section 5)

---

## Summary

**Synthesis Claim 2:** Basin of attraction is the organizing principle.

| Aspect | Basin Role |
|--------|-----------|
| Self-Maintenance | Basin depth determines stability |
| Survival | Basin existence determines persistence |
| Visibility | Basin period determines phase alignment |
| Computation | Exception—requires trajectories instead |

The fundamental insight: **robustness and computation are in tension** because they require opposite phase space structures. Understanding this tension is essential for engineering robust computational systems.

---

*Provenance: Synthesized from Papers 3, 5, 6, with structural analysis from Paper 1.*
