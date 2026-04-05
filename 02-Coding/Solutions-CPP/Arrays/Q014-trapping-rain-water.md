# Solution: Trapping Rain Water

[← Back to Question](../../DSA-Questions/Arrays/Q014-trapping-rain-water.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | ✗ |
| Prefix-Suffix arrays | O(n) | O(n) | ✗ |
| Two Pointers | O(n) | O(1) | ✓ |

---

## Approach 1: Brute Force

### Intuition
For each bar, find the maximum height to its left and right. Water at that bar = min(leftMax, rightMax) - height[i].

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int trapBrute(vector<int>& height) {
        int n = height.size();
        int water = 0;
        for (int i = 0; i < n; i++) {
            int leftMax = 0, rightMax = 0;
            for (int j = 0; j <= i; j++) leftMax = max(leftMax, height[j]);
            for (int j = i; j < n; j++) rightMax = max(rightMax, height[j]);
            water += min(leftMax, rightMax) - height[i];
        }
        return water;
    }
};

int main() {
    Solution sol;
    vector<int> h = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << sol.trapBrute(h) << endl; // 6
    return 0;
}
```

---

## Approach 2: Two Pointers (Optimal)

### Intuition
Use two pointers from both ends. At each step, the pointer with the smaller max determines the water level. If `leftMax < rightMax`, we know water at left pointer is bounded by `leftMax`, so we process left and move it inward. Vice versa for right.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n <= 2) return 0;

        int left = 0, right = n - 1;
        int leftMax = 0, rightMax = 0;
        int water = 0;

        while (left <= right) {
            if (leftMax <= rightMax) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    water += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    water += rightMax - height[right];
                }
                right--;
            }
        }

        return water;
    }
};

int main() {
    Solution sol;

    // Test 1
    vector<int> h1 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << sol.trap(h1) << endl; // 6

    // Test 2
    vector<int> h2 = {4, 2, 0, 3, 2, 5};
    cout << sol.trap(h2) << endl; // 9

    // Test 3: no trapping
    vector<int> h3 = {1, 2, 3, 4, 5};
    cout << sol.trap(h3) << endl; // 0

    // Test 4: single bar
    vector<int> h4 = {5};
    cout << sol.trap(h4) << endl; // 0

    return 0;
}
```

### Dry Run
**Input:** `[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`

| Step | left | right | leftMax | rightMax | Action | water |
|------|------|-------|---------|----------|--------|-------|
| 1 | 0 | 11 | 0 | 0 | lM<=rM, h[0]=0>=lM → lM=0, left++ | 0 |
| 2 | 1 | 11 | 0 | 0 | lM<=rM, h[1]=1>=lM → lM=1, left++ | 0 |
| 3 | 2 | 11 | 1 | 0 | lM>rM, h[11]=1>=rM → rM=1, right-- | 0 |
| 4 | 2 | 10 | 1 | 1 | lM<=rM, h[2]=0<lM → +1, left++ | 1 |
| 5 | 3 | 10 | 1 | 1 | lM<=rM, h[3]=2>=lM → lM=2, left++ | 1 |
| ... | ... | ... | ... | ... | ... | ... |
| final | — | — | — | — | — | **6** |

### Complexity Analysis
- **Time:** O(n) — single pass with two pointers
- **Space:** O(1) — constant extra space

---

## Common Mistakes
1. Not handling edge cases (n < 3 means no water can be trapped)
2. Confusing which pointer to advance
3. Off-by-one errors in the loop condition

## Interview Tips
- This is a classic hard problem — very impressive if solved optimally in interview
- Start with brute force, then prefix arrays, then optimize to two pointers
- Follow-up: container with most water (different problem, simpler)
