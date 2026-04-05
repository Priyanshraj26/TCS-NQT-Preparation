# Solution: Rotate Array by K Positions

[← Back to Question](../../DSA-Questions/Arrays/Q003-rotate-array.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force (rotate one by one) | O(n*k) | O(1) | ✗ |
| Using extra array | O(n) | O(n) | ✗ |
| Reversal Algorithm | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
Rotate the array one position at a time, k times.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotateBrute(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        for (int i = 0; i < k; i++) {
            int last = nums[n - 1];
            for (int j = n - 1; j > 0; j--) {
                nums[j] = nums[j - 1];
            }
            nums[0] = last;
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    sol.rotateBrute(nums, 3);
    for (int x : nums) cout << x << " ";
    cout << endl; // 5 6 7 1 2 3 4
    return 0;
}
```

---

## Approach 2: Reversal Algorithm (Optimal)

### Intuition
To rotate right by k:
1. Reverse the entire array
2. Reverse the first k elements
3. Reverse the remaining n-k elements

Example: [1,2,3,4,5,6,7], k=3
- Reverse all: [7,6,5,4,3,2,1]
- Reverse first 3: [5,6,7,4,3,2,1]
- Reverse last 4: [5,6,7,1,2,3,4]

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        if (k == 0) return;

        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> v1 = {1, 2, 3, 4, 5, 6, 7};
    sol.rotate(v1, 3);
    for (int x : v1) cout << x << " "; // 5 6 7 1 2 3 4
    cout << endl;

    // Test 2
    vector<int> v2 = {-1, -100, 3, 99};
    sol.rotate(v2, 2);
    for (int x : v2) cout << x << " "; // 3 99 -1 -100
    cout << endl;

    // Test 3: k > n
    vector<int> v3 = {1, 2, 3};
    sol.rotate(v3, 5); // 5 % 3 = 2
    for (int x : v3) cout << x << " "; // 2 3 1
    cout << endl;

    return 0;
}
```

### Dry Run
**Input:** `[1, 2, 3, 4, 5, 6, 7]`, k = 3

| Step | Operation | Array State |
|------|-----------|-------------|
| 0 | Initial | [1, 2, 3, 4, 5, 6, 7] |
| 1 | Reverse all | [7, 6, 5, 4, 3, 2, 1] |
| 2 | Reverse [0..2] | [5, 6, 7, 4, 3, 2, 1] |
| 3 | Reverse [3..6] | [5, 6, 7, 1, 2, 3, 4] |

**Output:** `5 6 7 1 2 3 4`

### Complexity Analysis
- **Time:** O(n) — three reverses, each O(n)
- **Space:** O(1) — in-place

---

## Common Mistakes
1. Forgetting `k %= n` — k can be larger than array size
2. Off-by-one in reverse boundaries
3. Not handling k = 0 case

## Interview Tips
- The reversal trick is a classic — memorize the pattern
- For left rotation by k: reverse first k, reverse last n-k, reverse all
- Follow-up: rotate a linked list by k positions
