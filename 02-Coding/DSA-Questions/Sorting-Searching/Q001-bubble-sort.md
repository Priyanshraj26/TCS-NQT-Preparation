# Q001: Bubble Sort Implementation

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Sorting                      |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Implement **Bubble Sort** to sort an array of integers in ascending order.

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

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
Input:  arr = [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
```

### Example 2
```
Input:  arr = [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
```

---

## Hints

1. In each pass, the largest unsorted element "bubbles up" to its correct position.
2. Optimize by stopping early if no swaps occur in a pass (already sorted).
3. After k passes, the last k elements are in their final positions.

---

## Tags

`Sorting` `Bubble Sort` `In-place` `Stable Sort` `TCS NQT` `Easy`
