# Solution: Check if Array Has Duplicates

[← Back to Question](../../DSA-Questions/Arrays/Q004-contains-duplicate.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Sorting | O(n log n) | O(1) | ✗ |
| Hash Set | O(n) | O(n) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Compare every pair of elements.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicateBrute(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j]) return true;
            }
        }
        return false;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 1};
    cout << (sol.containsDuplicateBrute(nums) ? "true" : "false") << endl; // true
    return 0;
}
```

---

## Approach 2: Hash Set (Optimal)

### Intuition
Insert elements into a set one by one. If an element already exists in the set, we found a duplicate.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) return true;
            seen.insert(num);
        }
        return false;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 3, 1};
    cout << (sol.containsDuplicate(v1) ? "true" : "false") << endl; // true

    // Test 2
    vector<int> v2 = {1, 2, 3, 4};
    cout << (sol.containsDuplicate(v2) ? "true" : "false") << endl; // false

    // Test 3
    vector<int> v3 = {1, 1, 1, 3, 3};
    cout << (sol.containsDuplicate(v3) ? "true" : "false") << endl; // true

    // Test 4: single element
    vector<int> v4 = {5};
    cout << (sol.containsDuplicate(v4) ? "true" : "false") << endl; // false

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 3, 1]`

| Index | num | seen | Found? |
|-------|-----|------|--------|
| 0 | 1 | {1} | No |
| 1 | 2 | {1,2} | No |
| 2 | 3 | {1,2,3} | No |
| 3 | 1 | — | Yes → return true |

**Output:** `true`

### Complexity Analysis
- **Time:** O(n) — single pass, O(1) average set operations
- **Space:** O(n) — set stores up to n elements

---

## Common Mistakes
1. Using `unordered_map` when `unordered_set` suffices (wastes space)
2. Forgetting to handle single-element arrays

## Interview Tips
- Mention the sorting approach O(n log n) time O(1) space as a trade-off
- Follow-up: find all duplicates, or find the duplicate number (1 to n)
