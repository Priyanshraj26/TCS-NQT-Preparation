# Q010: Square Root using Binary Search

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Searching                    |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given a non-negative integer `x`, compute and return the **integer square root** of `x` (i.e., the floor of the square root). You must not use any built-in exponent function or operator.

---

## Input Format

- A single non-negative integer `x`

## Output Format

- The floor of the square root of x.

---

## Constraints

- 0 <= x <= 2^31 - 1

---

## Examples

### Example 1
```
Input:  x = 4
Output: 2
```

### Example 2
```
Input:  x = 8
Output: 2
Explanation: sqrt(8) = 2.828..., floor = 2
```

### Example 3
```
Input:  x = 0
Output: 0
```

---

## Hints

1. Binary search in range [0, x] for the largest number whose square <= x.
2. Use long long to avoid overflow when computing mid*mid.
3. Special cases: x = 0 and x = 1.

---

## Tags

`Binary Search` `Math` `TCS NQT` `Easy`
