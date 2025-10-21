# [Greedy Algorithms](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)
-  [x] Interval scheduling: be able to trace the algorithm
-  [x] Dijkstra’s Algorithm: be able to trace the algorithm
-  [ ] minimum spanning trees: characteristics; tracing Prim’s and Kruskal’s algorithms
-  [ ] be able to describe and apply (but not prove) the cycle property and the cut property
-  [ ] graduate students: be able to understand why Dijkstra’s algorithm produces correct
results
- graduate students: be able to explain why the cycle property and the cut property
hold

## Interval scheduling
 - Interval Scheduling is a classic greedy algorithm problem.
 - You are given a set of activities (or intervals) each with a start time and finish time, and you want to select the maximum number of mutually compatible activities — i.e., no overlapping intervals.

#### Greedy Strategy
 - Sort all intervals by their finish time (earliest finish first).
 - Iteratively select an interval if it doesn’t overlap with the last chosen one.

#### Complexity
Complexity: 𝑂(𝑛log𝑛)

## Dijkstra’s algorithm
 - Dijkstra’s algorithm finds the shortest path from a starting node to all other nodes in a weighted graph — as long as all edge weights are nonnegative.
#### problem setup
 - A set of vertices (nodes)
 - Weighted edges (connections between nodes)
 - A start vertex 𝑠
#### Goal
Find the shortest (minimum total weight) distance from 𝑠 to every other vertex.
####  Core idea (Greedy choice)
1. Keep track of the shortest distance found so far to each vertex.
1. Always choose the unvisited vertex with the smallest known distance.
1. “Lock it in” — once a vertex’s shortest distance is known, it never changes.
1. Update the distances to its neighbors if shorter paths are found.



