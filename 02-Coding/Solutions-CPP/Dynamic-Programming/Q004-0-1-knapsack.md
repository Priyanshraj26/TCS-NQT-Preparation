# Solution: 0/1 Knapsack Problem

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q004-0-1-knapsack.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^n) | O(n) | ✗ |
| Memoization (Top-Down) | O(n*W) | O(n*W) | ✓ |
| Tabulation (Bottom-Up) | O(n*W) | O(n*W) | ✓ |
| Space Optimized | O(n*W) | O(W) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
For each item, you have two choices: include it (if it fits) or exclude it. Try both and return the maximum profit.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int knapsackRecursive(vector<int>& wt, vector<int>& val, int W, int n) {
        if (n == 0 || W == 0) return 0;

        // If current item weight exceeds capacity, skip it
        if (wt[n - 1] > W)
            return knapsackRecursive(wt, val, W, n - 1);

        // Max of (include, exclude)
        int include = val[n - 1] + knapsackRecursive(wt, val, W - wt[n - 1], n - 1);
        int exclude = knapsackRecursive(wt, val, W, n - 1);
        return max(include, exclude);
    }
};

int main() {
    Solution sol;
    vector<int> wt = {1, 3, 4, 5};
    vector<int> val = {1, 4, 5, 7};
    int W = 7;
    cout << sol.knapsackRecursive(wt, val, W, wt.size()) << endl; // 9
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^n)
- **Space:** O(n) recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
The state is defined by (item index, remaining capacity). Cache results for each unique state.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

class Solution {
public:
    int dp[101][1001]; // n <= 100, W <= 1000

    int solve(vector<int>& wt, vector<int>& val, int W, int n) {
        if (n == 0 || W == 0) return 0;
        if (dp[n][W] != -1) return dp[n][W];

        if (wt[n - 1] > W)
            dp[n][W] = solve(wt, val, W, n - 1);
        else
            dp[n][W] = max(
                val[n - 1] + solve(wt, val, W - wt[n - 1], n - 1),
                solve(wt, val, W, n - 1)
            );
        return dp[n][W];
    }

    int knapsack(vector<int>& wt, vector<int>& val, int W) {
        memset(dp, -1, sizeof(dp));
        return solve(wt, val, W, wt.size());
    }
};

int main() {
    Solution sol;
    vector<int> wt = {1, 3, 4, 5};
    vector<int> val = {1, 4, 5, 7};
    cout << sol.knapsack(wt, val, 7) << endl; // 9

    vector<int> wt2 = {2, 3, 4, 5};
    vector<int> val2 = {3, 4, 5, 6};
    cout << sol.knapsack(wt2, val2, 5) << endl; // 7
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n*W)
- **Space:** O(n*W)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
Build a 2D table where `dp[i][w]` = maximum value using first `i` items with capacity `w`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int knapsack(vector<int>& wt, vector<int>& val, int W) {
        int n = wt.size();
        vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                dp[i][w] = dp[i - 1][w]; // exclude item i
                if (wt[i - 1] <= w) {
                    dp[i][w] = max(dp[i][w],
                                   val[i - 1] + dp[i - 1][w - wt[i - 1]]);
                }
            }
        }
        return dp[n][W];
    }
};

int main() {
    Solution sol;
    vector<int> wt = {1, 3, 4, 5};
    vector<int> val = {1, 4, 5, 7};
    cout << sol.knapsack(wt, val, 7) << endl; // 9

    vector<int> wt2 = {2, 3, 4, 5};
    vector<int> val2 = {3, 4, 5, 6};
    cout << sol.knapsack(wt2, val2, 5) << endl; // 7

    vector<int> wt3 = {10};
    vector<int> val3 = {100};
    cout << sol.knapsack(wt3, val3, 5) << endl; // 0 (item doesn't fit)
    return 0;
}
```

### Dry Run
**Input:** wt = [1, 3, 4, 5], val = [1, 4, 5, 7], W = 7

| i\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 (w=1,v=1) | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 (w=3,v=4) | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
| 3 (w=4,v=5) | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
| 4 (w=5,v=7) | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |

**Output:** 9 (items 2 and 3 with weights 3+4=7, values 4+5=9)

### Complexity Analysis
- **Time:** O(n*W)
- **Space:** O(n*W)

---

## Approach 4: Space Optimized (1D Array)

### Intuition
Each row only depends on the previous row. Use a single 1D array and iterate capacity in **reverse** to avoid using updated values.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int knapsack(vector<int>& wt, vector<int>& val, int W) {
        int n = wt.size();
        vector<int> dp(W + 1, 0);

        for (int i = 0; i < n; i++) {
            // Traverse RIGHT to LEFT to ensure each item used at most once
            for (int w = W; w >= wt[i]; w--) {
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
            }
        }
        return dp[W];
    }
};

int main() {
    Solution sol;
    vector<int> wt = {1, 3, 4, 5};
    vector<int> val = {1, 4, 5, 7};
    cout << sol.knapsack(wt, val, 7) << endl; // 9

    vector<int> wt2 = {2, 3, 4, 5};
    vector<int> val2 = {3, 4, 5, 6};
    cout << sol.knapsack(wt2, val2, 5) << endl; // 7
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n*W)
- **Space:** O(W)

---

## Common Mistakes
1. Iterating left-to-right in 1D optimization (this converts it to unbounded knapsack)
2. Forgetting that this is 0/1 -- each item can be used at most once
3. Not handling the case where item weight exceeds current capacity

## Interview Tips
- Clarify: is it 0/1 knapsack or unbounded? The DP transitions differ
- The 1D space optimization with reverse iteration is a common follow-up
- Many problems are variations: subset sum, equal partition, target sum
- If asked to print selected items, backtrack through the 2D table
