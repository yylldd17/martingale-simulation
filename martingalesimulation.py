import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
np.random.seed(42)
num_simulations = 1000  # number of independent games
max_steps = 1000        # maximum steps per game to prevent infinite loops
target = 5              # stopping threshold: stop if gain reaches +5 or -5

# Initial value
Z0 = 0
stopped_values = []

# Run simulations
for _ in range(num_simulations):
    Z = Z0
    for _ in range(max_steps):
        step = np.random.choice([-1, 1])  # fair coin toss: -1 for tails, +1 for heads
        Z += step
        if abs(Z) == target:  # stopping condition: hit ±target
            break
    stopped_values.append(Z)

# Compute expected value at stopping time
mean_stopped = np.mean(stopped_values)

# Plot histogram of stopped values
plt.hist(stopped_values, bins=range(-target, target + 2), edgecolor='black', align='left')
plt.axvline(x=mean_stopped, color='red', linestyle='--', label=f'E[Z_N] ≈ {mean_stopped:.2f}')
plt.axvline(x=Z0, color='blue', linestyle=':', label='Z_0 = 0')
plt.title("Martingale Game - Stopping Theorem Simulation")
plt.xlabel("Gain at Stopping Time")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
