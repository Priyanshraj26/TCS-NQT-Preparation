# Q003: Insertion Sort Implementation

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Sorting                      |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Implement **Insertion Sort** to sort an array of integers in ascending order.

Insertion Sort builds the sorted array one element at a time by repeatedly picking the next element and inserting it into its correct position among the already-sorted elements.

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
Input:  arr = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]
```

### Example 2
```
Input:  arr = [4, 3, 2, 10, 12, 1, 5, 6]
Output: [1, 2, 3, 4, 5, 6, 10, 12]
```

---

## Hints

1. Start from the second element. Compare it with elements before it.
2. Shift larger elements one position to the right.
3. Insert the current element at its correct position.

---

## Tags

`Sorting` `Insertion Sort` `In-place` `Stable Sort` `TCS NQT` `Easy`
