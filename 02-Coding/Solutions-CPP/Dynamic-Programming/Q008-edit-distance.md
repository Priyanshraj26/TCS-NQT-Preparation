# Solution: Edit Distance (Levenshtein Distance)

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q008-edit-distance.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(3^(m+n)) | O(m+n) | ✗ |
| Memoization (Top-Down) | O(m*n) | O(m*n) | ✓ |
| Tabulation (Bottom-Up) | O(m*n) | O(m*n) | ✓✓ |
| Space Optimized | O(m*n) | O(n) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
Compare characters from the end. If they match, move both pointers. If not, try all three operations (insert, delete, replace) and take the minimum.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int solve(string& s1, string& s2, int i, int j) {
        if (i == 0) return j; // insert remaining j characters
        if (j == 0) return i; // delete remaining i characters

        if (s1[i - 1] == s2[j - 1])
            return solve(s1, s2, i - 1, j - 1);

        int insert_op  = 1 + solve(s1, s2, i, j - 1);
        int delete_op  = 1 + solve(s1, s2, i - 1, j);
        int replace_op = 1 + solve(s1, s2, i - 1, j - 1);

        return min({insert_op, delete_op, replace_op});
    }

    int editDistance(string s1, string s2) {
        return solve(s1, s2, s1.size(), s2.size());
    }
};

int main() {
    Solution sol;
    cout << sol.editDistance("horse", "ros") << endl;      // 3
    cout << sol.editDistance("intention", "execution") << endl; // 5
    return 0;
}
```

### Complexity Analysis
- **Time:** O(3^(m+n)) -- three recursive calls at each mismatch
- **Space:** O(m+n) -- recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
State = (i, j) representing lengths of the two string prefixes being compared. Cache results.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> dp;

    int solve(string& s1, string& s2, int i, int j) {
        if (i == 0) return j;
        if (j == 0) return i;
        if (dp[i][j] != -1) return dp[i][j];

        if (s1[i - 1] == s2[j - 1])
            return dp[i][j] = solve(s1, s2, i - 1, j - 1);

        return dp[i][j] = 1 + min({
            solve(s1, s2, i, j - 1),     // insert
            solve(s1, s2, i - 1, j),     // delete
            solve(s1, s2, i - 1, j - 1)  // replace
        });
    }

    int editDistance(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        dp.assign(m + 1, vector<int>(n + 1, -1));
        return solve(s1, s2, m, n);
    }
};

int main() {
    Solution sol;
    cout << sol.editDistance("horse", "ros") << endl;          // 3
    cout << sol.editDistance("intention", "execution") << endl; // 5
    cout << sol.editDistance("", "abc") << endl;                // 3
    cout << sol.editDistance("abc", "abc") << endl;             // 0
    return 0;
}
```

### Complexity Analysis
- **Time:** O(m*n)
- **Space:** O(m*n)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
Build a 2D table where `dp[i][j]` = edit distance between `s1[0..i-1]` and `s2[0..j-1]`.

**Transitions:**
- If `s1[i-1] == s2[j-1]`: `dp[i][j] = dp[i-1][j-1]`
- Else: `dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])`

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int editDistance(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // Base cases
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + min({dp[i][j - 1],      // insert
                                         dp[i - 1][j],      // delete
                                         dp[i - 1][j - 1]}); // replace
            }
        }
        return dp[m][n];
    }
};

int main() {
    Solution sol;
    cout << sol.editDistance("horse", "ros") << endl;          // 3
    cout << sol.editDistance("intention", "execution") << endl; // 5
    cout << sol.editDistance("saturday", "sunday") << endl;     // 3
    cout << sol.editDistance("", "") << endl;                   // 0
    return 0;
}
```

### Dry Run
**Input:** s1 = "horse", s2 = "ros"

|   | "" | r | o | s |
|---|---|---|---|---|
| "" | 0 | 1 | 2 | 3 |
| h | 1 | 1 | 2 | 3 |
| o | 2 | 2 | 1 | 2 |
| r | 3 | 2 | 2 | 2 |
| s | 4 | 3 | 3 | 2 |
| e | 5 | 4 | 4 | **3** |

**Output:** 3 (horse -> rorse -> rose -> ros)

### Complexity Analysis
- **Time:** O(m*n)
- **Space:** O(m*n)

---

## Approach 4: Space Optimized

### Intuition
Each row depends only on the previous row. Use two 1D arrays.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int editDistance(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        vector<int> prev(n + 1), curr(n + 1);

        for (int j = 0; j <= n; j++) prev[j] = j;

        for (int i = 1; i <= m; i++) {
            curr[0] = i;
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1])
                    curr[j] = prev[j - 1];
                else
                    curr[j] = 1 + min({curr[j - 1], prev[j], prev[j - 1]});
            }
            swap(prev, curr);
        }
        return prev[n];
    }
};

int main() {
    Solution sol;
    cout << sol.editDistance("horse", "ros") << endl;          // 3
    cout << sol.editDistance("intention", "execution") << endl; // 5
    cout << sol.editDistance("saturday", "sunday") << endl;     // 3
    return 0;
}
```

### Complexity Analysis
- **Time:** O(m*n)
- **Space:** O(n)

---

## Common Mistakes
1. Forgetting base cases: dp[i][0] = i, dp[0][j] = j
2. Getting the three operations mixed up (insert/delete/replace correspond to different table cells)
3. Off-by-one errors with 1-indexed table vs 0-indexed strings

## Interview Tips
- Explain each operation clearly: insert into s1 = dp[i][j-1], delete from s1 = dp[i-1][j], replace = dp[i-1][j-1]
- This problem is used in spell checkers, DNA sequence alignment, and diff tools
- Follow-up: reconstruct the sequence of operations by backtracking through the table
- TCS NQT may ask for just the distance value -- the tabulation approach is the safest to code
