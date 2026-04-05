# Q001: Binary Tree Inorder Traversal

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #94, TCS NQT         |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `binary-tree`, `traversal`, `recursion`, `stack` |

---

## Problem Statement

Given the root of a binary tree, return the **inorder traversal** of its nodes' values.

**Inorder:** Left -> Root -> Right

---

## Input Format

- Root node of a binary tree.

## Output Format

- A list of integers representing the inorder traversal.

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
Output: [1, 3, 2]
```

### Example 2
```
Input:        4
             / \
            2   6
           / \ / \
          1  3 5  7
Output: [1, 2, 3, 4, 5, 6, 7]
```
**Explanation:** For a BST, inorder traversal gives sorted order.

---

## Hints

1. **Recursive:** Recursively visit left subtree, then root, then right subtree.
2. **Iterative:** Use a stack. Push all left children, then process, then go right.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive      | O(n)     | O(h)    |
| Iterative      | O(n)     | O(h)    |

where h = height of tree (log n for balanced, n for skewed)

---

**Solution:** [Solutions-CPP/Trees/Q001-inorder-traversal.cpp](../../Solutions-CPP/Trees/Q001-inorder-traversal.cpp)
