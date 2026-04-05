# Solution: Reverse a String

[< Back to Question](../../DSA-Questions/Strings/Q001-reverse-string.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Two Pointers (In-Place) | O(n) | O(1) | Best approach |
| Using STL reverse() | O(n) | O(1) | Shortest code |
| New String (Brute Force) | O(n) | O(n) | Extra space used |

---

## Approach 1: Brute Force - Build New String

Iterate from the end of the string to the beginning and append each character to a new string.

```cpp
#include <iostream>
#include <string>
using namespace std;

string reverseStringBrute(string s) {
    string result = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        result += s[i];
    }
    return result;
}

int main() {
    // Test cases
    string tests[] = {"hello", "TCS NQT", "abcba", "a", ""};
    string expected[] = {"olleh", "TQN SCT", "abcba", "a", ""};

    for (int i = 0; i < 5; i++) {
        string result = reverseStringBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> Output: \"" << result << "\"";
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for the new string

---

## Approach 2: Optimized - Two Pointers (In-Place)

Use two pointers starting at the beginning and end. Swap characters and move inward until they meet.

```cpp
#include <iostream>
#include <string>
using namespace std;

void reverseString(string &s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }
}

int main() {
    // Test cases
    string tests[] = {"hello", "TCS NQT", "abcba", "a", "ab"};
    string expected[] = {"olleh", "TQN SCT", "abcba", "a", "ba"};

    for (int i = 0; i < 5; i++) {
        string s = tests[i];
        reverseString(s);
        cout << "Input: \"" << tests[i] << "\" -> Output: \"" << s << "\"";
        cout << (s == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"hello"`

| Step | left | right | Action | String |
|------|------|-------|--------|--------|
| 0 | 0 | 4 | swap h,o | "oellh" |
| 1 | 1 | 3 | swap e,l | "olleh" |
| 2 | 2 | 2 | left >= right, stop | "olleh" |

**Time Complexity:** O(n) - single pass with two pointers  
**Space Complexity:** O(1) - in-place swap, no extra space

---

## Common Mistakes

1. **Off-by-one error:** Using `left <= right` instead of `left < right` (works but does an unnecessary swap when left == right).
2. **Forgetting to handle empty string:** Always check for edge cases.
3. **Creating a new string when in-place is required:** Read the problem carefully.

## Interview Tips

- Mention the two-pointer technique explicitly -- interviewers look for this.
- If asked to do it recursively, swap `s[0]` and `s[n-1]`, then recurse on the substring `s[1..n-2]`.
- In C++ you can also use `reverse(s.begin(), s.end())` from `<algorithm>` for a one-liner.
