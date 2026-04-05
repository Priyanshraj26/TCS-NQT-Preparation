# Find Missing Number (1 to N)

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an array `nums` containing `n` distinct numbers taken from the range `[1, n+1]`, find the one number in the range that is missing from the array.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- A single integer — the missing number

## Constraints
- 1 <= n <= 10^5
- All numbers in the array are distinct
- Each number is in the range [1, n+1]

## Examples

### Example 1:
**Input:**
```
4
1 2 4 5
```
**Output:**
```
3
```

### Example 2:
**Input:**
```
3
3 1 2
```
**Output:**
```
4
```
**Explanation:** Range is [1, 4]. Missing number is 4.

## Hints
<details>
<summary>Hint 1</summary>
Sum of first n+1 natural numbers is (n+1)*(n+2)/2. What if you subtract the array sum?
</details>

<details>
<summary>Hint 2</summary>
Alternatively, XOR all numbers from 1 to n+1 and XOR with all array elements.
</details>

## Tags
`array` `math` `xor` `sum`
