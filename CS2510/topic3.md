# [Adversarial games: minimax, expectiminimax, other techniques](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)

## Minimax
> Minimax is a **decision making** algorithm used in **two-player**, **zero-sum games**.

#### Time complexity
<img width="70" height="41" alt="image" src="https://github.com/user-attachments/assets/3f985a1c-870a-4b78-b0a2-bc2576d1fb25" />

 - **b** = branching factor (moves per position)
 - **d** = depth of the tree

#### Space complexity
<img width="75" height="35" alt="image" src="https://github.com/user-attachments/assets/70494ab5-420e-4c4a-bacf-a516effba270" />

## Expectiminimax
**Expectiminimax** is a version of **minimax** used when there is **randomness** in the game.
### How It Works
> There are 3 types of nodes:
1. MAX node
 - Chooses the maximum value (like minimax)
2. MIN node
 - Chooses the minimum value
3. CHANCE node
 - Computes the expected value:
<img width="570" height="66" alt="image" src="https://github.com/user-attachments/assets/376998cb-4a7a-4064-8115-720d29fa943c" />

>Instead of choosing max or min, it averages based on probability.


## Alpha beta pruning
 - **Alpha** = best already explored option along path to the root for **maximizer**
 - **Beta** = best already explored option along path to the root for **minimizer**
 - if **Alpha >= Beta** then you prune the branch
<img width="496" height="347" alt="image" src="https://github.com/user-attachments/assets/805f9dbf-5c93-4e14-bb9e-d6c81c2f1733" />

---------------------
>Quiescent search extends the search past the depth limit until the position becomes stable (quiet).
