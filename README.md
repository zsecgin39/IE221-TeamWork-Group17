# IE221-TeamWork-Group17
# IE221-TeamWork-Group17

# Teamwork 3: SLLN & CLT Simulations

## Project Description
This project aims to experimentally verify the Strong Law of Large Numbers (SLLN) and the Central Limit Theorem (CLT) using Python-based simulations. It also demonstrates a practical application of SLLN through Monte Carlo Pi estimation.

## Team Members
- Sadenur Toker (Student ID: 2211021038)
- Hilal Avcı (Student ID: 2211021043)
- Sultan Dilara Bilgili (Student ID: 2211021003)
- Zeynep Seçgin (Student ID: 2211021021)

## Installation
To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt

Usage 
Each simulation script can be executed from the command line. Use the following commands to run the projects and generate figures:
SLLN Simulation:
 ```bash python src/slln_simulation.py
This script plots the cumulative mean vs. the number of observations to show convergence.
CLT Simulation:
python src/clt_simulation.py
This script generates histograms of standardized sums for different values of n and overlays the N(0,1) density function.
Monte Carlo Pi Estimation:
python src/monte_carlo_pi.py
This script estimates $\pi$ by dropping random points into a unit square and tracking the proportion inside a circle.

Project Structure:
The repository follows the exact folder structure required by the project instructions:
src/: Contains the Python source code for all simulations.
slln_simulation.py: Simulation for the Strong Law of Large Numbers.
clt_simulation.py: Simulation for the Central Limit Theorem.
monte_carlo_pi.py: Code for Monte Carlo Pi estimation.
results/figures/: All generated plots (SLLN convergence, CLT histograms, and Pi estimation graphs) are stored here.
data/: A directory designated for any generated or source data files.
reports/: Contains the technical reports (TW2_Report.pdf and TW3_Report.pdf) describing the findings.
requirements.txt: Lists the required Python packages (e.g., numpy, matplotlib).
.gitignore: Specifies files and directories to be ignored by the repository.
README.md: This file, providing project details and instructions.
