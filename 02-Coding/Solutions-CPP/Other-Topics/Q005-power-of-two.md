# Solution: Power of Two

[← Back to Question](../../DSA-Questions/Other-Topics/Q005-power-of-two.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Iterative Division | O(log n) | O(1) | ✓ |
| Bit Manipulation: n & (n-1) | O(1) | O(1) | ✓✓ |
| Count Set Bits | O(log n) | O(1) | ✓ |

---

## Approach 1: Iterative Division

### Intuition
Keep dividing by 2. If we reach 1, it is a power of two. If at any point it is odd (and not 1), it is not.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false;
        while (n > 1) {
            if (n % 2 != 0) return false;
            n /= 2;
        }
        return true; // n == 1
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isPowerOfTwo(1) << endl;   // true (2^0)
    cout << sol.isPowerOfTwo(16) << endl;  // true (2^4)
    cout << sol.isPowerOfTwo(3) << endl;   // false
    cout << sol.isPowerOfTwo(0) << endl;   // false
    cout << sol.isPowerOfTwo(-4) << endl;  // false
    cout << sol.isPowerOfTwo(1024) << endl; // true
    return 0;
}
```

### Complexity Analysis
- **Time:** O(log n)
- **Space:** O(1)

---

## Approach 2: Bit Manipulation -- n & (n-1) (Optimal)

### Intuition
A power of two in binary has exactly one bit set: 1, 10, 100, 1000, etc. When you subtract 1, all bits below flip: 1000 - 1 = 0111. So `n & (n-1)` clears the only set bit, giving 0.

**Formula:** `n > 0 && (n & (n-1)) == 0`

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isPowerOfTwo(1) << endl;    // true  (1 = 0001, 0 = 0000, & = 0)
    cout << sol.isPowerOfTwo(2) << endl;    // true  (10 & 01 = 00)
    cout << sol.isPowerOfTwo(4) << endl;    // true  (100 & 011 = 000)
    cout << sol.isPowerOfTwo(16) << endl;   // true  (10000 & 01111 = 00000)
    cout << sol.isPowerOfTwo(3) << endl;    // false (11 & 10 = 10 != 0)
    cout << sol.isPowerOfTwo(6) << endl;    // false (110 & 101 = 100 != 0)
    cout << sol.isPowerOfTwo(0) << endl;    // false (n <= 0)
    cout << sol.isPowerOfTwo(-8) << endl;   // false (n <= 0)
    cout << sol.isPowerOfTwo(1024) << endl; // true
    return 0;
}
```

### Dry Run
**n & (n-1) for various values:**

| n | Binary(n) | Binary(n-1) | n & (n-1) | Power of 2? |
|---|-----------|-------------|-----------|-------------|
| 1 | 0001 | 0000 | 0000 = 0 | Yes |
| 2 | 0010 | 0001 | 0000 = 0 | Yes |
| 4 | 0100 | 0011 | 0000 = 0 | Yes |
| 8 | 1000 | 0111 | 0000 = 0 | Yes |
| 3 | 0011 | 0010 | 0010 != 0 | No |
| 6 | 0110 | 0101 | 0100 != 0 | No |
| 12 | 1100 | 1011 | 1000 != 0 | No |

### Complexity Analysis
- **Time:** O(1) -- single bitwise operation
- **Space:** O(1)

---

## Approach 3: Count Set Bits

### Intuition
A power of two has exactly one set bit. Count the set bits and check if the count is 1.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false;
        return __builtin_popcount(n) == 1;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isPowerOfTwo(1) << endl;   // true
    cout << sol.isPowerOfTwo(16) << endl;  // true
    cout << sol.isPowerOfTwo(3) << endl;   // false
    cout << sol.isPowerOfTwo(0) << endl;   // false
    return 0;
}
```

### Complexity Analysis
- **Time:** O(1) -- `__builtin_popcount` is typically a single CPU instruction
- **Space:** O(1)

---

## Common Mistakes
1. Forgetting to check `n > 0` (0 and negative numbers are not powers of two, but `0 & (-1) == 0`)
2. Using `n & (n-1) == 0` without parentheses (`==` has higher precedence than `&` in C++)
3. Not handling n = 1 (2^0 = 1 is a valid power of two)

## Interview Tips
- The `n & (n-1)` trick is one of the most important bit manipulation techniques
- It clears the **lowest set bit** -- useful for counting set bits too (Brian Kernighan's algorithm)
- Other ways: check if `log2(n)` is an integer, or check if `n` divides a large power of 2
- For TCS NQT: know the binary representation explanation clearly
- Related problems: power of 3, power of 4 (need additional checks)
