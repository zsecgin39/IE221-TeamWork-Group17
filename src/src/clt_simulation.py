import numpy as np
import matplotlib.pyplot as plt

# SLLN Simulation - IE 221
# Parameters: Standard uniform distribution U[0,1]
n = 10000  # Recommended: n >= 10,000
mu = 0.5   # Expected value for U[0,1]

# Generate successive observations
data = np.random.uniform(0, 1, n)

# Calculate cumulative mean: Sn = (X1 + ... + Xn) / n
cumulative_mean = np.cumsum(data) / np.arange(1, n + 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(cumulative_mean, label='Cumulative Mean ($S_n$)')
plt.axhline(y=mu, color='r', linestyle='--', label=f'Reference Line ($\mu$={mu})')
plt.title('Strong Law of Large Numbers (SLLN) Simulation')
plt.xlabel('Number of observations (n)')
plt.ylabel('Cumulative mean')
plt.legend()
plt.grid(True)

# Save figure to the required folder
plt.savefig('../results/figures/slln_convergence.png')
plt.show()
