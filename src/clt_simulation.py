"""
CLT Simulation Script

This script demonstrates the Central Limit Theorem (CLT) using Monte Carlo simulation.

We generate m independent experiments. In each experiment, we sample n i.i.d.
random variables from Uniform(0,1), compute their sum S_n, and then standardize it:

    Z = (S_n - n*μ) / (σ*sqrt(n))

According to the CLT, as n increases, the distribution of Z approaches N(0,1)
(convergence in distribution).

Outputs:
    - ../results/figures/clt_analysis.png
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os


def run_clt_simulation(
    m: int = 1000,
    n_values: list[int] = None,
    seed: int | None = None,
    save_path: str = "../results/figures/clt_analysis.png"
):
    """
    Runs CLT simulations for multiple sample sizes n, and produces:
        - Histogram of standardized sums vs standard normal density
        - Normal Q-Q plots

    Parameters:
        m (int): Number of experiments/replications for each n.
        n_values (list[int]): Different sample sizes to compare CLT behavior.
        seed (int | None): Random seed for reproducibility (optional).
        save_path (str): Path to save the output figure.

    Returns:
        dict: A dictionary containing z-scores for each n.
              Example: results[n] = np.array([...])
    """
    if n_values is None:
        n_values = [2, 5, 10, 30, 50]

    # Fix seed for reproducibility
    if seed is not None:
        np.random.seed(seed)

    # For Uniform(0,1): theoretical mean and standard deviation
    mu = 0.5
    sigma = np.sqrt(1 / 12)

    # Create subplot layout: 1 row per n, 2 columns (histogram + Q-Q plot)
    fig, axes = plt.subplots(len(n_values), 2, figsize=(12, 20))

    results = {}

    for idx, n in enumerate(n_values):
        # Generate samples: m experiments, each experiment has n observations
        # samples shape: (m, n)
        samples = np.random.uniform(0, 1, (m, n))

        # Compute S_n for each experiment (sum over n variables)
        sums = np.sum(samples, axis=1)

        # Standardization for CLT:
        # Z = (S_n - n*μ) / (σ*sqrt(n))
        z_scores = (sums - n * mu) / (sigma * np.sqrt(n))
        results[n] = z_scores

        # --- Plot 1: Histogram vs Standard Normal PDF ---
        axes[idx, 0].hist(
            z_scores,
            bins=30,
            density=True,
            alpha=0.6,
            edgecolor="black",
            label="Simulated Z"
        )

        # Plot theoretical standard normal density for comparison
        x = np.linspace(-4, 4, 200)
        axes[idx, 0].plot(x, stats.norm.pdf(x, 0, 1), lw=2, label="N(0,1)")

        axes[idx, 0].set_title(f"Histogram of Standardized Sums (n={n})")
        axes[idx, 0].legend()

        # --- Plot 2: Normal Q-Q Plot ---
        # If points lie approximately on a straight line => distribution ~ normal
        stats.probplot(z_scores, dist="norm", plot=axes[idx, 1])
        axes[idx, 1].set_title(f"Normal Q-Q Plot (n={n})")

    plt.tight_layout()

    # Ensure output directory exists then save
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)

    print(f"CLT simulation complete. Figure saved to {save_path}")
    plt.show()

    return results


if __name__ == "__main__":
    run_clt_simulation(m=1000, n_values=[2, 5, 10, 30, 50], seed=42)

