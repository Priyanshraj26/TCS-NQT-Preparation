# Longest Common Prefix

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★

## Problem Statement

Given an array of strings, find the **longest common prefix** among all strings.

If there is no common prefix, return an empty string "".

## Input Format

- First line: an integer `n` (number of strings).
- Next `n` lines: one string per line.

## Output Format

- Print the longest common prefix, or an empty string if none exists.

## Constraints

- 1 <= n <= 200
- 0 <= |strings[i]| <= 200
- All strings contain only lowercase English letters.

## Examples

### Example 1
```
Input:
3
flower
flow
flight
Output: fl
```

### Example 2
```
Input:
3
dog
racecar
car
Output:
```
**Explanation:** No common prefix among the input strings.

### Example 3
```
Input:
3
interview
internet
internal
Output: inter
```

## Hints

1. **Vertical scanning:** Compare characters column by column across all strings.
2. Start with the first string as the prefix and progressively shorten it.
3. The prefix length cannot exceed the length of the shortest string.

## Tags

`String` `Prefix` `Comparison` `TCS NQT` `Easy`
