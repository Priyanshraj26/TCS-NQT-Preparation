# Solution: Find Max and Min in Minimum Comparisons

[← Back to Question](../../DSA-Questions/Arrays/Q010-max-min-element.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Linear Scan (2n-2 comparisons) | O(n) | O(1) | ✗ |
| Pair Comparison (3n/2 comparisons) | O(n) | O(1) | ✓ |

---

## Approach 1: Linear Scan (Brute Force)

### Intuition
Traverse the array, comparing each element with current min and max.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    pair<int,int> findMinMaxBrute(vector<int>& nums) {
        int mn = nums[0], mx = nums[0];
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] < mn) mn = nums[i];
            if (nums[i] > mx) mx = nums[i];
        }
        return {mn, mx};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {3, 5, 1, 8, 2, 9};
    auto [mn, mx] = sol.findMinMaxBrute(nums);
    cout << mn << " " << mx << endl; // 1 9
    return 0;
}
```

---

## Approach 2: Pair Comparison (Optimal — 3n/2 comparisons)

### Intuition
Process elements in pairs. Compare the two elements of each pair first (1 comparison), then compare the smaller with current min and the larger with current max (2 more). This gives 3 comparisons per 2 elements = 3n/2 total.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    pair<int,int> findMinMax(vector<int>& nums) {
        int n = nums.size();
        int mn, mx;
        int i;

        // Initialize based on odd/even size
        if (n % 2 == 0) {
            if (nums[0] < nums[1]) {
                mn = nums[0]; mx = nums[1];
            } else {
                mn = nums[1]; mx = nums[0];
            }
            i = 2;
        } else {
            mn = mx = nums[0];
            i = 1;
        }

        // Process pairs
        while (i < n - 1) {
            if (nums[i] < nums[i + 1]) {
                if (nums[i] < mn) mn = nums[i];
                if (nums[i + 1] > mx) mx = nums[i + 1];
            } else {
                if (nums[i + 1] < mn) mn = nums[i + 1];
                if (nums[i] > mx) mx = nums[i];
            }
            i += 2;
        }

        return {mn, mx};
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {3, 5, 1, 8, 2, 9};
    auto [mn1, mx1] = sol.findMinMax(v1);
    cout << mn1 << " " << mx1 << endl; // 1 9

    // Test 2: single element
    vector<int> v2 = {42};
    auto [mn2, mx2] = sol.findMinMax(v2);
    cout << mn2 << " " << mx2 << endl; // 42 42

    // Test 3: two elements
    vector<int> v3 = {10, 5};
    auto [mn3, mx3] = sol.findMinMax(v3);
    cout << mn3 << " " << mx3 << endl; // 5 10

    // Test 4: all same
    vector<int> v4 = {7, 7, 7};
    auto [mn4, mx4] = sol.findMinMax(v4);
    cout << mn4 << " " << mx4 << endl; // 7 7

    return 0;
}
```

### Dry Run
**Input:** `[3, 5, 1, 8, 2, 9]` (n=6, even)

| Step | Pair | Compare pair | Update min | Update max | mn | mx |
|------|------|-------------|-----------|-----------|----|----|
| Init | (3,5) | 3<5 | mn=3 | mx=5 | 3 | 5 |
| i=2 | (1,8) | 1<8 | 1<3 → mn=1 | 8>5 → mx=8 | 1 | 8 |
| i=4 | (2,9) | 2<9 | 2>1 → no | 9>8 → mx=9 | 1 | 9 |

**Output:** `1 9` (Total comparisons: 1 + 3 + 3 = 7, vs linear 10)

### Complexity Analysis
- **Time:** O(n) — but only 3n/2 comparisons (optimal)
- **Space:** O(1)

---

## Common Mistakes
1. Not handling odd vs even array sizes in initialization
2. Off-by-one when processing pairs

## Interview Tips
- The 3n/2 comparison bound is provably optimal — mention this
- In practice, the simple linear scan is fine; pair comparison is asked to test algorithmic thinking
