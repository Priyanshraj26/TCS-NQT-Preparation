# Q008: Mirror/Invert a Binary Tree

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Trees                          |
| **Source**      | LeetCode #226, TCS NQT        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `binary-tree`, `recursion`, `bfs` |

---

## Problem Statement

Given the root of a binary tree, **invert** (mirror) the tree and return its root.

---

## Input Format

- Root node of a binary tree.

## Output Format

- Root of the inverted binary tree.

---

## Constraints

- The number of nodes is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Examples

### Example 1
```
Input:        4
             / \
            2   7
           / \ / \
          1  3 6  9

Output:       4
             / \
            7   2
           / \ / \
          9  6 3  1
```

### Example 2
```
Input:   2
        / \
       1   3
Output:  2
        / \
       3   1
```

---

## Hints

1. Swap left and right children at every node.
2. Recursively invert left subtree and right subtree.
3. Can also be done iteratively with BFS.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive      | O(n)     | O(h)    |
| Iterative BFS  | O(n)     | O(w)    |

---

**Solution:** [Solutions-CPP/Trees/Q008-mirror-tree.cpp](../../Solutions-CPP/Trees/Q008-mirror-tree.cpp)
