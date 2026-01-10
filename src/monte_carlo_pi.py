"""
Monte Carlo π Estimation Script

This script estimates the value of π using the Monte Carlo method.
Random points are generated uniformly in the unit square [0,1] × [0,1].
The ratio of points that fall inside the quarter unit circle (x^2 + y^2 <= 1)
approximates π/4. Therefore, π can be estimated as:

    π ≈ 4 * (number of points inside circle) / (total number of points)

Output:
    - ../results/figures/pi_estimation.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def estimate_pi_monte_carlo(
    n: int = 10000,
    seed: int | None = None,
    save_path: str = "../results/figures/pi_estimation.png"
):
    """
    Estimates π using Monte Carlo simulation.

    Parameters:
        n (int): Number of random points to generate.
        seed (int | None): Random seed for reproducibility (optional).
        save_path (str): Path where the output figure will be saved.

    Returns:
        np.ndarray: Array of cumulative π estimates for k=1..n.
    """
    # Fix seed for reproducible results
    if seed is not None:
        np.random.seed(seed)

    # Generate random (x,y) points uniformly in the unit square [0,1]×[0,1]
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    # A point lies inside the quarter unit circle if x^2 + y^2 <= 1
    inside_circle = (x**2 + y**2) <= 1

    # Cumulative count of points inside the circle
    cumulative_inside = np.cumsum(inside_circle)

    # π estimate for each k: π_k = 4 * (inside points up to k) / k
    pi_estimates = 4 * cumulative_inside / np.arange(1, n + 1)

    # Plot the convergence of π estimate to true π
    plt.figure(figsize=(10, 6))
    plt.plot(pi_estimates, label="Monte Carlo Estimate", linewidth=1)

    # Reference line: true value of π
    plt.axhline(y=np.pi, linestyle="--", label=f"True $\\pi$ ({np.pi:.4f})")

    plt.title("Monte Carlo Estimation of $\\pi$")
    plt.xlabel("Number of Points (n)")
    plt.ylabel("Estimated Value")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Ensure output directory exists and save the figure
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)

    print(f"Monte Carlo simulation complete. Figure saved to {save_path}")
    plt.show()

    return pi_estimates


if __name__ == "__main__":
    estimate_pi_monte_carlo(n=10000, seed=42)

    # Ensure output directory exists and save the figure
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)

    print(f"Monte Carlo simulation complete. Figure saved to {save_path}")
    plt.show()

    return pi_estimates


if __name__ == "__main__":
    estimate_pi_monte_carlo(n=10000, seed=42)

