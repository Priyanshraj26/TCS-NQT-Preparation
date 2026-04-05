# Solution: Matrix Chain Multiplication

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q010-matrix-chain-multiplication.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^n) | O(n) | ✗ |
| Memoization (Top-Down) | O(n^3) | O(n^2) | ✓ |
| Tabulation (Bottom-Up) | O(n^3) | O(n^2) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
To multiply matrices A[i..j], try every possible split point `k` between `i` and `j`. The cost = cost of left part + cost of right part + cost of multiplying the two resulting matrices.

For dimensions array `p[]`, matrix `i` has dimensions `p[i-1] x p[i]`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int solve(vector<int>& p, int i, int j) {
        if (i == j) return 0; // single matrix, no cost

        int minCost = INT_MAX;
        for (int k = i; k < j; k++) {
            int cost = solve(p, i, k) + solve(p, k + 1, j)
                       + p[i - 1] * p[k] * p[j];
            minCost = min(minCost, cost);
        }
        return minCost;
    }

    int matrixChainOrder(vector<int>& p) {
        int n = p.size() - 1; // number of matrices
        return solve(p, 1, n);
    }
};

int main() {
    Solution sol;
    vector<int> p1 = {10, 20, 30, 40, 30};
    cout << sol.matrixChainOrder(p1) << endl; // 30000

    vector<int> p2 = {40, 20, 30, 10, 30};
    cout << sol.matrixChainOrder(p2) << endl; // 26000
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^n) -- exponential
- **Space:** O(n) -- recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
The state is (i, j) -- the range of matrices. Cache the minimum cost for each (i, j) pair.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
#include <cstring>
using namespace std;

class Solution {
public:
    int dp[101][101];

    int solve(vector<int>& p, int i, int j) {
        if (i == j) return 0;
        if (dp[i][j] != -1) return dp[i][j];

        dp[i][j] = INT_MAX;
        for (int k = i; k < j; k++) {
            int cost = solve(p, i, k) + solve(p, k + 1, j)
                       + p[i - 1] * p[k] * p[j];
            dp[i][j] = min(dp[i][j], cost);
        }
        return dp[i][j];
    }

    int matrixChainOrder(vector<int>& p) {
        memset(dp, -1, sizeof(dp));
        int n = p.size() - 1;
        return solve(p, 1, n);
    }
};

int main() {
    Solution sol;
    vector<int> p1 = {10, 20, 30, 40, 30};
    cout << sol.matrixChainOrder(p1) << endl; // 30000

    vector<int> p2 = {40, 20, 30, 10, 30};
    cout << sol.matrixChainOrder(p2) << endl; // 26000

    vector<int> p3 = {10, 20, 30};
    cout << sol.matrixChainOrder(p3) << endl; // 6000
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n^3) -- O(n^2) states, O(n) work per state
- **Space:** O(n^2)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
Fill the table by chain length. Start with chains of length 2 (pairs of matrices), then 3, and so on. `dp[i][j]` = minimum cost to multiply matrices `i` through `j`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int matrixChainOrder(vector<int>& p) {
        int n = p.size() - 1; // number of matrices
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        // l = chain length
        for (int l = 2; l <= n; l++) {
            for (int i = 1; i <= n - l + 1; i++) {
                int j = i + l - 1;
                dp[i][j] = INT_MAX;

                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k + 1][j]
                               + p[i - 1] * p[k] * p[j];
                    dp[i][j] = min(dp[i][j], cost);
                }
            }
        }
        return dp[1][n];
    }
};

int main() {
    Solution sol;

    vector<int> p1 = {10, 20, 30, 40, 30};
    cout << sol.matrixChainOrder(p1) << endl; // 30000

    vector<int> p2 = {40, 20, 30, 10, 30};
    cout << sol.matrixChainOrder(p2) << endl; // 26000

    vector<int> p3 = {10, 20, 30};
    cout << sol.matrixChainOrder(p3) << endl; // 6000

    vector<int> p4 = {1, 2, 3, 4};
    cout << sol.matrixChainOrder(p4) << endl; // 18
    return 0;
}
```

### Dry Run
**Input:** p = [10, 20, 30, 40, 30] -- 4 matrices: A1(10x20), A2(20x30), A3(30x40), A4(40x30)

**Chain length 2:**

| (i,j) | k | Cost formula | dp[i][j] |
|--------|---|-------------|-----------|
| (1,2) | 1 | 0+0+10*20*30=6000 | 6000 |
| (2,3) | 2 | 0+0+20*30*40=24000 | 24000 |
| (3,4) | 3 | 0+0+30*40*30=36000 | 36000 |

**Chain length 3:**

| (i,j) | k=i | k=i+1 | dp[i][j] |
|--------|-----|-------|-----------|
| (1,3) | k=1: 0+24000+10*20*40=32000 | k=2: 6000+0+10*30*40=18000 | 18000 |
| (2,4) | k=2: 0+36000+20*30*30=54000 | k=3: 24000+0+20*40*30=48000 | 48000 |

**Chain length 4:**

| (i,j) | k=1 | k=2 | k=3 | dp[i][j] |
|--------|-----|-----|-----|-----------|
| (1,4) | 0+48000+10*20*30=54000 | 6000+36000+10*30*30=51000 | 18000+0+10*40*30=30000 | **30000** |

**Output:** 30000

### Complexity Analysis
- **Time:** O(n^3)
- **Space:** O(n^2)

---

## Common Mistakes
1. Confusing matrix indices with dimension array indices (matrix `i` has dimensions `p[i-1] x p[i]`)
2. Wrong loop bounds: chain length starts at 2, not 1
3. Forgetting that dp[i][i] = 0 (single matrix needs no multiplication)
4. Using 0-indexed when the standard formulation is 1-indexed

## Interview Tips
- MCM is the classic **interval DP** problem -- recognize it by "split an interval into two parts"
- The pattern applies to: palindrome partitioning, burst balloons, optimal BST, rod cutting
- General MCM template: for each split point `k` in range `[i, j)`, combine left and right results
- This is frequently asked in TCS NQT and other placement exams
- To reconstruct the optimal parenthesization, maintain a `bracket[i][j]` table storing the best `k`
