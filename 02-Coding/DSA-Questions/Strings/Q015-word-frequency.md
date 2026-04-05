# Word Frequency Count

**Difficulty:** Easy  
**Topic:** String  
**Source:** TCS NQT  
**Frequency:** ★★★★

## Problem Statement

Given a sentence (string of words separated by spaces), count the **frequency** of each word and print each word with its count.

Words are case-insensitive (treat "Hello" and "hello" as the same word). Print the words in the order of their first appearance.

## Input Format

- A single line containing the sentence.

## Output Format

- For each unique word, print the word (in lowercase) followed by a space and its count, one per line.

## Constraints

- 1 <= number of words <= 10^4
- Each word contains only English letters.

## Examples

### Example 1
```
Input:  the cat sat on the mat the cat
Output:
the 3
cat 2
sat 1
on 1
mat 1
```

### Example 2
```
Input:  Hello hello HELLO
Output:
hello 3
```

### Example 3
```
Input:  one two three
Output:
one 1
two 1
three 1
```

## Hints

1. Use a hash map (`unordered_map` or `map`) to store word frequencies.
2. Convert each word to lowercase before counting.
3. To maintain insertion order, use a vector alongside the map, or use an ordered approach.

## Tags

`String` `Hash Map` `Counting` `Tokenization` `TCS NQT` `Easy`
