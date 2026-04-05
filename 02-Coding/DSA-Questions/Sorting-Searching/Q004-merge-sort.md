# Q004: Merge Sort Implementation

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Sorting                      |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Implement **Merge Sort** to sort an array of integers in ascending order.

Merge Sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts each half, and merges the sorted halves.

---

## Input Format

- First line: integer `n`
- Second line: n integers

## Output Format

- The sorted array in ascending order.

---

## Constraints

- 1 <= n <= 10^5
- -10^5 <= arr[i] <= 10^5

---

## Examples

### Example 1
```
Input:  arr = [38, 27, 43, 3, 9, 82, 10]
Output: [3, 9, 10, 27, 38, 43, 82]
```

### Example 2
```
Input:  arr = [5, 2, 4, 7, 1, 3, 2, 6]
Output: [1, 2, 2, 3, 4, 5, 6, 7]
```

---

## Hints

1. Divide array into two halves at midpoint.
2. Recursively sort each half.
3. Merge two sorted halves using two pointers.

---

## Tags

`Sorting` `Merge Sort` `Divide and Conquer` `Stable Sort` `TCS NQT` `Medium`
