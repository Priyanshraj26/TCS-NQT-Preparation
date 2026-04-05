# Q006: Check if Tree is BST

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #98, TCS NQT         |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `binary-tree`, `bst`, `recursion`, `inorder` |

---

## Problem Statement

Given the root of a binary tree, determine if it is a **valid Binary Search Tree (BST)**.

A valid BST is defined as:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be BSTs.

---

## Input Format

- Root node of a binary tree.

## Output Format

- `true` if the tree is a valid BST, `false` otherwise.

---

## Constraints

- The number of nodes is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

---

## Examples

### Example 1
```
Input:     2
          / \
         1   3
Output: true
```

### Example 2
```
Input:     5
          / \
         1   4
            / \
           3   6
Output: false
```
**Explanation:** Root's right child is 4, which is less than 5. Not a valid BST.

---

## Hints

1. **Wrong approach:** Just checking left child < root < right child is NOT enough. You must check against the entire subtree range.
2. **Range-based:** Pass min/max bounds recursively.
3. **Inorder approach:** Inorder traversal of a BST gives sorted order.

---

## Approach Overview

| Approach           | Time     | Space   |
|--------------------|----------|---------|
| Range checking     | O(n)     | O(h)    |
| Inorder traversal  | O(n)     | O(h)    |

---

**Solution:** [Solutions-CPP/Trees/Q006-check-bst.cpp](../../Solutions-CPP/Trees/Q006-check-bst.cpp)
