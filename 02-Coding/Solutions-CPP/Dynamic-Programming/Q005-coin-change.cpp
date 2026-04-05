/*
 * Q005: Coin Change (Minimum Coins)
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q005-coin-change.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Recursion             | O(S^n)    | O(S)    |
 * | Memoization (Top-Down)| O(n*S)    | O(S)    |
 * | Tabulation (Bottom-Up)| O(n*S)    | O(S)    |
 * +-----------------------+-----------+---------+
 * S = amount, n = number of coin types
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Memoization (Top-Down DP)
// ===========================================
int coinChangeMemoHelper(vector<int>& coins, int amount, vector<int>& memo) {
    if (amount == 0) return 0;
    if (amount < 0) return -1;
    if (memo[amount] != -2) return memo[amount];

    int minCoins = INT_MAX;
    for (int coin : coins) {
        int sub = coinChangeMemoHelper(coins, amount - coin, memo);
        if (sub >= 0) {
            minCoins = min(minCoins, sub + 1);
        }
    }
    memo[amount] = (minCoins == INT_MAX) ? -1 : minCoins;
    return memo[amount];
}

int coinChangeMemo(vector<int>& coins, int amount) {
    vector<int> memo(amount + 1, -2); // -2 means unvisited
    return coinChangeMemoHelper(coins, amount, memo);
}

// ===========================================
// Approach 2: Tabulation (Bottom-Up DP)
// ===========================================
int coinChangeTabulation(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1); // amount+1 acts as infinity
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i && dp[i - coin] != amount + 1) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}

// ===========================================
// Dry Run (coins=[1,5,10], amount=12)
// ===========================================
/*
 * dp[0]=0
 * dp[1]=1  (1)
 * dp[2]=2  (1+1)
 * dp[3]=3  (1+1+1)
 * dp[4]=4  (1+1+1+1)
 * dp[5]=1  (5)
 * dp[6]=2  (5+1)
 * dp[7]=3  (5+1+1)
 * dp[8]=4  (5+1+1+1)
 * dp[9]=5  (5+1+1+1+1)
 * dp[10]=1 (10)
 * dp[11]=2 (10+1)
 * dp[12]=3 (10+1+1)
 *
 * Answer: 3
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> c1 = {1, 5, 10};
    assert(coinChangeTabulation(c1, 12) == 3);
    assert(coinChangeMemo(c1, 12) == 3);

    vector<int> c2 = {2};
    assert(coinChangeTabulation(c2, 3) == -1);

    vector<int> c3 = {1};
    assert(coinChangeTabulation(c3, 0) == 0);

    vector<int> c4 = {1, 2, 5};
    assert(coinChangeTabulation(c4, 11) == 3); // 5+5+1

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n, amount;
    cout << "Enter number of coin types and amount: ";
    cin >> n >> amount;
    vector<int> coins(n);
    cout << "Enter coin denominations: ";
    for (int i = 0; i < n; i++) cin >> coins[i];
    cout << "Minimum coins: " << coinChangeTabulation(coins, amount) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Tabulation: Time O(n*amount), Space O(amount)
 *
 * Common Mistakes:
 *   - Using greedy (greedy doesn't always work for coin change)
 *   - Forgetting to handle the impossible case (-1)
 *   - Using INT_MAX without overflow check when adding 1
 *
 * Interview Tips:
 *   - This is unbounded knapsack variant (infinite supply of each coin)
 *   - Greedy works only for canonical coin systems (like US coins)
 *   - Variation: count number of ways instead of minimum coins
 */
