# Maximum Subarray Sum (Kadane's Algorithm)

**Difficulty:** Medium  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- A single integer representing the maximum subarray sum

## Constraints
- 1 <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

## Examples

### Example 1:
**Input:**
```
9
-2 1 -3 4 -1 2 1 -5 4
```
**Output:**
```
6
```
**Explanation:** The subarray [4, -1, 2, 1] has the largest sum = 6.

### Example 2:
**Input:**
```
1
-1
```
**Output:**
```
-1
```
**Explanation:** The array has only one element, so the answer is -1.

### Example 3:
**Input:**
```
5
5 4 -1 7 8
```
**Output:**
```
23
```
**Explanation:** The entire array is the subarray with maximum sum.

## Hints
<details>
<summary>Hint 1</summary>
At each index, you have two choices: either extend the previous subarray or start a new subarray from the current element.
</details>

<details>
<summary>Hint 2</summary>
If the running sum becomes negative, it is better to start fresh from the current element.
</details>

## Tags
`array` `dynamic-programming` `kadane` `subarray`
