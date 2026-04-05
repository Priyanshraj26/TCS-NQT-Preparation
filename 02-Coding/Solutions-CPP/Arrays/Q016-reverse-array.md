# Solution: Reverse an Array

[← Back to Question](../../DSA-Questions/Arrays/Q016-reverse-array.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Using extra array | O(n) | O(n) | ✗ |
| Two Pointers (in-place) | O(n) | O(1) | ✓ |

---

## Approach 1: Extra Array

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> reverseExtra(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        for (int i = 0; i < n; i++) {
            result[i] = nums[n - 1 - i];
        }
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    auto res = sol.reverseExtra(nums);
    for (int x : res) cout << x << " "; // 5 4 3 2 1
    cout << endl;
    return 0;
}
```

---

## Approach 2: Two Pointers (Optimal)

### Intuition
Place one pointer at the start and one at the end. Swap elements and move both pointers inward until they meet.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void reverseArray(vector<int>& nums) {
        int left = 0, right = (int)nums.size() - 1;
        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 3, 4, 5};
    sol.reverseArray(v1);
    for (int x : v1) cout << x << " "; // 5 4 3 2 1
    cout << endl;

    // Test 2
    vector<int> v2 = {10, 20, 30, 40};
    sol.reverseArray(v2);
    for (int x : v2) cout << x << " "; // 40 30 20 10
    cout << endl;

    // Test 3: single element
    vector<int> v3 = {7};
    sol.reverseArray(v3);
    for (int x : v3) cout << x << " "; // 7
    cout << endl;

    // Test 4: two elements
    vector<int> v4 = {1, 2};
    sol.reverseArray(v4);
    for (int x : v4) cout << x << " "; // 2 1
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 3, 4, 5]`

| Step | left | right | Swap | Array |
|------|------|-------|------|-------|
| 1 | 0 | 4 | swap(1,5) | [5, 2, 3, 4, 1] |
| 2 | 1 | 3 | swap(2,4) | [5, 4, 3, 2, 1] |
| 3 | 2 | 2 | left == right → stop | [5, 4, 3, 2, 1] |

**Output:** `5 4 3 2 1`

### Complexity Analysis
- **Time:** O(n) — n/2 swaps
- **Space:** O(1) — in-place

---

## Common Mistakes
1. Using `left <= right` works too but does an unnecessary self-swap for odd-length arrays
2. Forgetting to handle empty arrays

## Interview Tips
- Extremely basic but often asked as a warm-up
- This is a building block for array rotation (reversal algorithm)
- In C++ you can also use `std::reverse(nums.begin(), nums.end())`
