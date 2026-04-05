# Solution: Longest Increasing Subsequence

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q006-longest-increasing-subsequence.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^n) | O(n) | ✗ |
| Memoization (Top-Down) | O(n^2) | O(n^2) | ✓ |
| Tabulation (Bottom-Up) | O(n^2) | O(n) | ✓ |
| Binary Search + Patience | O(n log n) | O(n) | ✓✓ |

---

## Approach 1: Naive Recursion

### Intuition
For each element, decide whether to include it in the LIS (if it is greater than the previous element) or skip it.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int solve(vector<int>& nums, int prev, int idx) {
        if (idx == (int)nums.size()) return 0;

        // Skip current element
        int skip = solve(nums, prev, idx + 1);

        // Include current element if it extends the subsequence
        int take = 0;
        if (prev == -1 || nums[idx] > nums[prev])
            take = 1 + solve(nums, idx, idx + 1);

        return max(skip, take);
    }

    int lengthOfLIS(vector<int>& nums) {
        return solve(nums, -1, 0);
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << sol.lengthOfLIS(v1) << endl; // 4
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^n)
- **Space:** O(n) recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
State = (previous index, current index). Cache to avoid recomputation.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

class Solution {
public:
    int dp[2501][2501]; // shifted by 1 since prev can be -1

    int solve(vector<int>& nums, int prev, int idx) {
        if (idx == (int)nums.size()) return 0;
        if (dp[prev + 1][idx] != -1) return dp[prev + 1][idx];

        int skip = solve(nums, prev, idx + 1);
        int take = 0;
        if (prev == -1 || nums[idx] > nums[prev])
            take = 1 + solve(nums, idx, idx + 1);

        return dp[prev + 1][idx] = max(skip, take);
    }

    int lengthOfLIS(vector<int>& nums) {
        memset(dp, -1, sizeof(dp));
        return solve(nums, -1, 0);
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << sol.lengthOfLIS(v1) << endl; // 4

    vector<int> v2 = {0, 1, 0, 3, 2, 3};
    cout << sol.lengthOfLIS(v2) << endl; // 4
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n^2)
- **Space:** O(n^2)

---

## Approach 3: Tabulation (Bottom-Up DP) -- O(n^2)

### Intuition
`dp[i]` = length of LIS ending at index `i`. For each `i`, check all `j < i` where `nums[j] < nums[i]`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1); // every element is an LIS of length 1

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << sol.lengthOfLIS(v1) << endl; // 4

    vector<int> v2 = {0, 1, 0, 3, 2, 3};
    cout << sol.lengthOfLIS(v2) << endl; // 4

    vector<int> v3 = {7, 7, 7, 7};
    cout << sol.lengthOfLIS(v3) << endl; // 1
    return 0;
}
```

### Dry Run
**Input:** [10, 9, 2, 5, 3, 7, 101, 18]

| i | nums[i] | Check j < i | dp[i] |
|---|---------|-------------|-------|
| 0 | 10 | -- | 1 |
| 1 | 9 | 10>9 skip | 1 |
| 2 | 2 | 10>2, 9>2 skip | 1 |
| 3 | 5 | 2<5 -> dp[3]=dp[2]+1=2 | 2 |
| 4 | 3 | 2<3 -> dp[4]=dp[2]+1=2 | 2 |
| 5 | 7 | 2<7(2), 5<7(3), 3<7(3) | 3 |
| 6 | 101 | 10(2),9(2),2(2),5(3),3(3),7(4) | 4 |
| 7 | 18 | 2(2),5(3),3(3),7(4) | 4 |

**Output:** max(dp) = 4 (subsequence: 2, 5, 7, 101 or 2, 3, 7, 18)

### Complexity Analysis
- **Time:** O(n^2)
- **Space:** O(n)

---

## Approach 4: Binary Search -- O(n log n)

### Intuition
Maintain a "tails" array where `tails[i]` is the smallest tail element for an increasing subsequence of length `i+1`. For each element, use binary search to find its position. The length of `tails` at the end is the LIS length.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails; // tails of increasing subsequences

        for (int num : nums) {
            // Find the first element in tails >= num
            auto it = lower_bound(tails.begin(), tails.end(), num);

            if (it == tails.end()) {
                tails.push_back(num); // extend longest subsequence
            } else {
                *it = num; // replace to keep smallest possible tail
            }
        }
        return tails.size();
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << sol.lengthOfLIS(v1) << endl; // 4

    vector<int> v2 = {0, 1, 0, 3, 2, 3};
    cout << sol.lengthOfLIS(v2) << endl; // 4

    vector<int> v3 = {7, 7, 7, 7};
    cout << sol.lengthOfLIS(v3) << endl; // 1

    vector<int> v4 = {1, 3, 6, 7, 9, 4, 10, 5, 6};
    cout << sol.lengthOfLIS(v4) << endl; // 6
    return 0;
}
```

### Dry Run
**Input:** [10, 9, 2, 5, 3, 7, 101, 18]

| num | Action | tails |
|-----|--------|-------|
| 10 | append | [10] |
| 9 | replace 10 | [9] |
| 2 | replace 9 | [2] |
| 5 | append | [2, 5] |
| 3 | replace 5 | [2, 3] |
| 7 | append | [2, 3, 7] |
| 101 | append | [2, 3, 7, 101] |
| 18 | replace 101 | [2, 3, 7, 18] |

**Output:** tails.size() = 4

**Note:** `tails` is NOT the actual LIS -- it just has the correct length.

### Complexity Analysis
- **Time:** O(n log n) -- binary search for each of n elements
- **Space:** O(n)

---

## Common Mistakes
1. Confusing `lower_bound` (>=) with `upper_bound` (>) -- use `lower_bound` for strictly increasing
2. Thinking the `tails` array is the actual LIS (it is not)
3. Forgetting that the answer is `max(dp)`, not `dp[n-1]` in the O(n^2) approach

## Interview Tips
- Start with the O(n^2) DP -- it is easier to explain and code
- Mention the O(n log n) solution exists using binary search ("patience sorting")
- Follow-up: print the actual LIS (need parent tracking)
- Follow-up: longest non-decreasing subsequence (use `upper_bound` instead)
