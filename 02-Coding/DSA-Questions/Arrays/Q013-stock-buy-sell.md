# Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy and a single day to sell (sell day must be after buy day). Return the maximum profit. If no profit is possible, return 0.

## Input Format
- First line: integer `n` (number of days)
- Second line: `n` space-separated integers (prices)

## Output Format
- A single integer — maximum profit

## Constraints
- 1 <= n <= 10^5
- 0 <= prices[i] <= 10^4

## Examples

### Example 1:
**Input:**
```
6
7 1 5 3 6 4
```
**Output:**
```
5
```
**Explanation:** Buy on day 2 (price=1), sell on day 5 (price=6). Profit = 6-1 = 5.

### Example 2:
**Input:**
```
5
7 6 4 3 1
```
**Output:**
```
0
```
**Explanation:** Prices only decrease, no profitable transaction possible.

## Hints
<details>
<summary>Hint 1</summary>
Track the minimum price seen so far, and at each day compute the profit if you sold today.
</details>

## Tags
`array` `greedy` `single-pass`
