# Solution: String Compression (Run Length Encoding)

[< Back to Question](../../DSA-Questions/Strings/Q008-string-compression.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Iterative Count | O(n) | O(n) | Only approach needed |

---

## Approach 1: Brute Force - Character by Character

Iterate and count each consecutive run, building the result string.

```cpp
#include <iostream>
#include <string>
using namespace std;

string compressBrute(string s) {
    if (s.empty()) return s;

    string result = "";
    int i = 0;

    while (i < (int)s.length()) {
        char c = s[i];
        int count = 0;
        while (i < (int)s.length() && s[i] == c) {
            count++;
            i++;
        }
        result += c;
        result += to_string(count);
    }

    return result.length() < s.length() ? result : s;
}

int main() {
    string tests[] = {"aabcccccaaa", "abcdef", "aaabbaa", "a", "aaa"};
    string expected[] = {"a2b1c5a3", "abcdef", "a3b2a2", "a", "a3"};

    for (int i = 0; i < 5; i++) {
        string result = compressBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for the result string

---

## Approach 2: Optimized - With Early Termination

Same logic but slightly cleaner, using index comparison.

```cpp
#include <iostream>
#include <string>
using namespace std;

string compress(string s) {
    int n = s.length();
    if (n <= 1) return s;

    string result = "";
    int count = 1;

    for (int i = 1; i <= n; i++) {
        if (i < n && s[i] == s[i - 1]) {
            count++;
        } else {
            result += s[i - 1];
            result += to_string(count);
            count = 1;
        }
    }

    return (int)result.length() < n ? result : s;
}

int main() {
    string tests[] = {"aabcccccaaa", "abcdef", "aaabbaa", "a", "aaa", "aabbcc", "aaAAaa"};
    string expected[] = {"a2b1c5a3", "abcdef", "a3b2a2", "a", "a3", "aabbcc", "a2A2a2"};

    for (int i = 0; i < 7; i++) {
        string result = compress(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"aabcccccaaa"`

| i | s[i] | s[i-1] | Same? | count | Action | Result |
|---|------|--------|-------|-------|--------|--------|
| 1 | a | a | Yes | 2 | - | "" |
| 2 | b | a | No | 1 | Append "a2" | "a2" |
| 3 | c | b | No | 1 | Append "b1" | "a2b1" |
| 4 | c | c | Yes | 2 | - | "a2b1" |
| 5 | c | c | Yes | 3 | - | "a2b1" |
| 6 | c | c | Yes | 4 | - | "a2b1" |
| 7 | c | c | Yes | 5 | - | "a2b1" |
| 8 | a | c | No | 1 | Append "c5" | "a2b1c5" |
| 9 | a | a | Yes | 2 | - | "a2b1c5" |
| 10 | a | a | Yes | 3 | - | "a2b1c5" |
| 11 | end | a | No | 1 | Append "a3" | "a2b1c5a3" |

Length: 8 < 11 -> return **"a2b1c5a3"**

**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(n) - result string

---

## Common Mistakes

1. **Not returning original when compressed is longer:** "abcdef" -> "a1b1c1d1e1f1" is longer.
2. **Forgetting the last group:** The loop must process the final run of characters.
3. **Case sensitivity:** 'a' and 'A' are different characters.

## Interview Tips

- Always clarify whether to return the original string if compression does not save space.
- This is also known as Run Length Encoding (RLE) -- use the proper term.
- Mention that `to_string()` handles counts > 9 automatically.
