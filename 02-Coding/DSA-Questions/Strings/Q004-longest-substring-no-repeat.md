# Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters within the string.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print the length of the longest substring without repeating characters.

## Constraints

- 0 <= |s| <= 10^5
- The string consists of English letters, digits, symbols, and spaces.

## Examples

### Example 1
```
Input:  abcabcbb
Output: 3
```
**Explanation:** The answer is "abc", with a length of 3.

### Example 2
```
Input:  bbbbb
Output: 1
```
**Explanation:** The answer is "b", with a length of 1.

### Example 3
```
Input:  pwwkew
Output: 3
```
**Explanation:** The answer is "wke", with a length of 3. Note that "pwke" is a subsequence, not a substring.

## Hints

1. A brute force approach checks all substrings — but this is O(n^3).
2. Use the **sliding window** technique with two pointers.
3. Maintain a set or hash map to track characters in the current window.
4. When a duplicate is found, shrink the window from the left.

## Tags

`String` `Sliding Window` `Hash Map` `Two Pointers` `TCS NQT` `Medium`
