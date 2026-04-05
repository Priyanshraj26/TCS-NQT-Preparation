# Q001: Reverse a Linked List

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #206, TCS NQT, Infosys |
| **Frequency**  | ★★★★★ (Very High)             |
| **Tags**       | `linked-list`, `pointers`, `iterative`, `recursive` |

---

## Problem Statement

Given the head of a singly linked list, reverse the list and return the reversed list's head.

---

## Input Format

- A singly linked list represented by its head node.
- Each node contains an integer value and a pointer to the next node.

## Output Format

- Return the head of the reversed linked list.

---

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Examples

### Example 1
```
Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
```
**Explanation:** Each node's next pointer is reversed. The last node becomes the new head.

### Example 2
```
Input:  1 -> 2 -> NULL
Output: 2 -> 1 -> NULL
```

### Example 3
```
Input:  NULL (empty list)
Output: NULL
```

---

## Hints

1. Can you reverse the links between nodes one by one as you traverse?
2. Think about maintaining three pointers: `prev`, `curr`, and `next`.
3. Alternatively, think recursively -- reverse the rest of the list, then fix the head.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Iterative      | O(n)     | O(1)    |
| Recursive      | O(n)     | O(n)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q001-reverse-linked-list.cpp](../../Solutions-CPP/Linked-Lists/Q001-reverse-linked-list.cpp)
