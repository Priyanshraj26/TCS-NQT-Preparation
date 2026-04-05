# Solution: Print All Permutations of a String

[< Back to Question](../../DSA-Questions/Strings/Q011-all-permutations.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| STL next_permutation | O(n! * n) | O(1) | Simplest in C++ |
| Backtracking | O(n! * n) | O(n) | Classic recursion approach |

---

## Approach 1: Brute Force - Using STL next_permutation

Sort the string first, then use `next_permutation` to generate all permutations in order.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void printPermutationsSTL(string s) {
    sort(s.begin(), s.end());
    do {
        cout << s << endl;
    } while (next_permutation(s.begin(), s.end()));
}

int main() {
    cout << "=== Test 1: abc ===" << endl;
    printPermutationsSTL("abc");

    cout << "\n=== Test 2: ab ===" << endl;
    printPermutationsSTL("ab");

    cout << "\n=== Test 3: aab (duplicates) ===" << endl;
    printPermutationsSTL("aab");

    cout << "\n=== Test 4: a ===" << endl;
    printPermutationsSTL("a");

    return 0;
}
```

**Time Complexity:** O(n! * n) - n! permutations, each takes O(n) to generate/print  
**Space Complexity:** O(1) extra space (in-place permutation)

---

## Approach 2: Optimized - Backtracking with Duplicate Handling

Fix each character at the current position, then recursively permute the rest. Skip duplicates by sorting first and checking if the same character was already used at this position.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void backtrack(string &s, int start, vector<string> &result) {
    if (start == (int)s.length()) {
        result.push_back(s);
        return;
    }

    for (int i = start; i < (int)s.length(); i++) {
        // Skip duplicates: if s[i] was already placed at position 'start'
        // by a previous iteration, skip it
        bool skip = false;
        for (int j = start; j < i; j++) {
            if (s[j] == s[i]) {
                skip = true;
                break;
            }
        }
        if (skip) continue;

        swap(s[start], s[i]);
        backtrack(s, start + 1, result);
        swap(s[start], s[i]); // backtrack
    }
}

vector<string> getPermutations(string s) {
    vector<string> result;
    sort(s.begin(), s.end());
    backtrack(s, 0, result);
    sort(result.begin(), result.end()); // ensure lexicographic order
    return result;
}

int main() {
    // Test 1
    cout << "=== Test: abc ===" << endl;
    vector<string> perms = getPermutations("abc");
    for (string &p : perms) cout << p << endl;
    cout << "Total: " << perms.size() << " (expected 6)" << endl;

    // Test 2
    cout << "\n=== Test: aab ===" << endl;
    perms = getPermutations("aab");
    for (string &p : perms) cout << p << endl;
    cout << "Total: " << perms.size() << " (expected 3)" << endl;

    // Test 3
    cout << "\n=== Test: a ===" << endl;
    perms = getPermutations("a");
    for (string &p : perms) cout << p << endl;
    cout << "Total: " << perms.size() << " (expected 1)" << endl;

    return 0;
}
```

### Dry Run

Input: `"abc"`

```
backtrack("abc", 0)
  i=0: swap(0,0) -> "abc", recurse(1)
    i=1: swap(1,1) -> "abc", recurse(2)
      i=2: swap(2,2) -> "abc" -> STORE "abc"
    i=2: swap(1,2) -> "acb", recurse(2)
      STORE "acb"
    swap back -> "abc"
  i=1: swap(0,1) -> "bac", recurse(1)
    i=1: swap(1,1) -> "bac" -> ... -> STORE "bac"
    i=2: swap(1,2) -> "bca" -> ... -> STORE "bca"
    swap back -> "bac"
  swap back -> "abc"
  i=2: swap(0,2) -> "cba", recurse(1)
    i=1: swap(1,1) -> "cba" -> ... -> STORE "cba"
    i=2: swap(1,2) -> "cab" -> ... -> STORE "cab"
    swap back -> "cba"
  swap back -> "abc"
```

Result: abc, acb, bac, bca, cab, cba (sorted: abc, acb, bac, bca, cab, cba)

**Time Complexity:** O(n! * n)  
**Space Complexity:** O(n) recursion depth + O(n!) for storing results

---

## Common Mistakes

1. **Not handling duplicate characters:** "aab" should produce 3 permutations, not 6.
2. **Forgetting to backtrack (swap back):** This corrupts the string for subsequent iterations.
3. **Not sorting the output:** The problem asks for lexicographic order.

## Interview Tips

- For TCS NQT, the `next_permutation` approach is perfectly acceptable and much simpler.
- If asked to implement from scratch, use the backtracking approach.
- Always ask: are there duplicate characters? This changes the approach.
- Mention the total count: n! permutations for n distinct characters, fewer with duplicates.
