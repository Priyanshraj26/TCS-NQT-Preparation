# Q002: Detect Cycle in Linked List (Floyd's Algorithm)

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #141/#142, TCS NQT   |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `linked-list`, `two-pointers`, `floyd`, `cycle-detection` |

---

## Problem Statement

Given the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists if some node in the list can be reached again by continuously following the `next` pointer. Internally, `pos` denotes the index of the node that the tail's next pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle, otherwise return `false`.

**Follow-up:** Can you also find the starting node of the cycle?

---

## Input Format

- Head of a singly linked list.
- The list may or may not contain a cycle.

## Output Format

- Return `true` if a cycle exists, `false` otherwise.
- (Follow-up) Return the node where the cycle begins, or `NULL` if no cycle.

---

## Constraints

- The number of nodes is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` (no cycle) or a valid index in the list.

---

## Examples

### Example 1
```
Input:  3 -> 2 -> 0 -> -4 -> (back to node 2)
        pos = 1
Output: true
```
**Explanation:** There is a cycle where the tail connects back to the 1st node (0-indexed).

### Example 2
```
Input:  1 -> 2 -> (back to node 1)
        pos = 0
Output: true
```

### Example 3
```
Input:  1 -> NULL
        pos = -1
Output: false
```
**Explanation:** No cycle exists.

---

## Hints

1. **Brute Force:** Use a hash set to store visited nodes. If you visit a node twice, there is a cycle.
2. **Optimal (Floyd's):** Use two pointers -- slow moves 1 step, fast moves 2 steps. If they meet, there is a cycle.
3. **Finding cycle start:** After detection, reset one pointer to head. Move both one step at a time -- they meet at the cycle start.

---

## Approach Overview

| Approach           | Time     | Space   |
|--------------------|----------|---------|
| Hash Set           | O(n)     | O(n)    |
| Floyd's Algorithm  | O(n)     | O(1)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q002-detect-cycle.cpp](../../Solutions-CPP/Linked-Lists/Q002-detect-cycle.cpp)
