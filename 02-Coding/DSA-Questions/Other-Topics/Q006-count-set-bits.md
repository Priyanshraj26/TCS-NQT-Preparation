# Q006: Count Set Bits (Brian Kernighan's Algorithm)

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Bit Manipulation             |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given a non-negative integer `n`, count the number of **set bits** (1s) in its binary representation. This is also known as the **Hamming weight** or **popcount**.

---

## Input Format

- A single non-negative integer `n`

## Output Format

- Number of set bits.

---

## Constraints

- 0 <= n <= 2^31 - 1

---

## Examples

### Example 1
```
Input:  n = 13
Output: 3
Explanation: 13 = 1101 (binary), three 1s.
```

### Example 2
```
Input:  n = 7
Output: 3
Explanation: 7 = 111 (binary), three 1s.
```

### Example 3
```
Input:  n = 0
Output: 0
```

---

## Hints

1. n & (n-1) removes the rightmost set bit.
2. Count how many times you can do this until n becomes 0.
3. This is Brian Kernighan's algorithm -- O(number of set bits).

---

## Tags

`Bit Manipulation` `Brian Kernighan` `Hamming Weight` `TCS NQT` `Easy`
