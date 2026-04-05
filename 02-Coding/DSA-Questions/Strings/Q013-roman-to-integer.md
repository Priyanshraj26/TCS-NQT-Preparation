# Roman to Integer

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★

## Problem Statement

Given a Roman numeral string, convert it to an integer.

Roman numerals are represented by seven symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5    |
| X      | 10   |
| L      | 50   |
| C      | 100  |
| D      | 500  |
| M      | 1000 |

Roman numerals use subtraction for certain combinations:
- `IV` = 4, `IX` = 9
- `XL` = 40, `XC` = 90
- `CD` = 400, `CM` = 900

## Input Format

- A single line containing a Roman numeral string.

## Output Format

- Print the integer value.

## Constraints

- 1 <= |s| <= 15
- `s` contains only characters: I, V, X, L, C, D, M.
- Input is guaranteed to be a valid Roman numeral in the range [1, 3999].

## Examples

### Example 1
```
Input:  III
Output: 3
```

### Example 2
```
Input:  LVIII
Output: 58
```
**Explanation:** L = 50, V = 5, III = 3.

### Example 3
```
Input:  MCMXCIV
Output: 1994
```
**Explanation:** M = 1000, CM = 900, XC = 90, IV = 4.

## Hints

1. Traverse from left to right. If the current value is less than the next value, subtract it; otherwise add it.
2. Use a map to store the value of each Roman character.

## Tags

`String` `Hash Map` `Math` `TCS NQT` `Easy`
