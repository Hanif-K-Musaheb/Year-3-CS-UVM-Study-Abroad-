# [Independent sets and vertex covers](https://github.com/Hanif-K-Musaheb/Year-3-CS-UVM-Study-Abroad-/blob/main/CS3240/cs3240.md)
## Independent Set — Definition
>An independent set in graph theory is a collection of vertices where no two vertices are connected by an edge, meaning they are "independent" of each other.
##### In other words:
 - Pick some vertices.
 - No edge is allowed between any two chosen vertices.

## Vertex Cover
A vertex cover is a set of vertices C⊆V such that:
 - Every **edge** in the graph has at least **one** **endpoint** in the set.

##### Examples:
 - The set of all vertices is always a vertex cover (trivial).
 - In a triangle,𝐾3, the smallest vertex cover has size 2.

## Relationship Between Independent Sets and Vertex Covers
<img width="942" height="336" alt="image" src="https://github.com/user-attachments/assets/6a238bbd-3bc7-4cbf-b203-a24d4662e9d8" />

## Quick summary
 - **Independent Set**: Set of vertices with no edges between them.
 - **Vertex Cover:** Set of vertices that touch all edges.
 - **Complement relationship:** S is independent ⟺ V∖S is a vertex cover.
 - How to construct:
    - **Independent set**: pick vertices that do not touch each other.
    - **Vertex cover**: pick vertices so every edge has an endpoint chosen.

