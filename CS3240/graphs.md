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
 - and it does not contain a cyc
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




