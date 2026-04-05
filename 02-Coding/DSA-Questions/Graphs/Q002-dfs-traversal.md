# Q002: DFS Traversal of Graph

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Graphs                         |
| **Source**      | LeetCode, TCS NQT, GFG        |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `graph`, `dfs`, `stack`, `recursion`, `traversal` |

---

## Problem Statement

Given an undirected graph represented as an adjacency list and a source vertex, perform a **Depth-First Search (DFS)** traversal starting from the source.

Return the DFS traversal order.

---

## Input Format

- Number of vertices `V` and edges `E`.
- `E` edges as pairs `(u, v)`.
- Source vertex `src`.

## Output Format

- List of vertices in DFS order.

---

## Constraints

- `1 <= V <= 10^4`
- `0 <= E <= V*(V-1)/2`
- `0 <= src < V`

---

## Examples

### Example 1
```
Input:  V=5, E=4
        Edges: (0,1), (0,2), (1,3), (2,4)
        src = 0
Output: [0, 1, 3, 2, 4]  (one possible order)
```
**Explanation:** Start at 0, go deep into 1->3, backtrack, then 2->4.

### Example 2
```
Input:  V=4, E=3
        Edges: (0,1), (0,2), (0,3)
        src = 0
Output: [0, 1, 2, 3]
```

---

## Hints

1. Use recursion (or explicit stack) and a visited array.
2. Mark node as visited, process it, recurse on unvisited neighbors.
3. DFS explores as deep as possible before backtracking.

---

## Approach Overview

| Approach       | Time       | Space     |
|----------------|------------|-----------|
| Recursive DFS  | O(V + E)   | O(V)      |
| Iterative DFS  | O(V + E)   | O(V)      |

---

**Solution:** [Solutions-CPP/Graphs/Q002-dfs-traversal.cpp](../../Solutions-CPP/Graphs/Q002-dfs-traversal.cpp)
