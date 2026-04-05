# Q010: Sieve of Eratosthenes

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Mathematics                  |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given an integer `n`, find all **prime numbers** less than or equal to `n` using the **Sieve of Eratosthenes** algorithm.

---

## Input Format

- A single integer `n`

## Output Format

- All prime numbers from 2 to n.

---

## Constraints

- 2 <= n <= 10^7

---

## Examples

### Example 1
```
Input:  n = 10
Output: 2 3 5 7
```

### Example 2
```
Input:  n = 30
Output: 2 3 5 7 11 13 17 19 23 29
```

### Example 3
```
Input:  n = 2
Output: 2
```

---

## Hints

1. Create a boolean array of size n+1, initialize all as true.
2. Starting from 2, mark all multiples of each prime as composite.
3. Only need to sieve up to sqrt(n).
4. Start marking multiples from i*i (smaller multiples already handled).

---

## Tags

`Mathematics` `Sieve` `Prime Numbers` `TCS NQT` `Medium`
