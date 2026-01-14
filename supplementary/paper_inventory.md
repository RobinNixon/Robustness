# Paper Inventory: Six Papers on Discrete Dynamical Systems

## Overview

This inventory extracts the core claims, key metrics, and central insights from each paper in the series. The goal is to identify the unifying structure for Paper 7 (Synthesis).

---

## Paper 1: The Five-Bit Threshold for Universal Computation (UCT)

**Core Claim:** Every universal computational system requires at least 5 bits of descriptive complexity under natural encodings.

**Key Metric:** Specification complexity K_spec (bits)

**Capability Decomposition:**
- Logic: ≥2 bits (NAND/NOR specification)
- Memory: ≥1 bit (read/write distinction)
- Control: ≥1 bit (branch/continue distinction)
- State: ≥1 bit (computing/halted distinction)
- **Total: 5 bits minimum**

**Control Conjecture:** The 5th bit enables Control - context-dependent divergence in interaction outcome. At 4 bits, collision outcomes are uniform; at 5 bits, they become conditional.

**Secondary Finding:** Self-Organization Threshold (SOT) at ~3 bits - systems can organize but cannot compute.

**Tightness:** Tag(2,2), SK calculus, Rule 110 all achieve exactly 5 bits.

**Optimality:** 5 bits is optimal (inverted U-curve - more bits degrade capability).

---

## Paper 2: Hidden State as the Mechanism of Control (Stickiness)

**Core Claim:** Hidden state is necessary for Control, and sufficient when satisfying three conditions: causal influence (C1), overwriteability (C2), and dynamic reachability (C3).

**Key Metric:** Control = context-dependent divergence (same visible state, different hidden states → different outputs)

**Key Theorems:**
1. **Necessity:** Control = 0 in memoryless systems (all standard ECAs have zero Control)
2. **Sufficiency:** Hidden state enables Control iff C1 ∧ C2 ∧ C3
3. **Universality:** 168/168 non-trivial ECA rules gain Control > 0 under stickiness

**Stickiness Mechanisms:**
- **Confirmation:** Changes require d consecutive requests before executing
- **Refractory:** Cooldown period after changes

**Connection to UCT:** "The 4-bit to 5-bit transition corresponds to acquiring hidden state. The 5th bit IS the hidden state."

**Causal Chain:** Stickiness → Hidden State → Context-Dependence → Control

**Spatial Structure:** Control concentrates at boundaries (r = 0.73 correlation)

---

## Paper 3: Self-Maintenance as Default Outcome

**Core Claim:** 83.7% of non-trivial ECA rules exhibit life-like behavior when hidden state is introduced through stickiness. Self-maintenance is the default, not the exception.

**Key Metric:** Life-like classification (jointly necessary and sufficient):
1. Control > 0 (hidden state influences output)
2. Absorption > 0.5 OR Repair > 0.7 (stability mechanism)
3. 0.05 ≤ Activity ≤ 0.5 (Goldilocks dynamics)

**Causal Chain:** Stickiness → Hidden State → Control → [Stability Substrate] → Life-Like

**Census:**
| Classification | Count | % Non-Trivial |
|---------------|-------|---------------|
| LIFE-LIKE | 159 | 83.7% |
| COMPUTING | 28 | 14.7% |
| CRYSTALLIZED | 3 | 1.6% |
| TRIVIAL | 66 | — |

**Key Orthogonalities:**
- Life-like ≠ Computation (Rule 110 is TC but NOT life-like)
- Life-like ≠ Chaos (Rule 30 is chaotic but NOT life-like)
- Life-like ≠ Stability (overdamped rules crystallize)

---

## Paper 4: Substrate Leakiness Predicts Life-Like Behavior

**Core Claim:** A two-axis framework (Leakiness × Capacity) predicts whether a substrate can exhibit life-like behavior, with R² = 0.96.

**Key Metrics:**

**Axis 1 - Leakiness:** How readily perturbations escape and amplify
- L = 0.33·Lyapunov + 0.29·Escape + 0.28·Branching + 0.10·Channels
- Phase transition at L ≈ 0.39

**Axis 2 - Capacity:** Whether substrate has sufficient structural complexity
- Measured via compression ratio (bits/cell)
- Threshold: < 1.1 bits/cell → PRONE; ≥ 1.1 → RESISTANT

**Stickiness Mechanism:** Works as temporal low-pass filter (not spatial selective damping)
- Acceptance ratio ≈ 1/d
- Blocks transient fluctuations (noise), passes sustained pressure (signal)

**Control Law:**
- d* = ((L₀ - L_min) / (L_crit - L_min))^(1/γ)
- Two-point calibration achieves r = 0.996

**Classification:**
- **Prone:** Rules 110, 54, 2D CA (compress to 0.51-0.95 bits/cell)
- **Resistant:** Rules 30, 90, 150 (hit 1.33 bits/cell, near-random)

**Key Insight:** Inverts "edge of chaos" - prone substrates are MORE structured (lower entropy), not intermediate complexity.

---

## Paper 5: Temporal Invariants (Basin of Attraction as Survival Criterion)

**Core Claim:** Basin of attraction strength is the sole criterion for structural survival under temporal filtering. "What survives is not what computes, but what repairs."

**Key Metric:** Basin type (none/point/cycle/large)

**Basin Criterion:**
| Structure Type | Basin Type | Survival |
|---------------|------------|----------|
| Chaos | Entire space | HIGH (trivially) |
| Amplifying | Large | HIGH |
| Still life | Point | HIGH |
| Oscillator | Cycle | HIGH |
| Glider | None | LOW |

**Intrinsicality Theorem:** Basins are intrinsic and non-transferable. A structure with a basin cannot export stability to a nearby structure without a basin.

**Computation-Robustness Tradeoff:** "Structures that compute tend not to survive, and structures that survive tend not to compute."
- Gliders compute but cannot repair
- Oscillators repair but cannot compute

**Information Types:**
- Discrete state (phase) → robust (can re-lock to attractor)
- Continuous state (position) → fragile (diffuses under perturbation)

**Model Accuracy:** ~98% across all tested substrates

---

## Paper 6: Carrier-Period Anti-Resonance

**Core Claim:** Information distinguishability is minimized at depths d ≡ 0 (mod P) for carriers of period P - "carrier-period anti-resonance."

**Key Metric:** Phase-normalized distinguishability D = Σᵢ |R₀(i) - R₁(i)|

**Mechanism:**
- At d ≡ 0 (mod P): Carrier returns to original phase, defect absorbed, low visibility
- At d ≢ 0 (mod P): Carrier in different phase, defect creates visible contrast

**Evidence:**
| Carrier Period | Worst Depth | Best Depth | Effect Size |
|---------------|-------------|------------|-------------|
| P = 2 | d ≡ 0 (mod 2) | d ≡ 1 (mod 2) | ~2.6× Hamming ratio |
| P = 4 | d ≡ 0 (mod 4) | d ≡ 2 (mod 4) | -3.2 distinguishability |

**Negative Control:** Rule 110 (quiescent background) shows no anti-resonance - effect requires oscillatory carrier.

**Key Insight:** Survival (Paper 5) and Visibility (Paper 6) are orthogonal axes:
- A structure may survive (basin dynamics) while being hard to read (anti-resonance)
- Synchrony with oscillations SUPPRESSES information visibility (counterintuitive)

---

## Summary Table

| Paper | Core Question | Key Metric | Central Finding |
|-------|--------------|------------|-----------------|
| 1 (UCT) | Minimum for computation? | Specification complexity | 5 bits (Control is the 5th) |
| 2 (Stickiness) | How does Control arise? | Control (context-dependence) | Hidden state is necessary and sufficient |
| 3 (Self-Maint) | When is life-like default? | Life-like classification | 83.7% of non-trivial rules |
| 4 (Leakiness) | Can we predict life-like? | Leakiness + Capacity | Two-axis framework, R² = 0.96 |
| 5 (Invariants) | What survives filtering? | Basin strength | Basin = survival criterion |
| 6 (Anti-Res) | When is info least readable? | Distinguishability | d ≡ 0 (mod P) = minimum visibility |

---

## Emerging Structure

### Orthogonal Axes Identified:
1. **Computational Capability** (Paper 1): ≥5 bits for universality
2. **Control** (Paper 2): Hidden state enables context-dependence
3. **Life-Like Behavior** (Papers 3-4): Control + Stability + Activity
4. **Survival** (Paper 5): Basin of attraction strength
5. **Visibility** (Paper 6): Carrier-period alignment

### Key Orthogonalities:
- Computation ⊥ Self-Maintenance (Rule 110 vs Rule 90)
- Survival ⊥ Visibility (can survive but be unreadable)
- Chaos ⊥ Life-Like (Rule 30 is neither computational nor life-like)

### Hierarchical Structure:
```
Level 0: Substrate Properties
  └── Leakiness (perturbation spread)
  └── Capacity (structural complexity)

Level 1: Emergent Capabilities
  └── Hidden State → Control (Paper 2)
  └── Basin Structure → Survival (Paper 5)
  └── Carrier Period → Visibility (Paper 6)

Level 2: Behavioral Outcomes
  └── Computation (≥5 bits + structure)
  └── Life-Like (Control + Stability + Activity)

Level 3: Information Properties
  └── Survives vs Dies (basin criterion)
  └── Readable vs Hidden (anti-resonance)
```

---

*Inventory completed: 2026-01-14*
*Next: Map relationships and construct synthesis framework*
