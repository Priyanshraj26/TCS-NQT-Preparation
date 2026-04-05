# Solution: Subarray with Given Sum

[← Back to Question](../../DSA-Questions/Arrays/Q015-subarray-given-sum.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Sliding Window | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Try every starting index and expand until sum equals or exceeds target.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    pair<int,int> subarraySumBrute(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum == target) return {i + 1, j + 1}; // 1-based
            }
        }
        return {-1, -1};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 7, 5};
    auto [s, e] = sol.subarraySumBrute(nums, 12);
    if (s == -1) cout << -1 << endl;
    else cout << s << " " << e << endl; // 2 4
    return 0;
}
```

---

## Approach 2: Sliding Window (Optimal)

### Intuition
Since all elements are non-negative, the subarray sum increases as we expand and decreases as we shrink. Use two pointers (start, end) to maintain a window whose sum we track.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    pair<int,int> subarraySum(vector<int>& nums, int target) {
        int n = nums.size();
        int start = 0;
        int currSum = 0;

        for (int end = 0; end < n; end++) {
            currSum += nums[end];

            while (currSum > target && start <= end) {
                currSum -= nums[start];
                start++;
            }

            if (currSum == target) {
                return {start + 1, end + 1}; // 1-based
            }
        }

        return {-1, -1};
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 3, 7, 5};
    auto [s1, e1] = sol.subarraySum(v1, 12);
    if (s1 == -1) cout << -1 << endl;
    else cout << s1 << " " << e1 << endl; // 2 4

    // Test 2
    vector<int> v2 = {1, 2, 3};
    auto [s2, e2] = sol.subarraySum(v2, 6);
    if (s2 == -1) cout << -1 << endl;
    else cout << s2 << " " << e2 << endl; // 1 3

    // Test 3: no subarray
    vector<int> v3 = {1, 2, 3};
    auto [s3, e3] = sol.subarraySum(v3, 10);
    if (s3 == -1) cout << -1 << endl;
    else cout << s3 << " " << e3 << endl; // -1

    // Test 4: target is 0
    vector<int> v4 = {0, 1, 2};
    auto [s4, e4] = sol.subarraySum(v4, 0);
    if (s4 == -1) cout << -1 << endl;
    else cout << s4 << " " << e4 << endl; // 1 1

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 3, 7, 5]`, target = 12

| end | nums[end] | currSum | start | Action |
|-----|-----------|---------|-------|--------|
| 0 | 1 | 1 | 0 | 1 < 12, continue |
| 1 | 2 | 3 | 0 | 3 < 12, continue |
| 2 | 3 | 6 | 0 | 6 < 12, continue |
| 3 | 7 | 13 | 0 | 13>12 → shrink: subtract nums[0]=1 → sum=12, start=1 |
| — | — | 12 | 1 | 12 == 12 → return (2, 4) |

**Output:** `2 4`

### Complexity Analysis
- **Time:** O(n) — each element added and removed from window at most once
- **Space:** O(1)

---

## Common Mistakes
1. Sliding window only works for non-negative arrays. For arrays with negatives, use prefix sum + hash map
2. Off-by-one with 1-based vs 0-based indexing
3. Not handling target = 0 (an element 0 in the array matches)

## Interview Tips
- Clarify: are elements non-negative? This determines the approach
- For arrays with negatives: use prefix sum with hash map (similar to two sum)
- Follow-up: count total number of subarrays with given sum
