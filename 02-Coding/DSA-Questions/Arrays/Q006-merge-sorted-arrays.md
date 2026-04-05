# Merge Two Sorted Arrays

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given two sorted integer arrays `nums1` and `nums2`, merge them into a single sorted array and return it.

## Input Format
- First line: integer `n` (size of first array)
- Second line: `n` space-separated integers (sorted)
- Third line: integer `m` (size of second array)
- Fourth line: `m` space-separated integers (sorted)

## Output Format
- (n+m) space-separated integers representing the merged sorted array

## Constraints
- 0 <= n, m <= 10^5
- -10^9 <= nums1[i], nums2[j] <= 10^9
- Both arrays are sorted in non-decreasing order

## Examples

### Example 1:
**Input:**
```
3
1 3 5
3
2 4 6
```
**Output:**
```
1 2 3 4 5 6
```

### Example 2:
**Input:**
```
4
1 2 3 4
2
0 7
```
**Output:**
```
0 1 2 3 4 7
```

## Hints
<details>
<summary>Hint 1</summary>
Use two pointers, one for each array. Compare elements and pick the smaller one.
</details>

## Tags
`array` `two-pointers` `merge` `sorting`
