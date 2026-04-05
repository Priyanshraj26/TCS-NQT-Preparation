# Q009: Factorial of Large Numbers

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Mathematics / Arrays         |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given a non-negative integer `n`, compute **n!** (n factorial). Since the result can be very large (even for small n like 25), standard data types may overflow. Handle arbitrarily large results.

---

## Input Format

- A single integer `n` (0 <= n <= 1000)

## Output Format

- The exact value of n! (all digits).

---

## Constraints

- 0 <= n <= 1000
- Must handle very large numbers (100! has 158 digits).

---

## Examples

### Example 1
```
Input:  n = 5
Output: 120
```

### Example 2
```
Input:  n = 10
Output: 3628800
```

### Example 3
```
Input:  n = 25
Output: 15511210043330985984000000
```

---

## Hints

1. Use an array/vector to store individual digits of the result.
2. Multiply each digit by the current number, handling carry.
3. This is essentially "big integer multiplication."

---

## Tags

`Mathematics` `Big Integer` `Array` `TCS NQT` `Medium`
