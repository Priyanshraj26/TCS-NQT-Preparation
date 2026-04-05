# Longest Palindromic Substring

**Difficulty:** Medium  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★

## Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

If there are multiple palindromic substrings of the same maximum length, return the first one found.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print the longest palindromic substring.

## Constraints

- 1 <= |s| <= 1000
- The string contains only lowercase English letters.

## Examples

### Example 1
```
Input:  babad
Output: bab
```
**Explanation:** "aba" is also a valid answer.

### Example 2
```
Input:  cbbd
Output: bb
```

### Example 3
```
Input:  racecar
Output: racecar
```

## Hints

1. **Brute force:** Check all substrings and verify if each is a palindrome. This is O(n^3).
2. **Expand around center:** For each character (and each pair of adjacent characters), expand outward while the substring remains a palindrome. This is O(n^2).
3. There are 2n - 1 possible centers (n single characters + n-1 gaps between characters).

## Tags

`String` `Dynamic Programming` `Expand Around Center` `TCS NQT` `Medium`
