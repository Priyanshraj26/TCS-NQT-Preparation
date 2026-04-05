# Print All Permutations of a String

**Difficulty:** Medium  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★

## Problem Statement

Given a string `s`, print all **permutations** of the string. A permutation is a rearrangement of all the characters.

Print the permutations in **lexicographically sorted** order. If there are duplicate characters, avoid printing duplicate permutations.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print each unique permutation on a new line, in sorted order.

## Constraints

- 1 <= |s| <= 8
- The string contains only lowercase English letters.

## Examples

### Example 1
```
Input:  abc
Output:
abc
acb
bac
bca
cab
cba
```

### Example 2
```
Input:  ab
Output:
ab
ba
```

### Example 3
```
Input:  aab
Output:
aab
aba
baa
```

## Hints

1. Sort the string first, then use `next_permutation()` from C++ STL for the simplest approach.
2. Alternatively, use **backtracking**: fix each character at the current position and recurse for the rest.
3. To avoid duplicates, skip characters that are the same as a previously fixed character at the same position.

## Tags

`String` `Backtracking` `Recursion` `Permutation` `TCS NQT` `Medium`
