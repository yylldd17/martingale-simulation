# martingale-simulation


This project simulates the **Martingale Stopping Theorem** using a simple fair coin-tossing game (i.e., +1 for heads, -1 for tails). The code demonstrates that under specific stopping rules, the **expected value at the stopping time equals the initial value**, validating the theoretical result.

---

## Theory: What Is the Martingale Stopping Theorem?

In a **martingale process**, the conditional expected value of the next state is equal to the current state — it represents a "fair game."

The **Martingale Stopping Theorem** states that under certain conditions (e.g., bounded stopping time, bounded martingale, or bounded increments with finite expected stopping time), if you stop the process at a *stopping time* (a time determined by the process history), the expected value at that point is still the same as the starting point.

Formally:

> If `{Z_n}` is a martingale and `N` is a valid stopping time under mild conditions, then  
> **`E[Z_N] = E[Z_0]`**

---

##  Simulation: Coin Toss Game

- You start with `Z_0 = 0` (no gain/loss).
- Each step is either +1 or -1 (fair coin toss).
- The game **stops when the total gain/loss hits +5 or -5**.
- This makes the stopping time dependent on the process (valid stopping time).
- We repeat the game 1000 times and record the final values.

---

##  Results

- The histogram shows that all players end with either +5 or -5.
- The **expected value** across all simulations is approximately **0**, which matches the **theoretical starting point**.
- This validates the **Martingale Stopping Theorem**.


