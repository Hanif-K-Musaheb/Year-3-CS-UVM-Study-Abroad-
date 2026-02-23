# [Week 5]()
### Admissibility
> A heuristic is **admissible** if it **never overestimates** the true cost to reach the goal.
> 
<img width="191" height="67" alt="image" src="https://github.com/user-attachments/assets/b3b74751-c173-4679-8fce-1d44be9b0c0d" />

##### Where:
 - h(n) = heuristic estimate
 - h∗(n) = true optimal cost to goal
##### Why this matters:
 - If a heuristic never overestimates, A* is guaranteed to find the optimal solution
   
### Consistency (Monotonicity)
 - Your heuristic should never drop too fast when you move to a neighbor.
>🧠 **Intuition:** Imagine you're walking toward a goal.
>If you're 10 miles away, and you take one small step that costs 1 mile,
your new estimate shouldn't suddenly say you're only 2 miles away.
>That would be suspicious.
>Consistency prevents that.

<img width="252" height="54" alt="image" src="https://github.com/user-attachments/assets/a87622f6-f09b-4243-92ac-280739a2397b" />

##### Translation:

>The estimated cost from where you are should be no more than:
(cost to move to neighbor) + (neighbor’s estimate)

### Optimality
An algorithm is **optimal** if it always finds the **lowest-cost solution**.
### Completeness
An algorithm is complete if it is **guaranteed** to find a **solution if one exists**.
### IDDFS (iterative deepening depth first search)
IDDFS combines:
- The **space efficiency of DFS**
- The **optimality/completeness of BFS**
> easier explanation: this algorithm is used instead of bfs because of space complexity BFS stores all the values in a queue so in a large tree it will use a lot of space. BUT IDDFS instead just repeatedly calls the DFS algorithm with increasing level of depth allowed.
##### IDDFS
 - Same completeness and optimality as **BFS**
 - Same time complexity as **BFS**
 - But same space complexity as **DFS**
### IDA* (iterative deeping A*)
#### Core Idea:
>IDDFS increases depth limit.

>IDA* increases f-cost limit.

>That’s the only difference.

#### Step-by-Step How IDA* Works:
##### Step 1: Initial threshold
 - Start with:
<img width="250" height="65" alt="image" src="https://github.com/user-attachments/assets/42ad507f-151f-4939-983d-514ef2bc71c1" />

##### Step 2: Run DFS
 - But with a rule:
 - Only expand nodes where
<img width="196" height="40" alt="image" src="https://github.com/user-attachments/assets/d573438d-f27b-4194-b400-75464d6098b2" />

 - If a node has larger f-value → stop exploring that branch.

##### Step 3: If goal not found
 - Increase threshold to:
 - The smallest f-value that exceeded the threshold.
 - Then repeat DFS.

#### Why This Is Powerful
 - Like IDDFS:
     - It repeats search.
     - It uses DFS memory (very small).
     - Memory = O(depth).

 - Like A*:
     - Uses heuristic.
     - Finds optimal solution (if heuristic admissible).
