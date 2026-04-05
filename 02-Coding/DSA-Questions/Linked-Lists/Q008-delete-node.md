# Q008: Delete a Node (Given Only Pointer to It)

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #237, TCS NQT        |
| **Frequency**  | ★★★ (Medium)                  |
| **Tags**       | `linked-list`, `pointer-manipulation` |

---

## Problem Statement

There is a singly linked list. You are given only a pointer/reference to the node to be deleted (not the head of the list). Delete the given node. Note that the given node is **not** the tail node.

---

## Input Format

- A pointer to the node to be deleted.
- The node is guaranteed not to be the tail.

## Output Format

- The linked list with the given node removed.

---

## Constraints

- The number of nodes is in the range `[2, 1000]`.
- `-1000 <= Node.val <= 1000`
- The value of each node is unique.
- The node to be deleted is not the tail.

---

## Examples

### Example 1
```
Input:  List: 4 -> 5 -> 1 -> 9,  node = 5
Output: 4 -> 1 -> 9
```
**Explanation:** Copy the next node's value (1) into the current node (5), then delete the next node.

### Example 2
```
Input:  List: 4 -> 5 -> 1 -> 9,  node = 1
Output: 4 -> 5 -> 9
```

---

## Hints

1. You do NOT have access to the head -- you cannot traverse from the beginning.
2. Copy the value of the next node into the current node.
3. Then point current node's next to next's next (effectively deleting the next node).

---

## Approach Overview

| Approach           | Time     | Space   |
|--------------------|----------|---------|
| Copy and delete    | O(1)     | O(1)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q008-delete-node.cpp](../../Solutions-CPP/Linked-Lists/Q008-delete-node.cpp)
