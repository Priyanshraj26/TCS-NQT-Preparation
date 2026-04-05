# Find Max and Min in Minimum Comparisons

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given an array of integers, find the maximum and minimum elements using the minimum number of comparisons.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- Two space-separated integers: minimum and maximum

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
6
3 5 1 8 2 9
```
**Output:**
```
1 9
```

### Example 2:
**Input:**
```
1
42
```
**Output:**
```
42 42
```

### Example 3:
**Input:**
```
2
10 5
```
**Output:**
```
5 10
```

## Hints
<details>
<summary>Hint 1</summary>
A simple linear scan uses 2(n-1) comparisons. Can you do it in about 3n/2 comparisons?
</details>

<details>
<summary>Hint 2</summary>
Process elements in pairs: compare the pair first, then compare the smaller with min and larger with max.
</details>

## Tags
`array` `comparison` `pair-processing`
