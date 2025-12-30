import numpy as np
import matplotlib.pyplot as plt
import os

# Configuration [cite: 54, 56]
n = 10000
mu = 0.5
sigma_sq = 1/12

# Generate random observations from U[0,1] [cite: 55]
data = np.random.uniform(0, 1, n)

# Calculate cumulative mean Sn = (X1 + ... + Xn) / n [cite: 55]
cumulative_indices = np.arange(1, n + 1)
cumulative_mean = np.cumsum(data) / cumulative_indices

# Plotting [cite: 55, 58]
plt.figure(figsize=(10, 6))
plt.plot(cumulative_indices, cumulative_mean, label='Cumulative Mean ($S_n$)', color='blue', linewidth=1)
plt.axhline(y=mu, color='red', linestyle='--', label=f'Theoretical Mean ($\mu$ = {mu})')

plt.title('Strong Law of Large Numbers (SLLN) Simulation')
plt.xlabel('Number of Observations (n)')
plt.ylabel('Cumulative Mean')
plt.legend()
plt.grid(True, alpha=0.3)

# Ensure results directory exists and save figure [cite: 27, 35, 91]
os.makedirs('../results/figures', exist_ok=True)
plt.savefig('../results/figures/slln_convergence.png')
print("SLLN simulation complete. Figure saved to results/figures/slln_convergence.png")
plt.show()
