# Count Vowels and Consonants

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement

Given a string `s`, count the number of **vowels** and **consonants** in it.

Vowels are: a, e, i, o, u (both uppercase and lowercase).  
Consonants are all other alphabetic characters.  
Non-alphabetic characters (digits, spaces, symbols) should be ignored.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print two space-separated integers: the number of vowels and the number of consonants.

## Constraints

- 1 <= |s| <= 10^5

## Examples

### Example 1
```
Input:  Hello World
Output: 3 7
```
**Explanation:** Vowels: e, o, o (3). Consonants: H, l, l, W, r, l, d (7). Space is ignored.

### Example 2
```
Input:  aeiou
Output: 5 0
```

### Example 3
```
Input:  bcdfg
Output: 0 5
```

## Hints

1. Convert each character to lowercase before checking.
2. Use `isalpha()` to filter out non-alphabetic characters.
3. Check if a character is in the set {'a','e','i','o','u'} for vowels; otherwise it is a consonant.

## Tags

`String` `Counting` `Basic` `TCS NQT` `Easy`
