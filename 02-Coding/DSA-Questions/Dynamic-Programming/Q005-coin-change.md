# Q005: Coin Change (Minimum Coins)

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given an array of coin denominations `coins[]` and a total amount `amount`, return the **minimum number of coins** needed to make up that amount. If it is not possible, return **-1**. You have an infinite supply of each coin denomination.

---

## Input Format

- First line: integer `n` (number of coin types) and `amount`
- Second line: n integers representing coin denominations

## Output Format

- Minimum number of coins, or -1 if not possible.

---

## Constraints

- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

---

## Examples

### Example 1
```
Input:  coins = [1, 5, 10], amount = 12
Output: 3
Explanation: 10 + 1 + 1 = 12 (3 coins)
```

### Example 2
```
Input:  coins = [2], amount = 3
Output: -1
Explanation: Cannot make 3 with only denomination 2.
```

### Example 3
```
Input:  coins = [1], amount = 0
Output: 0
Explanation: 0 coins needed for amount 0.
```

---

## Hints

1. dp[i] = minimum coins to make amount i.
2. For each amount, try every coin denomination.
3. dp[i] = min(dp[i], 1 + dp[i - coin]) for each valid coin.

---

## Tags

`Dynamic Programming` `Unbounded Knapsack` `TCS NQT` `Medium`
