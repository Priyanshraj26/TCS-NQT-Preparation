/*
 * Q001: Valid Parentheses
 * Question: ../../../DSA-Questions/Other-Topics/Q001-valid-parentheses.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Stack-based           | O(n)      | O(n)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <stack>
#include <string>
#include <cassert>
using namespace std;

// ===========================================
// Stack-based Solution
// ===========================================
bool isValid(const string& s) {
    stack<char> st;

    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } else {
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
    return st.empty();
}

// ===========================================
// Dry Run (s = "{[]}")
// ===========================================
/*
 * c='{': push '{' -> stack: ['{']
 * c='[': push '[' -> stack: ['{', '[']
 * c=']': top='[', matches -> pop -> stack: ['{']
 * c='}': top='{', matches -> pop -> stack: []
 * stack is empty -> return true
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(isValid("()") == true);
    assert(isValid("()[]{}") == true);
    assert(isValid("(]") == false);
    assert(isValid("([)]") == false);
    assert(isValid("{[]}") == true);
    assert(isValid("") == true);
    assert(isValid("(") == false);
    assert(isValid(")") == false);
    assert(isValid("((()))") == true);
    assert(isValid("({[)]}") == false);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    string s;
    cout << "Enter string: ";
    cin >> s;
    cout << (isValid(s) ? "YES" : "NO") << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(n), Space: O(n)
 *
 * Common Mistakes:
 *   - Forgetting to check if stack is empty before accessing top
 *   - Forgetting to check stack is empty at the end
 *   - Wrong matching pairs
 *
 * Interview Tips:
 *   - Most common stack problem
 *   - Can be extended: remove invalid parentheses, min additions, etc.
 *   - Alternative: use counter for single type, but stack needed for multiple types
 */
