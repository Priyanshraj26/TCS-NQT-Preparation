# Leaders in an Array

**Difficulty:** Easy  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
An element is a **leader** if it is greater than or equal to all the elements to its right. The rightmost element is always a leader. Find all leaders in the array and print them in order of their appearance.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- Space-separated leader elements in order of appearance

## Constraints
- 1 <= n <= 10^5
- 0 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
6
16 17 4 3 5 2
```
**Output:**
```
17 5 2
```
**Explanation:** 17 > all to its right, 5 > 2, and 2 is the last element.

### Example 2:
**Input:**
```
5
1 2 3 4 5
```
**Output:**
```
5
```

## Hints
<details>
<summary>Hint 1</summary>
Traverse from right to left, keeping track of the maximum seen so far.
</details>

## Tags
`array` `traversal` `right-to-left`
