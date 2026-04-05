# Solution: Check if Two Strings are Anagrams

[< Back to Question](../../DSA-Questions/Strings/Q003-anagram-check.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Sorting | O(n log n) | O(1) | Simple approach |
| Frequency Array | O(n) | O(1) | Optimal - 26-size array |

---

## Approach 1: Brute Force - Sorting

Sort both strings and compare. Anagrams will produce identical sorted strings.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isAnagramSort(string s, string t) {
    if (s.length() != t.length()) return false;
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    return s == t;
}

int main() {
    string s[] = {"listen", "hello", "anagram", "ab", "a"};
    string t[] = {"silent", "world", "nagaram", "ba", "b"};
    bool expected[] = {true, false, true, true, false};

    for (int i = 0; i < 5; i++) {
        bool result = isAnagramSort(s[i], t[i]);
        cout << "\"" << s[i] << "\" vs \"" << t[i] << "\" -> " << (result ? "YES" : "NO");
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n log n) due to sorting  
**Space Complexity:** O(1) if sorting in-place (ignoring sort's internal stack)

---

## Approach 2: Optimized - Frequency Array

Count character frequencies for both strings using an array of size 26. If all counts match, they are anagrams.

```cpp
#include <iostream>
#include <string>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;

    int freq[26] = {0};

    for (int i = 0; i < (int)s.length(); i++) {
        freq[s[i] - 'a']++;
        freq[t[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++) {
        if (freq[i] != 0) return false;
    }
    return true;
}

int main() {
    string s[] = {"listen", "hello", "anagram", "ab", "a", "abc"};
    string t[] = {"silent", "world", "nagaram", "ba", "b", "abcd"};
    bool expected[] = {true, false, true, true, false, false};

    for (int i = 0; i < 6; i++) {
        bool result = isAnagram(s[i], t[i]);
        cout << "\"" << s[i] << "\" vs \"" << t[i] << "\" -> " << (result ? "YES" : "NO");
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: s = `"listen"`, t = `"silent"`

| Step | char s | char t | freq after operation |
|------|--------|--------|---------------------|
| 0 | l(+1) | s(-1) | l:1, s:-1 |
| 1 | i(+1) | i(-1) | l:1, s:-1, i:0 |
| 2 | s(+1) | l(-1) | l:0, s:0 |
| 3 | t(+1) | e(-1) | t:1, e:-1 |
| 4 | e(+1) | n(-1) | t:1, e:0, n:-1 |
| 5 | n(+1) | t(-1) | t:0, n:0 |

All frequencies are 0 -> **YES** (anagram)

**Time Complexity:** O(n) - single pass through both strings  
**Space Complexity:** O(1) - fixed array of size 26

---

## Common Mistakes

1. **Forgetting length check:** If lengths differ, they cannot be anagrams.
2. **Case sensitivity:** Clarify if 'A' and 'a' should be treated the same.
3. **Using a map instead of array:** Works but slower; a fixed-size array is better for lowercase letters.

## Interview Tips

- Always check lengths first -- it is a quick early return.
- The single-array trick (increment for s, decrement for t) is elegant and memory efficient.
- If the character set is large (Unicode), use a hash map instead of a fixed array.
