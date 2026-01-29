# The Orthogonal Robustness Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Abstract

We present a unified framework for understanding robustness in discrete dynamical systems, synthesizing findings from six independent studies. The central thesis is that robustness is not a single property but manifests along four orthogonal axes: Computational Capability (can it compute?), Self-Maintenance (does it actively persist?), Survival (does it withstand temporal filtering?), and Visibility (is the information readable?). These axes are demonstrably independent—a structure's position on one axis provides no information about its position on another.

This orthogonality explains apparent paradoxes (e.g., why Rule 110 is Turing-complete but not life-like) and yields actionable design principles for engineering robust dynamical systems. We identify hidden state as the universal enabler across all four axes and basin of attraction as the organizing principle that determines survival, stability, and visibility.

**For a general-audience introduction, see [Why Complexity Is Rare](ESSAY.md)** — an essay explaining what we learned from the simplest possible worlds.

## Key Result

**Theorem (Orthogonal Robustness):** Discrete dynamical systems exhibit four independent axes of robustness:

| Axis | Question | Criterion | Source |
|------|----------|-----------|--------|
| **Computation** | Can it compute? | ≥5 bits + structure | Paper 1 |
| **Self-Maintenance** | Does it actively persist? | Control + Stability + Activity | Papers 2-4 |
| **Survival** | Does it withstand filtering? | Basin strength | Paper 5 |
| **Visibility** | Is information readable? | d ≢ 0 (mod P) | Paper 6 |

**Three Synthesis Claims:**
1. **Hidden state** is the universal enabler across all four axes
2. **Basin of attraction** is the organizing principle for self-maintenance, survival, and visibility
3. **Temporal filtering** is a diagnostic probe that reveals intrinsic structure properties

**Fundamental Insight:** *"Structures that compute tend not to survive, and structures that survive tend not to compute."* Resolution: **Compute briefly, then crystallize.**

## Repository Structure

```
Synthesis/
├── paper/
│   ├── bit_dynamics_framework.md      # Full paper (Markdown)
│   └── bit_dynamics_framework.tex     # Full paper (LaTeX)
├── figures/
│   ├── fig1_framework_overview.png    # Hierarchical framework structure
│   ├── fig2_orthogonality_matrix.png  # 2×2 orthogonality evidence
│   ├── fig3_hidden_state_cascade.png  # Hidden state as enabler
│   ├── fig4_paper_connections.png     # Paper dependency graph
│   └── fig5_four_axis_space.png       # 4D characterization examples
├── theory/
│   ├── INDEX.md                       # Theory file index
│   ├── FOUR_AXES.md                   # Definition of the four axes
│   ├── ORTHOGONALITY_PROOFS.md        # Evidence for independence
│   ├── HIDDEN_STATE_UNIFIER.md        # Hidden state as universal enabler
│   └── BASIN_ORGANIZER.md             # Basin of attraction framework
├── discussion/
│   ├── INDEX.md                       # Discussion file index
│   ├── DESIGN_PRINCIPLES.md           # Engineering applications
│   ├── BIOLOGICAL_IMPLICATIONS.md     # Predictions for living systems
│   ├── FUTURE_WORK.md                 # Open problems
│   └── FAQ.md                         # Anticipated objections
├── supplementary/
│   ├── paper_inventory.md             # Extracted claims from Papers 1-6
│   ├── relationship_map.md            # Cross-paper connections
│   └── reviewer_attacks.md            # Detailed defense preparation
├── code/
│   └── generate_figures.py            # Figure generation script
├── data/
│   ├── PROVENANCE.md                  # Source attribution for all materials
│   └── REFERENCES.md                  # Links to Papers 1-6
├── LICENSE
├── bit_dynamics_framework.pdf         # Compiled paper
├── ESSAY.md                           # General-audience introduction
└── README.md                          # This file
```

## Quick Start

### Requirements
- Python 3.10+
- NumPy, Matplotlib

### Generate Figures
```bash
cd code
python generate_figures.py
```

### Build Paper (LaTeX)
```bash
cd paper
pdflatex bit_dynamics_framework.tex
pdflatex bit_dynamics_framework.tex  # Second pass for references
```

## The Four Axes

### Axis 1: Computational Capability (Paper 1)
- **Question:** Can the system perform universal computation?
- **Criterion:** Specification complexity ≥5 bits under natural encoding, plus structural conditions
- **Key finding:** The 5th bit is Control—context-dependent divergence requiring hidden state

### Axis 2: Self-Maintenance (Papers 2-4)
- **Question:** Does the system exhibit life-like behavior?
- **Criterion:** Control > 0 AND Stability mechanism AND Activity within window
- **Key finding:** 83.7% of non-trivial ECA rules are life-like under stickiness; predictable from substrate properties (R² = 0.96)

### Axis 3: Survival (Paper 5)
- **Question:** Does the structure persist under temporal filtering?
- **Criterion:** Basin of attraction strength
- **Key finding:** "What survives is not what computes, but what repairs." Basin classification predicts survival with 98% accuracy.

### Axis 4: Visibility (Paper 6)
- **Question:** Is encoded information distinguishable?
- **Criterion:** Sampling depth d relative to carrier period P
- **Key finding:** Anti-resonance at d ≡ 0 (mod P) hides information; ~2.6× effect size

## Orthogonality Evidence

| Orthogonality | Evidence |
|---------------|----------|
| Computation ⊥ Self-Maintenance | Rule 110: computes, NOT life-like. Rule 90: life-like, NOT universal. |
| Survival ⊥ Visibility | Oscillator at d ≡ 0: survives but hidden. Glider at d ≢ 0: visible but destroyed. |
| Computation ⊥ Survival | Gliders: compute, fragile. Still lifes: survive, do not compute. |

## Design Principles

1. **Segregate Computation and Persistence** — Use fragile elements for logic; convert results immediately to robust storage. "Compute briefly, then crystallize."

2. **Match Sampling to Carrier Period** — Sample at d ≢ 0 (mod P) to maximize visibility. Avoid synchronous sampling.

3. **Build on Basins** — Design for basin-possessing structures. Basins are intrinsic and non-transferable.

4. **Pre-Screen Substrates** — Measure leakiness (phase transition at L ≈ 0.39) and capacity (threshold ~1.1 bits/cell) before engineering life-like behavior.

## Research Series

This paper is part of a seven-paper research series exploring computation, self-organization, and robustness in discrete dynamical systems.

| # | Paper | Repository | Key Contribution |
|---|-------|------------|------------------|
| 1 | The Five-Bit Threshold | [UCT](https://github.com/RobinNixon/UCT) | Minimum complexity for universal computation |
| 2 | Stickiness and Control | [Stickiness](https://github.com/RobinNixon/Stickiness) | Hidden state as mechanism for Control |
| 3 | Self-Maintenance | [Self-Maintenance](https://github.com/RobinNixon/Self-Maintenance) | 83.7% of ECA rules are life-like under stickiness |
| 4 | Substrate Leakiness | [Leakiness](https://github.com/RobinNixon/Leakiness) | Two-axis predictive framework (R² = 0.96) |
| 5 | Structural Invariants | [Invariants](https://github.com/RobinNixon/Invariants) | Basin criterion for survival under filtering |
| 6 | Anti-Resonance | [Anti-Resonance](https://github.com/RobinNixon/Anti-Resonance) | Carrier-period modulation of visibility |
| **7** | **Orthogonal Robustness** | **[Robustness](https://github.com/RobinNixon/Robustness)** | Unified framework: four independent axes |

## Citation

```bibtex
@article{orthogonal_robustness_2026,
  title={The Orthogonal Robustness Framework: A Unified Theory of Structure, Survival, and Visibility in Discrete Dynamical Systems},
  author={Bit Dynamics Lab},
  year={2026},
  note={Synthesis of Papers 1-6}
}
```

## License

MIT License - See [LICENSE](LICENSE) for details.

## Contributing

We welcome contributions, particularly:
- Tests of the framework in continuous dynamical systems
- Formal proofs of axis independence
- Applications to biological or engineered systems
- Identification of additional orthogonal axes

Please open an issue or submit a pull request.
