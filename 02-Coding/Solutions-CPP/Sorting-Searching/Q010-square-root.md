# Solution: Square Root of a Number

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q010-square-root.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Linear Search | O(sqrt(n)) | O(1) | ✗ |
| Binary Search on Answer | O(log n) | O(1) | ✓✓ |
| Newton's Method | O(log n) | O(1) | ✓ |

---

## Approach 1: Linear Search (Brute Force)

### Intuition
Try every integer from 1 upward until i*i exceeds n. The answer is i-1.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int n) {
        if (n == 0) return 0;
        int i = 1;
        while ((long long)i * i <= n) {
            i++;
        }
        return i - 1;
    }
};

int main() {
    Solution sol;
    cout << sol.mySqrt(0) << endl;  // 0
    cout << sol.mySqrt(1) << endl;  // 1
    cout << sol.mySqrt(4) << endl;  // 2
    cout << sol.mySqrt(8) << endl;  // 2
    cout << sol.mySqrt(25) << endl; // 5
    return 0;
}
```

### Complexity Analysis
- **Time:** O(sqrt(n))
- **Space:** O(1)

---

## Approach 2: Binary Search on Answer (Optimal)

### Intuition
The answer lies in [0, n]. Binary search for the largest integer `mid` such that `mid * mid <= n`. This is "binary search on the answer" -- we are not searching in an array but in a range of possible answers.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int n) {
        if (n == 0) return 0;

        int low = 1, high = n, ans = 0;

        while (low <= high) {
            long long mid = low + (high - low) / 2;

            if (mid * mid == n) {
                return mid;
            } else if (mid * mid < n) {
                ans = mid;       // mid could be the answer
                low = mid + 1;   // try larger
            } else {
                high = mid - 1;  // mid*mid > n, try smaller
            }
        }
        return ans;
    }
};

int main() {
    Solution sol;
    cout << sol.mySqrt(0) << endl;          // 0
    cout << sol.mySqrt(1) << endl;          // 1
    cout << sol.mySqrt(4) << endl;          // 2
    cout << sol.mySqrt(8) << endl;          // 2
    cout << sol.mySqrt(25) << endl;         // 5
    cout << sol.mySqrt(100) << endl;        // 10
    cout << sol.mySqrt(2147483647) << endl; // 46340 (INT_MAX)
    return 0;
}
```

### Dry Run
**Input:** n = 8

| Step | low | high | mid | mid*mid | Action | ans |
|------|-----|------|-----|---------|--------|-----|
| 1 | 1 | 8 | 4 | 16 | 16>8, high=3 | 0 |
| 2 | 1 | 3 | 2 | 4 | 4<8, ans=2, low=3 | 2 |
| 3 | 3 | 3 | 3 | 9 | 9>8, high=2 | 2 |
| 4 | low=3 > high=2 | STOP | | | | **2** |

**Output:** 2 (floor of sqrt(8) = 2.828...)

**Input:** n = 25

| Step | low | high | mid | mid*mid | Action |
|------|-----|------|-----|---------|--------|
| 1 | 1 | 25 | 13 | 169 | 169>25, high=12 |
| 2 | 1 | 12 | 6 | 36 | 36>25, high=5 |
| 3 | 1 | 5 | 3 | 9 | 9<25, ans=3, low=4 |
| 4 | 4 | 5 | 4 | 16 | 16<25, ans=4, low=5 |
| 5 | 5 | 5 | 5 | 25 | 25==25, return **5** |

### Complexity Analysis
- **Time:** O(log n) -- binary search halves the range each time
- **Space:** O(1)

---

## Approach 3: Newton's Method

### Intuition
Newton's method iteratively improves the guess: `x_new = (x + n/x) / 2`. This converges very quickly.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int n) {
        if (n == 0) return 0;
        long long x = n;
        while (x * x > n) {
            x = (x + n / x) / 2;
        }
        return (int)x;
    }
};

int main() {
    Solution sol;
    cout << sol.mySqrt(0) << endl;          // 0
    cout << sol.mySqrt(1) << endl;          // 1
    cout << sol.mySqrt(8) << endl;          // 2
    cout << sol.mySqrt(25) << endl;         // 5
    cout << sol.mySqrt(2147483647) << endl; // 46340
    return 0;
}
```

### Complexity Analysis
- **Time:** O(log n) -- Newton's method converges quadratically
- **Space:** O(1)

---

## Common Mistakes
1. **Integer overflow:** `mid * mid` can overflow `int` -- use `long long`
2. Not handling n = 0 as a special case
3. Returning `mid` when `mid*mid < n` without recording `ans` (misses the floor value)
4. Using `high = n/2` as optimization but forgetting it fails for n = 1

## Interview Tips
- This is a classic "binary search on answer" problem -- the search space is [0, n], not an array
- The pattern applies to many problems: kth smallest, capacity to ship, minimize maximum, etc.
- Always use `long long` for mid*mid to prevent overflow
- Newton's method is a nice bonus to mention but binary search is the expected answer
- For TCS NQT: know both the approach and the step-by-step trace
