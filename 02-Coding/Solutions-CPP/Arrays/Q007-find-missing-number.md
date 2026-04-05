# Solution: Find Missing Number (1 to N)

[← Back to Question](../../DSA-Questions/Arrays/Q007-find-missing-number.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force (sorting) | O(n log n) | O(1) | ✗ |
| Sum Formula | O(n) | O(1) | ✓ |
| XOR | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Sort the array and find where the sequence breaks.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int missingNumberBrute(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] != i + 1) return i + 1;
        }
        return nums.size() + 1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 4, 5};
    cout << sol.missingNumberBrute(nums) << endl; // 3
    return 0;
}
```

---

## Approach 2: Sum Formula (Optimal)

### Intuition
Expected sum of 1 to n+1 minus actual sum gives the missing number.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        long long expectedSum = (long long)(n + 1) * (n + 2) / 2;
        long long actualSum = 0;
        for (int x : nums) actualSum += x;
        return (int)(expectedSum - actualSum);
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 4, 5};
    cout << sol.missingNumber(v1) << endl; // 3

    // Test 2
    vector<int> v2 = {3, 1, 2};
    cout << sol.missingNumber(v2) << endl; // 4

    // Test 3: missing 1
    vector<int> v3 = {2, 3, 4};
    cout << sol.missingNumber(v3) << endl; // 1

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 4, 5]`, n = 4, range = [1, 5]

| Step | Calculation |
|------|-------------|
| Expected sum | 5 * 6 / 2 = 15 |
| Actual sum | 1 + 2 + 4 + 5 = 12 |
| Missing | 15 - 12 = **3** |

### Complexity Analysis
- **Time:** O(n) — single pass
- **Space:** O(1)

---

## Approach 3: XOR (Optimal — no overflow)

### Intuition
XOR of a number with itself is 0. XOR all values 1 to n+1 and XOR all array elements. Duplicates cancel out, leaving the missing number.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumberXOR(vector<int>& nums) {
        int n = nums.size();
        int xorAll = 0, xorArr = 0;
        for (int i = 1; i <= n + 1; i++) xorAll ^= i;
        for (int x : nums) xorArr ^= x;
        return xorAll ^ xorArr;
    }
};

int main() {
    Solution sol;
    vector<int> v1 = {1, 2, 4, 5};
    cout << sol.missingNumberXOR(v1) << endl; // 3
    return 0;
}
```

---

## Common Mistakes
1. Integer overflow with sum formula — use `long long`
2. Off-by-one: range is [1, n+1] not [0, n]

## Interview Tips
- Mention both sum and XOR approaches — XOR avoids overflow
- Follow-up: find two missing numbers (use system of equations or XOR trick)
