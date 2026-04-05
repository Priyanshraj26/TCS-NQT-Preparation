# Solution: Best Time to Buy and Sell Stock

[← Back to Question](../../DSA-Questions/Arrays/Q013-stock-buy-sell.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Single Pass (Greedy) | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Try every pair (buy day, sell day) where buy < sell.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfitBrute(vector<int>& prices) {
        int maxProfit = 0;
        int n = prices.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                maxProfit = max(maxProfit, prices[j] - prices[i]);
            }
        }
        return maxProfit;
    }
};

int main() {
    Solution sol;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << sol.maxProfitBrute(prices) << endl; // 5
    return 0;
}
```

---

## Approach 2: Single Pass (Optimal)

### Intuition
Keep track of the minimum price seen so far. At each day, the best profit if we sell today = today's price - min price so far. Track the global maximum of this profit.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            minPrice = min(minPrice, price);
            maxProfit = max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {7, 1, 5, 3, 6, 4};
    cout << sol.maxProfit(v1) << endl; // 5

    // Test 2: decreasing prices
    vector<int> v2 = {7, 6, 4, 3, 1};
    cout << sol.maxProfit(v2) << endl; // 0

    // Test 3: increasing prices
    vector<int> v3 = {1, 2, 3, 4, 5};
    cout << sol.maxProfit(v3) << endl; // 4

    // Test 4: single day
    vector<int> v4 = {5};
    cout << sol.maxProfit(v4) << endl; // 0

    return 0;
}
```

### Dry Run
**Input:** `[7, 1, 5, 3, 6, 4]`

| Day | price | minPrice | profit (price-min) | maxProfit |
|-----|-------|----------|-------------------|-----------|
| 0 | 7 | 7 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 5 | 1 | 4 | 4 |
| 3 | 3 | 1 | 2 | 4 |
| 4 | 6 | 1 | 5 | **5** |
| 5 | 4 | 1 | 3 | 5 |

**Output:** `5`

### Complexity Analysis
- **Time:** O(n) — single pass
- **Space:** O(1) — two variables

---

## Common Mistakes
1. Selling before buying (must ensure sell day > buy day — handled by left-to-right scan)
2. Returning negative profit instead of 0 when no profitable trade exists
3. Not considering that we must buy AND sell (can't just hold)

## Interview Tips
- One of the most asked easy questions at TCS NQT
- Follow-up: multiple transactions allowed (greedy: sum all positive diffs)
- Follow-up: at most k transactions (DP)
