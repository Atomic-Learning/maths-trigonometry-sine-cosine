#!/usr/bin/env python3
"""
Generate a unit circle diagram showing sin and cos definitions.
Outputs to unit-circle.png in the same directory.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(8, 8), dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=1.5)
ax.axvline(x=0, color='k', linewidth=1.5)

# Add axis labels
ax.set_xlabel('x', fontsize=12, fontweight='bold')
ax.set_ylabel('y', fontsize=12, fontweight='bold')
ax.set_title('Unit Circle: Definitions of Sine and Cosine', fontsize=14, fontweight='bold', pad=20)

# Draw unit circle
circle = patches.Circle((0, 0), 1, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(circle)

# Angle φ = 45 degrees = π/4 radians
phi = np.pi / 4
x = np.cos(phi)
y = np.sin(phi)

# Draw radius line
ax.plot([0, x], [0, y], 'r-', linewidth=2.5, label='radius = 1')
ax.plot(x, y, 'ro', markersize=8)

# Draw arc for angle
arc_angles = np.linspace(0, phi, 50)
arc_r = 0.3
ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), 'b--', linewidth=1.5)
ax.text(0.4, 0.08, r'$\varphi$', fontsize=13, color='blue', fontweight='bold')

# Draw cos φ projection (horizontal)
ax.plot([x, x], [0, y], 'g--', linewidth=2, alpha=0.7)
ax.plot([0, x], [0, 0], 'g-', linewidth=3, alpha=0.8)
ax.text(x/2, -0.15, r'$\cos \varphi$', fontsize=12, color='green', fontweight='bold', 
        ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

# Draw sin φ projection (vertical)
ax.plot([0, 0], [0, y], 'orange', linewidth=3, alpha=0.8)
ax.plot([0, x], [y, y], color='orange', linestyle='--', linewidth=2, alpha=0.7)
ax.text(-0.1, y/2, r'$\sin \varphi$', fontsize=12, color='darkorange', fontweight='bold',
        ha='right', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Label the point on the circle
ax.text(x + 0.05, y + 0.05, f'({x:.2f}, {y:.2f})', fontsize=10, 
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Mark key points on the circle
ax.text(1.03, -0.05, '(1, 0)', fontsize=10, ha='left', va='center')
ax.text(-1.03, -0.05, '(-1, 0)', fontsize=10, ha='right', va='center')
ax.text(-0.1, 1.03, '(0, 1)', fontsize=10, ha='center', va='bottom')
ax.text(-0.1, -1.03, '(0, -1)', fontsize=10, ha='center', va='top')

# Set ticks
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.tick_params(labelsize=10)

plt.tight_layout()
plt.savefig('unit-circle.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: unit-circle.png")
plt.close()
