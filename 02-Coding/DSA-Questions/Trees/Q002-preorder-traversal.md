# Q002: Binary Tree Preorder Traversal

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #144, TCS NQT        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `binary-tree`, `traversal`, `recursion`, `stack` |

---

## Problem Statement

Given the root of a binary tree, return the **preorder traversal** of its nodes' values.

**Preorder:** Root -> Left -> Right

---

## Input Format

- Root node of a binary tree.

## Output Format

- A list of integers representing the preorder traversal.

---

## Constraints

- The number of nodes is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Examples

### Example 1
```
Input:     1
            \
             2
            /
           3
Output: [1, 2, 3]
```

### Example 2
```
Input:        1
             / \
            2   3
           / \
          4   5
Output: [1, 2, 4, 5, 3]
```

---

## Hints

1. **Recursive:** Process root first, then recurse left, then right.
2. **Iterative:** Use a stack. Push right child first, then left (so left is processed first).

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive      | O(n)     | O(h)    |
| Iterative      | O(n)     | O(h)    |

---

**Solution:** [Solutions-CPP/Trees/Q002-preorder-traversal.cpp](../../Solutions-CPP/Trees/Q002-preorder-traversal.cpp)
