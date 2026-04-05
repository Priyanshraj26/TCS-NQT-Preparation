# Q004: Shortest Path in Unweighted Graph (BFS)

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Graphs                         |
| **Source**      | TCS NQT, GFG, Interview        |
| **Frequency**  | ★★★ (Medium)                  |
| **Tags**       | `graph`, `bfs`, `shortest-path` |

---

## Problem Statement

Given an unweighted undirected graph with `V` vertices and `E` edges, find the **shortest path** (minimum number of edges) from a source vertex `src` to all other vertices.

---

## Input Format

- Number of vertices `V`, edges `E`.
- `E` edges as pairs `(u, v)`.
- Source vertex `src`.

## Output Format

- Array of shortest distances from `src` to each vertex. Use `-1` for unreachable vertices.

---

## Constraints

- `1 <= V <= 10^4`
- `0 <= E <= V*(V-1)/2`

---

## Examples

### Example 1
```
Input:  V=6, E=7
        Edges: (0,1),(0,2),(1,3),(2,3),(3,4),(4,5),(2,5)
        src = 0
Output: [0, 1, 1, 2, 3, 2]
```
**Explanation:** Distance from 0: to 0=0, to 1=1, to 2=1, to 3=2, to 4=3, to 5=2.

### Example 2
```
Input:  V=3, E=1, Edge: (0,1), src=0
Output: [0, 1, -1]
```
**Explanation:** Vertex 2 is unreachable from 0.

---

## Hints

1. BFS naturally finds shortest paths in unweighted graphs.
2. Use a distance array initialized to -1 (or infinity).
3. When visiting a neighbor, set its distance = current distance + 1.

---

## Approach Overview

| Approach       | Time       | Space     |
|----------------|------------|-----------|
| BFS            | O(V + E)   | O(V)      |

---

**Solution:** [Solutions-CPP/Graphs/Q004-shortest-path-unweighted.cpp](../../Solutions-CPP/Graphs/Q004-shortest-path-unweighted.cpp)
