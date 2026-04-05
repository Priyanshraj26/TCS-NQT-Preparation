# String Compression (Run Length Encoding)

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★

## Problem Statement

Given a string `s`, compress it using **Run Length Encoding (RLE)**. In RLE, consecutive duplicate characters are replaced by the character followed by the count of repetitions.

If the compressed string is not shorter than the original, return the original string.

## Input Format

- A single line containing a string `s`.

## Output Format

- Print the compressed string.

## Constraints

- 1 <= |s| <= 10^5
- The string contains only uppercase and/or lowercase English letters.

## Examples

### Example 1
```
Input:  aabcccccaaa
Output: a2b1c5a3
```

### Example 2
```
Input:  abcdef
Output: abcdef
```
**Explanation:** Compressed form "a1b1c1d1e1f1" is longer, so return original.

### Example 3
```
Input:  aaabbaa
Output: a3b2a2
```

## Hints

1. Iterate through the string, counting consecutive identical characters.
2. When the character changes, append the character and its count to the result.
3. Compare the length of the compressed string with the original before returning.

## Tags

`String` `Run Length Encoding` `Compression` `TCS NQT` `Easy`
