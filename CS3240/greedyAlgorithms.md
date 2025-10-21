# [Greedy Algorithms](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)


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

## MST (minimum spanning tree)
Given a **connected**, **undirected**, **weighted graph**, a **spanning tree** is a subset of edges that:
 - Connects **all** vertices together
 - Has **no** cycles
 - Has exactly V − 1 edges (where V = number of vertices)

##### General Description
A **Minimum Spanning Tree (MST)** is the spanning tree with the **minimum total edge weight** among all possible spanning trees.

##### Properties
- **Cut property** For any cut (partition of vertices into two sets), the MST includes the lightest edge crossing the cut.
- **Cycle property** For any cycle, the heaviest edge in that cycle is not part of the MST.

### Prims Algorithm
##### General Description
Start from one vertex and grow the MST one edge at a time — always choosing the **minimum-weight edge** that connects a vertex **inside** the tree to a vertex **outside** it.
##### Pseudo code
```
Prim(Graph, start):
    MST = []
    visited = {start}
    while not all vertices are visited:
        choose the smallest edge (u, v) where u ∈ visited, v ∉ visited
        add (u, v) to MST
        mark v as visited
    return MST
```

### Kruskal's Algorithm
Start with **all vertices** and **no edges**.
Add edges in **increasing order of weight**, skipping any that would **form a cycle**, until you have 
𝑉−1 edges.
##### Pseudocode
```
Kruskal(Graph):
    sort all edges by increasing weight
    MST = []
    for each edge (u, v) in sorted order:
        if u and v are in different sets:
            add (u, v) to MST
            union(u, v)
    return MST
```

