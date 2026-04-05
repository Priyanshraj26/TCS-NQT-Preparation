# Check if String is Palindrome

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement

Given a string `s`, determine whether it is a **palindrome**. A palindrome reads the same forwards and backwards.

Consider only alphanumeric characters and ignore cases for the purpose of this problem.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print `YES` if the string is a palindrome, otherwise print `NO`.

## Constraints

- 1 <= |s| <= 10^5
- The string may contain lowercase/uppercase English letters, digits, spaces, and punctuation.

## Examples

### Example 1
```
Input:  madam
Output: YES
```

### Example 2
```
Input:  hello
Output: NO
```

### Example 3
```
Input:  A man a plan a canal Panama
Output: YES
```
**Explanation:** After removing spaces and ignoring case, the string becomes "amanaplanacanalpanama" which is a palindrome.

## Hints

1. Use two pointers from both ends of the string and compare characters moving inward.
2. Convert to lowercase first and skip non-alphanumeric characters for a cleaner comparison.
3. Alternatively, reverse the cleaned string and check if it equals the original cleaned string.

## Tags

`String` `Two Pointers` `Palindrome` `TCS NQT` `Easy`
