# Q009: Subset Sum Problem

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given an array of non-negative integers and a target sum, determine if there exists a **subset** whose elements sum up to the target.

---

## Input Format

- First line: integers `n` and `target`
- Second line: n non-negative integers

## Output Format

- "YES" if a subset with the given sum exists, "NO" otherwise.

---

## Constraints

- 1 <= n <= 200
- 0 <= arr[i] <= 10^4
- 0 <= target <= 10^4

---

## Examples

### Example 1
```
Input:  arr = [3, 34, 4, 12, 5, 2], target = 9
Output: YES
Explanation: Subset {4, 5} sums to 9.
```

### Example 2
```
Input:  arr = [3, 34, 4, 12, 5, 2], target = 30
Output: NO
Explanation: No subset sums to 30.
```

### Example 3
```
Input:  arr = [1, 2, 3], target = 0
Output: YES
Explanation: Empty subset sums to 0.
```

---

## Hints

1. This is a variation of 0/1 knapsack.
2. dp[i][s] = can we form sum s using first i elements?
3. For each element, either include it or exclude it.

---

## Tags

`Dynamic Programming` `Knapsack Variant` `Subset` `TCS NQT` `Medium`
