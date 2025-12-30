import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters [cite: 56, 80]
n = 10000

# Generate random (x, y) points in [0,1]x[0,1] [cite: 80]
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

# Check condition x^2 + y^2 <= 1 [cite: 81]
inside_circle = (x**2 + y**2) <= 1

# Calculate pi estimate: Pi = 4 * (points inside / total points) [cite: 82]
cumulative_inside = np.cumsum(inside_circle)
pi_estimates = 4 * cumulative_inside / np.arange(1, n + 1)

# Plotting [cite: 83, 84, 86]
plt.figure(figsize=(10, 6))
plt.plot(pi_estimates, label='Monte Carlo Estimate', color='green')
plt.axhline(y=np.pi, color='red', linestyle='--', label=f'True $\pi$ ({np.pi:.4f})')

plt.title('Monte Carlo Estimation of $\pi$')
plt.xlabel('Number of Points (n)')
plt.ylabel('Estimated Value')
plt.legend()
plt.grid(True, alpha=0.3)

# Save figure [cite: 27, 35, 91]
os.makedirs('../results/figures', exist_ok=True)
plt.savefig('../results/figures/pi_estimation.png')
print("Monte Carlo simulation complete. Figure saved to results/figures/pi_estimation.png")
plt.show()
