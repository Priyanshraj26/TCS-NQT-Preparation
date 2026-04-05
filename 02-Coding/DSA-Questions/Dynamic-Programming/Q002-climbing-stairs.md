# Q002: Climbing Stairs

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

You are climbing a staircase that has **n** steps. Each time you can climb either **1 step** or **2 steps**. In how many distinct ways can you reach the top?

---

## Input Format

- A single integer `n` (1 <= n <= 45)

## Output Format

- A single integer representing the number of distinct ways to climb to the top.

---

## Constraints

- 1 <= n <= 45

---

## Examples

### Example 1
```
Input:  n = 2
Output: 2
Explanation: Two ways: (1+1) or (2)
```

### Example 2
```
Input:  n = 3
Output: 3
Explanation: Three ways: (1+1+1), (1+2), (2+1)
```

### Example 3
```
Input:  n = 5
Output: 8
Explanation: 8 ways to reach step 5.
```

---

## Hints

1. To reach step n, you could have come from step n-1 or step n-2.
2. ways(n) = ways(n-1) + ways(n-2) -- this is essentially Fibonacci!
3. Base cases: ways(1) = 1, ways(2) = 2.

---

## Tags

`Dynamic Programming` `Fibonacci Variant` `TCS NQT` `Easy`
