# Solution: Move All Negatives to One Side

[← Back to Question](../../DSA-Questions/Arrays/Q012-move-negatives.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Extra array | O(n) | O(n) | ✗ |
| Two Pointers (partition) | O(n) | O(1) | ✓ |

---

## Approach 1: Extra Array

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void moveNegativesExtra(vector<int>& nums) {
        vector<int> neg, pos;
        for (int x : nums) {
            if (x < 0) neg.push_back(x);
            else pos.push_back(x);
        }
        int i = 0;
        for (int x : neg) nums[i++] = x;
        for (int x : pos) nums[i++] = x;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-12, 11, -13, -5, 6, -7, 5};
    sol.moveNegativesExtra(nums);
    for (int x : nums) cout << x << " ";
    cout << endl;
    return 0;
}
```

---

## Approach 2: Two Pointers (Optimal)

### Intuition
Use two pointers from left and right. Left pointer finds a positive element, right pointer finds a negative element, then swap them.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void moveNegatives(vector<int>& nums) {
        int left = 0, right = (int)nums.size() - 1;
        while (left <= right) {
            if (nums[left] < 0) {
                left++;
            } else if (nums[right] >= 0) {
                right--;
            } else {
                swap(nums[left], nums[right]);
                left++;
                right--;
            }
        }
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {-12, 11, -13, -5, 6, -7, 5};
    sol.moveNegatives(v1);
    for (int x : v1) cout << x << " ";
    cout << endl;

    // Test 2
    vector<int> v2 = {1, -1, 3, -2};
    sol.moveNegatives(v2);
    for (int x : v2) cout << x << " ";
    cout << endl;

    // Test 3: all negative
    vector<int> v3 = {-1, -2, -3};
    sol.moveNegatives(v3);
    for (int x : v3) cout << x << " ";
    cout << endl;

    // Test 4: all positive
    vector<int> v4 = {1, 2, 3};
    sol.moveNegatives(v4);
    for (int x : v4) cout << x << " ";
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** `[-12, 11, -13, -5, 6, -7, 5]`

| Step | left | right | Action | Array |
|------|------|-------|--------|-------|
| 1 | 0 | 6 | nums[0]=-12 < 0 → left++ | [-12,11,-13,-5,6,-7,5] |
| 2 | 1 | 6 | nums[1]=11>=0, nums[6]=5>=0 → right-- | same |
| 3 | 1 | 5 | nums[1]=11>=0, nums[5]=-7<0 → swap | [-12,-7,-13,-5,6,11,5] |
| 4 | 2 | 4 | nums[2]=-13<0 → left++ | same |
| 5 | 3 | 4 | nums[3]=-5<0 → left++ | same |
| 6 | 4 | 4 | nums[4]=6>=0 → right-- | same |
| 7 | left > right → done |

**Output:** `[-12, -7, -13, -5, 6, 11, 5]`

### Complexity Analysis
- **Time:** O(n) — each element visited at most once
- **Space:** O(1) — in-place

---

## Common Mistakes
1. Not handling zero (decide if zero is positive or negative per problem)
2. Infinite loop if both conditions advance the same pointer

## Interview Tips
- This is essentially the partition step of quicksort with pivot = 0
- Follow-up: maintain relative order (use stable partition — O(n) space or O(n log n) time)
