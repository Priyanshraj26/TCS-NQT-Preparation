# Q005: Check if Number is Power of 2

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Bit Manipulation             |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Given a positive integer `n`, determine if it is a **power of two**.

A number is a power of two if it can be expressed as 2^k for some non-negative integer k.

---

## Input Format

- A single integer `n`

## Output Format

- "YES" if n is a power of 2, "NO" otherwise.

---

## Constraints

- 1 <= n <= 2^31 - 1

---

## Examples

### Example 1
```
Input:  n = 16
Output: YES
Explanation: 16 = 2^4
```

### Example 2
```
Input:  n = 3
Output: NO
```

### Example 3
```
Input:  n = 1
Output: YES
Explanation: 1 = 2^0
```

---

## Hints

1. Powers of 2 in binary have exactly one set bit: 1, 10, 100, 1000, ...
2. n & (n-1) clears the lowest set bit.
3. For a power of 2: n & (n-1) == 0.

---

## Tags

`Bit Manipulation` `Math` `TCS NQT` `Easy`
