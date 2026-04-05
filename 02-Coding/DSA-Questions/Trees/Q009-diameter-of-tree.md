# Q009: Diameter of Binary Tree

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #543, TCS NQT        |
| **Frequency**  | ★★★ (Medium)                  |
| **Tags**       | `binary-tree`, `recursion`, `depth` |

---

## Problem Statement

Given the root of a binary tree, return the length of the **diameter** of the tree.

The diameter is the length of the **longest path** between any two nodes. This path may or may not pass through the root. The length is measured by the number of **edges**.

---

## Input Format

- Root node of a binary tree.

## Output Format

- An integer representing the diameter (number of edges on the longest path).

---

## Constraints

- The number of nodes is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Examples

### Example 1
```
Input:        1
             / \
            2   3
           / \
          4   5
Output: 3
```
**Explanation:** Longest path is 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3), which has 3 edges.

### Example 2
```
Input:   1
          \
           2
Output: 1
```

---

## Hints

1. At each node, the diameter passing through it = height(left) + height(right).
2. The answer is the maximum diameter across all nodes.
3. Compute height and diameter in a single DFS pass.

---

## Approach Overview

| Approach               | Time     | Space   |
|------------------------|----------|---------|
| DFS (single pass)      | O(n)     | O(h)    |

---

**Solution:** [Solutions-CPP/Trees/Q009-diameter-of-tree.cpp](../../Solutions-CPP/Trees/Q009-diameter-of-tree.cpp)
