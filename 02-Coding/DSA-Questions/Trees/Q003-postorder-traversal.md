# Q003: Binary Tree Postorder Traversal

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #145, TCS NQT        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `binary-tree`, `traversal`, `recursion`, `stack` |

---

## Problem Statement

Given the root of a binary tree, return the **postorder traversal** of its nodes' values.

**Postorder:** Left -> Right -> Root

---

## Input Format

- Root node of a binary tree.

## Output Format

- A list of integers representing the postorder traversal.

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
Output: [3, 2, 1]
```

### Example 2
```
Input:        1
             / \
            2   3
           / \
          4   5
Output: [4, 5, 2, 3, 1]
```

---

## Hints

1. **Recursive:** Recurse left, recurse right, then process root.
2. **Iterative:** Modified preorder (Root-Right-Left) then reverse the result.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive      | O(n)     | O(h)    |
| Iterative      | O(n)     | O(n)    |

---

**Solution:** [Solutions-CPP/Trees/Q003-postorder-traversal.cpp](../../Solutions-CPP/Trees/Q003-postorder-traversal.cpp)
