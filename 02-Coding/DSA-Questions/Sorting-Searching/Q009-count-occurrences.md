# Q009: Count Occurrences in Sorted Array

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Searching                    |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given a **sorted** array of integers and a target value, count the number of occurrences of the target in the array.

---

## Input Format

- First line: integers `n` and `target`
- Second line: n sorted integers

## Output Format

- Count of occurrences of the target.

---

## Constraints

- 1 <= n <= 10^5
- -10^5 <= arr[i] <= 10^5

---

## Examples

### Example 1
```
Input:  arr = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
```

### Example 2
```
Input:  arr = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
```

### Example 3
```
Input:  arr = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
```

---

## Hints

1. Find the first and last occurrence using binary search.
2. Count = lastIndex - firstIndex + 1.
3. If element not found, return 0.

---

## Tags

`Binary Search` `Counting` `Sorted Array` `TCS NQT` `Easy`
