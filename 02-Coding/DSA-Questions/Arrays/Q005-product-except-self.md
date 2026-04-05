# Product of Array Except Self

**Difficulty:** Medium  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must solve it **without using division** and in O(n) time.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- `n` space-separated integers representing the product array

## Constraints
- 2 <= n <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix fits in a 32-bit integer

## Examples

### Example 1:
**Input:**
```
4
1 2 3 4
```
**Output:**
```
24 12 8 6
```
**Explanation:** For index 0: 2*3*4=24, index 1: 1*3*4=12, etc.

### Example 2:
**Input:**
```
5
-1 1 0 -3 3
```
**Output:**
```
0 0 9 0 0
```

## Hints
<details>
<summary>Hint 1</summary>
Think about prefix products and suffix products.
</details>

<details>
<summary>Hint 2</summary>
For each index i, the answer is (product of all elements to the left) * (product of all elements to the right).
</details>

## Tags
`array` `prefix-product` `suffix-product`
