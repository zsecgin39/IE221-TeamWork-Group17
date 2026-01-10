"""
SLLN Simulation Script

This script demonstrates the Strong Law of Large Numbers (SLLN) using simulation.
We generate i.i.d. samples from Uniform(0,1), compute the cumulative sample mean S_n,
and visualize its convergence to the theoretical mean μ = 0.5.

Output:
    - ../results/figures/slln_convergence.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def run_slln_simulation(n: int = 10000, seed: int | None = None, save_path: str = "../results/figures/slln_convergence.png"):
    """
    Runs a simulation for the Strong Law of Large Numbers (SLLN).

    The SLLN states that for i.i.d. random variables with finite expected value μ,
    the sample mean converges to μ almost surely as n → ∞.

    In this simulation:
        - X_i ~ Uniform(0,1)
        - μ = 0.5

    Parameters:
        n (int): Number of observations (sample size).
        seed (int | None): Random seed for reproducibility (optional).
        save_path (str): File path for saving the output figure.

    Returns:
        tuple[np.ndarray, np.ndarray]:
            - cumulative_indices: array of indices 1..n
            - cumulative_mean: cumulative sample mean values S_n
    """
    # Set seed (optional) to make results reproducible
    if seed is not None:
        np.random.seed(seed)

    # Theoretical mean of Uniform(0,1)
    mu = 0.5

    # Generate n i.i.d. samples from Uniform(0,1)
    data = np.random.uniform(0, 1, n)

    # Compute S_n = (X1 + ... + Xn)/n for n = 1..N (single sample path)
    cumulative_indices = np.arange(1, n + 1)
    cumulative_mean = np.cumsum(data) / cumulative_indices

    # Plot convergence of the sample mean to the theoretical mean μ
    plt.figure(figsize=(10, 6))
    plt.plot(
        cumulative_indices,
        cumulative_mean,
        label="Cumulative Mean ($S_n$)",
        linewidth=1
    )

    # Reference line for the theoretical mean
    plt.axhline(y=mu, linestyle="--", label=f"Theoretical Mean ($\\mu$ = {mu})")

    plt.title("Strong Law of Large Numbers (SLLN) Simulation")
    plt.xlabel("Number of Observations (n)")
    plt.ylabel("Cumulative Mean")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Ensure output directory exists before saving
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)

    print(f"SLLN simulation complete. Figure saved to {save_path}")
    plt.show()

    return cumulative_indices, cumulative_mean


if __name__ == "__main__":
    run_slln_simulation(n=10000, seed=42)

