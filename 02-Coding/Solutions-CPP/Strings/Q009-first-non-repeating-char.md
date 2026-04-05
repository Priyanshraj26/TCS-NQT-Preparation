# Solution: First Non-Repeating Character

[< Back to Question](../../DSA-Questions/Strings/Q009-first-non-repeating-char.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (nested loop) | O(n^2) | O(1) | Check each char against all others |
| Frequency Array (two pass) | O(n) | O(1) | Optimal approach |

---

## Approach 1: Brute Force - Nested Loop

For each character, count its occurrences in the entire string.

```cpp
#include <iostream>
#include <string>
using namespace std;

int firstNonRepeatingBrute(string s) {
    int n = s.length();
    for (int i = 0; i < n; i++) {
        bool duplicate = false;
        for (int j = 0; j < n; j++) {
            if (i != j && s[i] == s[j]) {
                duplicate = true;
                break;
            }
        }
        if (!duplicate) return i;
    }
    return -1;
}

int main() {
    string tests[] = {"leetcode", "loveleetcode", "aabb", "a", "aadadaad"};
    int expected[] = {0, 2, -1, 0, -1};

    for (int i = 0; i < 5; i++) {
        int result = firstNonRepeatingBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << result;
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n^2)  
**Space Complexity:** O(1)

---

## Approach 2: Optimized - Frequency Array (Two Pass)

First pass: count frequency of each character. Second pass: find the first character with frequency 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

int firstNonRepeating(string s) {
    int freq[26] = {0};

    // Pass 1: Count frequencies
    for (char c : s) {
        freq[c - 'a']++;
    }

    // Pass 2: Find first with frequency 1
    for (int i = 0; i < (int)s.length(); i++) {
        if (freq[s[i] - 'a'] == 1) {
            return i;
        }
    }
    return -1;
}

int main() {
    string tests[] = {"leetcode", "loveleetcode", "aabb", "a", "aadadaad", "abcabc"};
    int expected[] = {0, 2, -1, 0, -1, -1};

    for (int i = 0; i < 6; i++) {
        int result = firstNonRepeating(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> Index: " << result;
        if (result != -1) cout << " ('" << tests[i][result] << "')";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"loveleetcode"`

**Pass 1 - Frequency Count:**

| Char | l | o | v | e | t | c | d |
|------|---|---|---|---|---|---|---|
| Freq | 1 | 2 | 1 | 4 | 1 | 1 | 1 |

**Pass 2 - Find First with freq=1:**

| Index | Char | Freq | Result |
|-------|------|------|--------|
| 0 | l | 1 | -- wait, l appears at index 0 and... |

Let me recount: l-o-v-e-l-e-e-t-c-o-d-e

| Char | l | o | v | e | t | c | d |
|------|---|---|---|---|---|---|---|
| Freq | 2 | 2 | 1 | 4 | 1 | 1 | 1 |

| Index | Char | Freq | Found? |
|-------|------|------|--------|
| 0 | l | 2 | No |
| 1 | o | 2 | No |
| 2 | v | 1 | Yes! Return 2 |

Result: **2** (character 'v')

**Time Complexity:** O(n) - two passes through the string  
**Space Complexity:** O(1) - fixed array of size 26

---

## Common Mistakes

1. **Returning the character instead of the index:** Read the problem statement carefully.
2. **Using a map and iterating over it:** Map iteration order is not the same as string order.
3. **Single pass approach errors:** Some try to do it in one pass but the logic is more complex.

## Interview Tips

- This is a very common TCS NQT question -- practice it until you can write it without thinking.
- The two-pass approach is simple and efficient; no need for anything more complex.
- If asked to find the first non-repeating character in a stream, mention using a queue + frequency array.
