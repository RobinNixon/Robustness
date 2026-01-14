# Relationship Map: Connecting the Six Papers

## 1. Sequential Dependencies

```
Paper 1 (UCT)
    │
    │ "The 5th bit IS the hidden state"
    ▼
Paper 2 (Stickiness)
    │
    │ "Stickiness → Hidden State → Control"
    ▼
Paper 3 (Self-Maintenance)
    │
    │ "Life-like = Control + Stability + Activity"
    ▼
Paper 4 (Leakiness)
    │
    │ "Predict life-like from substrate properties"
    ▼
Paper 5 (Invariants)
    │
    │ "Basin strength determines survival"
    ▼
Paper 6 (Anti-Resonance)
    │
    │ "Visibility orthogonal to survival"
    ▼
Paper 7 (Synthesis)
```

## 2. Explicit Cross-References

| From | To | Connection |
|------|-----|------------|
| Paper 2 | Paper 1 | "The Control bit in UCT can be physically realized by hidden state" |
| Paper 3 | Paper 2 | Uses stickiness mechanism to achieve life-like behavior |
| Paper 4 | Papers 2-3 | Provides predictive metrics for stickiness outcomes |
| Paper 5 | Papers 2-4 | Uses temporal filtering as probe, explains WHY stickiness works |
| Paper 6 | Paper 5 | Shows visibility is orthogonal to survival |

## 3. Conceptual Layers

### Layer 0: Substrate Properties (Paper 4)
```
┌─────────────────────────────────────────────────┐
│  SUBSTRATE LAYER                                │
│                                                 │
│  Leakiness (L)          Capacity (C)            │
│  • Lyapunov rate        • Compression ratio     │
│  • Escape dimensions    • bits/cell             │
│  • Branching factor     • Threshold: 1.1        │
│  • Phase transition     │                       │
│    at L ≈ 0.39          │                       │
│                         │                       │
│  HIGH L → resistant     LOW C → resistant       │
│  LOW L → prone          HIGH C → prone          │
└─────────────────────────────────────────────────┘
```

### Layer 1: Mechanism Layer (Papers 2, 5)
```
┌─────────────────────────────────────────────────┐
│  MECHANISM LAYER                                │
│                                                 │
│  Hidden State (Paper 2)    Basin Structure (5)  │
│  • Confirmation counter    • Point (still life) │
│  • Refractory period       • Cycle (oscillator) │
│  • Enables Control         • Large (amplifying) │
│                            • None (glider)      │
│                                                 │
│  Temporal Filtering:                            │
│  • 1/d acceptance          • Selects for basins │
│  • Low-pass filter         • Intrinsic property │
└─────────────────────────────────────────────────┘
```

### Layer 2: Capability Layer (Papers 1, 2, 3)
```
┌─────────────────────────────────────────────────┐
│  CAPABILITY LAYER                               │
│                                                 │
│  Computation (Paper 1)     Life-Like (Paper 3)  │
│  • ≥5 bits required        • Control > 0        │
│  • Logic + Memory +        • Stability mech.    │
│    Control + State         • Activity window    │
│  • Structural conditions   • 83.7% of non-triv  │
│                                                 │
│  ═══════════════════════════════════════════    │
│         THESE ARE ORTHOGONAL                    │
│  Rule 110: Computes, NOT life-like              │
│  Rule 90: Life-like, NOT universal              │
└─────────────────────────────────────────────────┘
```

### Layer 3: Outcome Layer (Papers 5, 6)
```
┌─────────────────────────────────────────────────┐
│  OUTCOME LAYER                                  │
│                                                 │
│  Survival (Paper 5)        Visibility (Paper 6) │
│  • Basin strength          • Phase alignment    │
│  • Intrinsic property      • d mod P            │
│  • ~98% predictive         • Anti-resonance     │
│                                                 │
│  ═══════════════════════════════════════════    │
│         THESE ARE ORTHOGONAL                    │
│  Structure can survive but be unreadable        │
│  Structure can be visible but not survive       │
└─────────────────────────────────────────────────┘
```

## 4. Key Orthogonalities

### Orthogonality 1: Computation × Self-Maintenance
```
                    COMPUTES
                       │
           YES         │         NO
            ┌──────────┼──────────┐
            │          │          │
       YES  │ Rule 110 │  Rule 90 │ LIFE-LIKE
            │ (rare)   │ (common) │
            │──────────┼──────────│
       NO   │ Rule 30  │  Rule 0  │
            │ (chaos)  │ (trivial)│
            └──────────┴──────────┘

Paper 1 addresses: Which systems can compute?
Paper 3 addresses: Which systems self-maintain?
Answer: These are independent questions.
```

### Orthogonality 2: Survival × Visibility
```
                    SURVIVES
                       │
           YES         │         NO
            ┌──────────┼──────────┐
            │ HIGH     │   N/A    │
       YES  │ basin +  │  (can't  │ VISIBLE
            │ off-period│ see dead)│
            │──────────┼──────────│
       NO   │ HIGH     │  LOW     │
            │ basin +  │  basin   │
            │ on-period│          │
            └──────────┴──────────┘

Paper 5 addresses: What survives temporal filtering?
Paper 6 addresses: When is information readable?
Answer: These are independent questions.
```

### Orthogonality 3: Control × Stability
```
                    HAS CONTROL
                       │
           YES         │         NO
            ┌──────────┼──────────┐
            │ LIFE-    │ CRYSTAL- │
       YES  │ LIKE     │ LIZED    │ STABLE
            │ (83.7%)  │ (3 rules)│
            │──────────┼──────────│
       NO   │ COMPUTING│ CHAOS/   │
            │ (14.7%)  │ TRIVIAL  │
            └──────────┴──────────┘

Paper 2 addresses: How does Control arise?
Paper 3 addresses: When does stability + control = life-like?
```

## 5. Causal Chains

### Chain 1: From Substrate to Computation
```
Substrate Properties (Paper 4)
    │
    ├── Leakiness < 0.39 ───┐
    │                        │
    └── Capacity > threshold─┴──► Hidden State Possible
                                        │
                                        ▼
                              Stickiness Applied (Paper 2)
                                        │
                                        ▼
                              Control > 0 (Paper 2)
                                        │
                                        ├──► + Stability ──► Life-Like (Paper 3)
                                        │
                                        └──► + Structure ──► Computation (Paper 1)
                                                               (if ≥5 bits)
```

### Chain 2: From Structure to Survival
```
Structure Type
    │
    ├── Has Basin?
    │       │
    │       ├── YES: Point/Cycle/Large
    │       │         │
    │       │         ▼
    │       │    SURVIVES (Paper 5)
    │       │         │
    │       │         ├── d ≡ 0 (mod P)? ──► LOW visibility (Paper 6)
    │       │         │
    │       │         └── d ≢ 0 (mod P)? ──► HIGH visibility (Paper 6)
    │       │
    │       └── NO: Trajectory (glider)
    │                 │
    │                 ▼
    │            DESTROYED (Paper 5)
    │
    └── "What survives is not what computes, but what repairs"
```

### Chain 3: The Computation-Robustness Tradeoff
```
COMPUTATIONAL STRUCTURES          ROBUST STRUCTURES
(trajectories, gliders)           (basins, oscillators)
         │                                │
         │ carry signals                  │ maintain state
         │ enable logic                   │ absorb perturbation
         │ NO BASIN                       │ STRONG BASIN
         │                                │
         ▼                                ▼
    FRAGILE under                    SURVIVE under
    temporal filtering               temporal filtering
         │                                │
         │ Rule 110 collisions ◄──────────┤
         │ create bulk that               │
         │ survives                       │
         │                                │
         ▼                                ▼
    "Compute briefly,                "What repairs
     then crystallize"                persists"
```

## 6. Unifying Themes

### Theme 1: Hidden State is the Key Enabler
- Paper 1: The 5th bit (Control) requires hidden state
- Paper 2: Hidden state is necessary and sufficient for Control
- Paper 3: Control (from hidden state) enables life-like behavior
- Paper 4: Stickiness creates hidden state; substrate properties determine if it works
- Paper 5: Hidden state creates basins that enable survival
- Paper 6: Hidden state (ether oscillation) creates anti-resonance

**Synthesis claim:** Hidden state is the universal enabler across all capabilities studied.

### Theme 2: Temporal Filtering as Universal Probe
- Paper 2: Introduced temporal filtering (stickiness)
- Paper 4: Temporal filtering = temporal low-pass filter
- Paper 5: Temporal filtering selects for basin-possessing structures
- Paper 6: Temporal filtering reveals carrier-period anti-resonance

**Synthesis claim:** Temporal filtering is not just a mechanism but a diagnostic that reveals intrinsic properties.

### Theme 3: Basin of Attraction as Organizing Principle
- Paper 3: Life-like behavior requires stability mechanisms (implicit basins)
- Paper 4: Prone substrates have structure (compression) enabling basins
- Paper 5: Basin strength is THE criterion for survival
- Paper 6: Anti-resonance is about phase alignment within basin cycles

**Synthesis claim:** Basin of attraction unifies survival, stability, and visibility.

### Theme 4: Orthogonality of Computation and Robustness
- Paper 1: Computation requires 5 bits + structure
- Paper 3: Life-like ≠ Computation (Rule 110 vs Rule 90)
- Paper 5: "What survives is not what computes, but what repairs"
- Paper 6: Visibility depends on carrier alignment, not computational content

**Synthesis claim:** Computation and robustness are fundamentally orthogonal. This is not a bug but a feature of dynamical systems.

---

## 7. Framework Candidates for Paper 7

### Candidate A: Two-Axis Robustness Map
```
                     VISIBILITY
                   (Paper 6)
                        │
                  HIGH  │
                   ┌────┼────┐
    SURVIVAL       │ A  │ B  │
    (Paper 5)      │    │    │
             ─────►├────┼────┤
                   │ C  │ D  │
                   │    │    │
                  LOW   │
                        │

A: Survives + Visible (ideal information carrier)
B: Survives + Hidden (dormant/steganographic)
C: Dies + Visible (transient signal)
D: Dies + Hidden (noise)
```

### Candidate B: Hierarchical Filter Model
```
Level 1: Does it EXIST?
         └── Leakiness + Capacity test (Paper 4)
                │
                ▼ (passes)
Level 2: Does it SURVIVE?
         └── Basin strength test (Paper 5)
                │
                ▼ (passes)
Level 3: Is it READABLE?
         └── Anti-resonance test (Paper 6)
                │
                ▼ (passes)
Level 4: Does it COMPUTE?
         └── UCT test (Paper 1)
                │
                ▼ (passes)
UNIVERSAL COMPUTATION
```

### Candidate C: Capability Decomposition
```
Substrate Properties:
├── Leakiness (L)
├── Capacity (C)
└── Hidden State Potential (H)

Emergent Capabilities (from H):
├── Control (Paper 2)
├── Basin Structure (Paper 5)
└── Phase Coherence (Paper 6)

Behavioral Outcomes:
├── Life-Like = Control + Stability + Activity (Paper 3)
├── Survival = Basin(strong) (Paper 5)
├── Visibility = d ≢ 0 (mod P) (Paper 6)
└── Computation = ≥5 bits + Structure (Paper 1)

Orthogonalities:
├── Computation ⊥ Self-Maintenance
├── Survival ⊥ Visibility
└── Control ⊥ Stability (can have one without other)
```

---

*Relationship map completed: 2026-01-14*
*Next: Construct synthesis framework and identify potential reviewer attacks*
