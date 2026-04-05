# Q007: GCD and LCM

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Mathematics                  |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Given two positive integers `a` and `b`, find their **Greatest Common Divisor (GCD)** and **Least Common Multiple (LCM)**.

---

## Input Format

- Two positive integers `a` and `b`

## Output Format

- Two integers: GCD and LCM.

---

## Constraints

- 1 <= a, b <= 10^9

---

## Examples

### Example 1
```
Input:  a = 12, b = 18
Output: GCD = 6, LCM = 36
```

### Example 2
```
Input:  a = 7, b = 13
Output: GCD = 1, LCM = 91
```

### Example 3
```
Input:  a = 20, b = 20
Output: GCD = 20, LCM = 20
```

---

## Hints

1. Euclidean algorithm: GCD(a, b) = GCD(b, a % b), base case: GCD(a, 0) = a.
2. LCM(a, b) = (a / GCD(a, b)) * b (divide first to avoid overflow).
3. GCD(a, b) * LCM(a, b) = a * b.

---

## Tags

`Mathematics` `GCD` `LCM` `Euclidean Algorithm` `TCS NQT` `Easy`
