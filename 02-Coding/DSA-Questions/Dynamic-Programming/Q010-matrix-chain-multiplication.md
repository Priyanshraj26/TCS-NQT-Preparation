# Q010: Matrix Chain Multiplication

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Hard                         |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★                           |

---

## Problem Statement

Given a sequence of matrices, find the most efficient way to multiply them. The problem is not to perform the multiplication, but to decide the **order** that minimizes the total number of scalar multiplications.

Given dimensions array `p[]` where the ith matrix has dimensions `p[i-1] x p[i]`, find the minimum number of multiplications needed.

---

## Input Format

- First line: integer `n` (number of matrices)
- Second line: n+1 integers representing dimensions array p[]

## Output Format

- Minimum number of scalar multiplications.

---

## Constraints

- 2 <= n <= 100
- 1 <= p[i] <= 500

---

## Examples

### Example 1
```
Input:  p = [10, 20, 30, 40, 30]  (4 matrices)
Output: 30000
Explanation: Optimal order: ((A1 x A2) x A3) x A4
```

### Example 2
```
Input:  p = [40, 20, 30, 10, 30]  (4 matrices)
Output: 26000
Explanation: Optimal parenthesization gives 26000.
```

---

## Hints

1. Try all possible ways to split the chain and take the minimum.
2. dp[i][j] = min cost to multiply matrices from i to j.
3. For each split point k: cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]

---

## Tags

`Dynamic Programming` `MCM Pattern` `Interval DP` `TCS NQT` `Hard`
