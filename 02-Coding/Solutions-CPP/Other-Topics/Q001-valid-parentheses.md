# Solution: Valid Parentheses

[← Back to Question](../../DSA-Questions/Other-Topics/Q001-valid-parentheses.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force (Replace) | O(n^2) | O(n) | ✗ |
| Stack-Based Matching | O(n) | O(n) | ✓✓ |

---

## Approach 1: Brute Force (Repeated Replacement)

### Intuition
Repeatedly remove adjacent valid pairs "()", "{}", "[]" until no more can be removed. If the string becomes empty, it is valid.

### C++ Code
```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        string prev = "";
        while (s != prev) {
            prev = s;
            size_t pos;
            while ((pos = s.find("()")) != string::npos) s.erase(pos, 2);
            while ((pos = s.find("{}")) != string::npos) s.erase(pos, 2);
            while ((pos = s.find("[]")) != string::npos) s.erase(pos, 2);
        }
        return s.empty();
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isValid("()") << endl;     // true
    cout << sol.isValid("()[]{}") << endl; // true
    cout << sol.isValid("(]") << endl;     // false
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n^2) -- each pass removes at most one pair, string operations are O(n)
- **Space:** O(n)

---

## Approach 2: Stack-Based Matching (Optimal)

### Intuition
Use a stack. For every opening bracket, push it. For every closing bracket, check if it matches the top of the stack. If it matches, pop; otherwise, the string is invalid. At the end, the stack must be empty.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                // Closing bracket -- must match top of stack
                if (st.empty()) return false;

                char top = st.top();
                if ((c == ')' && top == '(') ||
                    (c == '}' && top == '{') ||
                    (c == ']' && top == '[')) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }
        return st.empty(); // stack must be empty for valid string
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isValid("()") << endl;       // true
    cout << sol.isValid("()[]{}") << endl;   // true
    cout << sol.isValid("(]") << endl;       // false
    cout << sol.isValid("([)]") << endl;     // false
    cout << sol.isValid("{[]}") << endl;     // true
    cout << sol.isValid("") << endl;         // true (empty is valid)
    cout << sol.isValid("(") << endl;        // false
    cout << sol.isValid(")") << endl;        // false
    cout << sol.isValid("((()))") << endl;   // true
    return 0;
}
```

### Dry Run
**Input:** "{[()]}"

| Step | Char | Stack (top->bottom) | Action |
|------|------|---------------------|--------|
| 1 | { | { | push '{' |
| 2 | [ | [ { | push '[' |
| 3 | ( | ( [ { | push '(' |
| 4 | ) | [ { | ')' matches '(' -> pop |
| 5 | ] | { | ']' matches '[' -> pop |
| 6 | } | (empty) | '}' matches '{' -> pop |

Stack empty -> **true**

**Input:** "([)]"

| Step | Char | Stack (top->bottom) | Action |
|------|------|---------------------|--------|
| 1 | ( | ( | push '(' |
| 2 | [ | [ ( | push '[' |
| 3 | ) | -- | ')' does NOT match '[' -> **false** |

### Complexity Analysis
- **Time:** O(n) -- single pass through the string
- **Space:** O(n) -- stack can hold up to n/2 elements

---

## Common Mistakes
1. Forgetting to check `st.empty()` before accessing `st.top()` (causes undefined behavior)
2. Returning `true` when the loop ends without checking if stack is empty (e.g., "((" would be wrongly valid)
3. Only checking for one type of bracket

## Interview Tips
- This is the most classic stack problem -- appears very frequently in interviews and exams
- The key insight: a stack naturally handles nested structures (LIFO matches innermost first)
- Follow-up: minimum number of additions to make parentheses valid
- Follow-up: longest valid parentheses substring (DP or stack-based)
- For TCS NQT: be prepared to write this from memory
