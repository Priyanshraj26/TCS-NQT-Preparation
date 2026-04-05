# Solution: Longest Palindromic Substring

[< Back to Question](../../DSA-Questions/Strings/Q007-longest-palindromic-substring.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (all substrings) | O(n^3) | O(1) | Check each substring |
| Expand Around Center | O(n^2) | O(1) | Optimal for interviews |
| Dynamic Programming | O(n^2) | O(n^2) | DP table approach |

---

## Approach 1: Brute Force - Check All Substrings

Generate all substrings and check if each is a palindrome.

```cpp
#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string &s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++;
        right--;
    }
    return true;
}

string longestPalindromeBrute(string s) {
    int n = s.length();
    if (n < 2) return s;

    int start = 0, maxLen = 1;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (isPalindrome(s, i, j) && (j - i + 1) > maxLen) {
                start = i;
                maxLen = j - i + 1;
            }
        }
    }
    return s.substr(start, maxLen);
}

int main() {
    string tests[] = {"babad", "cbbd", "racecar", "a", "ac"};
    // Note: "babad" can return "bab" or "aba" - both are valid
    string expected[] = {"bab", "bb", "racecar", "a", "a"};

    for (int i = 0; i < 5; i++) {
        string result = longestPalindromeBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> \"" << result << "\"";
        cout << ((int)result.length() == (int)expected[i].length() ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n^3) - O(n^2) substrings, O(n) to check each  
**Space Complexity:** O(1)

---

## Approach 2: Optimized - Expand Around Center

For each possible center, expand outward while the substring is a palindrome. There are 2n-1 centers: n single characters and n-1 gaps between characters.

```cpp
#include <iostream>
#include <string>
using namespace std;

int expandAroundCenter(string &s, int left, int right) {
    while (left >= 0 && right < (int)s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1; // length of palindrome
}

string longestPalindrome(string s) {
    int n = s.length();
    if (n < 2) return s;

    int start = 0, maxLen = 1;

    for (int i = 0; i < n; i++) {
        // Odd-length palindromes (single center)
        int len1 = expandAroundCenter(s, i, i);
        // Even-length palindromes (two-char center)
        int len2 = expandAroundCenter(s, i, i + 1);

        int len = max(len1, len2);
        if (len > maxLen) {
            maxLen = len;
            start = i - (len - 1) / 2;
        }
    }
    return s.substr(start, maxLen);
}

int main() {
    string tests[] = {"babad", "cbbd", "racecar", "a", "ac", "aacabdkacaa", "bb"};
    int expLen[] = {3, 2, 7, 1, 1, 3, 2};

    for (int i = 0; i < 7; i++) {
        string result = longestPalindrome(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> \"" << result << "\" (len=" << result.length() << ")";
        cout << ((int)result.length() == expLen[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"cbbd"`

| Center i | Odd expand (i,i) | Even expand (i,i+1) | Best len | maxLen | start |
|----------|-------------------|---------------------|----------|--------|-------|
| 0 ('c') | "c" (1) | "cb" (0) | 1 | 1 | 0 |
| 1 ('b') | "b" (1) | "bb" (2) | 2 | 2 | 1 |
| 2 ('b') | "b" (1) | "bd" (0) | 1 | 2 | 1 |
| 3 ('d') | "d" (1) | - | 1 | 2 | 1 |

Result: `s.substr(1, 2)` = **"bb"**

**Time Complexity:** O(n^2) - for each center, expansion takes O(n)  
**Space Complexity:** O(1) - no extra space

---

## Common Mistakes

1. **Forgetting even-length palindromes:** Must check both single-char and two-char centers.
2. **Wrong start index calculation:** `start = i - (len - 1) / 2` is easy to get wrong.
3. **Returning length instead of the substring:** Read the problem carefully.

## Interview Tips

- Expand Around Center is the best approach for interviews -- easy to explain and implement.
- Mention Manacher's Algorithm (O(n)) if asked for further optimization, but it is rarely expected.
- Always handle edge cases: single character, all same characters, empty string.
