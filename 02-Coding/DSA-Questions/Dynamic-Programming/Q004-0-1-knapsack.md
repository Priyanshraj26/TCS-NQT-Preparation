# Q004: 0/1 Knapsack Problem

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given **n** items, each with a **weight** and a **value**, and a knapsack with capacity **W**, determine the maximum value you can carry. Each item can either be taken completely or left (0/1 -- no fractional items).

---

## Input Format

- First line: integers `n` (number of items) and `W` (knapsack capacity)
- Next n lines: two integers `weight[i]` and `value[i]`

## Output Format

- A single integer representing the maximum value achievable.

---

## Constraints

- 1 <= n <= 1000
- 1 <= W <= 1000
- 1 <= weight[i], value[i] <= 1000

---

## Examples

### Example 1
```
Input:  n = 3, W = 50
        weights = [10, 20, 30], values = [60, 100, 120]
Output: 220
Explanation: Take items with weights 20 and 30 (total weight = 50),
             total value = 100 + 120 = 220.
```

### Example 2
```
Input:  n = 3, W = 10
        weights = [5, 4, 6], values = [10, 40, 30]
Output: 50
Explanation: Take items with weights 5 and 4 (total weight = 9 <= 10),
             total value = 10 + 40 = 50.
```

---

## Hints

1. For each item, you have two choices: include it or exclude it.
2. dp[i][w] = max value using first i items with capacity w.
3. If weight[i] <= w: dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]])

---

## Tags

`Dynamic Programming` `Knapsack` `2D DP` `TCS NQT` `Medium`
