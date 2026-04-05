# Q008: Check if Number is Prime

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Mathematics                  |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Given a positive integer `n`, determine if it is a **prime number**. A prime number is greater than 1 and has no positive divisors other than 1 and itself.

---

## Input Format

- A single positive integer `n`

## Output Format

- "YES" if prime, "NO" otherwise.

---

## Constraints

- 1 <= n <= 10^9

---

## Examples

### Example 1
```
Input:  n = 7
Output: YES
```

### Example 2
```
Input:  n = 4
Output: NO
Explanation: 4 = 2 x 2
```

### Example 3
```
Input:  n = 1
Output: NO
Explanation: 1 is not a prime.
```

---

## Hints

1. Check divisibility only up to sqrt(n).
2. Handle 2 separately, then check only odd numbers.
3. Skip even numbers after checking 2.

---

## Tags

`Mathematics` `Prime` `Number Theory` `TCS NQT` `Easy`
