# Trapping Rain Water

**Difficulty:** Hard  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Input Format
- First line: integer `n` (number of bars)
- Second line: `n` space-separated non-negative integers (heights)

## Output Format
- A single integer — total units of trapped water

## Constraints
- 1 <= n <= 10^5
- 0 <= height[i] <= 10^4

## Examples

### Example 1:
**Input:**
```
12
0 1 0 2 1 0 1 3 2 1 2 1
```
**Output:**
```
6
```
**Explanation:** The elevation map traps 6 units of rain water.

### Example 2:
**Input:**
```
6
4 2 0 3 2 5
```
**Output:**
```
9
```

## Hints
<details>
<summary>Hint 1</summary>
Water above bar i = min(max height to its left, max height to its right) - height[i].
</details>

<details>
<summary>Hint 2</summary>
Precompute leftMax[] and rightMax[] arrays, or use two pointers for O(1) space.
</details>

## Tags
`array` `two-pointers` `prefix-suffix` `stack`
