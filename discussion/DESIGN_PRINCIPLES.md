# Design Principles

The Orthogonal Robustness Framework yields actionable engineering principles for designing robust dynamical systems.

---

## Principle 1: Segregate Computation and Persistence

### The Problem
Computation requires trajectories through state space (signals, collisions, transformations). Persistence requires basins that attract and stabilize. These are structurally incompatible for the same element.

### The Solution
Temporal segregation: "Compute briefly, then crystallize."

### Implementation
1. **Use fragile computational elements** for logic operations
2. **Convert results immediately** to robust storage structures
3. **Accept alternation:** compute → store → compute → store

### Examples

**Distributed Systems:**
- Computation happens in stateless workers (fragile, replaceable)
- Results persist in replicated databases (basin-like, self-repairing)
- This is standard practice—the framework explains *why* it works

**Biological Systems:**
- Neural firing (fragile computation)
- Synaptic weights (persistent storage)
- Gene expression (computation) vs. DNA sequence (persistence)

### Anti-Pattern
Expecting the same element to compute AND persist:
- "Self-healing computation" is an oxymoron at the structural level
- Consensus protocols are hard precisely because they try to compute with persistent state

**Source:** Paper 5 (Section 6.2)

---

## Principle 2: Match Sampling to Carrier Period

### The Problem
When monitoring oscillatory systems, sampling at multiples of the carrier period causes anti-resonance—information is hidden.

### The Solution
Sample at depths d ≢ 0 (mod P) where P is the carrier period.

### Implementation
1. **Identify carrier period P** of the oscillatory background
2. **Choose sampling interval** to avoid d ≡ 0 (mod P)
3. **Prefer asynchronous sampling** when period is unknown

### Examples

**Biological Monitoring:**
- Circadian rhythms have P ≈ 24 hours
- Sampling exactly every 24 hours may miss phase-dependent information
- Use irregular intervals: 23h, 25h, 17h

**Communication Systems:**
- Carrier frequency defines P
- Demodulation requires phase offset
- Synchronous sampling loses signal

**Industrial Monitoring:**
- Rotating machinery has characteristic frequencies
- Sampling at rotation frequency masks vibration signatures
- Use non-harmonic sampling rates

### Quantitative Guidance
Paper 6 shows ~2.6× difference in information visibility between optimal and anti-resonant sampling.

**Source:** Paper 6 (Section 5)

---

## Principle 3: Build on Basins

### The Problem
Structures without basins are destroyed by temporal filtering. You cannot borrow stability from neighbors.

### The Solution
Design for basin-possessing structures. Basins are intrinsic and non-transferable.

### Implementation
1. **Identify basin-possessing structures** in your substrate
2. **Design around attractors:** fixed points, limit cycles
3. **Build repair mechanisms** that actively return to attractors
4. **Accept intrinsicality:** each component must have its own basin

### Examples

**Fault-Tolerant Systems:**
- State machines with explicit "home" states (fixed point basins)
- Watchdog timers that reset to safe state (basin return)
- Redundancy that restores consensus (repair mechanism)

**Self-Healing Materials:**
- Polymers with shape memory (basin = original shape)
- Self-healing concrete with bacteria (repair mechanism)
- The material must have intrinsic basin; external repair is not self-healing

**Error Correction:**
- Hamming codes have basins (valid codewords)
- Errors push state out of codeword space
- Correction returns to nearest valid codeword (basin)

### Anti-Pattern
Relying on neighbors for stability:
- A fragile component near a robust component remains fragile
- "Failure isolation" works because basins don't transfer
- Don't expect cascade effects to provide stability

**Source:** Paper 5 (Section 4)

---

## Principle 4: Pre-Screen Substrates

### The Problem
Not all substrates can support life-like behavior. Attempting to engineer self-maintenance in an unsuitable substrate wastes effort.

### The Solution
Measure substrate properties before engineering.

### Implementation

**Step 1: Measure Leakiness (L)**
- Run perturbation experiments
- Measure divergence rate
- Phase transition at L ≈ 0.39

| Leakiness | Classification |
|-----------|---------------|
| L < 0.39 | "Prone" — likely to support life-like behavior |
| L > 0.39 | "Resistant" — unlikely without major intervention |

**Step 2: Measure Capacity (C)**
- Compute compression ratio of typical states
- Threshold at ~1.1 bits/cell

| Capacity | Classification |
|----------|---------------|
| C > 1.1 bits/cell | Has structure to exploit |
| C < 1.1 bits/cell | Insufficient structure |

**Step 3: Two-Point Calibration**
If prone + sufficient capacity:
- Test stickiness at d=2 and d=4
- Interpolate optimal confirmation depth
- Apply calibrated stickiness

### Examples

**Synthetic Biology:**
- Test chemical substrate leakiness before designing self-maintaining circuits
- Low leakiness = promising platform
- High leakiness = need stability mechanisms first

**Artificial Life:**
- Screen computational substrates before building agents
- Some substrates cannot support life-like behavior at any parameter
- Save effort by pre-screening

### Quantitative Prediction
The two-axis model (Leakiness × Capacity) achieves R² = 0.96 prediction accuracy for life-like emergence.

**Source:** Paper 4 (Section 4)

---

## Summary Table

| Principle | Problem | Solution | Key Metric |
|-----------|---------|----------|------------|
| Segregate | Computation ⊥ Persistence | Temporal alternation | — |
| Match Sampling | Anti-resonance hides info | d ≢ 0 (mod P) | 2.6× visibility |
| Build on Basins | Basins are intrinsic | Design for attractors | 98% survival |
| Pre-Screen | Not all substrates work | Measure L, C | R² = 0.96 |

---

## Application Domains

### 1. Distributed Systems
- Segregate computation (workers) from persistence (databases)
- Use basin-like consensus mechanisms
- Pre-screen protocols for robustness potential

### 2. Synthetic Biology
- Design life-like circuits with Control + Stability + Activity
- Pre-screen chemical substrates for leakiness
- Use basin-possessing motifs (oscillators, bistable switches)

### 3. Robotics
- Segregate sensing/computation from actuator persistence
- Match sensor sampling to environmental frequencies
- Build mechanical basins (stable postures)

### 4. Financial Systems
- Recognize that "self-healing markets" face Computation ⊥ Persistence tension
- Sample market oscillations at non-harmonic intervals
- Design circuit breakers as basin-return mechanisms

---

*Provenance: Principles derived from Papers 4-6, with examples adapted from discussion sections of each paper.*
