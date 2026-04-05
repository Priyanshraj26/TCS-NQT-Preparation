# Solution: Second Largest Element

[← Back to Question](../../DSA-Questions/Arrays/Q011-second-largest.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Sort and scan | O(n log n) | O(1) | ✗ |
| Two-pass | O(n) | O(1) | ✗ |
| Single-pass | O(n) | O(1) | ✓ |

---

## Approach 1: Sort and Scan

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int secondLargestSort(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] != nums[0]) return nums[i];
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {12, 35, 1, 10, 34};
    cout << sol.secondLargestSort(nums) << endl; // 34
    return 0;
}
```

---

## Approach 2: Single Pass (Optimal)

### Intuition
Track `first` (largest) and `second` (second largest). For each element:
- If it is greater than `first`, update `second = first`, then `first = nums[i]`
- Else if it is greater than `second` and not equal to `first`, update `second`

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int secondLargest(vector<int>& nums) {
        int first = INT_MIN, second = INT_MIN;

        for (int x : nums) {
            if (x > first) {
                second = first;
                first = x;
            } else if (x > second && x != first) {
                second = x;
            }
        }

        return (second == INT_MIN) ? -1 : second;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {12, 35, 1, 10, 34};
    cout << sol.secondLargest(v1) << endl; // 34

    // Test 2: all same
    vector<int> v2 = {10, 10, 10};
    cout << sol.secondLargest(v2) << endl; // -1

    // Test 3: two elements
    vector<int> v3 = {5, 10};
    cout << sol.secondLargest(v3) << endl; // 5

    // Test 4: single element
    vector<int> v4 = {7};
    cout << sol.secondLargest(v4) << endl; // -1

    // Test 5: negative numbers
    vector<int> v5 = {-3, -1, -5, -2};
    cout << sol.secondLargest(v5) << endl; // -2

    return 0;
}
```

### Dry Run
**Input:** `[12, 35, 1, 10, 34]`

| Index | x | first | second | Action |
|-------|---|-------|--------|--------|
| 0 | 12 | 12 | INT_MIN | x > first → second=INT_MIN, first=12 |
| 1 | 35 | 35 | 12 | x > first → second=12, first=35 |
| 2 | 1 | 35 | 12 | No update |
| 3 | 10 | 35 | 12 | No update (10 < 12) |
| 4 | 34 | 35 | 34 | x > second & x != first → second=34 |

**Output:** `34`

### Complexity Analysis
- **Time:** O(n) — single pass
- **Space:** O(1) — two variables

---

## Common Mistakes
1. Not handling duplicates (e.g., [35, 35, 10] — second largest is 10, not 35)
2. Using INT_MIN without checking if second was actually updated
3. Forgetting single-element arrays

## Interview Tips
- Very common TCS NQT question — be able to code it in under 3 minutes
- Follow-up: find kth largest element (use quickselect or heap)
