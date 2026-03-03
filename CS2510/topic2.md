# [Heuristic search: A*, IDA*; admissibility and consistency](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS2510/CS2510home.md)

## A*
>**A*** is a pathfinding algorithm. It finds the shortest path from a start node to a goal node

At every step, A* chooses the node with the smallest value of:

<img width="231" height="53" alt="image" src="https://github.com/user-attachments/assets/7f89afa3-969b-4508-a219-98c83a2d56c8" />

 - **g(n)** = cost from the start to node n
 - **h(n)** = estimated cost from n to the goal (this is called a heuristic)
 - **f(n)** = total estimated cost of a path going through n
> **in other words**: Actual cost so far + Estimated cost remaining

>When A* has multiple possible nodes it could explore next, it **always selects the one with the lowest**

#### why this approach works
 - **g(n)** prevents it from ignoring expensive paths already taken
 - **h(n)** prevents it from wandering aimlessly

#### open set
> Nodes we have discovered but haven’t fully explored yet.

> Or the **priority queue**, ordered by lowest f(n)
#### closed set
> Nodes we have already fully explored.

## IDA* (Iterative Deepening A*)
> **IDA*** is a memory-efficient version of A*.

#### combines tow ideas
 - A* (uses f(n)=g(n)+h(n))
 - Iterative Deepening DFS (searches with increasing limits)

### How It Works Step-by-Step
1. Set threshold = f(start)
1. Do a DFS, but:
   - If f(n) > threshold → stop exploring that branch
1. If goal not found:
   - Increase threshold to the smallest f(n) that was too large
1. Repeat

-------------

| Algorithm | Memory   | Speed          |
| --------- | -------- | -------------- |
| A*        | High  O(d)   | Usually faster |
| IDA*      | Very low  O(b^d) | Can be slower  |

### Admissable 
The heuristic never overestimates the real cost.
### Consistent
A heuristic is consistent if:

<img width="248" height="43" alt="image" src="https://github.com/user-attachments/assets/01fee99f-fd9a-4860-bc11-f2f679338ffb" />

Where:
`c(n,n′)` = cost to move from node `n` to neighbor `n′`

In simple words: The estimate must obey the triangle inequality.(The estimated cost from cannot be more than cost to neighbor + estimate from neighbor).



-------------


