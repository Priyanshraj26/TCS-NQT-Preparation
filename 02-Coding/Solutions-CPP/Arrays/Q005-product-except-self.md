# Solution: Product of Array Except Self

[← Back to Question](../../DSA-Questions/Arrays/Q005-product-except-self.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(n) | ✗ |
| Prefix & Suffix arrays | O(n) | O(n) | ✗ |
| Optimized (single output array) | O(n) | O(1)* | ✓ |

*O(1) extra space — output array not counted.

---

## Approach 1: Brute Force

### Intuition
For each index, multiply all other elements.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelfBrute(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    answer[i] *= nums[j];
                }
            }
        }
        return answer;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    auto res = sol.productExceptSelfBrute(nums);
    for (int x : res) cout << x << " "; // 24 12 8 6
    cout << endl;
    return 0;
}
```

---

## Approach 2: Prefix-Suffix (Optimal)

### Intuition
For each index `i`, the result = product of all elements to its left * product of all elements to its right. We compute left products in a forward pass and multiply right products in a backward pass, using the output array itself.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);

        // Forward pass: answer[i] = product of nums[0..i-1]
        int leftProduct = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = leftProduct;
            leftProduct *= nums[i];
        }

        // Backward pass: multiply by product of nums[i+1..n-1]
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return answer;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 3, 4};
    auto r1 = sol.productExceptSelf(v1);
    for (int x : r1) cout << x << " "; // 24 12 8 6
    cout << endl;

    // Test 2: contains zero
    vector<int> v2 = {-1, 1, 0, -3, 3};
    auto r2 = sol.productExceptSelf(v2);
    for (int x : r2) cout << x << " "; // 0 0 9 0 0
    cout << endl;

    // Test 3: two elements
    vector<int> v3 = {3, 5};
    auto r3 = sol.productExceptSelf(v3);
    for (int x : r3) cout << x << " "; // 5 3
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 3, 4]`

**Forward pass (left products):**

| i | leftProduct (before) | answer[i] | leftProduct (after) |
|---|---------------------|-----------|-------------------|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 2 |
| 2 | 2 | 2 | 6 |
| 3 | 6 | 6 | 24 |

**Backward pass (right products):**

| i | rightProduct (before) | answer[i] = answer[i]*right | rightProduct (after) |
|---|----------------------|---------------------------|---------------------|
| 3 | 1 | 6*1 = 6 | 4 |
| 2 | 4 | 2*4 = 8 | 12 |
| 1 | 12 | 1*12 = 12 | 24 |
| 0 | 24 | 1*24 = 24 | 24 |

**Output:** `24 12 8 6`

### Complexity Analysis
- **Time:** O(n) — two passes
- **Space:** O(1) extra — output array not counted

---

## Common Mistakes
1. Using division (fails when zeros are present, and problem forbids it)
2. Integer overflow — check constraints carefully
3. Not handling the case with multiple zeros

## Interview Tips
- Clarify whether division is allowed — if yes, total product / nums[i] works (handle zeros)
- This pattern of prefix/suffix computation appears in many problems
- Follow-up: handle it with zeros using division (count zeros)
