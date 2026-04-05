# Q002: Selection Sort Implementation

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Sorting                      |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Implement **Selection Sort** to sort an array of integers in ascending order.

Selection Sort divides the array into a sorted and unsorted part. It repeatedly selects the minimum element from the unsorted part and places it at the beginning of the unsorted part.

---

## Input Format

- First line: integer `n`
- Second line: n integers

## Output Format

- The sorted array in ascending order.

---

## Constraints

- 1 <= n <= 10^4
- -10^5 <= arr[i] <= 10^5

---

## Examples

### Example 1
```
Input:  arr = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
```

### Example 2
```
Input:  arr = [29, 10, 14, 37, 13]
Output: [10, 13, 14, 29, 37]
```

---

## Hints

1. Find the minimum element in the unsorted portion.
2. Swap it with the first element of the unsorted portion.
3. Repeat for each position.

---

## Tags

`Sorting` `Selection Sort` `In-place` `TCS NQT` `Easy`
