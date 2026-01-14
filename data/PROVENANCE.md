# Provenance and Attribution

This document tracks the source of all materials in the Paper 7 (Synthesis) repository.

---

## Principle

Paper 7 is a synthesis paper. It does not introduce new experiments or simulations. All empirical claims are inherited from Papers 1-6. This document provides clear attribution for all reused material.

---

## Paper Sources

### Paper 1: Universal Computation Threshold (UCT)
**Repository:** `../1. UCT/`

**Materials used:**
- Five-bit threshold theorem (Section 3)
- Capability decomposition (Logic, Memory, Control, State)
- Rule 110 universality analysis
- Structural conditions for universality

**Specific citations:**
- Table of capability bit requirements → theory/FOUR_AXES.md
- Rule 110 as 5-bit example → theory/ORTHOGONALITY_PROOFS.md

---

### Paper 2: Stickiness and Hidden State
**Repository:** `../2. Stickiness/`

**Materials used:**
- Stickiness mechanism definition
- Hidden state necessity proof (Theorem 1)
- Control definition (context-dependent divergence)
- Three conditions for effective hidden state (C1, C2, C3)

**Specific citations:**
- Stickiness mechanism → theory/HIDDEN_STATE_UNIFIER.md
- 168/168 universality result → paper/synthesis.md Section 4.1

---

### Paper 3: Self-Maintenance Census
**Repository:** `../3. Self-Maintenance/`

**Materials used:**
- Life-like criteria (Control + Stability + Activity)
- 83.7% classification result
- Rule 90 vs Rule 110 comparison
- Absorption and repair thresholds

**Specific citations:**
- Census percentages → theory/FOUR_AXES.md, Axis 2
- Orthogonality evidence → theory/ORTHOGONALITY_PROOFS.md

---

### Paper 4: Leakiness and Capacity
**Repository:** `../4. Leakiness/`

**Materials used:**
- Two-axis predictive framework
- Leakiness definition and threshold (L ≈ 0.39)
- Capacity definition and threshold (~1.1 bits/cell)
- R² = 0.96 prediction accuracy

**Specific citations:**
- Predictive model → theory/FOUR_AXES.md, Axis 2
- Design Principle 4 → discussion/DESIGN_PRINCIPLES.md

---

### Paper 5: Invariants Under Temporal Filtering
**Repository:** `../5. Invariants/`

**Materials used:**
- Basin criterion for survival
- Intrinsicality theorem
- Computation-robustness tradeoff
- "What survives is not what computes, but what repairs"
- 98% prediction accuracy

**Specific citations:**
- Survival classification → theory/FOUR_AXES.md, Axis 3
- Basin criterion → theory/BASIN_ORGANIZER.md
- Design Principle 1 → discussion/DESIGN_PRINCIPLES.md

---

### Paper 6: Anti-Resonance
**Repository:** `../6. Anti-Resonance/`

**Materials used:**
- Anti-resonance effect definition
- Visibility criterion (d ≢ 0 mod P)
- 2.6× effect size
- Survival ⊥ Visibility orthogonality

**Specific citations:**
- Visibility axis → theory/FOUR_AXES.md, Axis 4
- Orthogonality evidence → theory/ORTHOGONALITY_PROOFS.md
- Design Principle 2 → discussion/DESIGN_PRINCIPLES.md

---

## Original Materials

The following materials are original to Paper 7:

### Synthesis Framework
- Orthogonal Robustness Framework (name and structure)
- Three Synthesis Claims
- Four-axis characterization
- Design principles derived from cross-paper analysis

**Location:** paper/synthesis.md, theory/*.md

### Figures
All figures are conceptual/summarizing, not empirical:
- fig1_framework_overview.png — Original diagram
- fig2_orthogonality_matrix.png — Compiled from Papers 1, 3, 5, 6
- fig3_hidden_state_cascade.png — Synthesis visualization
- fig4_paper_connections.png — Original dependency diagram
- fig5_four_axis_space.png — Examples from Papers 1, 3, 5, 6

**Location:** figures/, code/generate_figures.py

### Discussion Materials
- Design principles — Derived from synthesis analysis
- Biological implications — Predictions from framework
- Future work — Open problems identified
- FAQ — Anticipated objections addressed

**Location:** discussion/*.md

---

## Verification

To verify any claim in this paper:
1. Identify the source paper from this provenance document
2. Navigate to the cited section in the source paper
3. Compare the claim with the original finding

All numerical results (83.7%, R² = 0.96, 2.6×, etc.) are taken directly from the source papers without modification.

---

## License

All materials are under MIT License, consistent with Papers 1-6.

---

*Provenance document created: 2026-01-14*
