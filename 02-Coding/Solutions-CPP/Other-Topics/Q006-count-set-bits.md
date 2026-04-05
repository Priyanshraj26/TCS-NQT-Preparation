# Solution: Count Set Bits (Number of 1s in Binary)

[← Back to Question](../../DSA-Questions/Other-Topics/Q006-count-set-bits.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Check Each Bit | O(log n) | O(1) | ✓ |
| Brian Kernighan's Algorithm | O(k) where k = set bits | O(1) | ✓✓ |
| Lookup Table | O(1) | O(256) | ✓ |

---

## Approach 1: Check Each Bit (Brute Force)

### Intuition
Check each bit position by right-shifting and checking if the last bit is 1.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int countSetBits(int n) {
        int count = 0;
        while (n > 0) {
            count += (n & 1); // check last bit
            n >>= 1;         // right shift
        }
        return count;
    }
};

int main() {
    Solution sol;
    cout << sol.countSetBits(7) << endl;   // 3 (111)
    cout << sol.countSetBits(13) << endl;  // 3 (1101)
    cout << sol.countSetBits(0) << endl;   // 0
    cout << sol.countSetBits(255) << endl; // 8 (11111111)
    cout << sol.countSetBits(1024) << endl; // 1 (10000000000)
    return 0;
}
```

### Dry Run
**Input:** n = 13 (binary: 1101)

| Step | n (binary) | n & 1 | count | n >> 1 |
|------|-----------|-------|-------|--------|
| 1 | 1101 | 1 | 1 | 110 |
| 2 | 0110 | 0 | 1 | 011 |
| 3 | 0011 | 1 | 2 | 001 |
| 4 | 0001 | 1 | 3 | 000 |
| 5 | 0000 | STOP | | |

**Output:** 3

### Complexity Analysis
- **Time:** O(log n) -- checks all bit positions (32 for int)
- **Space:** O(1)

---

## Approach 2: Brian Kernighan's Algorithm (Optimal)

### Intuition
The expression `n & (n-1)` clears the **lowest set bit** of n. Repeat until n becomes 0, counting each iteration. This runs in O(k) where k is the number of set bits -- faster than checking all 32 bits when set bits are few.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int countSetBits(int n) {
        int count = 0;
        while (n > 0) {
            n = n & (n - 1); // clear lowest set bit
            count++;
        }
        return count;
    }
};

int main() {
    Solution sol;
    cout << sol.countSetBits(7) << endl;    // 3  (111)
    cout << sol.countSetBits(13) << endl;   // 3  (1101)
    cout << sol.countSetBits(0) << endl;    // 0
    cout << sol.countSetBits(255) << endl;  // 8  (11111111)
    cout << sol.countSetBits(128) << endl;  // 1  (10000000)
    cout << sol.countSetBits(1023) << endl; // 10 (1111111111)
    return 0;
}
```

### Dry Run
**Input:** n = 13 (binary: 1101)

| Step | n (binary) | n-1 (binary) | n & (n-1) | count |
|------|-----------|-------------|-----------|-------|
| 1 | 1101 | 1100 | 1100 | 1 |
| 2 | 1100 | 1011 | 1000 | 2 |
| 3 | 1000 | 0111 | 0000 | 3 |
| 4 | 0000 | STOP | | |

**Output:** 3

**Key observation:** Only 3 iterations for 3 set bits (vs 4 iterations in the brute force for a 4-bit number).

**Input:** n = 128 (binary: 10000000)

| Step | n (binary) | n & (n-1) | count |
|------|-----------|-----------|-------|
| 1 | 10000000 | 00000000 | 1 |

Only 1 iteration!

### Complexity Analysis
- **Time:** O(k) where k = number of set bits (at most O(log n))
- **Space:** O(1)

---

## Approach 3: Using __builtin_popcount (GCC Built-in)

### Intuition
GCC provides `__builtin_popcount()` which typically maps to a single CPU instruction (POPCNT).

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int countSetBits(int n) {
        return __builtin_popcount(n);
    }
};

int main() {
    Solution sol;
    cout << sol.countSetBits(7) << endl;   // 3
    cout << sol.countSetBits(13) << endl;  // 3
    cout << sol.countSetBits(0) << endl;   // 0
    cout << sol.countSetBits(255) << endl; // 8
    return 0;
}
```

### Complexity Analysis
- **Time:** O(1)
- **Space:** O(1)

---

## Common Mistakes
1. Not handling n = 0 (the while loop correctly returns 0)
2. Using `n % 2` instead of `n & 1` (functionally same but bitwise is faster)
3. Infinite loop if n is negative (for unsigned, use `unsigned int` or handle carefully)
4. Confusing `n & (n-1)` (clears lowest set bit) with `n & (n+1)` (different operation)

## Interview Tips
- Brian Kernighan's algorithm is a must-know for bit manipulation interviews
- The trick `n & (n-1)` appears in many problems: power of two, counting bits, etc.
- `__builtin_popcount` is fine in competitive programming but explain the algorithm in interviews
- For negative numbers, use `unsigned int` or specify behavior
- Follow-up: count set bits for all numbers from 0 to n (use DP: dp[i] = dp[i >> 1] + (i & 1))
- TCS NQT frequently tests bit manipulation basics
