# Solution: Equilibrium Point / Index

[← Back to Question](../../DSA-Questions/Arrays/Q020-equilibrium-point.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Prefix Sum (single pass) | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
For each index, compute left sum and right sum separately.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int equilibriumBrute(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            long long leftSum = 0, rightSum = 0;
            for (int j = 0; j < i; j++) leftSum += nums[j];
            for (int j = i + 1; j < n; j++) rightSum += nums[j];
            if (leftSum == rightSum) return i;
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-7, 1, 5, 2, -4, 3, 0};
    cout << sol.equilibriumBrute(nums) << endl; // 3
    return 0;
}
```

---

## Approach 2: Prefix Sum (Optimal)

### Intuition
Compute total sum once. Traverse left to right, maintaining a running `leftSum`. At each index `i`:
- `rightSum = totalSum - leftSum - nums[i]`
- If `leftSum == rightSum`, index `i` is the equilibrium point
- Then add `nums[i]` to `leftSum`

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int equilibrium(vector<int>& nums) {
        int n = nums.size();
        long long totalSum = 0;
        for (int x : nums) totalSum += x;

        long long leftSum = 0;
        for (int i = 0; i < n; i++) {
            long long rightSum = totalSum - leftSum - nums[i];
            if (leftSum == rightSum) return i;
            leftSum += nums[i];
        }

        return -1;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {-7, 1, 5, 2, -4, 3, 0};
    cout << sol.equilibrium(v1) << endl; // 3

    // Test 2: no equilibrium
    vector<int> v2 = {1, 2, 3, 3};
    cout << sol.equilibrium(v2) << endl; // -1

    // Test 3
    vector<int> v3 = {1, 0, 1};
    cout << sol.equilibrium(v3) << endl; // 1

    // Test 4: single element (always equilibrium at 0)
    vector<int> v4 = {5};
    cout << sol.equilibrium(v4) << endl; // 0

    // Test 5: equilibrium at first index
    vector<int> v5 = {0, 0, 0};
    cout << sol.equilibrium(v5) << endl; // 0

    return 0;
}
```

### Dry Run
**Input:** `[-7, 1, 5, 2, -4, 3, 0]`, totalSum = 0

| i | nums[i] | leftSum | rightSum (total-left-nums[i]) | Equal? |
|---|---------|---------|------------------------------|--------|
| 0 | -7 | 0 | 0-0-(-7) = 7 | No |
| 1 | 1 | -7 | 0-(-7)-1 = 6 | No |
| 2 | 5 | -6 | 0-(-6)-5 = 1 | No |
| 3 | 2 | -1 | 0-(-1)-2 = -1 | **Yes** → return 3 |

**Output:** `3`

### Complexity Analysis
- **Time:** O(n) — one pass for total sum + one pass to check
- **Space:** O(1) — only a few variables

---

## Common Mistakes
1. Integer overflow — use `long long` for sums
2. Forgetting that a single-element array has equilibrium at index 0 (both sides sum to 0)
3. Adding `nums[i]` to `leftSum` before checking (must check first, then add)

## Interview Tips
- This is also known as the "pivot index" problem on LeetCode
- Clarify: is the element at the equilibrium index included in left/right sum? (No, it is not)
- Follow-up: find all equilibrium indices
