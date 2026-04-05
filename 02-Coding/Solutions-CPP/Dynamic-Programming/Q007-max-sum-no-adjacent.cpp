/*
 * Q007: Maximum Sum with No Two Adjacent Elements
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q007-max-sum-no-adjacent.md
 *
 * Approach Overview:
 * +-----------------------+-------+--------+
 * | Approach              | Time  | Space  |
 * +-----------------------+-------+--------+
 * | Recursion             | O(2^n)| O(n)   |
 * | Memoization (Top-Down)| O(n)  | O(n)   |
 * | Tabulation (Bottom-Up)| O(n)  | O(n)   |
 * | Space Optimized       | O(n)  | O(1)   |
 * +-----------------------+-------+--------+
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Memoization (Top-Down DP)
// ===========================================
int maxSumMemoHelper(vector<int>& arr, int i, vector<int>& memo) {
    if (i < 0) return 0;
    if (memo[i] != -1) return memo[i];
    memo[i] = max(maxSumMemoHelper(arr, i - 1, memo),
                  arr[i] + maxSumMemoHelper(arr, i - 2, memo));
    return memo[i];
}

int maxSumMemo(vector<int>& arr) {
    int n = arr.size();
    vector<int> memo(n, -1);
    return maxSumMemoHelper(arr, n - 1, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
int maxSumTabulation(vector<int>& arr) {
    int n = arr.size();
    if (n == 0) return 0;
    if (n == 1) return arr[0];

    vector<int> dp(n);
    dp[0] = arr[0];
    dp[1] = max(arr[0], arr[1]);
    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i - 1], arr[i] + dp[i - 2]);
    }
    return dp[n - 1];
}

// ===========================================
// Approach 3: Space Optimized (Best)
// ===========================================
int maxSumOptimized(vector<int>& arr) {
    int n = arr.size();
    if (n == 0) return 0;
    if (n == 1) return arr[0];

    int prev2 = arr[0];
    int prev1 = max(arr[0], arr[1]);
    for (int i = 2; i < n; i++) {
        int curr = max(prev1, arr[i] + prev2);
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

// ===========================================
// Dry Run (arr = [3, 2, 7, 10])
// ===========================================
/*
 * prev2 = 3, prev1 = max(3,2) = 3
 * i=2: curr = max(3, 7+3) = 10, prev2=3, prev1=10
 * i=3: curr = max(10, 10+3) = 13, prev2=10, prev1=13
 * Return 13
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {3, 2, 7, 10};
    assert(maxSumOptimized(v1) == 13);

    vector<int> v2 = {5, 5, 10, 100, 10, 5};
    assert(maxSumOptimized(v2) == 110);

    vector<int> v3 = {3, 2, 5, 10, 7};
    assert(maxSumOptimized(v3) == 15);

    vector<int> v4 = {5};
    assert(maxSumOptimized(v4) == 5);

    vector<int> v5 = {5, 1};
    assert(maxSumOptimized(v5) == 5);

    // Cross-check
    assert(maxSumMemo(v1) == 13);
    assert(maxSumTabulation(v1) == 13);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    vector<int> arr(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "Maximum sum: " << maxSumOptimized(arr) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Space Optimized: Time O(n), Space O(1)
 *
 * Common Mistakes:
 *   - Wrong base case: dp[1] = max(arr[0], arr[1]), not just arr[1]
 *   - Not handling n=1 edge case
 *
 * Interview Tips:
 *   - Same as LeetCode "House Robber"
 *   - Variation: circular array (House Robber II)
 *   - Very common in TCS NQT -- practice well
 */
