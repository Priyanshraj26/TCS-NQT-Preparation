# Solution: Count Vowels and Consonants

[< Back to Question](../../DSA-Questions/Strings/Q005-count-vowels-consonants.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Simple Iteration | O(n) | O(1) | Only approach needed |

---

## Approach 1: Brute Force - Using string::find

Check if each character exists in a vowels string.

```cpp
#include <iostream>
#include <string>
using namespace std;

void countVowelsConsonantsBrute(string s, int &vowels, int &consonants) {
    vowels = 0;
    consonants = 0;
    string vowelStr = "aeiouAEIOU";

    for (char c : s) {
        if (isalpha(c)) {
            if (vowelStr.find(c) != string::npos) {
                vowels++;
            } else {
                consonants++;
            }
        }
    }
}

int main() {
    string tests[] = {"Hello World", "aeiou", "bcdfg", "TCS NQT 2025"};
    int expV[] = {3, 5, 0, 1};
    int expC[] = {7, 0, 5, 5};

    for (int i = 0; i < 4; i++) {
        int v, c;
        countVowelsConsonantsBrute(tests[i], v, c);
        cout << "Input: \"" << tests[i] << "\" -> Vowels: " << v << ", Consonants: " << c;
        cout << (v == expV[i] && c == expC[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

**Time Complexity:** O(n * 10) = O(n) since vowel string has fixed length 10  
**Space Complexity:** O(1)

---

## Approach 2: Optimized - Using Set Lookup

Use a set for O(1) vowel lookup and a single pass.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

void countVowelsConsonants(string s, int &vowels, int &consonants) {
    vowels = 0;
    consonants = 0;
    unordered_set<char> vowelSet = {'a', 'e', 'i', 'o', 'u'};

    for (char c : s) {
        if (isalpha(c)) {
            if (vowelSet.count(tolower(c))) {
                vowels++;
            } else {
                consonants++;
            }
        }
    }
}

int main() {
    string tests[] = {"Hello World", "aeiou", "bcdfg", "TCS NQT 2025", "a", "Programming123"};
    int expV[] = {3, 5, 0, 1, 1, 4};
    int expC[] = {7, 0, 5, 5, 0, 7};

    for (int i = 0; i < 6; i++) {
        int v, c;
        countVowelsConsonants(tests[i], v, c);
        cout << "Input: \"" << tests[i] << "\" -> Vowels: " << v << ", Consonants: " << c;
        cout << (v == expV[i] && c == expC[i] ? " PASS" : " FAIL") << endl;
    }
    return 0;
}
```

### Dry Run

Input: `"Hello World"`

| Index | Char | isAlpha? | toLower | isVowel? | Vowels | Consonants |
|-------|------|----------|---------|----------|--------|------------|
| 0 | H | Yes | h | No | 0 | 1 |
| 1 | e | Yes | e | Yes | 1 | 1 |
| 2 | l | Yes | l | No | 1 | 2 |
| 3 | l | Yes | l | No | 1 | 3 |
| 4 | o | Yes | o | Yes | 2 | 3 |
| 5 | ' ' | No | - | - | 2 | 3 |
| 6 | W | Yes | w | No | 2 | 4 |
| 7 | o | Yes | o | Yes | 3 | 4 |
| 8 | r | Yes | r | No | 3 | 5 |
| 9 | l | Yes | l | No | 3 | 6 |
| 10 | d | Yes | d | No | 3 | 7 |

Result: **Vowels: 3, Consonants: 7**

**Time Complexity:** O(n) - single pass  
**Space Complexity:** O(1) - fixed-size set

---

## Common Mistakes

1. **Forgetting case sensitivity:** 'A' and 'a' are both vowels.
2. **Counting spaces/digits as consonants:** Only alphabetic characters should be counted.
3. **Not using `isalpha()` to filter:** Digits and symbols must be skipped.

## Interview Tips

- This is a straightforward problem, so focus on writing clean, bug-free code quickly.
- Mention that you are handling edge cases: uppercase, digits, special characters.
- In TCS NQT, this is often a warm-up question -- solve it confidently and quickly.
