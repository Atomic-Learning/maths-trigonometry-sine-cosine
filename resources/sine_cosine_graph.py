#!/usr/bin/env python3
"""
Generate a graph showing sine and cosine functions.
Outputs to sine-cosine-graph.png in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(12, 6), dpi=150)

# Generate angle values
phi = np.linspace(-2*np.pi, 2*np.pi, 1000)
sin_phi = np.sin(phi)
cos_phi = np.cos(phi)

# Plot the functions
ax.plot(phi, cos_phi, 'b-', linewidth=2.5, label=r'$\cos \varphi$', alpha=0.8)
ax.plot(phi, sin_phi, color='darkorange', linewidth=2.5, label=r'$\sin \varphi$', alpha=0.8)

# Add horizontal line at y=0
ax.axhline(y=0, color='k', linewidth=0.8, alpha=0.5)

# Grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Set labels and title
ax.set_xlabel('Angle (radians)', fontsize=12, fontweight='bold')
ax.set_ylabel('Value', fontsize=12, fontweight='bold')
ax.set_title('Sine and Cosine Functions', fontsize=14, fontweight='bold', pad=20)

# Set x-axis ticks at key angles
pi_ticks = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
pi_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', 
             r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
ax.set_xticks(pi_ticks)
ax.set_xticklabels(pi_labels, fontsize=11)

# Set y-axis ticks
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels(['-1', '-0.5', '0', '0.5', '1'], fontsize=11)

# Set limits
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-1.3, 1.3)

# Add legend
ax.legend(loc='upper right', fontsize=12, framealpha=0.95)

# Add vertical lines at key angles
for angle in [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]:
    ax.axvline(x=angle, color='gray', linestyle=':', linewidth=0.8, alpha=0.4)

plt.tight_layout()
plt.savefig('sine-cosine-graph.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: sine-cosine-graph.png")
plt.close()
