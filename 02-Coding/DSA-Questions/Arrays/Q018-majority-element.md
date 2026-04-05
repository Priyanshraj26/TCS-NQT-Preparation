# Majority Element (Moore's Voting Algorithm)

**Difficulty:** Medium  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an array `nums` of size `n`, find the majority element. The majority element is the element that appears more than `n/2` times. You may assume that the majority element always exists in the array.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- A single integer — the majority element

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9
- The majority element always exists

## Examples

### Example 1:
**Input:**
```
7
2 2 1 1 1 2 2
```
**Output:**
```
2
```
**Explanation:** 2 appears 4 times (> 7/2 = 3).

### Example 2:
**Input:**
```
3
3 2 3
```
**Output:**
```
3
```

## Hints
<details>
<summary>Hint 1</summary>
If you cancel out each occurrence of the majority element with a different element, the majority element will still remain.
</details>

<details>
<summary>Hint 2</summary>
Boyer-Moore Voting Algorithm: maintain a candidate and a count. When count reaches 0, pick a new candidate.
</details>

## Tags
`array` `voting-algorithm` `boyer-moore` `frequency`
