# Subarray with Given Sum

**Difficulty:** Medium  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an array of non-negative integers and a target sum, find a contiguous subarray that adds up to the given sum. Return the 1-based start and end indices.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated non-negative integers
- Third line: integer `target` (desired sum)

## Output Format
- Two space-separated integers: 1-based start and end indices of the subarray
- If no such subarray exists, print `-1`

## Constraints
- 1 <= n <= 10^5
- 0 <= nums[i] <= 10^4
- 0 <= target <= 10^7

## Examples

### Example 1:
**Input:**
```
5
1 2 3 7 5
12
```
**Output:**
```
2 4
```
**Explanation:** Subarray [2, 3, 7] (indices 2 to 4, 1-based) sums to 12.

### Example 2:
**Input:**
```
3
1 2 3
6
```
**Output:**
```
1 3
```

### Example 3:
**Input:**
```
3
1 2 3
10
```
**Output:**
```
-1
```

## Hints
<details>
<summary>Hint 1</summary>
Since all elements are non-negative, use the sliding window (two pointer) technique.
</details>

<details>
<summary>Hint 2</summary>
Expand the window by adding the right element. If the sum exceeds target, shrink from the left.
</details>

## Tags
`array` `sliding-window` `two-pointers` `prefix-sum`
