# Two Sum

**Difficulty:** Easy  
**Topic:** Array, Hash Map  
**Source:** TCS NQT 2023  
**Company:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers
- Third line: integer `target`

## Output Format
- Two space-separated integers representing the indices (0-based)

## Constraints
- 2 <= n <= 10^4
- -10^9 <= nums[i] <= 10^9
- Exactly one valid answer exists

## Examples

### Example 1:
**Input:**
```
4
2 7 11 15
9
```
**Output:**
```
0 1
```
**Explanation:** nums[0] + nums[1] = 2 + 7 = 9

### Example 2:
**Input:**
```
3
3 2 4
6
```
**Output:**
```
1 2
```

## Test Cases

### Edge Case - Two same elements:
**Input:** `n=2, nums=[3,3], target=6`  
**Output:** `0 1`

### Negative numbers:
**Input:** `n=3, nums=[-1,0,1], target=0`  
**Output:** `0 2`

## Hints
<details>
<summary>Hint 1</summary>
For each element, what value would you need to find to reach the target?
</details>

<details>
<summary>Hint 2</summary>
Can you use a hash map to store elements you've already seen?
</details>

## Tags
`array` `hash-map` `two-pointers`
