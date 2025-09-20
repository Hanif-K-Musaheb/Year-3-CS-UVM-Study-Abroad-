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



