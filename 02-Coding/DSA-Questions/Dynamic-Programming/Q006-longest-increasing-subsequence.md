# Q006: Longest Increasing Subsequence

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★                           |

---

## Problem Statement

Given an integer array `nums`, return the length of the **longest strictly increasing subsequence**.

---

## Input Format

- First line: integer `n`
- Second line: n integers

## Output Format

- Length of the longest increasing subsequence.

---

## Constraints

- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

---

## Examples

### Example 1
```
Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: LIS is [2, 3, 7, 101] or [2, 5, 7, 101], length = 4.
```

### Example 2
```
Input:  nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: LIS is [0, 1, 2, 3].
```

### Example 3
```
Input:  nums = [7, 7, 7, 7]
Output: 1
Explanation: Strictly increasing, so each element alone.
```

---

## Hints

1. dp[i] = length of LIS ending at index i.
2. For each i, check all j < i where nums[j] < nums[i].
3. There's an O(n log n) approach using binary search + patience sorting.

---

## Tags

`Dynamic Programming` `Binary Search` `TCS NQT` `Medium`
