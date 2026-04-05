# Q007: Lowest Common Ancestor in BST

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #235, TCS NQT        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `bst`, `recursion`, `lca` |

---

## Problem Statement

Given a Binary Search Tree (BST) and two nodes `p` and `q`, find the **Lowest Common Ancestor (LCA)** of the two nodes.

The LCA is the deepest node that has both `p` and `q` as descendants (a node can be a descendant of itself).

---

## Input Format

- Root of a BST, and two node values `p` and `q`.

## Output Format

- The LCA node.

---

## Constraints

- The number of nodes is in the range `[2, 10^5]`.
- All node values are unique.
- `p != q`
- `p` and `q` exist in the BST.

---

## Examples

### Example 1
```
Input:        6
             / \
            2   8
           / \ / \
          0  4 7  9
            / \
           3   5
        p = 2, q = 8
Output: 6
```
**Explanation:** LCA of 2 and 8 is 6 (root).

### Example 2
```
Same tree, p = 2, q = 4
Output: 2
```
**Explanation:** A node can be its own ancestor.

---

## Hints

1. In a BST, if both p and q are smaller than root, LCA is in the left subtree.
2. If both are larger, LCA is in the right subtree.
3. If one is on each side (or one equals root), the current node is the LCA.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive      | O(h)     | O(h)    |
| Iterative      | O(h)     | O(1)    |

---

**Solution:** [Solutions-CPP/Trees/Q007-lca-bst.cpp](../../Solutions-CPP/Trees/Q007-lca-bst.cpp)
