/*
 * Q006: Longest Increasing Subsequence
 * Question: ../../../DSA-Questions/Dynamic-Programming/Q006-longest-increasing-subsequence.md
 *
 * Approach Overview:
 * +-------------------------+-----------+---------+
 * | Approach                | Time      | Space   |
 * +-------------------------+-----------+---------+
 * | DP (O(n^2))             | O(n^2)    | O(n)    |
 * | Binary Search + Greedy  | O(n log n)| O(n)    |
 * +-------------------------+-----------+---------+
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Tabulation DP (O(n^2))
// ===========================================
int lisDP(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    vector<int> dp(n, 1); // each element is LIS of length 1

    int maxLen = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLen = max(maxLen, dp[i]);
    }
    return maxLen;
}

// ===========================================
// Approach 2: Binary Search (O(n log n))
// ===========================================
int lisBinarySearch(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;

    vector<int> tails; // tails[i] = smallest tail of all increasing subseq of length i+1

    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) {
            tails.push_back(num);
        } else {
            *it = num;
        }
    }
    return tails.size();
}

// ===========================================
// Dry Run (nums = [10, 9, 2, 5, 3, 7, 101, 18])
// ===========================================
/*
 * Binary Search approach - tails array evolution:
 * num=10:  tails = [10]
 * num=9:   tails = [9]        (replace 10)
 * num=2:   tails = [2]        (replace 9)
 * num=5:   tails = [2, 5]     (append)
 * num=3:   tails = [2, 3]     (replace 5)
 * num=7:   tails = [2, 3, 7]  (append)
 * num=101: tails = [2, 3, 7, 101] (append)
 * num=18:  tails = [2, 3, 7, 18]  (replace 101)
 *
 * Answer: tails.size() = 4
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {10, 9, 2, 5, 3, 7, 101, 18};
    assert(lisDP(v1) == 4);
    assert(lisBinarySearch(v1) == 4);

    vector<int> v2 = {0, 1, 0, 3, 2, 3};
    assert(lisDP(v2) == 4);
    assert(lisBinarySearch(v2) == 4);

    vector<int> v3 = {7, 7, 7, 7};
    assert(lisDP(v3) == 1);
    assert(lisBinarySearch(v3) == 1);

    vector<int> v4 = {1};
    assert(lisDP(v4) == 1);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << "LIS length: " << lisBinarySearch(nums) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   DP: Time O(n^2), Space O(n)
 *   Binary Search: Time O(n log n), Space O(n)
 *
 * Common Mistakes:
 *   - Forgetting "strictly" increasing (not <=, must be <)
 *   - In BS approach, tails array is NOT the actual LIS
 *   - Not initializing dp[i] = 1
 *
 * Interview Tips:
 *   - Start with O(n^2) DP, then mention O(n log n) optimization
 *   - The BS approach uses "patience sorting" concept
 *   - To print actual LIS, need to track parent pointers
 */
