/*
 * Q001: Nth Fibonacci Number
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q001-fibonacci.md
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
int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// ===========================================
// Approach 2: Memoization (Top-Down DP)
// ===========================================
int fibMemoHelper(int n, vector<int>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fibMemoHelper(n - 1, memo) + fibMemoHelper(n - 2, memo);
    return memo[n];
}

int fibMemo(int n) {
    vector<int> memo(n + 1, -1);
    return fibMemoHelper(n, memo);
}

// ===========================================
// Approach 3: Tabulation (Bottom-Up DP)
// ===========================================
int fibTabulation(int n) {
    if (n <= 1) return n;
    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

// ===========================================
// Approach 4: Space Optimized (Best)
// ===========================================
int fibOptimized(int n) {
    if (n <= 1) return n;
    int prev2 = 0, prev1 = 1;
    for (int i = 2; i <= n; i++) {
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
 * i=2: curr = 1+0 = 1, prev2=1, prev1=1
 * i=3: curr = 1+1 = 2, prev2=1, prev1=2
 * i=4: curr = 2+1 = 3, prev2=2, prev1=3
 * i=5: curr = 3+2 = 5, prev2=3, prev1=5
 * Return 5
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    // Test base cases
    assert(fibOptimized(0) == 0);
    assert(fibOptimized(1) == 1);

    // Test small values
    assert(fibOptimized(2) == 1);
    assert(fibOptimized(5) == 5);
    assert(fibOptimized(10) == 55);

    // Cross-check all approaches
    for (int i = 0; i <= 20; i++) {
        int expected = fibOptimized(i);
        assert(fibMemo(i) == expected);
        assert(fibTabulation(i) == expected);
    }

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "F(" << n << ") = " << fibOptimized(n) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Space Optimized: Time O(n), Space O(1)
 *
 * Common Mistakes:
 *   - Off-by-one: F(0)=0 not 1
 *   - Not handling n=0 edge case
 *   - Integer overflow for large n (use long long if n > 45)
 *
 * Interview Tips:
 *   - Start with recursion, then optimize step by step
 *   - Mention that this is the classic DP example
 *   - Mention O(log n) matrix exponentiation for bonus points
 */
