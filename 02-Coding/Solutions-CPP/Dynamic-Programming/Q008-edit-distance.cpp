/*
 * Q008: Edit Distance
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q008-edit-distance.md
 *
 * Approach Overview:
 * +-----------------------+---------+---------+
 * | Approach              | Time    | Space   |
 * +-----------------------+---------+---------+
 * | Recursion             | O(3^(m+n))| O(m+n)|
 * | Memoization (Top-Down)| O(m*n)  | O(m*n) |
 * | Tabulation (Bottom-Up)| O(m*n)  | O(m*n) |
 * | Space Optimized       | O(m*n)  | O(n)   |
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
int editMemoHelper(const string& w1, const string& w2, int i, int j, vector<vector<int>>& memo) {
    if (i == 0) return j;
    if (j == 0) return i;
    if (memo[i][j] != -1) return memo[i][j];

    if (w1[i - 1] == w2[j - 1]) {
        memo[i][j] = editMemoHelper(w1, w2, i - 1, j - 1, memo);
    } else {
        memo[i][j] = 1 + min({
            editMemoHelper(w1, w2, i - 1, j, memo),     // delete
            editMemoHelper(w1, w2, i, j - 1, memo),     // insert
            editMemoHelper(w1, w2, i - 1, j - 1, memo)  // replace
        });
    }
    return memo[i][j];
}

int editDistanceMemo(const string& w1, const string& w2) {
    int m = w1.size(), n = w2.size();
    vector<vector<int>> memo(m + 1, vector<int>(n + 1, -1));
    return editMemoHelper(w1, w2, m, n, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
int editDistanceTabulation(const string& w1, const string& w2) {
    int m = w1.size(), n = w2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (w1[i - 1] == w2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
            }
        }
    }
    return dp[m][n];
}

// ===========================================
// Approach 3: Space Optimized
// ===========================================
int editDistanceOptimized(const string& w1, const string& w2) {
    int m = w1.size(), n = w2.size();
    vector<int> prev(n + 1), curr(n + 1);

    for (int j = 0; j <= n; j++) prev[j] = j;

    for (int i = 1; i <= m; i++) {
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (w1[i - 1] == w2[j - 1]) {
                curr[j] = prev[j - 1];
            } else {
                curr[j] = 1 + min({prev[j], curr[j - 1], prev[j - 1]});
            }
        }
        swap(prev, curr);
    }
    return prev[n];
}

// ===========================================
// Dry Run (word1="horse", word2="ros")
// ===========================================
/*
 *       ""  r  o  s
 *  ""    0  1  2  3
 *  h     1  1  2  3
 *  o     2  2  1  2
 *  r     3  2  2  2
 *  s     4  3  3  2
 *  e     5  4  4  3
 *
 * Answer: dp[5][3] = 3
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(editDistanceOptimized("horse", "ros") == 3);
    assert(editDistanceMemo("horse", "ros") == 3);
    assert(editDistanceTabulation("horse", "ros") == 3);

    assert(editDistanceOptimized("intention", "execution") == 5);
    assert(editDistanceOptimized("", "") == 0);
    assert(editDistanceOptimized("abc", "") == 3);
    assert(editDistanceOptimized("", "abc") == 3);
    assert(editDistanceOptimized("abc", "abc") == 0);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    string w1, w2;
    cout << "Enter word1: ";
    cin >> w1;
    cout << "Enter word2: ";
    cin >> w2;
    cout << "Edit distance: " << editDistanceOptimized(w1, w2) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Space Optimized: Time O(m*n), Space O(n)
 *
 * Common Mistakes:
 *   - Forgetting base cases: dp[i][0]=i, dp[0][j]=j
 *   - Not considering all three operations
 *
 * Interview Tips:
 *   - Classic DP problem, often asked in interviews
 *   - Used in spell checkers, DNA sequence alignment
 *   - Also called Levenshtein distance
 */
