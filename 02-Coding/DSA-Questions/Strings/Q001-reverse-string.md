# Reverse a String

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement

Given a string `s`, reverse the string and return it.

You should try to solve this **in-place** (i.e., without using extra space for another string).

## Input Format

- A single line containing a string `s` (1 <= |s| <= 10^5).

## Output Format

- Print the reversed string.

## Constraints

- 1 <= |s| <= 10^5
- The string may contain lowercase/uppercase English letters, digits, and special characters.

## Examples

### Example 1
```
Input:  hello
Output: olleh
```

### Example 2
```
Input:  TCS NQT
Output: TQN SCT
```

### Example 3
```
Input:  abcba
Output: abcba
```
**Explanation:** This string is a palindrome, so its reverse is the same.

## Hints

1. Use two pointers — one at the beginning, one at the end. Swap characters and move inward.
2. The built-in `reverse()` function in C++ STL can also do this in one line.
3. Think about what happens if the string has odd vs even length.

## Tags

`String` `Two Pointers` `In-Place` `TCS NQT` `Easy`
