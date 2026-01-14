# Orthogonality Proofs

## Overview

The central claim of the Orthogonal Robustness Framework is that the four axes are independent. This document compiles evidence for three key orthogonalities.

---

## Orthogonality 1: Computation ⊥ Self-Maintenance

### Claim
Knowing whether a system computes provides no information about whether it self-maintains, and vice versa.

### Evidence Table

| Rule | Computes? | Life-like? | Notes |
|------|-----------|------------|-------|
| 110 | YES (Turing-complete) | NO | Fails stability criterion |
| 90 | NO (linear/additive) | YES | High absorption |
| 30 | NO (chaos) | NO | Neither property |
| 184 | NO | YES | Traffic model |

### Case Study: Rule 110

Rule 110 is Turing-complete (Cook 2004), achieving the 5-bit threshold with exactly 5 bits set in its rule table. It supports:
- Persistent localized structures (gliders)
- Collisions that implement logic gates
- Universal computation via tag system embedding

However, Rule 110 is **not life-like** under the Paper 3 criteria:
- It fails the stability criterion
- Perturbations propagate rather than being absorbed or repaired
- The computational structures (gliders) are trajectories, not basins

**Source:** Paper 1 (Section 3), Paper 3 (Section 4.2)

### Case Study: Rule 90

Rule 90 is the XOR rule: cell state = left neighbor XOR right neighbor. It is:
- **Linear:** Superposition principle applies
- **Not universal:** Cannot implement NAND (Paper 1, Theorem 4)
- **Life-like:** High absorption, stable patterns under stickiness

Rule 90 generates Sierpiński triangle patterns—complex-looking but entirely predictable. It self-maintains but cannot compute.

**Source:** Paper 3 (Section 4.1)

### Structural Interpretation

**Computation requires trajectories:** Information must traverse state space. Signals must propagate. Collisions must transform inputs to outputs.

**Self-maintenance requires basins:** Perturbations must be absorbed or repaired. States must return to attractors.

These are **structurally incompatible** requirements for the same structural element. A trajectory, by definition, moves through phase space. A basin, by definition, attracts nearby states to a fixed point or cycle.

### Implication
A system cannot simultaneously maximize computational capability AND self-maintenance using the same structural elements. Engineering design must choose or segregate these functions.

---

## Orthogonality 2: Survival ⊥ Visibility

### Claim
Knowing whether a structure survives provides no information about whether its information content is visible, and vice versa.

### Evidence Table

| Configuration | Survives? | Visible? | Mechanism |
|--------------|-----------|----------|-----------|
| Oscillator, d ≡ 0 (mod P) | YES | NO | Basin strong, anti-resonant |
| Oscillator, d ≢ 0 (mod P) | YES | YES | Basin strong, phase contrast |
| Glider, d ≢ 0 (mod P) | NO | YES (briefly) | No basin, visible until destroyed |
| Glider, d ≡ 0 (mod P) | NO | NO | No basin, would be hidden if survived |

### The Independence Mechanism

**Survival** depends on:
- Basin geometry (phase space topology)
- Intrinsic structural properties
- Whether the structure possesses an attractor

**Visibility** depends on:
- Carrier period P
- Sampling depth d
- The relationship d mod P

These reference **different aspects** of the system:
- Survival is about phase space topology
- Visibility is about temporal alignment

### Quantitative Evidence

Paper 6 demonstrates:
- Modulating depth d changes visibility by **2.6×**
- Survival remains constant (determined by basin strength, not d)
- The two metrics vary independently

### Implication

A robust storage system (strong basin, survives indefinitely) may carry information that is **unreadable** at certain sampling frequencies.

Conversely, a fragile signal (no basin, destroyed by filtering) may carry **highly visible** information during its brief existence.

**Source:** Paper 5 (Section 5), Paper 6 (Section 4)

---

## Orthogonality 3: Computation ⊥ Survival

### Claim
Structures that compute tend not to survive, and structures that survive tend not to compute.

### The Computation-Robustness Tradeoff

| Structure | Computational Role | Basin Type | Survival |
|-----------|-------------------|------------|----------|
| Glider | Signal carrier | None | LOW |
| Collision debris | Logic gate output | None | LOW |
| Still life | None | Point | HIGH |
| Oscillator | Clock (maybe) | Cycle | HIGH |
| Ether/background | None | Large | HIGH |

### Mechanistic Explanation

**Computational structures are trajectories:**
- They must move through state space to carry information
- They transform inputs to outputs via collisions
- Trajectories, by definition, do not remain in a basin
- They are **fragile** under temporal filtering

**Robust structures are basins:**
- They return to attractors after perturbation
- Attractor states are, by definition, fixed or cycling
- They do not traverse state space
- They **cannot carry** dynamic information

### Evidence from Rule 110

When gliders collide in Rule 110:
- Computational processing occurs (information is transformed)
- The gliders are destroyed
- Debris is produced
- Some debris crystallizes into stable bulk material

The stable bulk material survives but does not compute. The gliders computed but did not survive.

### Resolution: "Compute Briefly, Then Crystallize"

Paper 5 suggests a design pattern:
1. Use fragile computational elements for logic
2. Convert results immediately to robust storage
3. Accept that computation and persistence are temporally segregated

This is consistent with biological organization: active computation (neural firing, enzymatic reactions) is segregated from persistent storage (DNA, structural proteins).

**Source:** Paper 5 (Section 6.2)

---

## Formal Independence Argument

### Definition
Two axes A and B are orthogonal if:
```
P(A = high | B = high) = P(A = high | B = low)
```

That is, knowing B provides no information about A.

### Empirical Test

For Computation ⊥ Self-Maintenance:
- P(Computes | Life-like) = P(Rule 110 type) / P(Life-like) ≈ low
- P(Computes | NOT Life-like) = P(Rule 110 type) / P(NOT Life-like) ≈ similar

The 256-rule ECA census (Paper 3) provides the dataset. Computation is rare in both life-like and non-life-like subsets.

### Correlation Coefficients

Predicted correlations between axes:
| Pair | Expected r |
|------|------------|
| Computation × Self-Maintenance | ≈ 0 |
| Survival × Visibility | ≈ 0 |
| Computation × Survival | ≈ 0 (possibly slightly negative) |
| Self-Maintenance × Survival | > 0 (both use basins) |

Note: Self-Maintenance and Survival are not strictly orthogonal—both involve basins. However, they measure different aspects (active persistence vs. passive survival).

---

## Summary

| Orthogonality | Key Evidence | Interpretation |
|---------------|--------------|----------------|
| Computation ⊥ Self-Maintenance | Rule 110 vs Rule 90 | Trajectories vs basins |
| Survival ⊥ Visibility | Oscillator visibility varies with d | Phase space vs temporal alignment |
| Computation ⊥ Survival | Gliders die, still lifes persist | Motion vs stability |

The four axes measure genuinely different properties of structures. Understanding this orthogonality is essential for engineering robust dynamical systems.

---

*Provenance: Evidence compiled from Papers 1, 3, 5, 6. Formal definitions adapted from Paper 3 (Section 2) and Paper 5 (Section 3).*
