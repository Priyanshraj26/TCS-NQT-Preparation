# Q007: Maximum Sum with No Two Adjacent Elements

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given an array of positive integers, find the **maximum sum** of a subsequence such that **no two elements are adjacent** in the original array. (Also known as the "House Robber" problem.)

---

## Input Format

- First line: integer `n`
- Second line: n positive integers

## Output Format

- Maximum sum with no two adjacent elements selected.

---

## Constraints

- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^4

---

## Examples

### Example 1
```
Input:  arr = [3, 2, 7, 10]
Output: 13
Explanation: Pick 3 and 10 (indices 0 and 3). Sum = 13.
```

### Example 2
```
Input:  arr = [5, 5, 10, 100, 10, 5]
Output: 110
Explanation: Pick 5, 100, 5 (indices 0, 3, 5). Sum = 110.
```

### Example 3
```
Input:  arr = [3, 2, 5, 10, 7]
Output: 15
Explanation: Pick 3, 10 or 5, 7 -> best is 3 + 5 + 7 = 15.
```

---

## Hints

1. At each element, decide: include it (add to sum excluding previous) or skip it.
2. dp[i] = max(dp[i-1], arr[i] + dp[i-2])
3. Only need two previous values -- O(1) space.

---

## Tags

`Dynamic Programming` `House Robber` `TCS NQT` `Medium`
