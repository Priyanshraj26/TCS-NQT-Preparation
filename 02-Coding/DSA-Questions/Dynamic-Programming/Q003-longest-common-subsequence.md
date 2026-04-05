# Q003: Longest Common Subsequence

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Medium                       |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Given two strings `text1` and `text2`, return the length of their **longest common subsequence** (LCS). A subsequence is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

If there is no common subsequence, return 0.

---

## Input Format

- Two strings `text1` and `text2`

## Output Format

- An integer representing the length of the LCS.

---

## Constraints

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

---

## Examples

### Example 1
```
Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: LCS is "ace", length = 3.
```

### Example 2
```
Input:  text1 = "abc", text2 = "def"
Output: 0
Explanation: No common subsequence.
```

### Example 3
```
Input:  text1 = "abcba", text2 = "abcbcba"
Output: 5
Explanation: LCS is "abcba", length = 5.
```

---

## Hints

1. If the last characters match, LCS includes that character + LCS of remaining.
2. If they don't match, take the max of excluding one character from either string.
3. Build a 2D table where dp[i][j] = LCS of text1[0..i-1] and text2[0..j-1].

---

## Tags

`Dynamic Programming` `Strings` `2D DP` `TCS NQT` `Medium`
