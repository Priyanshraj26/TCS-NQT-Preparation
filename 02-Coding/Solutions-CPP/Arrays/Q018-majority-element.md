# Solution: Majority Element (Moore's Voting Algorithm)

[← Back to Question](../../DSA-Questions/Arrays/Q018-majority-element.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Hash Map | O(n) | O(n) | ✗ |
| Boyer-Moore Voting | O(n) | O(1) | ✓ |

---

## Approach 1: Hash Map

### Intuition
Count frequency of each element. Return the one with count > n/2.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int majorityElementMap(vector<int>& nums) {
        unordered_map<int, int> freq;
        int n = nums.size();
        for (int x : nums) {
            freq[x]++;
            if (freq[x] > n / 2) return x;
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    cout << sol.majorityElementMap(nums) << endl; // 2
    return 0;
}
```

---

## Approach 2: Boyer-Moore Voting Algorithm (Optimal)

### Intuition
The idea: if we cancel out each occurrence of the majority element with a different element, the majority element survives because it appears more than n/2 times.

Algorithm:
1. Initialize `candidate` and `count = 0`
2. For each element: if `count == 0`, pick current as new candidate. If current == candidate, increment count; else decrement count.
3. The surviving candidate is the majority element.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0, count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {2, 2, 1, 1, 1, 2, 2};
    cout << sol.majorityElement(v1) << endl; // 2

    // Test 2
    vector<int> v2 = {3, 2, 3};
    cout << sol.majorityElement(v2) << endl; // 3

    // Test 3: all same
    vector<int> v3 = {1, 1, 1, 1};
    cout << sol.majorityElement(v3) << endl; // 1

    // Test 4: single element
    vector<int> v4 = {5};
    cout << sol.majorityElement(v4) << endl; // 5

    return 0;
}
```

### Dry Run
**Input:** `[2, 2, 1, 1, 1, 2, 2]`

| Index | num | candidate | count | Action |
|-------|-----|-----------|-------|--------|
| 0 | 2 | 2 | 1 | count was 0, pick 2, count++ |
| 1 | 2 | 2 | 2 | match, count++ |
| 2 | 1 | 2 | 1 | mismatch, count-- |
| 3 | 1 | 2 | 0 | mismatch, count-- |
| 4 | 1 | 1 | 1 | count was 0, pick 1, count++ |
| 5 | 2 | 1 | 0 | mismatch, count-- |
| 6 | 2 | 2 | 1 | count was 0, pick 2, count++ |

**Output:** `2`

### Complexity Analysis
- **Time:** O(n) — single pass
- **Space:** O(1) — two variables

---

## Common Mistakes
1. Not verifying the candidate in a second pass (needed if majority element is NOT guaranteed to exist)
2. Confusing "more than n/2" with "exactly n/2" — n/2 is not a majority

## Interview Tips
- If the problem doesn't guarantee a majority exists, add a verification pass
- Name-drop "Boyer-Moore Voting Algorithm" in the interview
- Follow-up: find elements appearing more than n/3 times (extended Boyer-Moore with 2 candidates)
