# Q004: Next Greater Element

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Stack                        |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given an array, find the **Next Greater Element (NGE)** for every element. The NGE for an element is the first element on the right that is greater than the current element. If no such element exists, the answer is -1.

---

## Input Format

- First line: integer `n`
- Second line: n integers

## Output Format

- n integers representing the NGE for each element.

---

## Constraints

- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^9

---

## Examples

### Example 1
```
Input:  arr = [4, 5, 2, 25]
Output: [5, 25, 25, -1]
Explanation:
  4  -> next greater is 5
  5  -> next greater is 25
  2  -> next greater is 25
  25 -> no greater element, -1
```

### Example 2
```
Input:  arr = [13, 7, 6, 12]
Output: [-1, 12, 12, -1]
```

---

## Hints

1. Use a stack to keep track of elements whose NGE hasn't been found yet.
2. Traverse from right to left, maintaining a monotonic decreasing stack.
3. For each element, pop all smaller elements from the stack.

---

## Tags

`Stack` `Monotonic Stack` `Array` `TCS NQT` `Medium`
