# Check Balanced Parentheses

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★★

## Problem Statement

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string has **balanced (valid) parentheses**.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Input Format

- A single line containing the string `s`.

## Output Format

- Print `YES` if the parentheses are balanced, otherwise `NO`.

## Constraints

- 1 <= |s| <= 10^4
- `s` consists of only `()[]{}` characters.

## Examples

### Example 1
```
Input:  ()[]{}
Output: YES
```

### Example 2
```
Input:  (]
Output: NO
```

### Example 3
```
Input:  {[()]}
Output: YES
```

### Example 4
```
Input:  ([)]
Output: NO
```

## Hints

1. Use a **stack** data structure.
2. Push every opening bracket onto the stack.
3. For every closing bracket, check if the top of the stack is the matching opening bracket.
4. At the end, the stack should be empty for a valid string.

## Tags

`String` `Stack` `Parentheses` `TCS NQT` `Easy`
