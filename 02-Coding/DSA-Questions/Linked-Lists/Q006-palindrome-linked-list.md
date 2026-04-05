# Q006: Check if Linked List is Palindrome

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #234, TCS NQT        |
| **Frequency**  | ★★★ (Medium)                  |
| **Tags**       | `linked-list`, `two-pointers`, `stack`, `palindrome` |

---

## Problem Statement

Given the head of a singly linked list, return `true` if it is a palindrome, or `false` otherwise.

---

## Input Format

- Head of a singly linked list.

## Output Format

- `true` if the linked list is a palindrome, `false` otherwise.

---

## Constraints

- The number of nodes is in the range `[1, 10^5]`.
- `0 <= Node.val <= 9`

---

## Examples

### Example 1
```
Input:  1 -> 2 -> 2 -> 1 -> NULL
Output: true
```
**Explanation:** The list reads the same forwards and backwards.

### Example 2
```
Input:  1 -> 2 -> NULL
Output: false
```

### Example 3
```
Input:  1 -> 2 -> 3 -> 2 -> 1 -> NULL
Output: true
```

---

## Hints

1. **Brute Force:** Copy values to an array and check if the array is a palindrome.
2. **Optimal:** Find the middle, reverse the second half, then compare both halves.
3. Use slow-fast pointers to find the middle in one pass.

---

## Approach Overview

| Approach                    | Time     | Space   |
|-----------------------------|----------|---------|
| Copy to array               | O(n)     | O(n)    |
| Reverse second half         | O(n)     | O(1)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q006-palindrome-linked-list.cpp](../../Solutions-CPP/Linked-Lists/Q006-palindrome-linked-list.cpp)
