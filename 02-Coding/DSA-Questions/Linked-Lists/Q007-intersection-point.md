# Q007: Intersection Point of Two Linked Lists

| Property       | Value                          |
|----------------|--------------------------------|
| **Difficulty** | Medium                         |
| **Topic**      | Linked Lists                   |
| **Source**      | LeetCode #160, TCS NQT        |
| **Frequency**  | ★★★★ (High)                   |
| **Tags**       | `linked-list`, `two-pointers`, `hash-set` |

---

## Problem Statement

Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection, return `NULL`.

The linked lists must retain their original structure after the function returns.

---

## Input Format

- Heads of two singly linked lists.
- The lists may or may not intersect.

## Output Format

- Return the intersecting node, or `NULL` if no intersection.

---

## Constraints

- The number of nodes in `listA` is `m`, in `listB` is `n`.
- `1 <= m, n <= 3 * 10^4`
- `1 <= Node.val <= 10^5`

---

## Examples

### Example 1
```
Input:  listA = 4 -> 1 -> 8 -> 4 -> 5
        listB = 5 -> 6 -> 1 -> 8 -> 4 -> 5
        (Intersection at node with value 8)
Output: Node with value 8
```
**Explanation:** Both lists merge at the node with value 8.

### Example 2
```
Input:  listA = 2 -> 6 -> 4
        listB = 1 -> 5
Output: NULL
```
**Explanation:** No intersection.

---

## Hints

1. **Brute Force:** For each node in listA, check if it exists in listB. O(m*n).
2. **Hash Set:** Store all nodes of listA in a set. Traverse listB and check. O(m+n) time, O(m) space.
3. **Two Pointers:** Traverse both lists. When one reaches end, redirect to the other list's head. They will meet at intersection or both reach NULL. O(m+n) time, O(1) space.

---

## Approach Overview

| Approach       | Time     | Space   |
|----------------|----------|---------|
| Brute Force    | O(m*n)   | O(1)    |
| Hash Set       | O(m+n)   | O(m)    |
| Two Pointers   | O(m+n)   | O(1)    |

---

**Solution:** [Solutions-CPP/Linked-Lists/Q007-intersection-point.cpp](../../Solutions-CPP/Linked-Lists/Q007-intersection-point.cpp)
