# Solution: Two Sum

[← Back to Question](../../DSA-Questions/Arrays/Q001-two-sum.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Hash Map | O(n) | O(n) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Check every pair of numbers to see if they add up to the target.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Brute Force: O(n^2) time, O(1) space
    vector<int> twoSumBrute(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> res = sol.twoSumBrute(nums, target);
    cout << res[0] << " " << res[1] << endl; // 0 1
    return 0;
}
```

### Dry Run
**Input:** `[2, 7, 11, 15]`, target = 9

| i | j | nums[i]+nums[j] | Match? |
|---|---|-----------------|--------|
| 0 | 1 | 2+7=9 | ✓ |

**Output:** `0 1`

---

## Approach 2: Hash Map (Optimal)

### Intuition
For each element, check if `target - nums[i]` already exists in a hash map.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // Optimal: O(n) time, O(n) space
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp; // value -> index
        for (int i = 0; i < (int)nums.size(); i++) {
            int complement = target - nums[i];
            if (mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution sol;
    
    // Test 1
    vector<int> v1 = {2, 7, 11, 15};
    auto r1 = sol.twoSum(v1, 9);
    cout << r1[0] << " " << r1[1] << endl; // 0 1
    
    // Test 2
    vector<int> v2 = {3, 2, 4};
    auto r2 = sol.twoSum(v2, 6);
    cout << r2[0] << " " << r2[1] << endl; // 1 2
    
    // Test 3
    vector<int> v3 = {3, 3};
    auto r3 = sol.twoSum(v3, 6);
    cout << r3[0] << " " << r3[1] << endl; // 0 1
    
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n) — single pass, O(1) hash map lookup
- **Space:** O(n) — hash map stores up to n elements

---

## Key C++ Concepts
- `unordered_map<int,int>` for O(1) average lookup
- `map.find(key) != map.end()` to check existence
- Returning initializer list `{a, b}` as vector

## Common Mistakes
1. Using same element twice — store in map *after* checking complement
2. Not handling negative numbers — complement calculation works for all integers

## Interview Tips
- Start with brute force, then optimize
- If array is sorted → use two pointers (O(1) space)
- Follow-up: 3Sum, 4Sum problems
