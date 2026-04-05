# Solution: Maximum Subarray Sum (Kadane's Algorithm)

[← Back to Question](../../DSA-Questions/Arrays/Q002-max-subarray.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Kadane's Algorithm | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Check every possible subarray and track the maximum sum.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxSubArrayBrute(vector<int>& nums) {
        int n = nums.size();
        int maxSum = INT_MIN;
        for (int i = 0; i < n; i++) {
            int currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += nums[j];
                maxSum = max(maxSum, currSum);
            }
        }
        return maxSum;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << sol.maxSubArrayBrute(nums) << endl; // 6
    return 0;
}
```

### Dry Run
**Input:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| i | j range | Best sum starting at i |
|---|---------|----------------------|
| 0 | 0..8 | 1 (at j=1) then various |
| 3 | 3..6 | 4+(-1)+2+1 = 6 ✓ |

**Output:** `6`

---

## Approach 2: Kadane's Algorithm (Optimal)

### Intuition
Maintain a running sum. At each element, decide: extend the current subarray or start a new one. If the running sum becomes negative, starting fresh is always better.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        int currSum = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            currSum += nums[i];
            maxSum = max(maxSum, currSum);
            if (currSum < 0) {
                currSum = 0;
            }
        }
        return maxSum;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << sol.maxSubArray(v1) << endl; // 6

    // Test 2: single negative
    vector<int> v2 = {-1};
    cout << sol.maxSubArray(v2) << endl; // -1

    // Test 3: all positive
    vector<int> v3 = {5, 4, -1, 7, 8};
    cout << sol.maxSubArray(v3) << endl; // 23

    // Test 4: all negative
    vector<int> v4 = {-3, -2, -5, -1};
    cout << sol.maxSubArray(v4) << endl; // -1

    return 0;
}
```

### Dry Run
**Input:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| Index | nums[i] | currSum | maxSum | Reset? |
|-------|---------|---------|--------|--------|
| 0 | -2 | -2 | -2 | Yes (currSum<0 → 0) |
| 1 | 1 | 1 | 1 | No |
| 2 | -3 | -2 | 1 | Yes → 0 |
| 3 | 4 | 4 | 4 | No |
| 4 | -1 | 3 | 4 | No |
| 5 | 2 | 5 | 5 | No |
| 6 | 1 | 6 | **6** | No |
| 7 | -5 | 1 | 6 | No |
| 8 | 4 | 5 | 6 | No |

**Output:** `6`

### Complexity Analysis
- **Time:** O(n) — single pass through the array
- **Space:** O(1) — only two variables

---

## Common Mistakes
1. Initializing `maxSum = 0` — fails for all-negative arrays; use `INT_MIN`
2. Forgetting the subarray must contain at least one element
3. Resetting `currSum` before updating `maxSum`

## Interview Tips
- Kadane's is a classic DP problem — mention "local max vs global max"
- Follow-up: print the actual subarray (track start and end indices)
- Follow-up: maximum circular subarray sum
