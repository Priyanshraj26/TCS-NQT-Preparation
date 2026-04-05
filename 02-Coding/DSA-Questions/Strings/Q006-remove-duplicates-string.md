# Remove Duplicates from String

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★

## Problem Statement

Given a string `s`, remove all duplicate characters from it such that each character appears only **once**. The order of characters in the result should be the same as their **first occurrence** in the original string.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print the string after removing duplicate characters.

## Constraints

- 1 <= |s| <= 10^5
- The string contains only lowercase English letters.

## Examples

### Example 1
```
Input:  programming
Output: progamin
```
**Explanation:** Remove repeated characters: second 'r', second 'g', second 'm' are removed.

### Example 2
```
Input:  abcabc
Output: abc
```

### Example 3
```
Input:  aaaaaa
Output: a
```

## Hints

1. Use a boolean visited array of size 26 to track which characters have been seen.
2. Iterate through the string; if a character is not yet seen, add it to the result.
3. Alternatively, use an `unordered_set` for tracking.

## Tags

`String` `Hashing` `Set` `TCS NQT` `Easy`
