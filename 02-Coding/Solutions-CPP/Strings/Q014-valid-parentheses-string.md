# Solution: Check Balanced Parentheses

[< Back to Question](../../DSA-Questions/Strings/Q014-valid-parentheses-string.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Stack-based | O(n) | O(n) | Classic and optimal approach |
| Counter (single type only) | O(n) | O(1) | Only works for one bracket type |

---

## Approach 1: Brute Force - Repeated Removal

Repeatedly remove innermost valid pairs "()", "[]", "{}" until no more can be removed. If string becomes empty, it is valid.

```cpp
#include <iostream>
#include <string>
using namespace std;

bool isValidBrute(string s) {
    string prev = "";
    while (s != prev) {
        prev = s;
        string temp = "";
        int i = 0;
        while (i < (int)s.length()) {
            if (i + 1 < (int)s.length() &&
                ((s[i] == '(' && s[i+1] == ')') ||
                 (s[i] == '[' && s[i+1] == ']') ||
                 (s[i] == '{' && s[i+1] == '}'))) {
                i += 2; // skip the pair
            } else {
                temp += s[i];
                i++;
            }
        }
        s = temp;
    }
    return s.empty();
}

int main() {
    string tests[] = {"()[]{}", "(]", "{[()]}", "([)]", "(", "((()))", ""};
    bool expected[] = {true, false, true, false, false, true, true};

    for (int i = 0; i < 7; i++) {
        bool result = isValidBrute(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << (result ? "YES" : "NO");
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n^2) in worst case (repeated passes)  
**Space Complexity:** O(n)

---

## Approach 2: Optimized - Stack

Push opening brackets onto the stack. For each closing bracket, check if the top of the stack is the matching opening bracket.

```cpp
#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool isValid(string s) {
    stack<char> st;

    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            // Closing bracket
            if (st.empty()) return false;

            char top = st.top();
            if ((c == ')' && top == '(') ||
                (c == ']' && top == '[') ||
                (c == '}' && top == '{')) {
                st.pop();
            } else {
                return false;
            }
        }
    }
    return st.empty(); // stack must be empty for valid string
}

int main() {
    string tests[] = {"()[]{}", "(]", "{[()]}", "([)]", "(", "((()))", "", "{}", "((", ")("};
    bool expected[] = {true, false, true, false, false, true, true, true, false, false};

    for (int i = 0; i < 10; i++) {
        bool result = isValid(tests[i]);
        cout << "Input: \"" << tests[i] << "\" -> " << (result ? "YES" : "NO");
        cout << (result == expected[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"{[()]}"`

| Step | Char | Action | Stack |
|------|------|--------|-------|
| 1 | { | Push | { |
| 2 | [ | Push | { [ |
| 3 | ( | Push | { [ ( |
| 4 | ) | Match with (, Pop | { [ |
| 5 | ] | Match with [, Pop | { |
| 6 | } | Match with {, Pop | (empty) |

Stack is empty -> **YES**

Input: `"([)]"`

| Step | Char | Action | Stack |
|------|------|--------|-------|
| 1 | ( | Push | ( |
| 2 | [ | Push | ( [ |
| 3 | ) | Top is [, not ( | MISMATCH -> **NO** |

**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(n) - stack can hold up to n/2 elements

---

## Common Mistakes

1. **Not checking if stack is empty before popping:** A closing bracket with an empty stack means invalid.
2. **Forgetting to check if stack is empty at the end:** "((" has no mismatches but is still invalid.
3. **Only handling one type of bracket:** Must handle all three types.

## Interview Tips

- This is the most classic stack problem -- know it inside out.
- The key insight: a stack naturally handles the nesting property of brackets.
- Variant: what if the string contains other characters too? Just skip non-bracket characters.
- This is extremely common in TCS NQT -- practice until it is automatic.
