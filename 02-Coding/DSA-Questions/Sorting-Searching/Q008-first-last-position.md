# Q008: First and Last Position of Element in Sorted Array

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Searching                    |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given a sorted array of integers (may contain duplicates) and a target value, find the **first** and **last** positions of the target. If not found, return `[-1, -1]`.

Your solution must run in O(log n) time.

---

## Input Format

- First line: integers `n` and `target`
- Second line: n sorted integers

## Output Format

- Two integers: first and last positions (0-based).

---

## Constraints

- 0 <= n <= 10^5
- -10^9 <= arr[i] <= 10^9
- Array is sorted in non-decreasing order.

---

## Examples

### Example 1
```
Input:  arr = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
```

### Example 2
```
Input:  arr = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
```

### Example 3
```
Input:  arr = [], target = 0
Output: [-1, -1]
```

---

## Hints

1. Use binary search twice: once to find the first occurrence, once for the last.
2. For first occurrence: when arr[mid] == target, keep searching left.
3. For last occurrence: when arr[mid] == target, keep searching right.

---

## Tags

`Binary Search` `Sorted Array` `TCS NQT` `Medium`
