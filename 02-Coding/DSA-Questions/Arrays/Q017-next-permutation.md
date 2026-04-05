# Next Permutation

**Difficulty:** Medium  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given an array of integers, rearrange the numbers into the lexicographically next greater permutation. If the array is in descending order (last permutation), rearrange it to the first permutation (ascending order). The replacement must be in-place using only constant extra memory.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- The next permutation as space-separated integers

## Constraints
- 1 <= n <= 100
- 0 <= nums[i] <= 100

## Examples

### Example 1:
**Input:**
```
3
1 2 3
```
**Output:**
```
1 3 2
```

### Example 2:
**Input:**
```
3
3 2 1
```
**Output:**
```
1 2 3
```
**Explanation:** Last permutation wraps around to first.

### Example 3:
**Input:**
```
4
1 1 5 1
```
**Output:**
```
1 5 1 1
```

## Hints
<details>
<summary>Hint 1</summary>
Find the rightmost index i where nums[i] < nums[i+1]. This is the "break point."
</details>

<details>
<summary>Hint 2</summary>
Find the rightmost index j > i where nums[j] > nums[i]. Swap them, then reverse the suffix after i.
</details>

## Tags
`array` `permutation` `in-place` `greedy`
