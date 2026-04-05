/*
 * Q003: Longest Common Subsequence
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q003-longest-common-subsequence.md
 *
 * Approach Overview:
 * +-----------------------+---------+---------+
 * | Approach              | Time    | Space   |
 * +-----------------------+---------+---------+
 * | Naive Recursion       | O(2^(m+n))| O(m+n)|
 * | Memoization (Top-Down)| O(m*n)  | O(m*n) |
 * | Tabulation (Bottom-Up)| O(m*n)  | O(m*n) |
 * | Space Optimized       | O(m*n)  | O(min(m,n))|
 * +-----------------------+---------+---------+
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Memoization (Top-Down DP)
// ===========================================
int lcsMemoHelper(const string& s1, const string& s2, int i, int j, vector<vector<int>>& memo) {
    if (i == 0 || j == 0) return 0;
    if (memo[i][j] != -1) return memo[i][j];

    if (s1[i - 1] == s2[j - 1]) {
        memo[i][j] = 1 + lcsMemoHelper(s1, s2, i - 1, j - 1, memo);
    } else {
        memo[i][j] = max(lcsMemoHelper(s1, s2, i - 1, j, memo),
                         lcsMemoHelper(s1, s2, i, j - 1, memo));
    }
    return memo[i][j];
}

int lcsMemo(const string& s1, const string& s2) {
    int m = s1.size(), n = s2.size();
    vector<vector<int>> memo(m + 1, vector<int>(n + 1, -1));
    return lcsMemoHelper(s1, s2, m, n, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
int lcsTabulation(const string& s1, const string& s2) {
    int m = s1.size(), n = s2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}

// ===========================================
// Approach 3: Space Optimized
// ===========================================
int lcsOptimized(const string& s1, const string& s2) {
    int m = s1.size(), n = s2.size();
    vector<int> prev(n + 1, 0), curr(n + 1, 0);

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                curr[j] = 1 + prev[j - 1];
            } else {
                curr[j] = max(prev[j], curr[j - 1]);
            }
        }
        swap(prev, curr);
        fill(curr.begin(), curr.end(), 0);
    }
    return prev[n];
}

// ===========================================
// Dry Run (s1="abcde", s2="ace", Tabulation)
// ===========================================
/*
 *     ""  a  c  e
 *  ""  0  0  0  0
 *  a   0  1  1  1
 *  b   0  1  1  1
 *  c   0  1  2  2
 *  d   0  1  2  2
 *  e   0  1  2  3
 *
 * Answer: dp[5][3] = 3
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(lcsOptimized("abcde", "ace") == 3);
    assert(lcsOptimized("abc", "def") == 0);
    assert(lcsOptimized("abcba", "abcbcba") == 5);
    assert(lcsOptimized("", "abc") == 0);
    assert(lcsOptimized("a", "a") == 1);

    // Cross-check
    assert(lcsMemo("abcde", "ace") == 3);
    assert(lcsTabulation("abcde", "ace") == 3);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    string s1, s2;
    cout << "Enter string 1: ";
    cin >> s1;
    cout << "Enter string 2: ";
    cin >> s2;
    cout << "LCS length: " << lcsOptimized(s1, s2) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Tabulation: Time O(m*n), Space O(m*n)
 *   Space Optimized: Time O(m*n), Space O(min(m,n))
 *
 * Common Mistakes:
 *   - Confusing subsequence with substring (substring must be contiguous)
 *   - Off-by-one errors with 1-indexed dp table
 *
 * Interview Tips:
 *   - Classic 2D DP problem -- know it cold
 *   - Can extend to print the actual LCS by backtracking through dp table
 *   - Variations: Longest Common Substring, Shortest Common Supersequence
 */
