# Solution: Leaders in an Array

[← Back to Question](../../DSA-Questions/Arrays/Q009-leaders-in-array.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Right-to-Left Scan | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
For each element, check if it is greater than all elements to its right.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> leadersBrute(vector<int>& nums) {
        int n = nums.size();
        vector<int> result;
        for (int i = 0; i < n; i++) {
            bool isLeader = true;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] > nums[i]) {
                    isLeader = false;
                    break;
                }
            }
            if (isLeader) result.push_back(nums[i]);
        }
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {16, 17, 4, 3, 5, 2};
    auto res = sol.leadersBrute(nums);
    for (int x : res) cout << x << " "; // 17 5 2
    cout << endl;
    return 0;
}
```

---

## Approach 2: Right-to-Left Scan (Optimal)

### Intuition
Traverse from right to left. The rightmost element is always a leader. Track the maximum from the right. If current element >= max so far, it is a leader.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> leaders(vector<int>& nums) {
        int n = nums.size();
        vector<int> result;
        int maxFromRight = nums[n - 1];
        result.push_back(nums[n - 1]);

        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] >= maxFromRight) {
                result.push_back(nums[i]);
                maxFromRight = nums[i];
            }
        }

        reverse(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {16, 17, 4, 3, 5, 2};
    auto r1 = sol.leaders(v1);
    for (int x : r1) cout << x << " "; // 17 5 2
    cout << endl;

    // Test 2: sorted ascending
    vector<int> v2 = {1, 2, 3, 4, 5};
    auto r2 = sol.leaders(v2);
    for (int x : r2) cout << x << " "; // 5
    cout << endl;

    // Test 3: sorted descending (all leaders)
    vector<int> v3 = {5, 4, 3, 2, 1};
    auto r3 = sol.leaders(v3);
    for (int x : r3) cout << x << " "; // 5 4 3 2 1
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** `[16, 17, 4, 3, 5, 2]`

| i | nums[i] | maxFromRight | Leader? | result (reversed at end) |
|---|---------|-------------|---------|--------------------------|
| 5 | 2 | 2 | Yes | [2] |
| 4 | 5 | 5 | Yes | [2, 5] |
| 3 | 3 | 5 | No | [2, 5] |
| 2 | 4 | 5 | No | [2, 5] |
| 1 | 17 | 17 | Yes | [2, 5, 17] |
| 0 | 16 | 17 | No | [2, 5, 17] |

After reverse: `[17, 5, 2]`

### Complexity Analysis
- **Time:** O(n) — single right-to-left pass + O(n) reverse
- **Space:** O(1) extra — result is required output

---

## Common Mistakes
1. Forgetting to reverse the result (we collect right to left)
2. Not including the last element as a leader
3. Using `>` instead of `>=` when problem says "greater than or equal to"

## Interview Tips
- Simple but tests understanding of array traversal direction
- Follow-up: find leaders from the left side
