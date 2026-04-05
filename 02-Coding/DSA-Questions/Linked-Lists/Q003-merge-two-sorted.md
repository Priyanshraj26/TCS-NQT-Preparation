# Q003: Merge Two Sorted Linked Lists

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Easy                           |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #21, TCS NQT         |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `linked-list`, `merge`, `sorting`, `recursion` |

---

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The merged list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

## Input Format

- Two sorted singly linked lists represented by their head nodes.

## Output Format

- Return the head of the merged sorted linked list.

---

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

---

## Examples

### Example 1
```
Input:  list1 = 1 -> 2 -> 4 -> NULL
        list2 = 1 -> 3 -> 4 -> NULL
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> NULL
```
**Explanation:** Nodes are merged in sorted order by comparing heads of both lists.

### Example 2
```
Input:  list1 = NULL
        list2 = NULL
Output: NULL
```

### Example 3
```
Input:  list1 = NULL
        list2 = 0 -> NULL
Output: 0 -> NULL
```

---

## Hints

1. Use a dummy head node to simplify edge cases.
2. Compare current nodes of both lists and attach the smaller one.
3. When one list is exhausted, attach the remaining nodes of the other list.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Iterative      | O(n+m)   | O(1)    |
| Recursive      | O(n+m)   | O(n+m)  |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q003-merge-two-sorted.cpp](../../Solutions-CPP/Linked-Lists/Q003-merge-two-sorted.cpp)
