# Solution: Coin Change (Minimum Coins)

[← Back to Question](../../DSA-Questions/Dynamic-Programming/Q005-coin-change.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive Recursion | O(S^n) | O(S) | ✗ |
| Memoization (Top-Down) | O(n*S) | O(S) | ✓ |
| Tabulation (Bottom-Up) | O(n*S) | O(S) | ✓✓ |
| BFS Approach | O(n*S) | O(S) | ✓ |

Where S = amount, n = number of coin denominations.

---

## Approach 1: Naive Recursion (Brute Force)

### Intuition
Try using each coin and recursively solve for the remaining amount. Return the minimum number of coins needed.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;

        int minCoins = INT_MAX;
        for (int coin : coins) {
            int res = coinChange(coins, amount - coin);
            if (res >= 0)
                minCoins = min(minCoins, res + 1);
        }
        return minCoins == INT_MAX ? -1 : minCoins;
    }
};

int main() {
    Solution sol;
    vector<int> coins = {1, 5, 11};
    cout << sol.coinChange(coins, 15) << endl; // 3
    return 0;
}
```

### Complexity Analysis
- **Time:** O(S^n) -- exponential
- **Space:** O(S) -- recursion depth

---

## Approach 2: Memoization (Top-Down DP)

### Intuition
The subproblem is "minimum coins for amount `a`". Cache results for each amount value.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    vector<int> memo;

    int solve(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;
        if (memo[amount] != -2) return memo[amount];

        int minCoins = INT_MAX;
        for (int coin : coins) {
            int res = solve(coins, amount - coin);
            if (res >= 0)
                minCoins = min(minCoins, res + 1);
        }
        memo[amount] = (minCoins == INT_MAX) ? -1 : minCoins;
        return memo[amount];
    }

    int coinChange(vector<int>& coins, int amount) {
        memo.assign(amount + 1, -2); // -2 = unvisited
        return solve(coins, amount);
    }
};

int main() {
    Solution sol;
    vector<int> c1 = {1, 5, 11};
    cout << sol.coinChange(c1, 15) << endl; // 3 (5+5+5)

    vector<int> c2 = {2};
    cout << sol.coinChange(c2, 3) << endl;  // -1 (impossible)

    vector<int> c3 = {1, 2, 5};
    cout << sol.coinChange(c3, 11) << endl; // 3 (5+5+1)
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n*S)
- **Space:** O(S)

---

## Approach 3: Tabulation (Bottom-Up DP)

### Intuition
`dp[i]` = minimum coins needed to make amount `i`. For each amount, try every coin denomination and pick the minimum.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i && dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};

int main() {
    Solution sol;

    vector<int> c1 = {1, 5, 11};
    cout << sol.coinChange(c1, 15) << endl; // 3

    vector<int> c2 = {2};
    cout << sol.coinChange(c2, 3) << endl;  // -1

    vector<int> c3 = {1, 2, 5};
    cout << sol.coinChange(c3, 11) << endl; // 3

    vector<int> c4 = {1};
    cout << sol.coinChange(c4, 0) << endl;  // 0
    return 0;
}
```

### Dry Run
**Input:** coins = [1, 5, 11], amount = 15

| i | Try coin=1 | Try coin=5 | Try coin=11 | dp[i] |
|---|-----------|-----------|------------|-------|
| 0 | -- | -- | -- | 0 |
| 1 | dp[0]+1=1 | -- | -- | 1 |
| 2 | dp[1]+1=2 | -- | -- | 2 |
| 3 | dp[2]+1=3 | -- | -- | 3 |
| 4 | dp[3]+1=4 | -- | -- | 4 |
| 5 | dp[4]+1=5 | dp[0]+1=1 | -- | 1 |
| 10 | dp[9]+1=6 | dp[5]+1=2 | -- | 2 |
| 11 | dp[10]+1=3 | dp[6]+1=3 | dp[0]+1=1 | 1 |
| 15 | dp[14]+1=5 | dp[10]+1=3 | dp[4]+1=5 | **3** |

**Output:** 3 (5+5+5)

### Complexity Analysis
- **Time:** O(n*S)
- **Space:** O(S)

---

## Approach 4: BFS Approach

### Intuition
Think of each amount as a node. From each node, you can subtract any coin to reach another node. BFS finds the shortest path (fewest coins) from `amount` to `0`.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        vector<bool> visited(amount + 1, false);
        queue<int> q;
        q.push(amount);
        visited[amount] = true;
        int level = 0;

        while (!q.empty()) {
            level++;
            int size = q.size();
            while (size--) {
                int curr = q.front(); q.pop();
                for (int coin : coins) {
                    int next = curr - coin;
                    if (next == 0) return level;
                    if (next > 0 && !visited[next]) {
                        visited[next] = true;
                        q.push(next);
                    }
                }
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> c1 = {1, 5, 11};
    cout << sol.coinChange(c1, 15) << endl; // 3

    vector<int> c2 = {2};
    cout << sol.coinChange(c2, 3) << endl;  // -1

    vector<int> c3 = {1, 2, 5};
    cout << sol.coinChange(c3, 11) << endl; // 3
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n*S)
- **Space:** O(S)

---

## Common Mistakes
1. Greedy does NOT work here (e.g., coins=[1,5,11], amount=15: greedy gives 11+1+1+1+1=5 coins, optimal is 5+5+5=3)
2. Forgetting to check `dp[i-coin] != INT_MAX` before adding 1 (overflow)
3. Not returning -1 when the amount cannot be formed

## Interview Tips
- This is an **unbounded knapsack** variant (each coin can be used unlimited times)
- Greedy failure is a great talking point to justify DP
- BFS approach shows graph-thinking and is a nice alternative to mention
- Follow-up: count the total number of ways to make change (different DP)
