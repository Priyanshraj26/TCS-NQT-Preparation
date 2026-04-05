# Q001: Valid Parentheses

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Stack                        |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string has **valid** (balanced) parentheses.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket.

---

## Input Format

- A string `s` consisting of parentheses characters.

## Output Format

- "YES" if valid, "NO" otherwise.

---

## Constraints

- 1 <= s.length <= 10^4
- s consists of only `()[]{}` characters.

---

## Examples

### Example 1
```
Input:  s = "()"
Output: YES
```

### Example 2
```
Input:  s = "()[]{}"
Output: YES
```

### Example 3
```
Input:  s = "(]"
Output: NO
```

### Example 4
```
Input:  s = "([)]"
Output: NO
```

### Example 5
```
Input:  s = "{[]}"
Output: YES
```

---

## Hints

1. Use a stack to track opening brackets.
2. When encountering a closing bracket, check if the stack top is the matching opening bracket.
3. At the end, the stack must be empty.

---

## Tags

`Stack` `String` `Parentheses` `TCS NQT` `Easy`
