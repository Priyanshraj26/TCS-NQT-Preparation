# Check if Two Strings are Anagrams

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★

## Problem Statement

Given two strings `s` and `t`, determine if `t` is an **anagram** of `s`. An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

## Input Format

- Two lines, each containing a string (`s` and `t`).

## Output Format

- Print `YES` if the strings are anagrams, otherwise print `NO`.

## Constraints

- 1 <= |s|, |t| <= 10^5
- The strings contain only lowercase English letters.

## Examples

### Example 1
```
Input:
listen
silent
Output: YES
```

### Example 2
```
Input:
hello
world
Output: NO
```

### Example 3
```
Input:
anagram
nagaram
Output: YES
```

## Hints

1. If two strings are anagrams, they must have the same length.
2. Sort both strings and compare — anagrams will become identical after sorting.
3. A more efficient approach: use a frequency array of size 26 to count character occurrences.

## Tags

`String` `Hashing` `Sorting` `Frequency Array` `TCS NQT` `Easy`
