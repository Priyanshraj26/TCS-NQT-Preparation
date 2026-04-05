# Check if Array Has Duplicates

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- `true` or `false`

## Constraints
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
4
1 2 3 1
```
**Output:**
```
true
```
**Explanation:** 1 appears twice.

### Example 2:
**Input:**
```
4
1 2 3 4
```
**Output:**
```
false
```

### Example 3:
**Input:**
```
5
1 1 1 3 3
```
**Output:**
```
true
```

## Hints
<details>
<summary>Hint 1</summary>
What data structure lets you check if an element was seen before in O(1)?
</details>

<details>
<summary>Hint 2</summary>
Alternatively, if you sort the array, duplicates will be adjacent.
</details>

## Tags
`array` `hash-set` `sorting`
