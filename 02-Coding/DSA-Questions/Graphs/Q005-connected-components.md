# Q005: Number of Connected Components

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Graphs                         |
| **Source**      | LeetCode #323, TCS NQT        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `graph`, `dfs`, `bfs`, `connected-components`, `union-find` |

---

## Problem Statement

Given an undirected graph with `V` vertices (labeled 0 to V-1) and `E` edges, find the **number of connected components**.

---

## Input Format

- Number of vertices `V` and edges `E`.
- `E` edges as pairs `(u, v)`.

## Output Format

- An integer: the number of connected components.

---

## Constraints

- `1 <= V <= 10^5`
- `0 <= E <= V*(V-1)/2`

---

## Examples

### Example 1
```
Input:  V=5, E=3
        Edges: (0,1), (1,2), (3,4)
Output: 2
```
**Explanation:** Component 1: {0,1,2}, Component 2: {3,4}.

### Example 2
```
Input:  V=4, E=0
Output: 4
```
**Explanation:** No edges, each vertex is its own component.

---

## Hints

1. Run DFS/BFS from each unvisited vertex.
2. Each new DFS/BFS call = one new connected component.
3. Count the number of times you start a new traversal.

---

## Approach Overview

| Approach       | Time       | Space     |
|----------------|------------|-----------|
| DFS/BFS        | O(V + E)   | O(V)      |

---

**Solution:** [Solutions-CPP/Graphs/Q005-connected-components.cpp](../../Solutions-CPP/Graphs/Q005-connected-components.cpp)
