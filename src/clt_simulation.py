import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parameters [cite: 68]
m = 1000 
n_values = [2, 5, 10, 30, 50]
mu = 0.5
sigma = np.sqrt(1/12)

fig, axes = plt.subplots(len(n_values), 2, figsize=(12, 20))

for i, n in enumerate(n_values):
    # m experiments: the sum of n random variables U[0,1] [cite: 68]
    samples = np.random.uniform(0, 1, (m, n))
    sums = np.sum(samples, axis=1)
    
   # Standardisation [cite: 68]
    standardized_sums = (sums - n * mu) / (sigma * np.sqrt(n))
    
    # Histogram and Normal Curve [cite: 69, 70]
    axes[i, 0].hist(standardized_sums, bins=30, density=True, alpha=0.6, color='skyblue')
    x = np.linspace(-4, 4, 100)
    axes[i, 0].plot(x, stats.norm.pdf(x, 0, 1), 'r', lw=2)
    axes[i, 0].set_title(f'Histogram (n={n})')
    
    # Q-Q Plot [cite: 70]
    stats.probplot(standardized_sums, dist="norm", plot=axes[i, 1])
    axes[i, 1].set_title(f'Q-Q Plot (n={n})')

plt.tight_layout()
plt.savefig('../results/figures/clt_histograms.png') # [cite: 28]
plt.show()
