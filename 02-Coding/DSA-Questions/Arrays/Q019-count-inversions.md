# Count Inversions (Merge Sort)

**Difficulty:** Hard  
**Topic:** Array  
**Source:** TCS NQT  
**Frequency:** ★★★★☆

## Problem Statement
Given an array of integers, count the number of inversions. An inversion is a pair `(i, j)` such that `i < j` and `nums[i] > nums[j]`. The inversion count indicates how far the array is from being sorted.

## Input Format
- First line: integer `n` (size of array)
- Second line: `n` space-separated integers

## Output Format
- A single integer — the number of inversions

## Constraints
- 1 <= n <= 10^5
- 1 <= nums[i] <= 10^9

## Examples

### Example 1:
**Input:**
```
5
2 4 1 3 5
```
**Output:**
```
3
```
**Explanation:** Inversions are (2,1), (4,1), (4,3).

### Example 2:
**Input:**
```
5
5 4 3 2 1
```
**Output:**
```
10
```
**Explanation:** Every pair is an inversion. C(5,2) = 10.

### Example 3:
**Input:**
```
3
1 2 3
```
**Output:**
```
0
```

## Hints
<details>
<summary>Hint 1</summary>
Modify merge sort. During the merge step, when an element from the right half is picked before elements from the left half, it contributes inversions.
</details>

<details>
<summary>Hint 2</summary>
If left[i] > right[j], then all remaining elements in the left half (from i to mid) form inversions with right[j].
</details>

## Tags
`array` `merge-sort` `divide-and-conquer` `inversions`
