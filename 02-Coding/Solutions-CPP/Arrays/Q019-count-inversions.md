# Solution: Count Inversions (Merge Sort)

[← Back to Question](../../DSA-Questions/Arrays/Q019-count-inversions.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Modified Merge Sort | O(n log n) | O(n) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Check every pair (i, j) where i < j and count those where nums[i] > nums[j].

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long countInversionsBrute(vector<int>& nums) {
        long long count = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] > nums[j]) count++;
            }
        }
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 4, 1, 3, 5};
    cout << sol.countInversionsBrute(nums) << endl; // 3
    return 0;
}
```

---

## Approach 2: Modified Merge Sort (Optimal)

### Intuition
During the merge step of merge sort, when we pick an element from the right half before all elements of the left half are exhausted, each such pick contributes inversions equal to the number of remaining elements in the left half.

If `left[i] > right[j]`, then `left[i], left[i+1], ..., left[mid]` are ALL greater than `right[j]`, so we add `(mid - i + 1)` inversions.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long mergeCount(vector<int>& nums, int left, int right) {
        if (left >= right) return 0;

        int mid = left + (right - left) / 2;
        long long count = 0;

        count += mergeCount(nums, left, mid);
        count += mergeCount(nums, mid + 1, right);
        count += merge(nums, left, mid, right);

        return count;
    }

    long long merge(vector<int>& nums, int left, int mid, int right) {
        vector<int> temp;
        int i = left, j = mid + 1;
        long long count = 0;

        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                temp.push_back(nums[i++]);
            } else {
                count += (mid - i + 1); // All remaining left elements form inversions
                temp.push_back(nums[j++]);
            }
        }

        while (i <= mid) temp.push_back(nums[i++]);
        while (j <= right) temp.push_back(nums[j++]);

        for (int k = left; k <= right; k++) {
            nums[k] = temp[k - left];
        }

        return count;
    }

    long long countInversions(vector<int>& nums) {
        return mergeCount(nums, 0, (int)nums.size() - 1);
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {2, 4, 1, 3, 5};
    cout << sol.countInversions(v1) << endl; // 3

    // Test 2: reverse sorted (max inversions)
    vector<int> v2 = {5, 4, 3, 2, 1};
    cout << sol.countInversions(v2) << endl; // 10

    // Test 3: already sorted (0 inversions)
    vector<int> v3 = {1, 2, 3};
    cout << sol.countInversions(v3) << endl; // 0

    // Test 4: single element
    vector<int> v4 = {1};
    cout << sol.countInversions(v4) << endl; // 0

    // Test 5
    vector<int> v5 = {1, 20, 6, 4, 5};
    cout << sol.countInversions(v5) << endl; // 5

    return 0;
}
```

### Dry Run
**Input:** `[2, 4, 1, 3, 5]`

```
Split: [2, 4, 1, 3, 5]
  Left: [2, 4]   Right: [1, 3, 5]

Merge [2, 4]: i=0, j=1
  2 <= 4 → pick 2. No inversions.
  Pick 4. Result: [2, 4]. Inversions = 0

Split Right: [1, 3, 5]
  Left: [1]  Right: [3, 5]
  Merge [3, 5]: 0 inversions → [3, 5]
  Merge [1] and [3, 5]: 1 <= 3 → pick 1, then 3, then 5. Inversions = 0.
  Result: [1, 3, 5]

Merge [2, 4] and [1, 3, 5]:
  i=0, j=0: 2 > 1 → count += (1-0+1) = 2, pick 1
  i=0, j=1: 2 <= 3 → pick 2
  i=1, j=1: 4 > 3 → count += (1-1+1) = 1, pick 3
  i=1, j=2: 4 <= 5 → pick 4
  j=2: pick 5
  Inversions in merge = 3
```

**Total inversions = 0 + 0 + 0 + 3 = 3**

### Complexity Analysis
- **Time:** O(n log n) — merge sort time complexity
- **Space:** O(n) — temporary array during merge

---

## Common Mistakes
1. Using `int` instead of `long long` for count — max inversions for n=10^5 is about 5 * 10^9
2. Not copying back from temp to original array
3. Using `<` instead of `<=` in the merge comparison (affects stability and count)

## Interview Tips
- Clearly explain WHY `mid - i + 1` gives the inversion count
- This is a classic divide-and-conquer problem
- Follow-up: count reverse pairs where nums[i] > 2 * nums[j]
