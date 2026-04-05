# Solution: Word Frequency Count

[< Back to Question](../../DSA-Questions/Strings/Q015-word-frequency.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (nested loop) | O(n^2) | O(n) | Check each word against all |
| Hash Map + Vector | O(n) | O(n) | Optimal - preserves order |

---

## Approach 1: Brute Force - Nested Loop

For each word, check if it was already counted. If not, count its occurrences.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

string toLowerStr(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

void wordFrequencyBrute(string sentence) {
    vector<string> words;
    stringstream ss(sentence);
    string word;
    while (ss >> word) {
        words.push_back(toLowerStr(word));
    }

    vector<bool> counted(words.size(), false);

    for (int i = 0; i < (int)words.size(); i++) {
        if (counted[i]) continue;
        int count = 0;
        for (int j = i; j < (int)words.size(); j++) {
            if (words[j] == words[i]) {
                count++;
                counted[j] = true;
            }
        }
        cout << words[i] << " " << count << endl;
    }
}

int main() {
    cout << "=== Test 1 ===" << endl;
    wordFrequencyBrute("the cat sat on the mat the cat");

    cout << "\n=== Test 2 ===" << endl;
    wordFrequencyBrute("Hello hello HELLO");

    cout << "\n=== Test 3 ===" << endl;
    wordFrequencyBrute("one two three");

    return 0;
}
```

**Time Complexity:** O(n^2) where n is the number of words  
**Space Complexity:** O(n)

---

## Approach 2: Optimized - Hash Map with Insertion Order

Use an `unordered_map` for counting and a `vector` to preserve the order of first appearance.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <algorithm>
using namespace std;

string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

void wordFrequency(string sentence) {
    unordered_map<string, int> freq;
    vector<string> order; // to preserve insertion order
    stringstream ss(sentence);
    string word;

    while (ss >> word) {
        word = toLower(word);
        if (freq.find(word) == freq.end()) {
            order.push_back(word); // first appearance
        }
        freq[word]++;
    }

    for (string &w : order) {
        cout << w << " " << freq[w] << endl;
    }
}

int main() {
    cout << "=== Test 1 ===" << endl;
    wordFrequency("the cat sat on the mat the cat");
    // Expected: the 3, cat 2, sat 1, on 1, mat 1

    cout << "\n=== Test 2 ===" << endl;
    wordFrequency("Hello hello HELLO");
    // Expected: hello 3

    cout << "\n=== Test 3 ===" << endl;
    wordFrequency("one two three");
    // Expected: one 1, two 1, three 1

    cout << "\n=== Test 4 ===" << endl;
    wordFrequency("a a a b b c");
    // Expected: a 3, b 2, c 1

    return 0;
}
```

### Dry Run

Input: `"the cat sat on the mat the cat"`

| Word | Already in map? | freq after | order |
|------|----------------|------------|-------|
| the | No | {the:1} | [the] |
| cat | No | {the:1, cat:1} | [the, cat] |
| sat | No | {the:1, cat:1, sat:1} | [the, cat, sat] |
| on | No | {..., on:1} | [the, cat, sat, on] |
| the | Yes | {the:2, ...} | (unchanged) |
| mat | No | {..., mat:1} | [the, cat, sat, on, mat] |
| the | Yes | {the:3, ...} | (unchanged) |
| cat | Yes | {..., cat:2} | (unchanged) |

**Output:**
```
the 3
cat 2
sat 1
on 1
mat 1
```

**Time Complexity:** O(n) where n is the number of words - hash map operations are O(1) average  
**Space Complexity:** O(n) for the map and order vector

---

## Common Mistakes

1. **Not handling case insensitivity:** "Hello" and "hello" must be treated as the same word.
2. **Losing insertion order:** `unordered_map` does not preserve order, so use a separate vector.
3. **Not tokenizing properly:** Handle multiple spaces or trailing spaces using `stringstream`.

## Interview Tips

- Use `stringstream` for tokenization -- it handles multiple spaces automatically.
- The combination of `unordered_map` + `vector` for ordered frequency counting is a useful pattern.
- In Python this is trivial with `collections.Counter` and `OrderedDict`, but in C++ you need to be explicit.
- This is a common TCS NQT question -- focus on clean, correct code.
