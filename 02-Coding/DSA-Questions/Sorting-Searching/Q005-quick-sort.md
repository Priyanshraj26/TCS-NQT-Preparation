# Q005: Quick Sort Implementation

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Sorting                      |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Implement **Quick Sort** to sort an array of integers in ascending order.

Quick Sort picks a "pivot" element, partitions the array around it (elements smaller than pivot go left, larger go right), and recursively sorts the partitions.

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
Input:  arr = [10, 80, 30, 90, 40, 50, 70]
Output: [10, 30, 40, 50, 70, 80, 90]
```

### Example 2
```
Input:  arr = [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
```

---

## Hints

1. Choose a pivot (last element is common choice).
2. Partition: place pivot at correct position with smaller elements left, larger right.
3. Recursively sort left and right partitions.

---

## Tags

`Sorting` `Quick Sort` `Divide and Conquer` `Partition` `TCS NQT` `Medium`
