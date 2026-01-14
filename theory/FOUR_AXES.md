# The Four Axes of Robustness

## Overview

The Orthogonal Robustness Framework identifies four independent dimensions along which structures in discrete dynamical systems can be characterized. Each axis answers a distinct question about the structure's capabilities and behavior.

---

## Axis 1: Computational Capability

**Source:** Paper 1 (Universal Computation Threshold)

### Question
Can the system perform universal computation?

### Criterion
Specification complexity ≥ 5 bits under natural encoding, plus structural conditions.

### Capability Decomposition
The 5-bit threshold decomposes as:

| Capability | Bits | Requirement | Classical Reference |
|------------|------|-------------|---------------------|
| Logic (L) | ≥ 2 | Boolean completeness | Post 1941 |
| Memory (M) | ≥ 1 | Unbounded storage | Turing 1936 |
| Control (K) | ≥ 1 | Conditional branching | Böhm-Jacopini 1966 |
| State (S) | ≥ 1 | Halting distinction | Minsky 1967 |

**Total: 2 + 1 + 1 + 1 = 5 bits minimum**

### Structural Conditions
The 5-bit threshold is necessary but not sufficient. Additional conditions apply:

- **1D CA:** Asymmetry > 0.3, collision diversity > 0.5
- **2D systems:** Collision geometry with ≥4 directions
- **Tag systems:** Production growth for some symbol

### The Control Conjecture
The critical 5th bit is Control—the capacity for context-dependent divergence in interaction outcomes. Paper 2 proves that Control requires hidden state.

### Examples
| System | Bits | Universal? | Notes |
|--------|------|------------|-------|
| Rule 110 | 5 | YES | Achieves threshold exactly |
| Rule 30 | 4 | NO | Missing Control |
| Tag(2,2) | 5 | YES | Minimal universal tag system |
| SK calculus | 5 | YES | Combinatory logic |

---

## Axis 2: Self-Maintenance

**Source:** Papers 2-4 (Stickiness, Self-Maintenance Census, Leakiness)

### Question
Does the system exhibit life-like behavior—active persistence through environmental interaction?

### Criterion
Three conditions must hold simultaneously:

1. **Control > 0** (Paper 2)
   - Context-dependent responses
   - Requires hidden state

2. **Stability mechanism** (Paper 3)
   - Either: Absorption > 0.5 (perturbations absorbed without state change)
   - Or: Repair > 0.7 (active return to prior state)

3. **Activity within window** (Paper 3)
   - 0.05 ≤ Activity ratio ≤ 0.5
   - Neither frozen nor chaotic

### Predictive Model (Paper 4)
Life-like emergence can be predicted from substrate properties:

| Property | Threshold | Interpretation |
|----------|-----------|----------------|
| Leakiness (L) | ≈ 0.39 | Phase transition; below = "prone" |
| Capacity (C) | ≈ 1.1 bits/cell | Structure threshold |

Two-axis model achieves R² = 0.96 prediction accuracy.

### Census Result
When stickiness is applied to elementary cellular automata:
- **168/194** non-trivial rules (83.7%) exhibit life-like behavior
- This is a dramatic increase from native ECA behavior

### Examples
| Rule | Life-like? | Mechanism |
|------|------------|-----------|
| 90 | YES | High absorption (XOR pattern) |
| 110 | NO | Fails stability criterion |
| 184 | YES | Traffic model dynamics |
| 30 | NO | Chaotic, no repair |

---

## Axis 3: Survival

**Source:** Paper 5 (Invariants Under Temporal Filtering)

### Question
Does the structure persist under temporal filtering?

### Criterion
Basin of attraction strength.

### Classification

| Structure Type | Basin Type | Survival Probability |
|---------------|------------|---------------------|
| Still life | Point attractor | 100% |
| Oscillator | Limit cycle | 100% |
| Amplifying pattern | Large basin | >95% |
| Glider/signal | No basin (trajectory) | <5% |
| Chaos | Entire space | 100% (trivial) |

### The Basin Criterion
> "What survives is not what computes, but what repairs."

Survival is determined by basin geometry, not computational importance.

### Intrinsicality Theorem
Basins are intrinsic properties of structures. Proximity to a basin-possessing structure does not confer stability on a structure without a basin.

**Implication:** A glider passing near an oscillator is not stabilized by the oscillator's basin.

### Quantitative Result
Basin classification predicts survival with **98% accuracy** across tested configurations.

---

## Axis 4: Visibility

**Source:** Paper 6 (Anti-Resonance)

### Question
Is encoded information distinguishable from the carrier?

### Criterion
Sampling depth d relative to carrier period P.

### Anti-Resonance Effect

| Condition | Visibility | Mechanism |
|-----------|------------|-----------|
| d ≡ 0 (mod P) | MINIMUM | Phase alignment hides signal |
| d ≢ 0 (mod P) | MAXIMUM | Phase mismatch creates contrast |

### Requirements
- Oscillatory carrier (not quiescent background)
- Defect-on-carrier encoding

### Effect Size
~2.6× difference in Hamming ratio between optimal and anti-resonant depths.

### Critical Observation
Visibility is orthogonal to survival:
- An oscillator at anti-resonant depth **survives** (strong basin) but carries **hidden** information
- A glider at non-anti-resonant depth is **visible** but **destroyed** (no basin)

---

## Summary Table

| Axis | Question | Criterion | Key Metric |
|------|----------|-----------|------------|
| Computation | Can it compute? | ≥5 bits + structure | Specification complexity |
| Self-Maintenance | Does it persist actively? | Control + Stability + Activity | Life-like classification |
| Survival | Does it withstand filtering? | Basin strength | Survival probability |
| Visibility | Is information readable? | d ≢ 0 (mod P) | Hamming ratio |

---

## The Four-Dimensional Space

Every structure can be characterized by its position: (C, SM, Su, V)

| Structure | C | SM | Su | V | Description |
|-----------|---|----|----|---|-------------|
| Rule 110 glider | 1 | 0 | 0 | 1 | Computes, visible, fragile |
| Rule 90 bulk | 0 | 1 | 1 | 1 | Self-maintains, survives |
| Still life | 0 | 0 | 1 | 1 | Survives, visible, passive |
| Anti-resonant oscillator | 0 | 1 | 1 | 0 | Self-maintains, hidden |

The framework predicts all 16 combinations should be realizable.

---

*Provenance: Synthesized from Papers 1-6. See individual papers for detailed proofs and experimental data.*
