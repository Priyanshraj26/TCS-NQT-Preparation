# First Non-Repeating Character

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement

Given a string `s`, find the **first non-repeating character** in it and return its index. If it does not exist, return -1.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print the index (0-based) of the first non-repeating character, or -1 if all characters repeat.

## Constraints

- 1 <= |s| <= 10^5
- The string contains only lowercase English letters.

## Examples

### Example 1
```
Input:  leetcode
Output: 0
```
**Explanation:** 'l' is the first character that does not repeat.

### Example 2
```
Input:  loveleetcode
Output: 2
```
**Explanation:** 'v' at index 2 is the first non-repeating character.

### Example 3
```
Input:  aabb
Output: -1
```

## Hints

1. Use a frequency array of size 26 to count occurrences of each character.
2. Make a second pass through the string and return the first character with a count of 1.
3. This is a classic two-pass approach with O(n) time.

## Tags

`String` `Hashing` `Frequency Array` `TCS NQT` `Easy`
