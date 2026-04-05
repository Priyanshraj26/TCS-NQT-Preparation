/*
 * Q009: Subset Sum Problem
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q009-subset-sum.md
 *
 * Approach Overview:
 * +-----------------------+---------+---------+
 * | Approach              | Time    | Space   |
 * +-----------------------+---------+---------+
 * | Recursion             | O(2^n)  | O(n)    |
 * | Memoization (Top-Down)| O(n*S)  | O(n*S)  |
 * | Tabulation (Bottom-Up)| O(n*S)  | O(n*S)  |
 * | Space Optimized (1D)  | O(n*S)  | O(S)    |
 * +-----------------------+---------+---------+
 * S = target sum
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Memoization (Top-Down DP)
// ===========================================
bool subsetMemoHelper(vector<int>& arr, int n, int sum, vector<vector<int>>& memo) {
    if (sum == 0) return true;
    if (n == 0) return false;
    if (memo[n][sum] != -1) return memo[n][sum];

    if (arr[n - 1] > sum) {
        memo[n][sum] = subsetMemoHelper(arr, n - 1, sum, memo);
    } else {
        memo[n][sum] = subsetMemoHelper(arr, n - 1, sum, memo) ||
                       subsetMemoHelper(arr, n - 1, sum - arr[n - 1], memo);
    }
    return memo[n][sum];
}

bool subsetSumMemo(vector<int>& arr, int target) {
    int n = arr.size();
    vector<vector<int>> memo(n + 1, vector<int>(target + 1, -1));
    return subsetMemoHelper(arr, n, target, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
bool subsetSumTabulation(vector<int>& arr, int target) {
    int n = arr.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));

    // Base case: sum 0 is always achievable (empty subset)
    for (int i = 0; i <= n; i++) dp[i][0] = true;

    for (int i = 1; i <= n; i++) {
        for (int s = 1; s <= target; s++) {
            dp[i][s] = dp[i - 1][s]; // exclude current element
            if (arr[i - 1] <= s) {
                dp[i][s] = dp[i][s] || dp[i - 1][s - arr[i - 1]]; // include
            }
        }
    }
    return dp[n][target];
}

// ===========================================
// Approach 3: Space Optimized (1D)
// ===========================================
bool subsetSumOptimized(vector<int>& arr, int target) {
    int n = arr.size();
    vector<bool> dp(target + 1, false);
    dp[0] = true;

    for (int i = 0; i < n; i++) {
        // Traverse right to left (like 0/1 knapsack)
        for (int s = target; s >= arr[i]; s--) {
            dp[s] = dp[s] || dp[s - arr[i]];
        }
    }
    return dp[target];
}

// ===========================================
// Dry Run (arr=[3,34,4,12,5,2], target=9)
// ===========================================
/*
 * 1D DP approach:
 * Initial: dp = [T, F, F, F, F, F, F, F, F, F]
 * After 3:  dp = [T, F, F, T, F, F, F, F, F, F]
 * After 34: no change (34 > 9)
 * After 4:  dp = [T, F, F, T, T, F, F, T, F, F]
 * After 12: no change (12 > 9)
 * After 5:  dp = [T, F, F, T, T, T, F, T, T, T]
 * After 2:  dp = [T, F, T, T, T, T, T, T, T, T]
 *
 * dp[9] = true -> YES
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {3, 34, 4, 12, 5, 2};
    assert(subsetSumOptimized(v1, 9) == true);
    assert(subsetSumOptimized(v1, 30) == false);
    assert(subsetSumMemo(v1, 9) == true);
    assert(subsetSumTabulation(v1, 9) == true);

    vector<int> v2 = {1, 2, 3};
    assert(subsetSumOptimized(v2, 0) == true);
    assert(subsetSumOptimized(v2, 6) == true);
    assert(subsetSumOptimized(v2, 7) == false);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n, target;
    cout << "Enter n and target: ";
    cin >> n >> target;
    vector<int> arr(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << (subsetSumOptimized(arr, target) ? "YES" : "NO") << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Space Optimized: Time O(n*S), Space O(S)
 *
 * Common Mistakes:
 *   - Forgetting that sum=0 is always achievable
 *   - Traversing left to right in 1D optimization (must go right to left)
 *
 * Interview Tips:
 *   - Foundation for: equal partition, count subsets with sum, etc.
 *   - This is 0/1 knapsack where value = weight = arr[i]
 *   - NP-complete in general, but pseudo-polynomial with DP
 */
