# Q004: Height/Depth of Binary Tree

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #104, TCS NQT        |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `binary-tree`, `recursion`, `bfs`, `depth` |

---

## Problem Statement

Given the root of a binary tree, return its **maximum depth** (height).

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Input Format

- Root node of a binary tree.

## Output Format

- An integer representing the maximum depth.

---

## Constraints

- The number of nodes is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Examples

### Example 1
```
Input:        3
             / \
            9  20
              /  \
             15   7
Output: 3
```

### Example 2
```
Input:   1
          \
           2
Output: 2
```

---

## Hints

1. **Recursive:** Height = 1 + max(height of left subtree, height of right subtree).
2. **BFS:** Count the number of levels using level-order traversal.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive DFS  | O(n)     | O(h)    |
| BFS (levels)   | O(n)     | O(w)    |

where w = maximum width of tree

---

**Solution:** [Solutions-CPP/Trees/Q004-height-of-tree.cpp](../../Solutions-CPP/Trees/Q004-height-of-tree.cpp)
