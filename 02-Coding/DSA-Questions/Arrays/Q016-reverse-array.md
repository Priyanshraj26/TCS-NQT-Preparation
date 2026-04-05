# Reverse an Array

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an array of integers, reverse the array in-place.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- The reversed array as space-separated integers

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
5
1 2 3 4 5
```
**Output:**
```
5 4 3 2 1
```

### Example 2:
**Input:**
```
4
10 20 30 40
```
**Output:**
```
40 30 20 10
```

### Example 3:
**Input:**
```
1
7
```
**Output:**
```
7
```

## Hints
<details>
<summary>Hint 1</summary>
Use two pointers: one at the start, one at the end. Swap and move inward.
</details>

## Tags
`array` `two-pointers` `basic` `in-place`
