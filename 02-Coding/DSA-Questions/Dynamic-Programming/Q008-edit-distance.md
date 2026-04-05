# Q008: Edit Distance

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Hard                         |
| **Topic**      | Dynamic Programming          |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★                           |

---

## Problem Statement

Given two strings `word1` and `word2`, return the **minimum number of operations** required to convert `word1` to `word2`. You have three operations:
- **Insert** a character
- **Delete** a character
- **Replace** a character

---

## Input Format

- Two strings `word1` and `word2`

## Output Format

- Minimum number of operations (edit distance).

---

## Constraints

- 0 <= word1.length, word2.length <= 500
- Strings consist of lowercase English letters.

---

## Examples

### Example 1
```
Input:  word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse (replace h with r) -> rose (remove r) -> ros (remove e)
```

### Example 2
```
Input:  word1 = "intention", word2 = "execution"
Output: 5
```

---

## Hints

1. If last characters match, no operation needed for them.
2. If they don't match, try all three operations and take the minimum.
3. dp[i][j] = edit distance between word1[0..i-1] and word2[0..j-1].

---

## Tags

`Dynamic Programming` `Strings` `2D DP` `TCS NQT` `Hard`
