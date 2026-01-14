# References

## Primary Sources (Papers 1-6)

### Paper 1: Universal Computation Threshold (UCT)
**Full Title:** The Five-Bit Threshold for Universal Computation
**Repository:** `../1. UCT/`
**Key Contribution:** Proves minimum complexity for universal computation is 5 bits

**Key Results:**
- Capability decomposition: Logic (2) + Memory (1) + Control (1) + State (1) = 5 bits
- Rule 110 achieves threshold with exactly 5 bits
- Structural conditions required beyond bit threshold

---

### Paper 2: Stickiness and Hidden State
**Full Title:** Stickiness as the Mechanism of Control
**Repository:** `../2. Stickiness/`
**Key Contribution:** Proves hidden state is necessary and sufficient for Control

**Key Results:**
- Stickiness mechanism definition (confirmation counters)
- 168/168 non-trivial rules gain Control under stickiness
- Three conditions for effective hidden state (C1, C2, C3)

---

### Paper 3: Self-Maintenance Census
**Full Title:** Self-Maintenance in Elementary Cellular Automata
**Repository:** `../3. Self-Maintenance/`
**Key Contribution:** 83.7% of ECA rules are life-like under stickiness

**Key Results:**
- Life-like criteria: Control + Stability + Activity
- 168/194 non-trivial rules classified as life-like
- Rule 110 (universal) is NOT life-like

---

### Paper 4: Leakiness and Capacity
**Full Title:** Substrate Leakiness as Predictor of Life-Like Emergence
**Repository:** `../4. Leakiness/`
**Key Contribution:** Two-axis predictive framework with R² = 0.96

**Key Results:**
- Leakiness threshold: L ≈ 0.39 (phase transition)
- Capacity threshold: ~1.1 bits/cell
- Two-point calibration protocol

---

### Paper 5: Invariants Under Temporal Filtering
**Full Title:** Structural Invariants Under Temporal Filtering
**Repository:** `../5. Invariants/`
**Key Contribution:** Basin criterion for survival (98% accuracy)

**Key Results:**
- "What survives is not what computes, but what repairs"
- Intrinsicality theorem: basins are non-transferable
- Computation-robustness tradeoff

---

### Paper 6: Anti-Resonance
**Full Title:** Anti-Resonance in Temporally Filtered Cellular Automata
**Repository:** `../6. Anti-Resonance/`
**Key Contribution:** Carrier-period modulation of visibility

**Key Results:**
- Anti-resonance at d ≡ 0 (mod P)
- 2.6× effect size on Hamming ratio
- Survival ⊥ Visibility orthogonality

---

## Classical References

### Computation Theory
1. Turing, A.M. (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*.
2. Post, E. (1941). "The Two-Valued Iterative Systems of Mathematical Logic." *Annals of Mathematics Studies*.
3. Minsky, M. (1967). *Computation: Finite and Infinite Machines*. Prentice-Hall.
4. Böhm, C. & Jacopini, G. (1966). "Flow Diagrams, Turing Machines and Languages with Only Two Formation Rules." *Communications of the ACM*.

### Cellular Automata
5. Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.
6. Cook, M. (2004). "Universality in Elementary Cellular Automata." *Complex Systems*.

### Dynamical Systems
7. Strogatz, S. (1994). *Nonlinear Dynamics and Chaos*. Addison-Wesley.
8. Kauffman, S. (1993). *The Origins of Order*. Oxford University Press.

### Origins of Life
9. Schrödinger, E. (1944). *What Is Life?*. Cambridge University Press.
10. Waddington, C.H. (1957). *The Strategy of the Genes*. Allen & Unwin.

---

## Repository Links

| Paper | Short Name | Key Figure |
|-------|-----------|------------|
| 1 | UCT | Capability decomposition |
| 2 | Stickiness | Hidden state mechanism |
| 3 | Self-Maintenance | Life-like census |
| 4 | Leakiness | Two-axis prediction |
| 5 | Invariants | Basin classification |
| 6 | Anti-Resonance | Visibility modulation |
| **7** | **Synthesis** | **Orthogonal framework** |

---

## Citation

```bibtex
@article{orthogonal_robustness_2026,
  title={The Orthogonal Robustness Framework: A Unified Theory of Structure,
         Survival, and Visibility in Discrete Dynamical Systems},
  author={Bit Dynamics Lab},
  year={2026},
  note={Synthesis of Papers 1-6}
}
```

---

*References compiled: 2026-01-14*
