# Solution: Next Permutation

[← Back to Question](../../DSA-Questions/Arrays/Q017-next-permutation.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force (generate all) | O(n! * n) | O(n!) | ✗ |
| Single Pass Algorithm | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Generate all permutations in sorted order, find the current one, return the next. This is impractical for large n.

---

## Approach 2: Optimal Algorithm

### Intuition
The algorithm has three steps:
1. **Find break point:** Traverse from right, find the first index `i` where `nums[i] < nums[i+1]`. Everything to the right of `i` is in descending order.
2. **Find swap candidate:** From the right, find the first index `j` where `nums[j] > nums[i]`. Swap `nums[i]` and `nums[j]`.
3. **Reverse suffix:** Reverse the subarray from `i+1` to end (converts descending to ascending, giving the smallest possible suffix).

If no break point exists (entire array is descending), just reverse the whole array.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;

        // Step 1: Find break point
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            // Step 2: Find rightmost element greater than nums[i]
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }

        // Step 3: Reverse suffix from i+1 to end
        reverse(nums.begin() + i + 1, nums.end());
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 3};
    sol.nextPermutation(v1);
    for (int x : v1) cout << x << " "; // 1 3 2
    cout << endl;

    // Test 2: last permutation
    vector<int> v2 = {3, 2, 1};
    sol.nextPermutation(v2);
    for (int x : v2) cout << x << " "; // 1 2 3
    cout << endl;

    // Test 3
    vector<int> v3 = {1, 1, 5, 1};
    sol.nextPermutation(v3);
    for (int x : v3) cout << x << " "; // 1 5 1 1
    cout << endl;

    // Test 4
    vector<int> v4 = {2, 3, 1};
    sol.nextPermutation(v4);
    for (int x : v4) cout << x << " "; // 3 1 2
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 3]`

| Step | Description | Array |
|------|-------------|-------|
| Initial | — | [1, 2, 3] |
| Step 1 | i=1 (nums[1]=2 < nums[2]=3) → break point at i=1 | — |
| Step 2 | j=2 (nums[2]=3 > nums[1]=2) → swap(2,3) | [1, 3, 2] |
| Step 3 | Reverse from i+1=2 to end → [2] (single element, no change) | [1, 3, 2] |

**Output:** `1 3 2`

**Input:** `[2, 3, 1]`

| Step | Description | Array |
|------|-------------|-------|
| Initial | — | [2, 3, 1] |
| Step 1 | i=0 (nums[0]=2 < nums[1]=3) | — |
| Step 2 | j=1 (nums[1]=3 > nums[0]=2) → swap(2,3) | [3, 2, 1] |
| Step 3 | Reverse from index 1 to end | [3, 1, 2] |

**Output:** `3 1 2`

### Complexity Analysis
- **Time:** O(n) — at most three linear scans
- **Space:** O(1) — in-place

---

## Common Mistakes
1. Using `>` instead of `>=` in step 1 — must handle duplicates (e.g., [1,5,1])
2. Forgetting to reverse the suffix after swapping
3. Not handling the case where no break point exists (descending array)

## Interview Tips
- This algorithm is based on the standard library's `std::next_permutation`
- Walk through the 3 steps clearly in the interview
- Follow-up: previous permutation (mirror the algorithm)
