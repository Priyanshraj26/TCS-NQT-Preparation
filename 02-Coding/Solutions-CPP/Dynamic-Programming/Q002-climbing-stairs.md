# Solution: Climbing Stairs

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q002-climbing-stairs.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(2^n) | O(n) | ✗ |
| Memoization (Top-Down) | O(n) | O(n) | ✓ |
| Tabulation (Bottom-Up) | O(n) | O(n) | ✓ |
| Space Optimized | O(n) | O(1) | ✓✓ |

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
From step `i`, you can go to step `i+1` or `i+2`. The total number of ways to reach step `n` is the sum of ways to reach `n-1` and `n-2`. This is exactly the Fibonacci pattern.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute Force: O(2^n) time
    int climbStairs(int n) {
        if (n <= 1) return 1;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};

int main() {
    Solution sol;
    cout << sol.climbStairs(2) << endl; // 2
    cout << sol.climbStairs(3) << endl; // 3
    cout << sol.climbStairs(5) << endl; // 8
    return 0;
}
```

### Complexity Analysis
- **Time:** O(2^n)
- **Space:** O(n) recursion stack

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
Cache computed results to avoid solving the same subproblem multiple times.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> dp;

    int solve(int n) {
        if (n <= 1) return 1;
        if (dp[n] != -1) return dp[n];
        dp[n] = solve(n - 1) + solve(n - 2);
        return dp[n];
    }

    int climbStairs(int n) {
        dp.assign(n + 1, -1);
        return solve(n);
    }
};

int main() {
    Solution sol;
    cout << sol.climbStairs(2) << endl;  // 2
    cout << sol.climbStairs(3) << endl;  // 3
    cout << sol.climbStairs(5) << endl;  // 8
    cout << sol.climbStairs(10) << endl; // 89
    return 0;
}
```

### Dry Run
**Input:** n = 4

| Call | n | Cached? | Result |
|------|---|---------|--------|
| solve(4) | 4 | No | solve(3)+solve(2) |
| solve(3) | 3 | No | solve(2)+solve(1) |
| solve(2) | 2 | No | solve(1)+solve(0) = 1+1 = 2 |
| solve(1) | 1 | base | 1 |
| solve(3) | 3 | -- | 2+1 = 3 |
| solve(2) | 2 | Yes | 2 |
| solve(4) | 4 | -- | 3+2 = 5 |

**Output:** 5

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(n)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
Build the answer iteratively. `dp[i]` = number of ways to reach step `i`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Tabulation: O(n) time, O(n) space
    int climbStairs(int n) {
        if (n <= 1) return 1;
        vector<int> dp(n + 1);
        dp[0] = 1; // 1 way to stay at ground
        dp[1] = 1; // 1 way to reach step 1
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};

int main() {
    Solution sol;
    cout << sol.climbStairs(2) << endl;  // 2
    cout << sol.climbStairs(3) << endl;  // 3
    cout << sol.climbStairs(5) << endl;  // 8
    cout << sol.climbStairs(10) << endl; // 89
    return 0;
}
```

### Dry Run
**Input:** n = 5

| i | dp[i-2] | dp[i-1] | dp[i] |
|---|---------|---------|-------|
| 0 | -- | -- | 1 |
| 1 | -- | -- | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 1 | 2 | 3 |
| 4 | 2 | 3 | 5 |
| 5 | 3 | 5 | 8 |

**Output:** 8

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(n)

---

## Approach 4: Space Optimized

### Intuition
Same as Fibonacci -- only the last two values matter.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    // Space Optimized: O(n) time, O(1) space
    int climbStairs(int n) {
        if (n <= 1) return 1;
        int prev2 = 1, prev1 = 1;
        for (int i = 2; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};

int main() {
    Solution sol;
    cout << sol.climbStairs(1) << endl;  // 1
    cout << sol.climbStairs(2) << endl;  // 2
    cout << sol.climbStairs(3) << endl;  // 3
    cout << sol.climbStairs(5) << endl;  // 8
    cout << sol.climbStairs(10) << endl; // 89
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Common Mistakes
1. Confusing base cases: dp[0] = 1 (standing at ground counts as one way)
2. Off-by-one: the answer is at dp[n], not dp[n-1]
3. Mixing up with Fibonacci indexing (F(0)=0 vs stairs(0)=1)

## Interview Tips
- Immediately recognize this as the Fibonacci pattern
- Mention the follow-up: what if you can take 1, 2, or 3 steps? (generalized: dp[i] = sum of dp[i-1..i-k])
- This problem tests whether you can identify DP patterns in disguised problems
