# Solution: Maximum Sum with No Adjacent Elements (House Robber)

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q007-max-sum-no-adjacent.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^n) | O(n) | ✗ |
| Memoization (Top-Down) | O(n) | O(n) | ✓ |
| Tabulation (Bottom-Up) | O(n) | O(n) | ✓ |
| Space Optimized | O(n) | O(1) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
At each index, either take the current element (and skip to i+2) or skip it (move to i+1). Return the maximum.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int solve(vector<int>& nums, int i) {
        if (i >= (int)nums.size()) return 0;
        int take = nums[i] + solve(nums, i + 2); // take and skip next
        int skip = solve(nums, i + 1);             // skip current
        return max(take, skip);
    }

    int maxSumNoAdjacent(vector<int>& nums) {
        return solve(nums, 0);
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {2, 7, 9, 3, 1};
    cout << sol.maxSumNoAdjacent(v1) << endl; // 12 (2+9+1)

    vector<int> v2 = {1, 2, 3, 1};
    cout << sol.maxSumNoAdjacent(v2) << endl; // 4 (1+3)
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^n)
- **Space:** O(n)

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
State = current index. Cache the maximum sum obtainable starting from index `i`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> dp;

    int solve(vector<int>& nums, int i) {
        if (i >= (int)nums.size()) return 0;
        if (dp[i] != -1) return dp[i];
        int take = nums[i] + solve(nums, i + 2);
        int skip = solve(nums, i + 1);
        return dp[i] = max(take, skip);
    }

    int maxSumNoAdjacent(vector<int>& nums) {
        dp.assign(nums.size(), -1);
        return solve(nums, 0);
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {2, 7, 9, 3, 1};
    cout << sol.maxSumNoAdjacent(v1) << endl; // 12

    vector<int> v2 = {1, 2, 3, 1};
    cout << sol.maxSumNoAdjacent(v2) << endl; // 4

    vector<int> v3 = {5};
    cout << sol.maxSumNoAdjacent(v3) << endl; // 5
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(n)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
`dp[i]` = maximum sum considering elements from index 0 to i. Transition: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSumNoAdjacent(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            dp[i] = max(dp[i - 1],          // skip nums[i]
                        nums[i] + dp[i - 2]); // take nums[i]
        }
        return dp[n - 1];
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {2, 7, 9, 3, 1};
    cout << sol.maxSumNoAdjacent(v1) << endl; // 12

    vector<int> v2 = {1, 2, 3, 1};
    cout << sol.maxSumNoAdjacent(v2) << endl; // 4

    vector<int> v3 = {2, 1, 1, 2};
    cout << sol.maxSumNoAdjacent(v3) << endl; // 4
    return 0;
}
```

### Dry Run
**Input:** [2, 7, 9, 3, 1]

| i | nums[i] | dp[i-2]+nums[i] | dp[i-1] | dp[i] |
|---|---------|-----------------|---------|-------|
| 0 | 2 | -- | -- | 2 |
| 1 | 7 | -- | 2 | 7 |
| 2 | 9 | 2+9=11 | 7 | 11 |
| 3 | 3 | 7+3=10 | 11 | 11 |
| 4 | 1 | 11+1=12 | 11 | 12 |

**Output:** 12 (elements 2, 9, 1)

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(n)

---

## Approach 4: Space Optimized

### Intuition
We only need the previous two values. Use two variables.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSumNoAdjacent(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        int prev2 = nums[0];
        int prev1 = max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            int curr = max(prev1, nums[i] + prev2);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {2, 7, 9, 3, 1};
    cout << sol.maxSumNoAdjacent(v1) << endl; // 12

    vector<int> v2 = {1, 2, 3, 1};
    cout << sol.maxSumNoAdjacent(v2) << endl; // 4

    vector<int> v3 = {6, 7, 1, 30, 8, 2, 4};
    cout << sol.maxSumNoAdjacent(v3) << endl; // 41 (6+30+4+... actually 6+1+... no: 7+30+4=41)
    return 0;
}
```

### Dry Run
**Input:** [2, 7, 9, 3, 1]

| i | nums[i] | prev2 | prev1 | curr |
|---|---------|-------|-------|------|
| - | - | 2 | 7 | -- |
| 2 | 9 | 2 | 7 | max(7, 9+2)=11 |
| 3 | 3 | 7 | 11 | max(11, 3+7)=11 |
| 4 | 1 | 11 | 11 | max(11, 1+11)=12 |

**Output:** 12

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Common Mistakes
1. Forgetting dp[1] = max(nums[0], nums[1]), not just nums[1]
2. Not handling edge cases: empty array, single element
3. Confusing this with "circular" house robber (House Robber II)

## Interview Tips
- This is the classic "House Robber" problem on LeetCode
- The key insight is: include/exclude pattern with the constraint of no two adjacent
- Follow-up: House Robber II (circular array) -- run the algorithm twice: once excluding first, once excluding last
- Follow-up: House Robber III (binary tree) -- DP on trees
