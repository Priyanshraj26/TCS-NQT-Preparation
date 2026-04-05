# Q007: Search in Rotated Sorted Array

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Searching                    |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given a sorted array that has been **rotated** at some pivot (e.g., [4,5,6,7,0,1,2] was rotated from [0,1,2,4,5,6,7]), search for a target value. Return its index or -1 if not found.

All elements are **unique**.

---

## Input Format

- First line: integers `n` and `target`
- Second line: n integers (rotated sorted array)

## Output Format

- Index of target (0-based), or -1 if not found.

---

## Constraints

- 1 <= n <= 5000
- -10^4 <= arr[i] <= 10^4
- All values are unique.

---

## Examples

### Example 1
```
Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

### Example 2
```
Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

### Example 3
```
Input:  arr = [1], target = 0
Output: -1
```

---

## Hints

1. One half of the array is always sorted.
2. Determine which half is sorted, then check if target lies in that half.
3. Modified binary search -- O(log n).

---

## Tags

`Binary Search` `Rotated Array` `TCS NQT` `Medium`
