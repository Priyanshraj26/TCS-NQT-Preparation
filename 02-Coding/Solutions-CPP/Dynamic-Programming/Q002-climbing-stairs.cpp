/*
 * Q002: Climbing Stairs
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q002-climbing-stairs.md
 *
 * Approach Overview:
 * +-----------------------+-------+--------+
 * | Approach              | Time  | Space  |
 * +-----------------------+-------+--------+
 * | Naive Recursion       | O(2^n)| O(n)   |
 * | Memoization (Top-Down)| O(n)  | O(n)   |
 * | Tabulation (Bottom-Up)| O(n)  | O(n)   |
 * | Space Optimized       | O(n)  | O(1)   |
 * +-----------------------+-------+--------+
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Naive Recursion (Brute Force)
// ===========================================
int climbRecursive(int n) {
    if (n <= 2) return n;
    return climbRecursive(n - 1) + climbRecursive(n - 2);
}

// ===========================================
// Approach 2: Memoization (Top-Down DP)
// ===========================================
int climbMemoHelper(int n, vector<int>& memo) {
    if (n <= 2) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = climbMemoHelper(n - 1, memo) + climbMemoHelper(n - 2, memo);
    return memo[n];
}

int climbMemo(int n) {
    vector<int> memo(n + 1, -1);
    return climbMemoHelper(n, memo);
}

// ===========================================
// Approach 3: Tabulation (Bottom-Up DP)
// ===========================================
int climbTabulation(int n) {
    if (n <= 2) return n;
    vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

// ===========================================
// Approach 4: Space Optimized (Best)
// ===========================================
int climbOptimized(int n) {
    if (n <= 2) return n;
    int prev2 = 1, prev1 = 2;
    for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

// ===========================================
// Dry Run (n = 5, Space Optimized)
// ===========================================
/*
 * prev2=1, prev1=2
 * i=3: curr=2+1=3, prev2=2, prev1=3
 * i=4: curr=3+2=5, prev2=3, prev1=5
 * i=5: curr=5+3=8, prev2=5, prev1=8
 * Return 8
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(climbOptimized(1) == 1);
    assert(climbOptimized(2) == 2);
    assert(climbOptimized(3) == 3);
    assert(climbOptimized(5) == 8);
    assert(climbOptimized(10) == 89);

    // Cross-check approaches
    for (int i = 1; i <= 20; i++) {
        int expected = climbOptimized(i);
        assert(climbMemo(i) == expected);
        assert(climbTabulation(i) == expected);
    }

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "Ways to climb " << n << " stairs: " << climbOptimized(n) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Space Optimized: Time O(n), Space O(1)
 *
 * Common Mistakes:
 *   - Confusing with Fibonacci indexing (here dp[1]=1, dp[2]=2)
 *   - Forgetting that order matters: (1,2) != (2,1)
 *
 * Interview Tips:
 *   - Recognize the Fibonacci pattern immediately
 *   - Mention generalization: what if you can take 1,2,...,k steps?
 */
