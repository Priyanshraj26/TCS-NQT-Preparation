# Rotate Array by K Positions

**Difficulty:** Medium  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given an integer array `nums`, rotate the array to the right by `k` steps. Perform the rotation in-place.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers
- Third line: integer `k` (number of positions to rotate)

## Output Format
- The rotated array as space-separated integers

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

## Examples

### Example 1:
**Input:**
```
7
1 2 3 4 5 6 7
3
```
**Output:**
```
5 6 7 1 2 3 4
```
**Explanation:** Rotate right by 3: [1,2,3,4,5,6,7] → [5,6,7,1,2,3,4]

### Example 2:
**Input:**
```
4
-1 -100 3 99
2
```
**Output:**
```
3 99 -1 -100
```

## Hints
<details>
<summary>Hint 1</summary>
If k >= n, rotating by k is the same as rotating by k % n.
</details>

<details>
<summary>Hint 2</summary>
Try reversing parts of the array: reverse entire array, then reverse first k elements, then reverse remaining elements.
</details>

## Tags
`array` `reverse` `in-place` `rotation`
