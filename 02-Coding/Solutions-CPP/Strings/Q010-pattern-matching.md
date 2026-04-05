# Solution: Pattern Matching / String Search

[< Back to Question](../../DSA-Questions/Strings/Q010-pattern-matching.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (Naive) | O(n * m) | O(1) | Simple sliding |
| KMP Algorithm | O(n + m) | O(m) | Optimal with LPS array |

---

## Approach 1: Brute Force - Naive Pattern Matching

Slide the pattern over the text one position at a time and check for a match.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> naiveSearch(string text, string pattern) {
    vector<int> result;
    int n = text.length();
    int m = pattern.length();

    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++) {
            if (text[i + j] != pattern[j]) break;
        }
        if (j == m) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    string texts[] = {"aabaacaadaabaaba", "abcdef", "aaaaaa"};
    string patterns[] = {"aaba", "gh", "aa"};

    for (int i = 0; i < 3; i++) {
        vector<int> result = naiveSearch(texts[i], patterns[i]);
        cout << "Text: \"" << texts[i] << "\", Pattern: \"" << patterns[i] << "\" -> ";
        if (result.empty()) {
            cout << -1;
        } else {
            for (int j = 0; j < (int)result.size(); j++) {
                if (j > 0) cout << " ";
                cout << result[j];
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n * m) in worst case  
**Space Complexity:** O(1) excluding output

---

## Approach 2: Optimized - KMP (Knuth-Morris-Pratt) Algorithm

Build an LPS (Longest Proper Prefix which is also Suffix) array for the pattern, then use it to skip unnecessary comparisons.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Build the LPS (failure function) array
vector<int> buildLPS(string pattern) {
    int m = pattern.length();
    vector<int> lps(m, 0);
    int len = 0; // length of previous longest prefix suffix
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1]; // fall back
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

vector<int> kmpSearch(string text, string pattern) {
    vector<int> result;
    int n = text.length();
    int m = pattern.length();

    if (m == 0 || m > n) return result;

    vector<int> lps = buildLPS(pattern);

    int i = 0; // index for text
    int j = 0; // index for pattern

    while (i < n) {
        if (text[i] == pattern[j]) {
            i++;
            j++;
        }

        if (j == m) {
            result.push_back(i - j); // match found
            j = lps[j - 1];         // continue searching
        } else if (i < n && text[i] != pattern[j]) {
            if (j != 0) {
                j = lps[j - 1]; // skip using LPS
            } else {
                i++;
            }
        }
    }
    return result;
}

int main() {
    // Test cases
    struct TestCase {
        string text, pattern;
        vector<int> expected;
    };

    TestCase tests[] = {
        {"aabaacaadaabaaba", "aaba", {0, 9, 12}},
        {"abcdef", "gh", {}},
        {"aaaaaa", "aa", {0, 1, 2, 3, 4}},
        {"abcabcabc", "abc", {0, 3, 6}},
    };

    for (int i = 0; i < 4; i++) {
        vector<int> result = kmpSearch(tests[i].text, tests[i].pattern);
        cout << "Text: \"" << tests[i].text << "\", Pattern: \"" << tests[i].pattern << "\" -> ";
        if (result.empty()) {
            cout << -1;
        } else {
            for (int j = 0; j < (int)result.size(); j++) {
                if (j > 0) cout << " ";
                cout << result[j];
            }
        }
        bool pass = (result == tests[i].expected);
        cout << (pass ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: text = `"aabaacaadaabaaba"`, pattern = `"aaba"`

**Step 1: Build LPS for "aaba"**

| i | pattern[i] | len | lps |
|---|-----------|-----|-----|
| 0 | a | - | [0, 0, 0, 0] |
| 1 | a | 0->1 | [0, 1, 0, 0] |
| 2 | b | 1->0 | [0, 1, 0, 0] |
| 3 | a | 0->1 | [0, 1, 0, 1] |

LPS = [0, 1, 0, 1]

**Step 2: Search**

| i | j | Match? | Action | Found? |
|---|---|--------|--------|--------|
| 0 | 0 | a==a | i++,j++ | - |
| 1 | 1 | a==a | i++,j++ | - |
| 2 | 2 | b==b | i++,j++ | - |
| 3 | 3 | a==a | i++,j++ | j==4: Found at 0! j=lps[3]=1 |
| 4 | 1 | a==a | i++,j++ | - |
| 5 | 2 | c!=b | j=lps[1]=1 | - |
| 5 | 1 | c!=a | j=lps[0]=0 | - |
| 5 | 0 | c!=a | i++ | - |
| ... | ... | ... | ... | Found at 9 and 12 |

Result: **0 9 12**

**Time Complexity:** O(n + m) - LPS build is O(m), search is O(n)  
**Space Complexity:** O(m) for the LPS array

---

## Common Mistakes

1. **Off-by-one in naive approach:** Loop should go up to `n - m`, not `n`.
2. **Incorrect LPS construction:** The fallback `len = lps[len - 1]` is often forgotten.
3. **Not handling overlapping matches:** "aaa" in "aaaa" should find matches at 0, 1.

## Interview Tips

- For TCS NQT, the naive approach is usually sufficient. KMP is a bonus.
- In C++, `string::find()` can be used in a loop as a quick alternative.
- If asked about KMP, focus on explaining the LPS array -- that is the core idea.
