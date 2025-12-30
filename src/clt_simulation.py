import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# Parameters [cite: 67, 68]
m = 1000  # Number of experiments
n_values = [2, 5, 10, 30, 50]  # Different sample sizes
mu = 0.5
sigma = np.sqrt(1/12)

# Set up the plot [cite: 69, 70]
fig, axes = plt.subplots(len(n_values), 2, figsize=(12, 20))

for idx, n in enumerate(n_values):
    # Generate m sums of n variables [cite: 68]
    samples = np.random.uniform(0, 1, (m, n))
    sums = np.sum(samples, axis=1)
    
    # Standardize the sums: Zi = (Sn - n*mu) / (sigma * sqrt(n)) [cite: 68]
    z_scores = (sums - n * mu) / (sigma * np.sqrt(n))
    
    # Plot 1: Histogram vs Standard Normal Density [cite: 69, 70, 72]
    axes[idx, 0].hist(z_scores, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
    x = np.linspace(-4, 4, 100)
    axes[idx, 0].plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2, label='N(0,1)')
    axes[idx, 0].set_title(f'Histogram of Standardized Sums (n={n})')
    axes[idx, 0].legend()
    
    # Plot 2: Normal Q-Q Plot [cite: 70]
    stats.probplot(z_scores, dist="norm", plot=axes[idx, 1])
    axes[idx, 1].set_title(f'Normal Q-Q Plot (n={n})')

plt.tight_layout()
# Save figure [cite: 27, 35, 91]
os.makedirs('../results/figures', exist_ok=True)
plt.savefig('../results/figures/clt_analysis.png')
print("CLT simulation complete. Figure saved to results/figures/clt_analysis.png")
plt.show()
