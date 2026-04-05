# Move All Negatives to One Side

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★☆☆

## Problem Statement
Given an array of positive and negative integers, move all negative numbers to the beginning of the array and all positive numbers to the end. The relative order within negatives or positives does not need to be preserved.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- The rearranged array (all negatives first, then positives)

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
7
-12 11 -13 -5 6 -7 5
```
**Output:**
```
-12 -13 -5 -7 11 6 5
```
**Explanation:** All negatives are on the left. Order within groups may vary.

### Example 2:
**Input:**
```
4
1 -1 3 -2
```
**Output:**
```
-1 -2 3 1
```

## Hints
<details>
<summary>Hint 1</summary>
Use a two-pointer approach similar to the partition step of quicksort.
</details>

## Tags
`array` `two-pointers` `partition`
