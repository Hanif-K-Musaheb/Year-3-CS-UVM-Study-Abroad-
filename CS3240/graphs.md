# [Graphs](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)
### Dependency Network
### Path
We say there is a path in an undirected graph 𝐺 from 𝑣𝑗 to 𝑣𝑘 when:
 - there is a sequence of edges from consecutive pairs of nodes 𝑣𝑗 , 𝑣𝑗+1, ..., 𝑣𝑘−1, 𝑣𝑘

##### Cycle
A cycle is a path in which the first and last nodes are the same

### Tree
An undirected graph G is a tree when:
 - it is connected
 - and it does not contain a cycle
     - given a tree having 𝑛 nodes, how many edges are there?
     - there are 𝑛 − 1 edges
  
### BFS (Breadth First Search)
##### Basic (and simple!) idea
 - start at a given node
 - and explore outward in all possible directions
 - adding new nodes one “layer” at a time
##### More specifically:
 - start at a particular node 𝑠
 - then visit each of the unvisited nodes that are joined by an edge to 𝑠
 - then visit each of the unvisited nodes that are joined by an edge to a node in that second group
 - and so on, until no unvisited nodes are encountered
 - and at this point, we will have reached every connected node to the root node so depending on the graph we may or may not have reached every node.

### DFS Depth-First Search 
Similarly, to explore a graph:
 - start at a node 𝑠
 - pick an edge from 𝑠, and use that edge to move to a different unexplored node 𝑡
 - and pick and edge from 𝑡 and move to a different unexplored node 𝑢
 - and keep doing this until we can't move to an unexplored node
 - then, backtrack: go back up the chain of explored nodes until we find an edgethat will take us to an unexplored node and keep doing this until we can't move to an unexplored node

#### DFS will also yield a tree:
 - called a depth-first search tree
 - rooted at the starting node
 - and consisting of the connected component containing the starting node
 - and representing, through its structure, the order in which the nodes were explored


### Representing Graphs
A simple way to represent a graph
- using an adjacency matrix
- assume the nodes in 𝑉 are numbered 1, 2, 3, ... , 𝑛
- build an 𝑛 × 𝑛 matrix 𝐴, in which 𝐴𝑢,𝑣 is 1 if the graph contains an edge 𝑢. 𝑣 , and 0 otherwise
#### For an undirected graph:
- we'll say that 𝐴 must be symmetric
- so if 𝐴𝑢,𝑣 = 1, then we must also have 𝐴𝑣,𝑢 = 1 for all nodes 𝑢, 𝑣 ∈ 𝑉
#### And so for a directed graph:
- 𝐴 does not have to be symmetric

<img width="700" height="290" alt="image" src="https://github.com/user-attachments/assets/3cd9e8b3-df65-4ec9-a827-cbb3eb310ecd" />

| Advantages                                                                 | Disadvantages                                                                                                       |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| • We can check whether an edge (u, v) exists in **O(1)** time <br> • i.e., in constant time (independent of m or n) | • The representation takes **Θ(n²)** space <br> • When m = E ≪ n², most entries will be zero → very inefficient memory use <br> • For a given node u, examining all edges incident to u requires **O(n)** time in the worst case <br> • Realistically, each node u has only a small number of incident edges, so we might want a more efficient way to find them |


### Bipartite Graph
In a bipartite graph, the node set 𝑉 can be partitioned into sets 𝑋 and 𝑌 such that every edge has one end in 𝑋 and one end in 𝑌. A bipartite graph can not habr an odd cycle in it.

##### BFS & Bipartite Graphs
BFS will let us color a graph naturally
 - color the initial node blue
 - color all adjacent nodes red
 - color each of the nodes adjacent to those nodes blue

### Directed graphs
#### Strong Connectivity 
We say that a directed graph is strongly connected if:
 - for every two nodes 𝑢 and 𝑣, there is a path from 𝑢 to 𝑣 and a path from 𝑣 to 𝑢
 - so a directed graph is strongly connected if every pair of nodes is mutually reachable

#### To check whether a graph 𝐺 is strongly connected:
 - pick a node 𝑠 and run DFS or BFS in 𝐺
 - then run DFS or BFS, again starting from 𝑠, in 𝐺𝑟𝑒𝑣
 - if one of these two searches fails to reach every node, then 𝐺 is not strongly connected

<img width="425" height="160" alt="image" src="https://github.com/user-attachments/assets/01d520eb-1924-4de1-be2c-cb44c6e0cffe" />

#### Directed Acyclic Graphs (DAG)
Fact: if an undirected graph has no cycles, then each of its connected components is a tree
A directed graph that has no cycles is called a directed acyclic graph (DAG)
- DAGs are common in computer science
- they model dependency relationships

#### Topological Ordering
 - A way to order nodes in a DAG so that all edges go forward.
 - Example: ordering courses so prerequisites are taken first.
Theorem:
 - If a graph has a topological ordering, it must be a DAG.
 - Every DAG has at least one node with no incoming edges (a “starting task”).



### Algorithms for Topological Ordering
#### Basic Algorithm (O(n²))
##### Idea: 
Repeatedly find a node with no incoming edges, add it to the ordering, and remove it.
##### Steps:
1. Find a node with no incoming edges.
2. Add it to the output list (this is the next in the order).
3. Remove the node and all its outgoing edges from the graph.
4. Repeat until all nodes are processed.
##### Running time:
 - Each step may require scanning all nodes to find one with no incoming edges.
 - That makes it O(n²) in the worst case.
 - When it works best: dense graphs (lots of edges)
#### Refined Algorithm (Kahn’s Algorithm, O(m + n))
[Youtube Video explaining it (important part is at min 6)](https://www.youtube.com/watch?v=cIBFEhD77b4)
##### **Goal**: 
make the process more efficient by keeping track of "ready-to-remove" nodes dynamically.
##### **Key ideas**:
 - Maintain the number of active incoming edges for each node.
 - Keep a set S of nodes that have zero incoming edges.
##### Steps: 
1. Initialize:
   - Mark all nodes as active.
   - Compute incoming edge counts for each node.
   - Place all nodes with 0 incoming edges into set S.
2. While S is not empty:
   - Select a node v from S and add it to the topological order.
   - Remove v from the graph (mark inactive).
   - For each neighbor w of v:
      - Reduce w’s incoming edge count by 1.
      - If w now has 0 incoming edges, add it to S.
3. Continue until all nodes are removed.
###### Running time:
 - Initialization = O(m + n) (scan through all nodes and edges once).
 - Each edge is considered only once when we reduce counts.
 - Total = O(m + n).
###### Failure case:
 - If the graph has a cycle, eventually S becomes empty while some nodes remain.
 - This means no valid topological order exists.

``` java
/**
 * This topological sort implementation takes an adjacency list of an acyclic graph and returns an
 * array with the indexes of the nodes in a (non unique) topological order which tells you how to
 * process the nodes in the graph. More precisely from wiki: A topological ordering is a linear
 * ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes
 * before v in the ordering.
 *
 * <p>Time Complexity: O(V + E)
 *
 * @author William Fiset, william.alexandre.fiset@gmail.com
 */
package com.williamfiset.algorithms.graphtheory;

import java.util.*;

public class TopologicalSortAdjacencyList {

  // Helper Edge class to describe edges in the graph
  static class Edge {
    int from, to, weight;

    public Edge(int f, int t, int w) {
      from = f;
      to = t;
      weight = w;
    }
  }

  // Helper method that performs a depth first search on the graph to give
  // us the topological ordering we want. Instead of maintaining a stack
  // of the nodes we see we simply place them inside the ordering array
  // in reverse order for simplicity.
  private static int dfs(
      int i, int at, boolean[] visited, int[] ordering, Map<Integer, List<Edge>> graph) {

    visited[at] = true;

    List<Edge> edges = graph.get(at);

    if (edges != null)
      for (Edge edge : edges) if (!visited[edge.to]) i = dfs(i, edge.to, visited, ordering, graph);

    ordering[i] = at;
    return i - 1;
  }

  // Finds a topological ordering of the nodes in a Directed Acyclic Graph (DAG)
  // The input to this function is an adjacency list for a graph and the number
  // of nodes in the graph.
  //
  // NOTE: 'numNodes' is not necessarily the number of nodes currently present
  // in the adjacency list since you can have singleton nodes with no edges which
  // wouldn't be present in the adjacency list but are still part of the graph!
  //
  public static int[] topologicalSort(Map<Integer, List<Edge>> graph, int numNodes) {

    int[] ordering = new int[numNodes];
    boolean[] visited = new boolean[numNodes];

    int i = numNodes - 1;
    for (int at = 0; at < numNodes; at++)
      if (!visited[at]) i = dfs(i, at, visited, ordering, graph);

    return ordering;
  }

  // A useful application of the topological sort is to find the shortest path
  // between two nodes in a Directed Acyclic Graph (DAG). Given an adjacency list
  // this method finds the shortest path to all nodes starting at 'start'
  //
  // NOTE: 'numNodes' is not necessarily the number of nodes currently present
  // in the adjacency list since you can have singleton nodes with no edges which
  // wouldn't be present in the adjacency list but are still part of the graph!
  //
  public static Integer[] dagShortestPath(Map<Integer, List<Edge>> graph, int start, int numNodes) {

    int[] topsort = topologicalSort(graph, numNodes);
    Integer[] dist = new Integer[numNodes];
    dist[start] = 0;

    for (int i = 0; i < numNodes; i++) {

      int nodeIndex = topsort[i];
      if (dist[nodeIndex] != null) {
        List<Edge> adjacentEdges = graph.get(nodeIndex);
        if (adjacentEdges != null) {
          for (Edge edge : adjacentEdges) {

            int newDist = dist[nodeIndex] + edge.weight;
            if (dist[edge.to] == null) dist[edge.to] = newDist;
            else dist[edge.to] = Math.min(dist[edge.to], newDist);
          }
        }
      }
    }

    return dist;
  }

  // Example usage of topological sort
  public static void main(String[] args) {

    // Graph setup
    final int N = 7;
    Map<Integer, List<Edge>> graph = new HashMap<>();
    for (int i = 0; i < N; i++) graph.put(i, new ArrayList<>());
    graph.get(0).add(new Edge(0, 1, 3));
    graph.get(0).add(new Edge(0, 2, 2));
    graph.get(0).add(new Edge(0, 5, 3));
    graph.get(1).add(new Edge(1, 3, 1));
    graph.get(1).add(new Edge(1, 2, 6));
    graph.get(2).add(new Edge(2, 3, 1));
    graph.get(2).add(new Edge(2, 4, 10));
    graph.get(3).add(new Edge(3, 4, 5));
    graph.get(5).add(new Edge(5, 4, 7));

    int[] ordering = topologicalSort(graph, N);

    // // Prints: [6, 0, 5, 1, 2, 3, 4]
    System.out.println(java.util.Arrays.toString(ordering));

    // Finds all the shortest paths starting at node 0
    Integer[] dists = dagShortestPath(graph, 0, N);

    // Find the shortest path from 0 to 4 which is 8.0
    System.out.println(dists[4]);

    // Find the shortest path from 0 to 6 which
    // is null since 6 is not reachable!
    System.out.println(dists[6]);
  }
}
```

# Graph Theory Quick Reference


| Concept / Formula | Explanation |
|---|---|
| **Spanning tree** | A subgraph that contains all vertices, is connected, and has no cycles. |
| `Edges in a tree` | For a tree with `n` vertices: `m = n - 1`. |
| `Every connected graph has a spanning tree` | True — you can obtain one by deleting edges until no cycle remains while keeping the graph connected. |
| `Cayley's formula` | Number of spanning trees in `K_n`: `n^(n-2)`. |
| `Handshaking lemma` | Sum of degrees = `2m`. (i.e., `sum_{v in V} deg(v) = 2m`) |
| `Average degree` | `d_avg = 2m / n`. |
| `Max edges (simple graph)` | `m_max = n(n-1)/2` (complete graph `K_n`). |
| `Edges in complete graph K_n` | `m = n(n-1)/2`. |
| `Max edges (bipartite with parts n1,n2)` | `m_max = n1 * n2`. Over all partitions this ≤ `floor(n^2 / 4)`. |
| `Min edges (connected graph)` | `m_min = n - 1` (a tree). |
| `Cycle C_n` | `m = n`. |
| `Path P_n` | `m = n - 1`. |
| `Tree characterizations` | Equivalent: connected + acyclic; acyclic + m = n-1; connected + m = n-1; minimally connected. |
| `Diameter` | Maximum shortest-path distance between any two vertices; for a tree it's the length of the longest simple path. |



## Kruskals algorithm to produce a MST




