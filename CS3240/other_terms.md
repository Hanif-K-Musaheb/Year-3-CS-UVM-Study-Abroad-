# [misc terms for second exam](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)
### bipartiteness (as in a bipartite graph)

A graph, G=(V,E) is bipartite if its vertex set V can be split into two disjoint sets 
R (called parts) such that every edge connects a vertex in 
L to a vertex in 𝑅. No edge is allowed between vertices within the same part.

###### How to Test Bipartiteness
 - Use BFS or DFS:
 - Assign the start vertex a color.
 - Assign alternating colors to neighbors.
 - If you ever find an edge connecting two vertices of the same color, the graph is **not** bipartite.



### a matching on a bipartite graph
### completeness (as in a complete graph)
> **Definition**: A graph is complete if every pair of distinct vertices is connected by an edge.

<img width="523" height="117" alt="image" src="https://github.com/user-attachments/assets/3ad55635-e09f-4e1f-9ca2-a4a567c8e195" />

### the degree of a node in a graph
> **Definition**: The degree of a vertex `𝑣` in an undirected graph **is the number of edges incident** to `𝑣`
