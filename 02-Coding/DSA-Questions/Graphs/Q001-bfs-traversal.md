# Q001: BFS Traversal of Graph

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Graphs                         |
| **Source**      | LeetCode, TCS NQT, GFG        |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `graph`, `bfs`, `queue`, `traversal` |

---

## Problem Statement

Given an undirected graph represented as an adjacency list and a source vertex, perform a **Breadth-First Search (BFS)** traversal starting from the source.

Return the BFS traversal order.

---

## Input Format

- Number of vertices `V` and edges `E`.
- `E` edges as pairs `(u, v)`.
- Source vertex `src`.

## Output Format

- List of vertices in BFS order.

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
Output: [0, 1, 2, 3, 4]
```
**Explanation:** Start at 0, visit neighbors 1 and 2, then their neighbors 3 and 4.

### Example 2
```
Input:  V=3, E=2
        Edges: (0,1), (1,2)
        src = 2
Output: [2, 1, 0]
```

---

## Hints

1. Use a queue and a visited array.
2. Enqueue the source, mark visited.
3. While queue is not empty: dequeue, process, enqueue all unvisited neighbors.

---

## Approach Overview

| Approach       | Time       | Space     |
|----------------|------------|-----------|
| BFS (Queue)    | O(V + E)   | O(V)      |

---

**Solution:** [Solutions-CPP/Graphs/Q001-bfs-traversal.cpp](../../Solutions-CPP/Graphs/Q001-bfs-traversal.cpp)
