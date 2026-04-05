# Solution: Subset Sum Problem

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q009-subset-sum.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^n) | O(n) | ✗ |
| Memoization (Top-Down) | O(n*sum) | O(n*sum) | ✓ |
| Tabulation (Bottom-Up) | O(n*sum) | O(n*sum) | ✓ |
| Space Optimized | O(n*sum) | O(sum) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
For each element, either include it in the subset or exclude it. If the remaining sum becomes 0, a valid subset exists.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool subsetSum(vector<int>& arr, int n, int sum) {
        if (sum == 0) return true;
        if (n == 0) return false;

        // If current element is greater than sum, skip it
        if (arr[n - 1] > sum)
            return subsetSum(arr, n - 1, sum);

        // Include or exclude
        return subsetSum(arr, n - 1, sum - arr[n - 1]) ||
               subsetSum(arr, n - 1, sum);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {3, 34, 4, 12, 5, 2};
    cout << boolalpha;
    cout << sol.subsetSum(arr, arr.size(), 9) << endl;  // true (4+5)
    cout << sol.subsetSum(arr, arr.size(), 30) << endl; // false
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^n) -- two choices per element
- **Space:** O(n) -- recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
State = (index, remaining sum). Cache whether a subset with the given sum exists using the first `n` elements.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // dp[i][s] = 0 (unvisited), 1 (true), -1 (false)
    vector<vector<int>> dp;

    bool solve(vector<int>& arr, int n, int sum) {
        if (sum == 0) return true;
        if (n == 0) return false;
        if (dp[n][sum] != 0) return dp[n][sum] == 1;

        bool result;
        if (arr[n - 1] > sum)
            result = solve(arr, n - 1, sum);
        else
            result = solve(arr, n - 1, sum - arr[n - 1]) ||
                     solve(arr, n - 1, sum);

        dp[n][sum] = result ? 1 : -1;
        return result;
    }

    bool subsetSum(vector<int>& arr, int sum) {
        int n = arr.size();
        dp.assign(n + 1, vector<int>(sum + 1, 0));
        return solve(arr, n, sum);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {3, 34, 4, 12, 5, 2};
    cout << boolalpha;
    cout << sol.subsetSum(arr, 9) << endl;  // true
    cout << sol.subsetSum(arr, 30) << endl; // false
    cout << sol.subsetSum(arr, 1) << endl;  // false
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n * sum)
- **Space:** O(n * sum)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
`dp[i][j]` = true if a subset of the first `i` elements can form sum `j`. Base case: `dp[i][0] = true` for all `i` (empty subset has sum 0).

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool subsetSum(vector<int>& arr, int sum) {
        int n = arr.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(sum + 1, false));

        // Base case: sum 0 is always achievable (empty subset)
        for (int i = 0; i <= n; i++)
            dp[i][0] = true;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                dp[i][j] = dp[i - 1][j]; // exclude current element
                if (arr[i - 1] <= j)
                    dp[i][j] = dp[i][j] || dp[i - 1][j - arr[i - 1]]; // include
            }
        }
        return dp[n][sum];
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {3, 34, 4, 12, 5, 2};
    cout << boolalpha;
    cout << sol.subsetSum(v1, 9) << endl;  // true (4+5 or 3+4+2)
    cout << sol.subsetSum(v1, 30) << endl; // false

    vector<int> v2 = {1, 5, 11, 5};
    cout << sol.subsetSum(v2, 11) << endl; // true (subset for equal partition)

    vector<int> v3 = {2, 3, 7};
    cout << sol.subsetSum(v3, 6) << endl;  // false
    return 0;
}
```

### Dry Run
**Input:** arr = [3, 34, 4, 12, 5, 2], sum = 9

| i\j | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-----|---|---|---|---|---|---|---|---|---|---|
| 0 | T | F | F | F | F | F | F | F | F | F |
| 1 (3) | T | F | F | T | F | F | F | F | F | F |
| 2 (34) | T | F | F | T | F | F | F | F | F | F |
| 3 (4) | T | F | F | T | T | F | F | T | F | F |
| 4 (12) | T | F | F | T | T | F | F | T | F | F |
| 5 (5) | T | F | F | T | T | T | F | T | T | **T** |
| 6 (2) | T | F | T | T | T | T | T | T | T | **T** |

**Output:** true (subsets: {4,5} or {3,4,2})

### Complexity Analysis
- **Time:** O(n * sum)
- **Space:** O(n * sum)

---

## Approach 4: Space Optimized (1D Array)

### Intuition
Like 0/1 knapsack, use a single array and iterate right to left.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool subsetSum(vector<int>& arr, int sum) {
        int n = arr.size();
        vector<bool> dp(sum + 1, false);
        dp[0] = true;

        for (int i = 0; i < n; i++) {
            // RIGHT to LEFT to avoid using same element twice
            for (int j = sum; j >= arr[i]; j--) {
                dp[j] = dp[j] || dp[j - arr[i]];
            }
        }
        return dp[sum];
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {3, 34, 4, 12, 5, 2};
    cout << boolalpha;
    cout << sol.subsetSum(v1, 9) << endl;  // true
    cout << sol.subsetSum(v1, 30) << endl; // false

    vector<int> v2 = {1, 5, 11, 5};
    cout << sol.subsetSum(v2, 11) << endl; // true
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n * sum)
- **Space:** O(sum)

---

## Common Mistakes
1. Iterating left-to-right in 1D optimization (allows reusing the same element)
2. Forgetting base case dp[0] = true
3. Not handling edge case: if any element equals sum, answer is immediately true

## Interview Tips
- Subset sum is the foundation for: equal partition, count of subsets with given sum, minimum subset difference
- This is essentially a boolean version of 0/1 knapsack
- Time complexity is **pseudo-polynomial** (depends on the value of sum, not just input size)
- Follow-up: count the number of subsets with a given sum (change `||` to `+`)
