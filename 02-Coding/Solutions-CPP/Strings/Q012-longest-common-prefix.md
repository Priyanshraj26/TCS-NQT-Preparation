# Solution: Longest Common Prefix

[< Back to Question](../../DSA-Questions/Strings/Q012-longest-common-prefix.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Vertical Scanning | O(S) | O(1) | S = sum of all characters |
| Horizontal Scanning | O(S) | O(1) | Compare pairs progressively |
| Sorting-based | O(n*m*log n) | O(1) | Sort then compare first and last |

---

## Approach 1: Brute Force - Horizontal Scanning

Start with the first string as the prefix. Compare it with each subsequent string, shortening the prefix each time.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string longestCommonPrefixHorizontal(vector<string> &strs) {
    if (strs.empty()) return "";

    string prefix = strs[0];

    for (int i = 1; i < (int)strs.size(); i++) {
        // Shorten prefix until it matches the beginning of strs[i]
        while (strs[i].find(prefix) != 0) {
            prefix = prefix.substr(0, prefix.length() - 1);
            if (prefix.empty()) return "";
        }
    }
    return prefix;
}

int main() {
    vector<vector<string>> tests = {
        {"flower", "flow", "flight"},
        {"dog", "racecar", "car"},
        {"interview", "internet", "internal"},
        {"a"},
        {"", "b"}
    };
    string expected[] = {"fl", "", "inter", "a", ""};

    for (int i = 0; i < 5; i++) {
        string result = longestCommonPrefixHorizontal(tests[i]);
        cout << "Input: [";
        for (int j = 0; j < (int)tests[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << "\"" << tests[i][j] << "\"";
        }
        cout << "] -> \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(S) where S is the sum of all string lengths  
**Space Complexity:** O(1) extra space

---

## Approach 2: Optimized - Vertical Scanning

Compare characters column by column across all strings. Stop at the first mismatch.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string longestCommonPrefix(vector<string> &strs) {
    if (strs.empty()) return "";

    for (int col = 0; col < (int)strs[0].length(); col++) {
        char c = strs[0][col];
        for (int row = 1; row < (int)strs.size(); row++) {
            // If current string is too short or character doesn't match
            if (col >= (int)strs[row].length() || strs[row][col] != c) {
                return strs[0].substr(0, col);
            }
        }
    }
    return strs[0]; // entire first string is the prefix
}

int main() {
    vector<vector<string>> tests = {
        {"flower", "flow", "flight"},
        {"dog", "racecar", "car"},
        {"interview", "internet", "internal"},
        {"a"},
        {"", "b"},
        {"abc", "abc", "abc"}
    };
    string expected[] = {"fl", "", "inter", "a", "", "abc"};

    for (int i = 0; i < 6; i++) {
        string result = longestCommonPrefix(tests[i]);
        cout << "Input: [";
        for (int j = 0; j < (int)tests[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << "\"" << tests[i][j] << "\"";
        }
        cout << "] -> \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `["flower", "flow", "flight"]`

| Col | Char (strs[0]) | strs[1] | strs[2] | Match? |
|-----|----------------|---------|---------|--------|
| 0 | 'f' | 'f' | 'f' | Yes |
| 1 | 'l' | 'l' | 'l' | Yes |
| 2 | 'o' | 'o' | 'i' | No! Return "fl" |

Result: **"fl"**

**Time Complexity:** O(S) where S = sum of all characters, but in best case stops early  
**Space Complexity:** O(1)

---

## Common Mistakes

1. **Not handling empty array or empty strings:** Always check edge cases first.
2. **Going out of bounds on shorter strings:** Must check length before accessing characters.
3. **Using the longest string as base:** Should handle the case where any string might be shortest.

## Interview Tips

- Vertical scanning is the cleanest and most intuitive approach.
- An alternative trick: sort the array, then only compare the first and last strings (they are the most different).
- This is a LeetCode Easy problem -- solve it quickly and move on in interviews.
