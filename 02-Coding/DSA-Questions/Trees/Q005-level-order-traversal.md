# Q005: Level Order Traversal (BFS)

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #102, TCS NQT        |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `binary-tree`, `bfs`, `queue`, `level-order` |

---

## Problem Statement

Given the root of a binary tree, return the **level order traversal** of its nodes' values (i.e., from left to right, level by level).

---

## Input Format

- Root node of a binary tree.

## Output Format

- A 2D list where each inner list contains node values at that level.

---

## Constraints

- The number of nodes is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

## Examples

### Example 1
```
Input:        3
             / \
            9  20
              /  \
             15   7
Output: [[3], [9, 20], [15, 7]]
```

### Example 2
```
Input:   1
Output: [[1]]
```

---

## Hints

1. Use a queue for BFS.
2. Process all nodes at the current level before moving to the next.
3. Track the size of the queue at each level to separate levels.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| BFS (Queue)    | O(n)     | O(w)    |

where w = maximum width of tree

---

**Solution:** [Solutions-CPP/Trees/Q005-level-order-traversal.cpp](../../Solutions-CPP/Trees/Q005-level-order-traversal.cpp)
