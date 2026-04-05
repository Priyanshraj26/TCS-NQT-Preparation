# Equilibrium Point / Index

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given an array of integers, find the equilibrium index. An index `i` is an equilibrium index if the sum of elements at lower indices equals the sum of elements at higher indices. That is, `sum(nums[0..i-1]) == sum(nums[i+1..n-1])`. Return the first equilibrium index (0-based). If none exists, return -1.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- A single integer — the equilibrium index (0-based), or -1

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
7
-7 1 5 2 -4 3 0
```
**Output:**
```
3
```
**Explanation:** Left sum at index 3 = -7+1+5 = -1. Right sum = -4+3+0 = -1. Equal.

### Example 2:
**Input:**
```
4
1 2 3 3
```
**Output:**
```
-1
```

### Example 3:
**Input:**
```
3
1 0 1
```
**Output:**
```
1
```

## Hints
<details>
<summary>Hint 1</summary>
Compute the total sum. Traverse left to right maintaining a running left sum. Right sum = total - leftSum - nums[i].
</details>

## Tags
`array` `prefix-sum` `single-pass`
