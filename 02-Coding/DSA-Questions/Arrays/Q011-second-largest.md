# Second Largest Element

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an array of integers, find the second largest distinct element. If no second largest exists, return -1.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- A single integer — the second largest element, or -1 if it doesn't exist

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
5
12 35 1 10 34
```
**Output:**
```
34
```

### Example 2:
**Input:**
```
3
10 10 10
```
**Output:**
```
-1
```
**Explanation:** All elements are the same, no second largest exists.

### Example 3:
**Input:**
```
2
5 10
```
**Output:**
```
5
```

## Hints
<details>
<summary>Hint 1</summary>
Track both the largest and second largest in a single pass.
</details>

## Tags
`array` `single-pass` `basic`
