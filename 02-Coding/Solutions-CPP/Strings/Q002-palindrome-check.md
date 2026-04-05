# Solution: Check if String is Palindrome

[< Back to Question](../../DSA-Questions/Strings/Q002-palindrome-check.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Reverse and Compare | O(n) | O(n) | Simple but uses extra space |
| Two Pointers | O(n) | O(1) | Optimal approach |

---

## Approach 1: Brute Force - Reverse and Compare

Clean the string, reverse it, and compare with the original cleaned string.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isPalindromeBrute(string s) {
    // Clean the string: keep only alphanumeric, convert to lowercase
    string cleaned = "";
    for (char c : s) {
        if (isalnum(c)) {
            cleaned += tolower(c);
        }
    }

    string reversed = cleaned;
    reverse(reversed.begin(), reversed.end());
    return cleaned == reversed;
}

int main() {
    string tests[] = {"madam", "hello", "A man a plan a canal Panama", "racecar", "ab"};
    bool expected[] = {true, false, true, true, false};

    for (int i = 0; i < 5; i++) {
        bool result = isPalindromeBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << (result ? "YES" : "NO");
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for the cleaned and reversed strings

---

## Approach 2: Optimized - Two Pointers

Use two pointers from both ends, skipping non-alphanumeric characters, comparing in lowercase.

```cpp
#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string s) {
    int left = 0, right = s.length() - 1;

    while (left < right) {
        // Skip non-alphanumeric from left
        while (left < right && !isalnum(s[left])) left++;
        // Skip non-alphanumeric from right
        while (left < right && !isalnum(s[right])) right--;

        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    string tests[] = {"madam", "hello", "A man a plan a canal Panama", "racecar", "ab", "a", ""};
    bool expected[] = {true, false, true, true, false, true, true};

    for (int i = 0; i < 7; i++) {
        bool result = isPalindrome(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << (result ? "YES" : "NO");
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"A man a plan a canal Panama"`

| Step | left | right | s[left] | s[right] | Match? |
|------|------|-------|---------|----------|--------|
| 1 | 0 | 26 | 'A' | 'a' | Yes (both 'a') |
| 2 | 2 | 25 | 'm' | 'm' | Yes |
| 3 | 3 | 24 | 'a' | 'a' | Yes |
| 4 | 4 | 23 | 'n' | 'n' | Yes |
| ... | ... | ... | ... | ... | All match |

Result: **YES** (palindrome)

**Time Complexity:** O(n) - each character visited at most once  
**Space Complexity:** O(1) - no extra space used

---

## Common Mistakes

1. **Not handling case sensitivity:** "Madam" should be treated as a palindrome.
2. **Not skipping non-alphanumeric characters:** Spaces and punctuation should be ignored.
3. **Empty string edge case:** An empty string is considered a palindrome.

## Interview Tips

- Clarify with the interviewer: should we ignore case? Should we ignore non-alphanumeric characters?
- The two-pointer approach is the go-to for palindrome problems.
- Mention that this pattern extends to many problems: valid palindrome II (allow one deletion), etc.
