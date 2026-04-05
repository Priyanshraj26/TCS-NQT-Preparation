# Q003: Detect Cycle in Undirected Graph

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Graphs                         |
| **Source**      | LeetCode, TCS NQT, GFG        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `graph`, `dfs`, `bfs`, `cycle-detection`, `union-find` |

---

## Problem Statement

Given an undirected graph with `V` vertices and `E` edges, detect whether the graph contains a **cycle**.

---

## Input Format

- Number of vertices `V` and edges `E`.
- `E` edges as pairs `(u, v)`.

## Output Format

- `true` if the graph contains a cycle, `false` otherwise.

---

## Constraints

- `1 <= V <= 10^5`
- `0 <= E <= V*(V-1)/2`
- No self-loops or multiple edges.

---

## Examples

### Example 1
```
Input:  V=4, E=4
        Edges: (0,1), (1,2), (2,3), (3,0)
Output: true
```
**Explanation:** 0->1->2->3->0 forms a cycle.

### Example 2
```
Input:  V=3, E=2
        Edges: (0,1), (1,2)
Output: false
```
**Explanation:** This is a simple path, no cycle.

---

## Hints

1. **DFS:** If you visit a node that is already visited and it is NOT the parent of the current node, there is a cycle.
2. **BFS:** Same logic -- if a visited neighbor is not the parent, cycle exists.
3. **Union-Find:** If two nodes of an edge are already in the same set, adding this edge creates a cycle.

---

## Approach Overview

| Approach       | Time       | Space     |
|----------------|------------|-----------|
| DFS            | O(V + E)   | O(V)      |
| BFS            | O(V + E)   | O(V)      |

---

**Solution:** [Solutions-CPP/Graphs/Q003-detect-cycle-undirected.cpp](../../Solutions-CPP/Graphs/Q003-detect-cycle-undirected.cpp)
