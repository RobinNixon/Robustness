"""
Figure generation for Paper 7: Synthesis Framework
Orthogonal Robustness in Discrete Dynamical Systems

This script generates conceptual figures for the synthesis paper.
No new experiments or simulations are performed - all figures are
illustrative or summarizing existing findings from Papers 1-6.

Provenance: Original code created for Paper 7.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

def fig1_framework_overview():
    """
    Figure 1: The Orthogonal Robustness Framework
    Shows the four axes and their relationships

    Content: Conceptual diagram showing hierarchical structure
    - Substrate properties (Paper 4)
    - Hidden state mechanism (Paper 2)
    - Three emergent mechanisms: Control, Basin, Phase
    - Four orthogonal outcomes
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Title
    ax.text(50, 97, 'The Orthogonal Robustness Framework',
            ha='center', va='top', fontsize=16, fontweight='bold')

    # Substrate layer (top)
    substrate_box = mpatches.FancyBboxPatch((15, 78), 70, 12,
                                             boxstyle="round,pad=0.05",
                                             facecolor='lightblue', edgecolor='navy', linewidth=2)
    ax.add_patch(substrate_box)
    ax.text(50, 84, 'SUBSTRATE PROPERTIES', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(30, 81, 'Leakiness (L)', ha='center', va='center', fontsize=9)
    ax.text(70, 81, 'Capacity (C)', ha='center', va='center', fontsize=9)

    # Arrow down
    ax.annotate('', xy=(50, 68), xytext=(50, 78),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

    # Hidden state layer
    hidden_box = mpatches.FancyBboxPatch((25, 58), 50, 10,
                                          boxstyle="round,pad=0.05",
                                          facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(hidden_box)
    ax.text(50, 63, 'HIDDEN STATE', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(50, 60, 'Stickiness Mechanism', ha='center', va='center', fontsize=9, style='italic')

    # Arrows to three mechanisms
    ax.annotate('', xy=(25, 48), xytext=(35, 58),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax.annotate('', xy=(50, 48), xytext=(50, 58),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax.annotate('', xy=(75, 48), xytext=(65, 58),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

    # Three mechanism boxes
    control_box = mpatches.FancyBboxPatch((5, 38), 25, 10,
                                           boxstyle="round,pad=0.05",
                                           facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
    ax.add_patch(control_box)
    ax.text(17.5, 43, 'Control', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(17.5, 40, '(Paper 2)', ha='center', va='center', fontsize=8)

    basin_box = mpatches.FancyBboxPatch((37.5, 38), 25, 10,
                                         boxstyle="round,pad=0.05",
                                         facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
    ax.add_patch(basin_box)
    ax.text(50, 43, 'Basin Structure', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(50, 40, '(Paper 5)', ha='center', va='center', fontsize=8)

    phase_box = mpatches.FancyBboxPatch((70, 38), 25, 10,
                                         boxstyle="round,pad=0.05",
                                         facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
    ax.add_patch(phase_box)
    ax.text(82.5, 43, 'Phase Coherence', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(82.5, 40, '(Paper 6)', ha='center', va='center', fontsize=8)

    # Arrows to four outcomes
    ax.annotate('', xy=(10, 25), xytext=(15, 38),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax.annotate('', xy=(35, 25), xytext=(20, 38),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax.annotate('', xy=(60, 25), xytext=(52, 38),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax.annotate('', xy=(85, 25), xytext=(82.5, 38),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

    # Four outcome boxes
    titles = ['COMPUTATION', 'SELF-MAINT', 'SURVIVAL', 'VISIBILITY']
    papers = ['Paper 1', 'Paper 3', 'Paper 5', 'Paper 6']
    criteria = ['>=5 bits', 'C+S+A', 'Basin', 'd!=0(mod P)']
    positions = [(2, 10), (27, 10), (52, 10), (77, 10)]

    for i, (pos, title, paper, crit) in enumerate(zip(positions, titles, papers, criteria)):
        box = mpatches.FancyBboxPatch(pos, 21, 15,
                                       boxstyle="round,pad=0.05",
                                       facecolor='lightsalmon', edgecolor='darkred', linewidth=2)
        ax.add_patch(box)
        ax.text(pos[0]+10.5, pos[1]+12, title, ha='center', va='center', fontsize=9, fontweight='bold')
        ax.text(pos[0]+10.5, pos[1]+8, paper, ha='center', va='center', fontsize=8)
        ax.text(pos[0]+10.5, pos[1]+4, crit, ha='center', va='center', fontsize=8, style='italic')

    # Orthogonality label
    ax.text(50, 3, 'ORTHOGONAL AXES: Each axis independent of the others',
            ha='center', va='center', fontsize=10, style='italic', color='darkred')

    plt.tight_layout()
    plt.savefig('../figures/fig1_framework_overview.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated: fig1_framework_overview.png")


def fig2_orthogonality_matrix():
    """
    Figure 2: Orthogonality Evidence
    Shows the 2x2 matrices demonstrating independence

    Content: Three 2x2 matrices showing:
    - Computation vs Self-Maintenance (Rule 110 vs Rule 90)
    - Survival vs Visibility (oscillator conditions)
    - Control vs Stability (life-like classification)

    Provenance: Data from Papers 1, 3, 5, 6
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Orthogonality 1: Computation x Self-Maintenance
    ax1 = axes[0]
    data1 = np.array([[1, 1], [1, 1]])
    ax1.imshow(data1, cmap='Greens', vmin=0, vmax=2)
    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xticklabels(['Computes', 'No Compute'])
    ax1.set_yticklabels(['Life-Like', 'Not Life-Like'])
    ax1.set_xlabel('Computational Capability')
    ax1.set_ylabel('Self-Maintenance')
    ax1.set_title('Computation vs Self-Maintenance', fontweight='bold')

    ax1.text(0, 0, 'Rare\n(R110+repair?)', ha='center', va='center', fontsize=9)
    ax1.text(1, 0, 'Rule 90\n(common)', ha='center', va='center', fontsize=9)
    ax1.text(0, 1, 'Rule 110\n(universal)', ha='center', va='center', fontsize=9)
    ax1.text(1, 1, 'Rule 30\n(chaotic)', ha='center', va='center', fontsize=9)

    # Orthogonality 2: Survival x Visibility
    ax2 = axes[1]
    data2 = np.array([[1, 0.3], [1, 1]])
    ax2.imshow(data2, cmap='Blues', vmin=0, vmax=2)
    ax2.set_xticks([0, 1])
    ax2.set_yticks([0, 1])
    ax2.set_xticklabels(['Survives', 'Dies'])
    ax2.set_yticklabels(['Visible', 'Hidden'])
    ax2.set_xlabel('Survival')
    ax2.set_ylabel('Visibility')
    ax2.set_title('Survival vs Visibility', fontweight='bold')

    ax2.text(0, 0, 'Oscillator\noff-period', ha='center', va='center', fontsize=9)
    ax2.text(1, 0, 'Glider\n(transient)', ha='center', va='center', fontsize=9)
    ax2.text(0, 1, 'Oscillator\non-period', ha='center', va='center', fontsize=9)
    ax2.text(1, 1, 'Dead\nstructure', ha='center', va='center', fontsize=9, color='gray')

    # Orthogonality 3: Control x Stability
    ax3 = axes[2]
    data3 = np.array([[1, 1], [1, 1]])
    ax3.imshow(data3, cmap='Oranges', vmin=0, vmax=2)
    ax3.set_xticks([0, 1])
    ax3.set_yticks([0, 1])
    ax3.set_xticklabels(['Has Control', 'No Control'])
    ax3.set_yticklabels(['Stable', 'Unstable'])
    ax3.set_xlabel('Control')
    ax3.set_ylabel('Stability')
    ax3.set_title('Control vs Stability', fontweight='bold')

    ax3.text(0, 0, 'LIFE-LIKE\n(83.7%)', ha='center', va='center', fontsize=9, fontweight='bold')
    ax3.text(1, 0, 'Crystallized\n(3 rules)', ha='center', va='center', fontsize=9)
    ax3.text(0, 1, 'Computing\n(14.7%)', ha='center', va='center', fontsize=9)
    ax3.text(1, 1, 'Trivial/\nChaotic', ha='center', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig('../figures/fig2_orthogonality_matrix.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated: fig2_orthogonality_matrix.png")


def fig3_hidden_state_cascade():
    """
    Figure 3: Hidden State as Universal Enabler
    Shows how hidden state enables all four capabilities

    Content: Central hidden state box with arrows to four capabilities
    Provenance: Synthesis of Papers 1, 2, 3, 5, 6
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Central hidden state box
    center_box = mpatches.FancyBboxPatch((35, 45), 30, 15,
                                          boxstyle="round,pad=0.1",
                                          facecolor='gold', edgecolor='darkgoldenrod', linewidth=3)
    ax.add_patch(center_box)
    ax.text(50, 52.5, 'HIDDEN STATE', ha='center', va='center', fontsize=14, fontweight='bold')

    # Four capability boxes
    capabilities = [
        ('COMPUTATION', 'The 5th bit\n(Control)', 20, 80, 'lightcoral'),
        ('SELF-MAINTENANCE', 'Control enables\nlife-like', 70, 80, 'lightgreen'),
        ('SURVIVAL', 'Creates basins\nfor repair', 20, 15, 'lightblue'),
        ('VISIBILITY', 'Enables carrier\noscillation', 70, 15, 'lightyellow'),
    ]

    for title, desc, x, y, color in capabilities:
        box = mpatches.FancyBboxPatch((x-12, y-8), 24, 16,
                                       boxstyle="round,pad=0.05",
                                       facecolor=color, edgecolor='gray', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y+3, title, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(x, y-3, desc, ha='center', va='center', fontsize=8)

    # Arrows from center to capabilities
    arrow_params = dict(arrowstyle='->', lw=2, color='darkgoldenrod')
    ax.annotate('', xy=(20, 72), xytext=(40, 60), arrowprops=arrow_params)
    ax.annotate('', xy=(70, 72), xytext=(60, 60), arrowprops=arrow_params)
    ax.annotate('', xy=(20, 31), xytext=(40, 45), arrowprops=arrow_params)
    ax.annotate('', xy=(70, 31), xytext=(60, 45), arrowprops=arrow_params)

    # Paper references
    ax.text(8, 80, 'Paper 1', fontsize=8, style='italic')
    ax.text(82, 80, 'Paper 3', fontsize=8, style='italic')
    ax.text(8, 15, 'Paper 5', fontsize=8, style='italic')
    ax.text(82, 15, 'Paper 6', fontsize=8, style='italic')

    # Title
    ax.text(50, 95, 'Hidden State: The Universal Enabler',
            ha='center', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../figures/fig3_hidden_state_cascade.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated: fig3_hidden_state_cascade.png")


def fig4_paper_connections():
    """
    Figure 4: Paper Dependency Graph
    Shows how the six papers connect

    Content: Flow diagram of paper dependencies
    Provenance: Original to Paper 7
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Paper positions
    papers = {
        1: (50, 90, 'Paper 1: UCT\n5-bit threshold', 'lightcoral'),
        2: (25, 70, 'Paper 2: Stickiness\nHidden state', 'lightgreen'),
        3: (50, 50, 'Paper 3: Self-Maint\n83.7% life-like', 'lightblue'),
        4: (75, 70, 'Paper 4: Leakiness\nPredictive model', 'lightyellow'),
        5: (25, 30, 'Paper 5: Invariants\nBasin criterion', 'lightpink'),
        6: (75, 30, 'Paper 6: Anti-Res\nVisibility', 'lightcyan'),
        7: (50, 10, 'Paper 7: SYNTHESIS\nOrthogonal Robustness', 'gold'),
    }

    for num, (x, y, label, color) in papers.items():
        box = mpatches.FancyBboxPatch((x-15, y-8), 30, 16,
                                       boxstyle="round,pad=0.05",
                                       facecolor=color, edgecolor='gray', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8)

    # Arrows showing dependencies
    arrows = [
        (50, 82, 25, 78),   # 1 -> 2
        (25, 62, 50, 58),   # 2 -> 3
        (75, 62, 50, 58),   # 4 -> 3
        (50, 42, 25, 38),   # 3 -> 5
        (50, 42, 75, 38),   # 3 -> 6
        (25, 22, 50, 18),   # 5 -> 7
        (75, 22, 50, 18),   # 6 -> 7
    ]

    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))

    # Title
    ax.text(50, 98, 'Paper Dependency Structure',
            ha='center', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../figures/fig4_paper_connections.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated: fig4_paper_connections.png")


def fig5_four_axis_space():
    """
    Figure 5: The 4D Structure Space
    Shows example structures positioned in the 4-axis space

    Content: Table showing structure coordinates
    Provenance: Examples from Papers 1, 3, 5, 6
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Example structures with their 4D coordinates
    structures = [
        ('Rule 110 glider', 1, 0, 0, 1, 'red'),
        ('Rule 90 bulk', 0, 1, 1, 1, 'green'),
        ('Still life', 0, 0, 1, 1, 'blue'),
        ('Oscillator (on-period)', 0, 1, 1, 0, 'orange'),
        ('Rule 30 chaos', 0, 0, 1, 1, 'purple'),
    ]

    ax.axis('off')

    # Headers
    headers = ['Structure', 'Computes', 'Self-Maint', 'Survives', 'Visible']
    col_positions = [0.1, 0.35, 0.5, 0.65, 0.8]

    for i, (header, x) in enumerate(zip(headers, col_positions)):
        ax.text(x, 0.9, header, ha='center', va='center', fontsize=11, fontweight='bold',
                transform=ax.transAxes)

    # Data rows
    for j, (name, c1, c2, c3, c4, color) in enumerate(structures):
        y = 0.75 - j * 0.12
        ax.text(col_positions[0], y, name, ha='center', va='center', fontsize=10,
                color=color, transform=ax.transAxes)
        for i, val in enumerate([c1, c2, c3, c4]):
            symbol = 'Y' if val else 'N'
            ax.text(col_positions[i+1], y, symbol, ha='center', va='center', fontsize=14,
                    color='green' if val else 'red', transform=ax.transAxes)

    # Title
    ax.text(0.5, 0.98, 'Structure Characterization in 4D Robustness Space',
            ha='center', va='top', fontsize=14, fontweight='bold', transform=ax.transAxes)

    # Note
    ax.text(0.5, 0.1, 'Each structure has a unique position in the 4-axis space.\n'
            'Axes are orthogonal: position on one axis does not predict position on another.',
            ha='center', va='center', fontsize=10, style='italic', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('../figures/fig5_four_axis_space.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated: fig5_four_axis_space.png")


if __name__ == '__main__':
    print("Generating figures for Paper 7: Synthesis Framework")
    print("=" * 50)
    print("Note: These are conceptual figures only.")
    print("No new experiments or simulations are performed.")
    print("=" * 50)

    fig1_framework_overview()
    fig2_orthogonality_matrix()
    fig3_hidden_state_cascade()
    fig4_paper_connections()
    fig5_four_axis_space()

    print("=" * 50)
    print("All figures generated successfully!")
