# Solution: Merge Two Sorted Arrays

[← Back to Question](../../DSA-Questions/Arrays/Q006-merge-sorted-arrays.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Concatenate and Sort | O((n+m) log(n+m)) | O(n+m) | ✗ |
| Two Pointers | O(n+m) | O(n+m) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Concatenate both arrays and sort.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> mergeBrute(vector<int>& a, vector<int>& b) {
        vector<int> result(a.begin(), a.end());
        result.insert(result.end(), b.begin(), b.end());
        sort(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> a = {1, 3, 5}, b = {2, 4, 6};
    auto res = sol.mergeBrute(a, b);
    for (int x : res) cout << x << " "; // 1 2 3 4 5 6
    cout << endl;
    return 0;
}
```

---

## Approach 2: Two Pointers (Optimal)

### Intuition
Maintain two pointers, one for each array. At each step, pick the smaller element and advance that pointer.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> merge(vector<int>& a, vector<int>& b) {
        int n = a.size(), m = b.size();
        vector<int> result;
        result.reserve(n + m);
        int i = 0, j = 0;

        while (i < n && j < m) {
            if (a[i] <= b[j]) {
                result.push_back(a[i++]);
            } else {
                result.push_back(b[j++]);
            }
        }
        while (i < n) result.push_back(a[i++]);
        while (j < m) result.push_back(b[j++]);

        return result;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> a1 = {1, 3, 5}, b1 = {2, 4, 6};
    auto r1 = sol.merge(a1, b1);
    for (int x : r1) cout << x << " "; // 1 2 3 4 5 6
    cout << endl;

    // Test 2
    vector<int> a2 = {1, 2, 3, 4}, b2 = {0, 7};
    auto r2 = sol.merge(a2, b2);
    for (int x : r2) cout << x << " "; // 0 1 2 3 4 7
    cout << endl;

    // Test 3: one empty
    vector<int> a3 = {}, b3 = {1, 2};
    auto r3 = sol.merge(a3, b3);
    for (int x : r3) cout << x << " "; // 1 2
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** a = `[1, 3, 5]`, b = `[2, 4, 6]`

| Step | i | j | Compare | Pick | result |
|------|---|---|---------|------|--------|
| 1 | 0 | 0 | 1 vs 2 | 1 | [1] |
| 2 | 1 | 0 | 3 vs 2 | 2 | [1,2] |
| 3 | 1 | 1 | 3 vs 4 | 3 | [1,2,3] |
| 4 | 2 | 1 | 5 vs 4 | 4 | [1,2,3,4] |
| 5 | 2 | 2 | 5 vs 6 | 5 | [1,2,3,4,5] |
| 6 | 3 | 2 | — | 6 | [1,2,3,4,5,6] |

**Output:** `1 2 3 4 5 6`

### Complexity Analysis
- **Time:** O(n+m) — each element processed once
- **Space:** O(n+m) — for the result array

---

## Common Mistakes
1. Forgetting to handle remaining elements after main loop
2. Not handling empty arrays

## Interview Tips
- This is the merge step of merge sort — fundamental building block
- Follow-up: merge in-place (gap method) for O(1) extra space
- Follow-up: merge k sorted arrays using min-heap
