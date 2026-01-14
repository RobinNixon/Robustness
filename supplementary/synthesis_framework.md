# The Orthogonal Robustness Framework

## A Unified Theory of Structure, Survival, and Visibility in Discrete Dynamical Systems

---

## 1. The Central Thesis

**Claim:** Discrete dynamical systems exhibit multiple independent axes of robustness. A structure's fate under perturbation cannot be reduced to a single metric. Instead, four orthogonal properties determine different aspects of a structure's behavior:

1. **Computational Capability** (Can it compute?)
2. **Self-Maintenance** (Does it actively persist?)
3. **Survival** (Does it withstand temporal filtering?)
4. **Visibility** (Is the information readable?)

These axes are orthogonal—knowing a structure's position on one axis provides no information about its position on another. This orthogonality is not a limitation of our framework but a fundamental property of dynamical systems.

---

## 2. The Four Axes

### Axis 1: Computational Capability (Paper 1)

**Question:** Can the system perform universal computation?

**Criterion:** Specification complexity ≥ 5 bits under natural encoding

**Capability Decomposition:**
- Logic ≥ 2 bits (Boolean completeness)
- Memory ≥ 1 bit (read/write)
- Control ≥ 1 bit (conditional branching)
- State ≥ 1 bit (halting distinction)

**The Control Conjecture:** The 5th bit is Control—context-dependent divergence in interaction outcome. This is the same Control that Paper 2 proves requires hidden state.

**Structural Conditions:** Meeting the 5-bit threshold is necessary but not sufficient. Structural conditions (asymmetry, collision diversity) are also required.

---

### Axis 2: Self-Maintenance (Papers 2, 3, 4)

**Question:** Does the system exhibit life-like behavior?

**Criterion:** Control > 0 AND Stability mechanism AND Activity within window

**Components:**
- **Control** (Paper 2): Hidden state → Context-dependence
- **Stability** (Paper 3): Absorption > 0.5 OR Repair > 0.7
- **Activity** (Paper 3): 0.05 ≤ A ≤ 0.5

**Predictive Model (Paper 4):**
- Leakiness predicts life-like percentage (R² = 0.96)
- Capacity (compression) separates prone vs resistant substrates
- Two-point calibration predicts optimal confirmation depth

**Census Result:** 83.7% of non-trivial ECA rules are life-like under stickiness

---

### Axis 3: Survival (Paper 5)

**Question:** Does the structure persist under temporal filtering?

**Criterion:** Basin of attraction strength

**Classification:**
| Structure Type | Basin Type | Survival |
|---------------|------------|----------|
| Amplifying | Large | HIGH |
| Still life | Point | HIGH |
| Oscillator | Cycle | HIGH |
| Glider | None | LOW |
| Chaos | Entire space | HIGH (trivially) |

**The Basin Criterion:** "What survives is not what computes, but what repairs."

**Intrinsicality Theorem:** Basins are intrinsic and non-transferable. Proximity to a basin-possessing structure does not stabilize a structure without a basin.

---

### Axis 4: Visibility (Paper 6)

**Question:** Is encoded information distinguishable?

**Criterion:** Depth d relative to carrier period P

**Anti-Resonance:**
- At d ≡ 0 (mod P): Minimum visibility (carrier absorbs signal)
- At d ≢ 0 (mod P): Maximum visibility (phase mismatch creates contrast)

**Requirements:**
- Oscillatory carrier (not quiescent background)
- Defect-on-carrier encoding

**Effect Size:** ~2.6× Hamming ratio between optimal and anti-resonant depths

---

## 3. Orthogonality Proofs

### Orthogonality 1: Computation ⊥ Self-Maintenance

**Evidence:**
- Rule 110: Turing-complete (computes) but NOT life-like (fails stability criterion)
- Rule 90: Life-like (high absorption) but NOT universal (linear/additive)

**Interpretation:** Computation requires trajectories through state space. Self-maintenance requires basins that attract nearby states. These are structurally incompatible requirements for the same structure.

**Implication:** A system cannot simultaneously be maximally computational AND maximally self-maintaining using the same structural elements. Design must choose or segregate.

---

### Orthogonality 2: Survival ⊥ Visibility

**Evidence:**
- High-basin oscillator at d ≡ 0 (mod P): Survives but information is hidden
- Low-basin glider at d ≢ 0 (mod P): Visible but destroyed

**Interpretation:** Survival depends on basin geometry (phase space topology). Visibility depends on carrier-period alignment (temporal relationship). These reference different aspects of the system.

**Implication:** A structure can survive temporal filtering (strong basin) while carrying information that is unreadable (anti-resonant depth). Conversely, a structure can carry highly visible information (off-period sampling) while being destroyed (no basin).

---

### Orthogonality 3: Computation ⊥ Survival

**Evidence:**
- Gliders: Computational workhorses (carry signals, enable logic) but fragile (no basin)
- Still lifes: Survive perfectly (point attractor) but carry no information

**The Computation-Robustness Tradeoff (Paper 5):**
> "Structures that compute tend not to survive, and structures that survive tend not to compute."

**Resolution:** Rule 110's collision purification suggests a design pattern: "Compute briefly, then crystallize." Use fragile computational elements, convert results immediately to robust storage.

---

## 4. The Unified Picture

### 4.1 The Four-Dimensional Space

Every structure in a discrete dynamical system can be characterized by its position in a 4D space:

```
(Computational, Self-Maintaining, Surviving, Visible)
```

Examples:
- Rule 110 glider: (1, 0, 0, 1) - computes, visible, but neither self-maintaining nor surviving
- Rule 90 bulk: (0, 1, 1, 1) - self-maintains, survives, visible, but doesn't compute
- Still life: (0, 0, 1, 1) - survives, visible, but neither computes nor self-maintains
- Anti-resonant oscillator: (0, 1, 1, 0) - self-maintains, survives, but NOT visible

### 4.2 The Hidden State Unifier

All four axes share a common enabler: **hidden state**.

- **Computation:** The 5th bit (Control) requires hidden state to enable conditional branching
- **Self-Maintenance:** Control (from hidden state) is the first criterion for life-like behavior
- **Survival:** Basins are created by hidden state dynamics (confirmation counters)
- **Visibility:** Anti-resonance requires oscillatory carrier (temporal hidden state)

**Synthesis Claim 1:** Hidden state is the universal enabler. Without hidden state, a system is memoryless, deterministic, and has zero Control. With hidden state, all four capabilities become possible (though not guaranteed).

### 4.3 The Basin Organizer

Three of the four axes are organized by basin of attraction:

- **Self-Maintenance:** Stability mechanisms create/exploit basins
- **Survival:** Basin strength IS the survival criterion
- **Visibility:** Anti-resonance occurs when carrier basin cycle aligns with sampling

**Synthesis Claim 2:** Basin of attraction is the organizing principle. The geometry of phase space—where basins exist, how deep they are, what their periods are—determines self-maintenance, survival, and visibility.

### 4.4 The Temporal Filter Diagnostic

Temporal filtering (stickiness) serves as a universal probe:

- **Paper 2:** Temporal filtering creates hidden state
- **Paper 4:** Temporal filtering reveals substrate capacity
- **Paper 5:** Temporal filtering selects for basin-possessing structures
- **Paper 6:** Temporal filtering reveals carrier-period relationships

**Synthesis Claim 3:** Temporal filtering is not just a mechanism but a diagnostic. By varying filter depth and observing outcomes, we reveal intrinsic properties of structures that are not visible in unfiltered dynamics.

---

## 5. Design Principles

The framework yields actionable design principles:

### Principle 1: Segregate Computation and Persistence
Since computation requires trajectories and persistence requires basins, do not expect the same structural element to provide both. Instead:
- Use fragile computational elements for logic
- Convert results immediately to robust storage
- "Compute briefly, then crystallize"

### Principle 2: Match Sampling to Carrier Period
To maximize information visibility:
- Identify carrier period P
- Sample at depths d ≢ 0 (mod P)
- Avoid synchronous sampling

### Principle 3: Build on Basins
To achieve self-maintenance and survival:
- Identify or create basin-possessing structures
- Recognize that basins are intrinsic (cannot be borrowed)
- Design for repair, not just stability

### Principle 4: Pre-Screen Substrates
Before attempting to engineer life-like behavior:
- Measure leakiness (phase transition at L ≈ 0.39)
- Measure capacity (compression < 1.1 bits/cell)
- Apply two-point calibration for optimal depth

---

## 6. The Framework Diagram

```
                    ┌─────────────────────────────────────────┐
                    │         SUBSTRATE PROPERTIES            │
                    │   Leakiness (L)      Capacity (C)       │
                    │   Paper 4            Paper 4            │
                    └────────────────┬────────────────────────┘
                                     │
                                     ▼
                    ┌─────────────────────────────────────────┐
                    │           HIDDEN STATE                  │
                    │   Stickiness mechanism (Paper 2)        │
                    │   Creates confirmation counters         │
                    │   Necessary for Control                 │
                    └────────────────┬────────────────────────┘
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           │                         │                         │
           ▼                         ▼                         ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   CONTROL        │    │   BASIN          │    │   PHASE          │
│   (Paper 2)      │    │   STRUCTURE      │    │   COHERENCE      │
│                  │    │   (Paper 5)      │    │   (Paper 6)      │
│ Context-dependent│    │ Attractor        │    │ Carrier period   │
│ divergence       │    │ geometry         │    │ alignment        │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         │              ┌────────┴────────┐              │
         │              │                 │              │
         ▼              ▼                 ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ COMPUTATION  │ │ SELF-MAINT   │ │  SURVIVAL    │ │  VISIBILITY  │
│ (Paper 1)    │ │ (Paper 3)    │ │  (Paper 5)   │ │  (Paper 6)   │
│              │ │              │ │              │ │              │
│ ≥5 bits +    │ │ Control +    │ │ Basin        │ │ d ≢ 0 (mod P)│
│ structure    │ │ Stability +  │ │ strength     │ │              │
│              │ │ Activity     │ │              │ │              │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
       │                │                │                │
       └────────────────┴────────────────┴────────────────┘
                                │
                    ┌───────────┴───────────┐
                    │   ORTHOGONAL AXES     │
                    │   Each independent    │
                    │   of the others       │
                    └───────────────────────┘
```

---

## 7. Summary

The six papers in this series establish:

1. **Paper 1 (UCT):** Universal computation requires ≥5 bits, with Control as the critical capability
2. **Paper 2 (Stickiness):** Hidden state is necessary and sufficient for Control
3. **Paper 3 (Self-Maintenance):** 83.7% of rules are life-like when hidden state is introduced
4. **Paper 4 (Leakiness):** Substrate properties predict life-like emergence with R² = 0.96
5. **Paper 5 (Invariants):** Basin strength determines survival under temporal filtering
6. **Paper 6 (Anti-Resonance):** Visibility depends on carrier-period alignment, orthogonal to survival

The synthesis framework unifies these findings:

- **Hidden state** is the universal enabler
- **Basin of attraction** is the organizing principle
- **Temporal filtering** is the diagnostic probe
- **Four orthogonal axes** (Computation, Self-Maintenance, Survival, Visibility) characterize structures

The fundamental insight: **Robustness is not one thing.** A structure's fate depends on which axis we query. Computation and persistence are in tension. Survival and visibility are independent. Understanding this orthogonality is essential for engineering robust dynamical systems.

---

*Framework version 1.0*
*Status: Ready for stress testing*
