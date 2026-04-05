# Solution: Longest Substring Without Repeating Characters

[< Back to Question](../../DSA-Questions/Strings/Q004-longest-substring-no-repeat.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (all substrings) | O(n^3) | O(min(n, m)) | Check every substring |
| Sliding Window + Set | O(2n) = O(n) | O(min(n, m)) | Good approach |
| Sliding Window + Map | O(n) | O(min(n, m)) | Optimal - jump left pointer |

---

## Approach 1: Brute Force - Check All Substrings

For each starting index, find the longest substring without repeats.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int lengthOfLongestSubstringBrute(string s) {
    int n = s.length();
    int maxLen = 0;

    for (int i = 0; i < n; i++) {
        unordered_set<char> seen;
        for (int j = i; j < n; j++) {
            if (seen.count(s[j])) break;
            seen.insert(s[j]);
            maxLen = max(maxLen, j - i + 1);
        }
    }
    return maxLen;
}

int main() {
    string tests[] = {"abcabcbb", "bbbbb", "pwwkew", "", "abcdef"};
    int expected[] = {3, 1, 3, 0, 6};

    for (int i = 0; i < 5; i++) {
        int result = lengthOfLongestSubstringBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << result;
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n^2) (with early break; worst case O(n^2))  
**Space Complexity:** O(min(n, m)) where m is the character set size

---

## Approach 2: Optimized - Sliding Window with Hash Map

Maintain a window [left, right]. Use a map to store the last index of each character. When a duplicate is found, jump the left pointer past the previous occurrence.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int lengthOfLongestSubstring(string s) {
    int n = s.length();
    unordered_map<char, int> lastIndex; // char -> last seen index
    int maxLen = 0;
    int left = 0;

    for (int right = 0; right < n; right++) {
        char c = s[right];
        // If character was seen and is within current window
        if (lastIndex.count(c) && lastIndex[c] >= left) {
            left = lastIndex[c] + 1; // jump left past the duplicate
        }
        lastIndex[c] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}

int main() {
    string tests[] = {"abcabcbb", "bbbbb", "pwwkew", "", "abcdef", "abba", "tmmzuxt"};
    int expected[] = {3, 1, 3, 0, 6, 2, 5};

    for (int i = 0; i < 7; i++) {
        int result = lengthOfLongestSubstring(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << result;
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"abcabcbb"`

| right | char | lastIndex[c] | left | window | maxLen |
|-------|------|-------------|------|--------|--------|
| 0 | a | - | 0 | "a" | 1 |
| 1 | b | - | 0 | "ab" | 2 |
| 2 | c | - | 0 | "abc" | 3 |
| 3 | a | 0 (>=0) | 1 | "bca" | 3 |
| 4 | b | 1 (>=1) | 2 | "cab" | 3 |
| 5 | c | 2 (>=2) | 3 | "abc" | 3 |
| 6 | b | 4 (>=3) | 5 | "cb" | 3 |
| 7 | b | 6 (>=5) | 7 | "b" | 3 |

Result: **3**

**Time Complexity:** O(n) - single pass, each character processed once  
**Space Complexity:** O(min(n, m)) where m is the character set size

---

## Common Mistakes

1. **Not checking if the duplicate is within the current window:** `lastIndex[c] >= left` is crucial. Without this check, "abba" gives wrong answer.
2. **Using a set-based sliding window and forgetting to shrink properly:** The set approach requires removing characters one by one from the left.
3. **Off-by-one errors:** The window length is `right - left + 1`.

## Interview Tips

- This is a classic sliding window problem -- mention the pattern name.
- The key insight is that when you find a duplicate, you can jump the left pointer directly to `lastIndex[c] + 1` instead of incrementing one by one.
- For ASCII characters only, you can use an array of size 128 instead of a hash map for better performance.
