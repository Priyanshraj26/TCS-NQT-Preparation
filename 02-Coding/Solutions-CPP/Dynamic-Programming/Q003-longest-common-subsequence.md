# Solution: Longest Common Subsequence

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q003-longest-common-subsequence.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^(m+n)) | O(m+n) | ✗ |
| Memoization (Top-Down) | O(m*n) | O(m*n) | ✓ |
| Tabulation (Bottom-Up) | O(m*n) | O(m*n) | ✓ |
| Space Optimized | O(m*n) | O(min(m,n)) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
Compare characters from the end of both strings. If they match, include them and move both pointers. Otherwise, try skipping one character from each string and take the maximum.

### C++ Code
```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int lcsRecursive(string& s1, string& s2, int i, int j) {
        if (i == 0 || j == 0) return 0;
        if (s1[i - 1] == s2[j - 1])
            return 1 + lcsRecursive(s1, s2, i - 1, j - 1);
        return max(lcsRecursive(s1, s2, i - 1, j),
                   lcsRecursive(s1, s2, i, j - 1));
    }

    int longestCommonSubsequence(string s1, string s2) {
        return lcsRecursive(s1, s2, s1.size(), s2.size());
    }
};

int main() {
    Solution sol;
    cout << sol.longestCommonSubsequence("abcde", "ace") << endl;   // 3
    cout << sol.longestCommonSubsequence("abc", "abc") << endl;     // 3
    cout << sol.longestCommonSubsequence("abc", "def") << endl;     // 0
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^(m+n)) -- exponential branching
- **Space:** O(m+n) -- recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
The recursion has overlapping subproblems -- cache results in a 2D table indexed by (i, j).

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> memo;

    int solve(string& s1, string& s2, int i, int j) {
        if (i == 0 || j == 0) return 0;
        if (memo[i][j] != -1) return memo[i][j];

        if (s1[i - 1] == s2[j - 1])
            memo[i][j] = 1 + solve(s1, s2, i - 1, j - 1);
        else
            memo[i][j] = max(solve(s1, s2, i - 1, j),
                             solve(s1, s2, i, j - 1));
        return memo[i][j];
    }

    int longestCommonSubsequence(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        memo.assign(m + 1, vector<int>(n + 1, -1));
        return solve(s1, s2, m, n);
    }
};

int main() {
    Solution sol;
    cout << sol.longestCommonSubsequence("abcde", "ace") << endl;    // 3
    cout << sol.longestCommonSubsequence("AGGTAB", "GXTXAYB") << endl; // 4
    cout << sol.longestCommonSubsequence("abc", "def") << endl;      // 0
    return 0;
}
```

### Complexity Analysis
- **Time:** O(m*n) -- each state computed once
- **Space:** O(m*n) -- memo table + recursion stack

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
Build a 2D table where `dp[i][j]` = LCS length of `s1[0..i-1]` and `s2[0..j-1]`. Fill row by row.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m][n];
    }
};

int main() {
    Solution sol;
    cout << sol.longestCommonSubsequence("abcde", "ace") << endl;      // 3
    cout << sol.longestCommonSubsequence("AGGTAB", "GXTXAYB") << endl; // 4
    cout << sol.longestCommonSubsequence("abc", "def") << endl;        // 0
    return 0;
}
```

### Dry Run
**Input:** s1 = "abcde", s2 = "ace"

|   | "" | a | c | e |
|---|---|---|---|---|
| "" | 0 | 0 | 0 | 0 |
| a | 0 | **1** | 1 | 1 |
| b | 0 | 1 | 1 | 1 |
| c | 0 | 1 | **2** | 2 |
| d | 0 | 1 | 2 | 2 |
| e | 0 | 1 | 2 | **3** |

**Output:** 3 (subsequence "ace")

### Complexity Analysis
- **Time:** O(m*n)
- **Space:** O(m*n)

---

## Approach 4: Space Optimized

### Intuition
Each row only depends on the previous row. Use two 1D arrays.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        // Ensure s2 is the shorter string for less space
        if (m < n) { swap(s1, s2); swap(m, n); }

        vector<int> prev(n + 1, 0), curr(n + 1, 0);

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1])
                    curr[j] = 1 + prev[j - 1];
                else
                    curr[j] = max(prev[j], curr[j - 1]);
            }
            swap(prev, curr);
            fill(curr.begin(), curr.end(), 0);
        }
        return prev[n];
    }
};

int main() {
    Solution sol;
    cout << sol.longestCommonSubsequence("abcde", "ace") << endl;      // 3
    cout << sol.longestCommonSubsequence("AGGTAB", "GXTXAYB") << endl; // 4
    cout << sol.longestCommonSubsequence("abc", "def") << endl;        // 0
    return 0;
}
```

### Complexity Analysis
- **Time:** O(m*n)
- **Space:** O(min(m,n))

---

## Common Mistakes
1. Confusing subsequence with substring (subsequence need not be contiguous)
2. Off-by-one with 1-indexed dp table vs 0-indexed strings
3. Forgetting to initialize dp[0][j] = dp[i][0] = 0

## Interview Tips
- LCS is a foundational DP problem -- many problems reduce to it (edit distance, shortest common supersequence, diff)
- Follow-up: print the actual LCS by backtracking through the table
- Follow-up: longest common substring (only count diagonal matches)
