# Solution: Nth Fibonacci Number

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q001-fibonacci.md)

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
Directly translate the mathematical recurrence F(n) = F(n-1) + F(n-2). This leads to exponential time because the same subproblems are solved repeatedly.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute Force: O(2^n) time, O(n) stack space
    int fibRecursive(int n) {
        if (n <= 1) return n;
        return fibRecursive(n - 1) + fibRecursive(n - 2);
    }
};

int main() {
    Solution sol;
    cout << sol.fibRecursive(0) << endl;  // 0
    cout << sol.fibRecursive(1) << endl;  // 1
    cout << sol.fibRecursive(5) << endl;  // 5
    cout << sol.fibRecursive(10) << endl; // 55
    return 0;
}
```

### Dry Run
**Input:** n = 5

```
fib(5) = fib(4) + fib(3)
       = (fib(3) + fib(2)) + (fib(2) + fib(1))
       = ((fib(2)+fib(1)) + (fib(1)+fib(0))) + ((fib(1)+fib(0)) + 1)
       = ((1+1) + (1+0)) + ((1+0) + 1)
       = (2 + 1) + (1 + 1)
       = 3 + 2 = 5
```

### Complexity Analysis
- **Time:** O(2^n) -- exponential due to overlapping subproblems
- **Space:** O(n) -- recursion stack depth

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
Cache already-computed results in an array. Before computing F(n), check if it is already stored. This eliminates redundant computations.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int dp[46];
    bool visited[46];

    int fibMemo(int n) {
        if (n <= 1) return n;
        if (visited[n]) return dp[n];
        visited[n] = true;
        dp[n] = fibMemo(n - 1) + fibMemo(n - 2);
        return dp[n];
    }

    int fibonacci(int n) {
        fill(visited, visited + 46, false);
        return fibMemo(n);
    }
};

int main() {
    Solution sol;
    cout << sol.fibonacci(0) << endl;  // 0
    cout << sol.fibonacci(5) << endl;  // 5
    cout << sol.fibonacci(10) << endl; // 55
    cout << sol.fibonacci(45) << endl; // 1134903170
    return 0;
}
```

### Dry Run
**Input:** n = 5

| Call | n | Cached? | Compute | Store |
|------|---|---------|---------|-------|
| 1 | 5 | No | fib(4)+fib(3) | -- |
| 2 | 4 | No | fib(3)+fib(2) | -- |
| 3 | 3 | No | fib(2)+fib(1) | -- |
| 4 | 2 | No | fib(1)+fib(0)=1 | dp[2]=1 |
| 5 | 1 | base | return 1 | -- |
| 6 | 3 | -- | 1+1=2 | dp[3]=2 |
| 7 | 2 | Yes | return 1 | -- |
| 8 | 4 | -- | 2+1=3 | dp[4]=3 |
| 9 | 3 | Yes | return 2 | -- |
| 10 | 5 | -- | 3+2=5 | dp[5]=5 |

### Complexity Analysis
- **Time:** O(n) -- each subproblem computed at most once
- **Space:** O(n) -- dp array + recursion stack

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
Build the solution iteratively from the base cases upward. Fill a table from index 0 to n.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Tabulation: O(n) time, O(n) space
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
};

int main() {
    Solution sol;
    cout << sol.fibTabulation(0) << endl;  // 0
    cout << sol.fibTabulation(5) << endl;  // 5
    cout << sol.fibTabulation(10) << endl; // 55
    cout << sol.fibTabulation(45) << endl; // 1134903170
    return 0;
}
```

### Dry Run
**Input:** n = 5

| i | dp[i-2] | dp[i-1] | dp[i] |
|---|---------|---------|-------|
| 0 | -- | -- | 0 |
| 1 | -- | -- | 1 |
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 3 |
| 5 | 2 | 3 | 5 |

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(n)

---

## Approach 4: Space Optimized

### Intuition
We only need the last two values at any point. Use two variables instead of an entire array.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    // Space Optimized: O(n) time, O(1) space
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
};

int main() {
    Solution sol;
    cout << sol.fibOptimized(0) << endl;  // 0
    cout << sol.fibOptimized(1) << endl;  // 1
    cout << sol.fibOptimized(5) << endl;  // 5
    cout << sol.fibOptimized(10) << endl; // 55
    cout << sol.fibOptimized(45) << endl; // 1134903170
    return 0;
}
```

### Dry Run
**Input:** n = 5

| i | prev2 | prev1 | curr |
|---|-------|-------|------|
| - | 0 | 1 | -- |
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 3 |
| 5 | 2 | 3 | 5 |

**Output:** 5

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Common Mistakes
1. Forgetting base case F(0) = 0 (not 1)
2. Off-by-one errors in loop bounds
3. Using `int` for large n -- overflow beyond n=46

## Interview Tips
- Always start by explaining the recurrence relation
- Mention that naive recursion has overlapping subproblems -- that is why DP helps
- The interviewer expects you to arrive at the O(1) space solution
- This is the **foundation** of all DP problems -- master this pattern
