/*
 * Q010: Matrix Chain Multiplication
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q010-matrix-chain-multiplication.md
 *
 * Approach Overview:
 * +-----------------------+---------+---------+
 * | Approach              | Time    | Space   |
 * +-----------------------+---------+---------+
 * | Recursion             | O(2^n)  | O(n)    |
 * | Memoization (Top-Down)| O(n^3)  | O(n^2)  |
 * | Tabulation (Bottom-Up)| O(n^3)  | O(n^2)  |
 * +-----------------------+---------+---------+
 */

#include <iostream>
#include <vector>
#include <climits>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Memoization (Top-Down DP)
// ===========================================
int mcmMemoHelper(vector<int>& p, int i, int j, vector<vector<int>>& memo) {
    if (i == j) return 0;
    if (memo[i][j] != -1) return memo[i][j];

    int minCost = INT_MAX;
    for (int k = i; k < j; k++) {
        int cost = mcmMemoHelper(p, i, k, memo)
                 + mcmMemoHelper(p, k + 1, j, memo)
                 + p[i - 1] * p[k] * p[j];
        minCost = min(minCost, cost);
    }
    memo[i][j] = minCost;
    return minCost;
}

int mcmMemo(vector<int>& p) {
    int n = p.size() - 1; // number of matrices
    vector<vector<int>> memo(n + 1, vector<int>(n + 1, -1));
    return mcmMemoHelper(p, 1, n, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
int mcmTabulation(vector<int>& p) {
    int n = p.size() - 1;
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

    // len is the chain length
    for (int len = 2; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
    return dp[1][n];
}

// ===========================================
// Dry Run (p = [10, 20, 30, 40, 30], n=4 matrices)
// ===========================================
/*
 * Matrices: A1(10x20), A2(20x30), A3(30x40), A4(40x30)
 *
 * len=2:
 *   dp[1][2] = 10*20*30 = 6000
 *   dp[2][3] = 20*30*40 = 24000
 *   dp[3][4] = 30*40*30 = 36000
 *
 * len=3:
 *   dp[1][3] = min(dp[1][1]+dp[2][3]+10*20*40, dp[1][2]+dp[3][3]+10*30*40)
 *            = min(0+24000+8000, 6000+0+12000) = min(32000, 18000) = 18000
 *   dp[2][4] = min(dp[2][2]+dp[3][4]+20*30*30, dp[2][3]+dp[4][4]+20*40*30)
 *            = min(0+36000+18000, 24000+0+24000) = min(54000, 48000) = 48000
 *
 * len=4:
 *   dp[1][4] = min(
 *     k=1: dp[1][1]+dp[2][4]+10*20*30 = 0+48000+6000 = 54000
 *     k=2: dp[1][2]+dp[3][4]+10*30*30 = 6000+36000+9000 = 51000
 *     k=3: dp[1][3]+dp[4][4]+10*40*30 = 18000+0+12000 = 30000
 *   ) = 30000
 *
 * Answer: 30000
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> p1 = {10, 20, 30, 40, 30};
    assert(mcmTabulation(p1) == 30000);
    assert(mcmMemo(p1) == 30000);

    vector<int> p2 = {40, 20, 30, 10, 30};
    assert(mcmTabulation(p2) == 26000);

    vector<int> p3 = {10, 20, 30};
    assert(mcmTabulation(p3) == 6000); // only one way

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter number of matrices: ";
    cin >> n;
    vector<int> p(n + 1);
    cout << "Enter " << n + 1 << " dimensions: ";
    for (int i = 0; i <= n; i++) cin >> p[i];
    cout << "Minimum multiplications: " << mcmTabulation(p) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Tabulation: Time O(n^3), Space O(n^2)
 *
 * Common Mistakes:
 *   - Wrong loop bounds: i starts from 1 (1-indexed matrices)
 *   - Forgetting that p has n+1 elements for n matrices
 *   - Not handling the base case (single matrix = 0 cost)
 *
 * Interview Tips:
 *   - MCM pattern applies to: palindrome partitioning, burst balloons, etc.
 *   - The key insight is "try all split points"
 *   - Can extend to print the optimal parenthesization
 */
