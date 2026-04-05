# Q004: Find Middle Element of Linked List

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #876, TCS NQT        |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `linked-list`, `two-pointers`, `slow-fast` |

---

## Problem Statement

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes (even-length list), return the **second middle** node.

---

## Input Format

- Head of a singly linked list.

## Output Format

- Return the middle node of the linked list.

---

## Constraints

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

---

## Examples

### Example 1
```
Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 3 (node with value 3)
```
**Explanation:** The middle node is 3.

### Example 2
```
Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Output: 4 (node with value 4)
```
**Explanation:** Two middle nodes (3 and 4), we return the second one.

---

## Hints

1. **Brute Force:** Count the total length, then traverse to length/2.
2. **Optimal:** Use slow and fast pointers. Slow moves 1 step, fast moves 2 steps. When fast reaches end, slow is at middle.

---

## Approach Overview

| Approach           | Time     | Space   |
|--------------------|----------|---------|
| Two-pass (count)   | O(n)     | O(1)    |
| Slow-Fast pointer  | O(n)     | O(1)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q004-middle-element.cpp](../../Solutions-CPP/Linked-Lists/Q004-middle-element.cpp)
