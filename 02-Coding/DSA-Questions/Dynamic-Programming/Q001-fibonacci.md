# Q001: Nth Fibonacci Number

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Given a positive integer **n**, find the **nth Fibonacci number**.

The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n >= 2

The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

---

## Input Format

- A single integer `n` (0 <= n <= 45)

## Output Format

- A single integer representing the nth Fibonacci number.

---

## Constraints

- 0 <= n <= 45
- The answer fits in a 32-bit signed integer.

---

## Examples

### Example 1
```
Input:  n = 5
Output: 5
Explanation: F(5) = F(4) + F(3) = 3 + 2 = 5
Sequence: 0, 1, 1, 2, 3, [5]
```

### Example 2
```
Input:  n = 0
Output: 0
Explanation: F(0) = 0 by definition.
```

### Example 3
```
Input:  n = 10
Output: 55
Explanation: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, [55]
```

---

## Hints

1. The naive recursive approach has exponential time complexity due to overlapping subproblems.
2. Store already-computed results to avoid redundant calculations (memoization).
3. You only need the last two values at any point (space optimization).

---

## Tags

`Dynamic Programming` `Recursion` `Memoization` `Tabulation` `TCS NQT` `Easy`
