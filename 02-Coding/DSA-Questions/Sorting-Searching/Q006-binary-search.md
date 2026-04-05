# Q006: Binary Search

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Searching                    |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Given a **sorted** array of integers and a target value, return the **index** of the target if found. If not found, return **-1**.

---

## Input Format

- First line: integers `n` and `target`
- Second line: n sorted integers

## Output Format

- Index of target (0-based), or -1 if not found.

---

## Constraints

- 1 <= n <= 10^5
- -10^4 <= arr[i] <= 10^4
- Array is sorted in ascending order.

---

## Examples

### Example 1
```
Input:  arr = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 is at index 4.
```

### Example 2
```
Input:  arr = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 is not in the array.
```

---

## Hints

1. Compare target with middle element.
2. If target < mid, search left half; if target > mid, search right half.
3. Use `mid = low + (high - low) / 2` to avoid integer overflow.

---

## Tags

`Searching` `Binary Search` `Divide and Conquer` `TCS NQT` `Easy`
