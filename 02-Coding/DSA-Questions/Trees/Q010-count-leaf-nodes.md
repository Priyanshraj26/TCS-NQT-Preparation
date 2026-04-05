# Q010: Count Leaf Nodes

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Trees                          |
| **Source**      | TCS NQT, Basic Interview       |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `binary-tree`, `recursion`, `bfs`, `leaf` |

---

## Problem Statement

Given the root of a binary tree, count the number of **leaf nodes** (nodes with no children).

---

## Input Format

- Root node of a binary tree.

## Output Format

- An integer representing the count of leaf nodes.

---

## Constraints

- The number of nodes is in the range `[0, 10^4]`.
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
**Explanation:** Leaf nodes are 4, 5, and 3.

### Example 2
```
Input:   1
Output: 1
```
**Explanation:** Single node is itself a leaf.

### Example 3
```
Input:   NULL (empty tree)
Output: 0
```

---

## Hints

1. A leaf node has both left and right children as NULL.
2. Recursively count leaves in left and right subtrees.
3. Can also use BFS -- count nodes with no children.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Recursive DFS  | O(n)     | O(h)    |
| Iterative BFS  | O(n)     | O(w)    |

---

**Solution:** [Solutions-CPP/Trees/Q010-count-leaf-nodes.cpp](../../Solutions-CPP/Trees/Q010-count-leaf-nodes.cpp)
