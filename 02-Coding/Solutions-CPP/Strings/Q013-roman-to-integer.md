# Solution: Roman to Integer

[< Back to Question](../../DSA-Questions/Strings/Q013-roman-to-integer.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Left to Right with Subtraction Rule | O(n) | O(1) | Clean and optimal |
| Right to Left | O(n) | O(1) | Alternative approach |

---

## Approach 1: Brute Force - Replace Subtractive Forms First

Replace all subtractive combinations (IV, IX, etc.) with placeholder values, then sum normally.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int romanToIntBrute(string s) {
    unordered_map<char, int> val = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    int result = 0;

    for (int i = 0; i < (int)s.length(); i++) {
        // If current value is less than next, it's a subtractive pair
        if (i + 1 < (int)s.length() && val[s[i]] < val[s[i + 1]]) {
            result += val[s[i + 1]] - val[s[i]];
            i++; // skip next character
        } else {
            result += val[s[i]];
        }
    }
    return result;
}

int main() {
    string tests[] = {"III", "LVIII", "MCMXCIV", "IV", "IX", "XL", "MMXXVI"};
    int expected[] = {3, 58, 1994, 4, 9, 40, 2026};

    for (int i = 0; i < 7; i++) {
        int result = romanToIntBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << result;
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Approach 2: Optimized - Left to Right Subtraction Rule

Traverse left to right. If the current value is less than the next value, subtract it; otherwise add it.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int romanToInt(string s) {
    unordered_map<char, int> val = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    int result = 0;
    int n = s.length();

    for (int i = 0; i < n; i++) {
        // If current value < next value, subtract current
        if (i < n - 1 && val[s[i]] < val[s[i + 1]]) {
            result -= val[s[i]];
        } else {
            result += val[s[i]];
        }
    }
    return result;
}

int main() {
    string tests[] = {"III", "LVIII", "MCMXCIV", "IV", "IX", "XL", "MMXXVI", "CDXLIV", "MMMCMXCIX"};
    int expected[] = {3, 58, 1994, 4, 9, 40, 2026, 444, 3999};

    for (int i = 0; i < 9; i++) {
        int result = romanToInt(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << result;
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"MCMXCIV"` (expected: 1994)

| i | s[i] | val[s[i]] | val[s[i+1]] | Action | result |
|---|------|-----------|-------------|--------|--------|
| 0 | M | 1000 | 100 (C) | 1000 > 100, ADD | 1000 |
| 1 | C | 100 | 1000 (M) | 100 < 1000, SUB | 900 |
| 2 | M | 1000 | 10 (X) | 1000 > 10, ADD | 1900 |
| 3 | X | 10 | 100 (C) | 10 < 100, SUB | 1890 |
| 4 | C | 100 | 1 (I) | 100 > 1, ADD | 1990 |
| 5 | I | 1 | 5 (V) | 1 < 5, SUB | 1989 |
| 6 | V | 5 | (end) | ADD | 1994 |

Result: **1994**

**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(1) - the map has fixed 7 entries

---

## Common Mistakes

1. **Forgetting subtraction cases:** IV=4, not I+V=6.
2. **Not checking bounds when comparing with next:** s[i+1] can be out of bounds at the last character.
3. **Using if-else chains instead of a map:** Both work, but a map is cleaner.

## Interview Tips

- The key insight is simple: if a smaller value appears before a larger value, subtract it.
- This problem tests your ability to translate clear rules into clean code.
- Mention the valid range is 1-3999 for standard Roman numerals.
