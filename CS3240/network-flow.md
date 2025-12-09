# [Network Flow](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)
## Valid Flow in a Network
A **flow network** is a directed graph with:
 - a source `s`
 - a sink `t` a capacity
 - c(u,v) on each edge (possibly 0 if no edge)

> A **flow** is a function f(u,v) that assigns a **value** to every **directed edge**.

#### A flow is valid if(needed to check validity):
1. **Capacity Constraint** --> not more than the capacity on that edge
2. **Conservation of flow** --> Flow in = flow out

## [Ford–Fulkerson Algorithm ](https://www.youtube.com/watch?v=Tl90tNtKvxs)
> **Goal**: Find a maximum flow from `s` to `t`.

> **Key Idea**: As long as you can push more flow from 
s to t, do so. This is done using **augmenting** paths in the **residual** graph.

### Residual Graph
For each edge (u,v):

Forward edge capacity:
<img width="284" height="29" alt="image" src="https://github.com/user-attachments/assets/e4926f77-234e-4409-baa1-8aade8cb64bd" />

Backward edge capacity:
<img width="182" height="30" alt="image" src="https://github.com/user-attachments/assets/6e615a04-ae27-4909-9bbf-5dfb36a2c3f4" />

>The residual graph shows where additional flow can be pushed (forward) or undone (backward).

### Ford-Fulkerson Algorithm Steps (important to include on cheat sheet)
1. Start with zero flow.
2. Construct the residual graph.
3. Find any augmenting path from s to t in the residual graph.
4. Compute the bottleneck (minimum residual capacity along that path).
5. Augment the flow:
      - **Increase** flow on forward edges.
      - **Decrease** flow on backward edges.
6. Update the residual graph.
7. Repeat until **no augmenting path exists**.

### Cuts in a Flow Network
<img width="548" height="242" alt="image" src="https://github.com/user-attachments/assets/fe7f8cda-61f9-4789-a859-432008403f51" />

### Max-Flow Min-Cut Theorem 
##### Theorem
###### The following three values are equal:
1. the value of the maximum flow
2. the capacity of the minimum cut
3. the maximum amount you can push from s to t without breaking capacity or conservation rules

##### Interpretation
 - A cut represents a “bottleneck” in the network.
 - The minimum cut is the tightest bottleneck.
 - The maximum flow is exactly equal to that bottleneck

## Why Ford–Fulkerson Terminates and Finds a Max Flow (Grad-Level Notes)




	

