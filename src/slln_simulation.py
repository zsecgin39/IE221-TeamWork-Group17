import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 10000  # Recommended n value [cite: 56]
mu = 0.5   # Standard uniform distribution expected value [cite: 54]

# Data generation (U[0,1]) [cite: 55]
data = np.random.uniform(0, 1, n)
cumulative_mean = np.cumsum(data) / np.arange(1, n + 1) # [cite: 55]

# Visualisation [cite: 55, 58]
plt.figure(figsize=(10, 6))
plt.plot(cumulative_mean, label='Cumulative Mean ($S_n$)')
plt.axhline(y=mu, color='r', linestyle='--', label=f'True Mean ($\mu$={mu})')
plt.title('Strong Law of Large Numbers (SLLN) Convergence')
plt.xlabel('Number of Observations (n)')
plt.ylabel('Cumulative Mean')
plt.legend()
plt.grid(True)
plt.savefig('../results/figures/slln_convergence.png') # [cite: 35]
plt.show()
