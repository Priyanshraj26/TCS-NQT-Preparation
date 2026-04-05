# Q005: Remove Nth Node from End of List

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #19, TCS NQT         |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `linked-list`, `two-pointers`, `one-pass` |

---

## Problem Statement

Given the head of a linked list, remove the `n`th node from the **end** of the list and return its head.

---

## Input Format

- Head of a singly linked list and an integer `n`.

## Output Format

- Return the head after removing the nth node from the end.

---

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Examples

### Example 1
```
Input:  1 -> 2 -> 3 -> 4 -> 5,  n = 2
Output: 1 -> 2 -> 3 -> 5
```
**Explanation:** The 2nd node from end is 4, which is removed.

### Example 2
```
Input:  1,  n = 1
Output: NULL
```

### Example 3
```
Input:  1 -> 2,  n = 1
Output: 1
```

---

## Hints

1. **Two-pass:** First find the length, then remove the `(length - n)`th node.
2. **One-pass:** Move the first pointer `n` steps ahead. Then move both pointers until the first reaches the end. The second pointer will be at the node just before the target.
3. Use a dummy node to handle the edge case of removing the head.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Two-pass       | O(n)     | O(1)    |
| One-pass       | O(n)     | O(1)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q005-remove-nth-from-end.cpp](../../Solutions-CPP/Linked-Lists/Q005-remove-nth-from-end.cpp)
