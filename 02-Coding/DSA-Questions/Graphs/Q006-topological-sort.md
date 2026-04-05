# Q006: Topological Sort (Kahn's / DFS)

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Graphs                         |
| **Source**      | LeetCode #210, TCS NQT        |
| **Frequency**  | ★★★ (Medium)                  |
| **Tags**       | `graph`, `dag`, `topological-sort`, `bfs`, `dfs` |

---

## Problem Statement

Given a **Directed Acyclic Graph (DAG)** with `V` vertices and `E` edges, find a **topological ordering** of its vertices.

A topological ordering is a linear ordering of vertices such that for every directed edge `(u, v)`, vertex `u` comes before `v` in the ordering.

---

## Input Format

- Number of vertices `V` and directed edges `E`.
- `E` directed edges as pairs `(u, v)` meaning u -> v.

## Output Format

- A valid topological ordering of vertices.
- (Note: Multiple valid orderings may exist.)

---

## Constraints

- `1 <= V <= 10^4`
- `0 <= E <= V*(V-1)/2`
- The graph is a DAG (no cycles).

---

## Examples

### Example 1
```
Input:  V=6, E=6
        Edges: (5,2), (5,0), (4,0), (4,1), (2,3), (3,1)
Output: [5, 4, 2, 3, 1, 0]  (one valid ordering)
```
**Explanation:** 5 must come before 2 and 0. 4 must come before 0 and 1. Etc.

### Example 2
```
Input:  V=3, E=2
        Edges: (0,1), (1,2)
Output: [0, 1, 2]
```

---

## Hints

1. **Kahn's (BFS):** Start with nodes having in-degree 0. Remove them, reduce in-degrees of neighbors. Repeat.
2. **DFS:** Post-order DFS, then reverse gives topological order.
3. Topological sort only works for DAGs (no cycles).

---

## Approach Overview

| Approach        | Time       | Space     |
|-----------------|------------|-----------|
| Kahn's (BFS)    | O(V + E)   | O(V)      |
| DFS             | O(V + E)   | O(V)      |

---

**Solution:** [Solutions-CPP/Graphs/Q006-topological-sort.cpp](../../Solutions-CPP/Graphs/Q006-topological-sort.cpp)
