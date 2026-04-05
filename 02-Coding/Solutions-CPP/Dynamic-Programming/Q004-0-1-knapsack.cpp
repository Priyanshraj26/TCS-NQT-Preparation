/*
 * Q004: 0/1 Knapsack Problem
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q004-0-1-knapsack.md
 *
 * Approach Overview:
 * +-----------------------+---------+---------+
 * | Approach              | Time    | Space   |
 * +-----------------------+---------+---------+
 * | Recursion             | O(2^n)  | O(n)    |
 * | Memoization (Top-Down)| O(n*W)  | O(n*W)  |
 * | Tabulation (Bottom-Up)| O(n*W)  | O(n*W)  |
 * | Space Optimized (1D)  | O(n*W)  | O(W)    |
 * +-----------------------+---------+---------+
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Memoization (Top-Down DP)
// ===========================================
int knapsackMemoHelper(vector<int>& wt, vector<int>& val, int n, int W, vector<vector<int>>& memo) {
    if (n == 0 || W == 0) return 0;
    if (memo[n][W] != -1) return memo[n][W];

    if (wt[n - 1] > W) {
        memo[n][W] = knapsackMemoHelper(wt, val, n - 1, W, memo);
    } else {
        memo[n][W] = max(
            knapsackMemoHelper(wt, val, n - 1, W, memo),
            val[n - 1] + knapsackMemoHelper(wt, val, n - 1, W - wt[n - 1], memo)
        );
    }
    return memo[n][W];
}

int knapsackMemo(vector<int>& wt, vector<int>& val, int n, int W) {
    vector<vector<int>> memo(n + 1, vector<int>(W + 1, -1));
    return knapsackMemoHelper(wt, val, n, W, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
int knapsackTabulation(vector<int>& wt, vector<int>& val, int n, int W) {
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= W; w++) {
            dp[i][w] = dp[i - 1][w]; // exclude item i
            if (wt[i - 1] <= w) {
                dp[i][w] = max(dp[i][w], val[i - 1] + dp[i - 1][w - wt[i - 1]]);
            }
        }
    }
    return dp[n][W];
}

// ===========================================
// Approach 3: Space Optimized (1D array)
// ===========================================
int knapsackOptimized(vector<int>& wt, vector<int>& val, int n, int W) {
    vector<int> dp(W + 1, 0);

    for (int i = 0; i < n; i++) {
        // Traverse RIGHT to LEFT to avoid using updated values
        for (int w = W; w >= wt[i]; w--) {
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
        }
    }
    return dp[W];
}

// ===========================================
// Dry Run (wt=[10,20,30], val=[60,100,120], W=50)
// ===========================================
/*
 * Tabulation dp table:
 *       w=0  10   20   30   40   50
 * i=0:   0    0    0    0    0    0
 * i=1:   0   60   60   60   60   60
 * i=2:   0   60  100  160  160  160
 * i=3:   0   60  100  160  180  220
 *
 * Answer: dp[3][50] = 220
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> wt1 = {10, 20, 30}, val1 = {60, 100, 120};
    assert(knapsackOptimized(wt1, val1, 3, 50) == 220);
    assert(knapsackMemo(wt1, val1, 3, 50) == 220);
    assert(knapsackTabulation(wt1, val1, 3, 50) == 220);

    vector<int> wt2 = {5, 4, 6}, val2 = {10, 40, 30};
    assert(knapsackOptimized(wt2, val2, 3, 10) == 50);

    vector<int> wt3 = {1}, val3 = {1};
    assert(knapsackOptimized(wt3, val3, 1, 0) == 0);
    assert(knapsackOptimized(wt3, val3, 1, 1) == 1);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n, W;
    cout << "Enter n and W: ";
    cin >> n >> W;
    vector<int> wt(n), val(n);
    cout << "Enter weight and value for each item:" << endl;
    for (int i = 0; i < n; i++) cin >> wt[i] >> val[i];
    cout << "Maximum value: " << knapsackOptimized(wt, val, n, W) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Space Optimized: Time O(n*W), Space O(W)
 *
 * Common Mistakes:
 *   - In 1D optimization, traversing left to right instead of right to left
 *   - Confusing 0/1 knapsack with unbounded knapsack
 *
 * Interview Tips:
 *   - This is the foundation for many DP problems (subset sum, coin change, etc.)
 *   - Mention the 1D optimization unprompted -- shows depth
 *   - Know the difference: 0/1 vs unbounded vs fractional knapsack
 */
