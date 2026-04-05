# Pattern Matching / String Search

**Difficulty:** Medium  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★

## Problem Statement

Given a text string `t` and a pattern string `p`, find all occurrences of `p` in `t`. Return the starting indices (0-based) of each occurrence.

## Input Format

- First line: the text string `t`.
- Second line: the pattern string `p`.

## Output Format

- Print the starting indices of all occurrences of the pattern, space-separated.
- If the pattern is not found, print -1.

## Constraints

- 1 <= |p| <= |t| <= 10^5
- Both strings contain only lowercase English letters.

## Examples

### Example 1
```
Input:
aabaacaadaabaaba
aaba
Output: 0 9 12
```

### Example 2
```
Input:
abcdef
gh
Output: -1
```

### Example 3
```
Input:
aaaaaa
aa
Output: 0 1 2 3 4
```

## Hints

1. **Brute force:** For each position in the text, check if the pattern matches. O(n*m).
2. **KMP Algorithm:** Precompute a longest-prefix-suffix (LPS) array to skip unnecessary comparisons. O(n+m).
3. The `string::find()` function in C++ can also be used in a loop.

## Tags

`String` `Pattern Matching` `KMP` `Brute Force` `TCS NQT` `Medium`
