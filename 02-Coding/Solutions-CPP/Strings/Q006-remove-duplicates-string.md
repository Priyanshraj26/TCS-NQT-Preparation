# Solution: Remove Duplicates from String

[< Back to Question](../../DSA-Questions/Strings/Q006-remove-duplicates-string.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (nested loop) | O(n^2) | O(n) | Check each char against previous |
| Boolean Array | O(n) | O(1) | Fixed 26-size array |
| unordered_set | O(n) | O(1) | Hash set for tracking |

---

## Approach 1: Brute Force - Check Against Previous Characters

For each character, check if it already appeared earlier in the string.

```cpp
#include <iostream>
#include <string>
using namespace std;

string removeDuplicatesBrute(string s) {
    string result = "";
    for (int i = 0; i < (int)s.length(); i++) {
        bool found = false;
        for (int j = 0; j < (int)result.length(); j++) {
            if (result[j] == s[i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            result += s[i];
        }
    }
    return result;
}

int main() {
    string tests[] = {"programming", "abcabc", "aaaaaa", "abcdef", "aabbcc"};
    string expected[] = {"progamin", "abc", "a", "abcdef", "abc"};

    for (int i = 0; i < 5; i++) {
        string result = removeDuplicatesBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n^2) in worst case  
**Space Complexity:** O(n) for the result string

---

## Approach 2: Optimized - Boolean Visited Array

Use a boolean array of size 26 to track which characters have been seen.

```cpp
#include <iostream>
#include <string>
using namespace std;

string removeDuplicates(string s) {
    bool seen[26] = {false};
    string result = "";

    for (char c : s) {
        if (!seen[c - 'a']) {
            seen[c - 'a'] = true;
            result += c;
        }
    }
    return result;
}

int main() {
    string tests[] = {"programming", "abcabc", "aaaaaa", "abcdef", "aabbcc", "a"};
    string expected[] = {"progamin", "abc", "a", "abcdef", "abc", "a"};

    for (int i = 0; i < 6; i++) {
        string result = removeDuplicates(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"programming"`

| Index | Char | seen? | Action | Result |
|-------|------|-------|--------|--------|
| 0 | p | No | Add | "p" |
| 1 | r | No | Add | "pr" |
| 2 | o | No | Add | "pro" |
| 3 | g | No | Add | "prog" |
| 4 | r | Yes | Skip | "prog" |
| 5 | a | No | Add | "proga" |
| 6 | m | No | Add | "progam" |
| 7 | m | Yes | Skip | "progam" |
| 8 | i | No | Add | "progami" |
| 9 | n | No | Add | "progamin" |
| 10 | g | Yes | Skip | "progamin" |

Result: **"progamin"**

**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(1) - fixed boolean array of size 26

---

## Common Mistakes

1. **Changing the order of characters:** The result must preserve first-occurrence order.
2. **Using sort to remove duplicates:** This changes the order -- not acceptable here.
3. **Not handling the constraint correctly:** If the string can have uppercase or special characters, adjust the array size.

## Interview Tips

- Clarify whether order matters -- it almost always does.
- The boolean array approach is the cleanest for lowercase-only inputs.
- For general character sets, use an `unordered_set<char>` instead.
