# Solution: GCD and LCM

[← Back to Question](../../DSA-Questions/Other-Topics/Q007-gcd-lcm.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force | O(min(a,b)) | O(1) | ✗ |
| Euclidean Algorithm (Iterative) | O(log(min(a,b))) | O(1) | ✓✓ |
| Euclidean Algorithm (Recursive) | O(log(min(a,b))) | O(log(min(a,b))) | ✓ |

---

## Approach 1: Brute Force

### Intuition
GCD: Try all numbers from min(a,b) down to 1, return the first one that divides both.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int gcdBrute(int a, int b) {
        int result = 1;
        for (int i = 1; i <= min(a, b); i++) {
            if (a % i == 0 && b % i == 0)
                result = i;
        }
        return result;
    }

    int lcmBrute(int a, int b) {
        int mx = max(a, b);
        for (int i = mx; i <= a * b; i += mx) {
            if (i % a == 0 && i % b == 0)
                return i;
        }
        return a * b;
    }
};

int main() {
    Solution sol;
    cout << "GCD(12,18) = " << sol.gcdBrute(12, 18) << endl; // 6
    cout << "LCM(12,18) = " << sol.lcmBrute(12, 18) << endl; // 36
    return 0;
}
```

### Complexity Analysis
- **GCD Time:** O(min(a,b))
- **LCM Time:** O(a*b/gcd in worst case)

---

## Approach 2: Euclidean Algorithm (Iterative)

### Intuition
**Key property:** GCD(a, b) = GCD(b, a % b). Keep replacing (a, b) with (b, a%b) until b becomes 0. At that point, a is the GCD.

**LCM formula:** LCM(a, b) = (a * b) / GCD(a, b)

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    long long lcm(int a, int b) {
        // Use long long to prevent overflow
        return (long long)a / gcd(a, b) * b; // divide first to avoid overflow
    }
};

int main() {
    Solution sol;

    cout << "GCD(12, 18) = " << sol.gcd(12, 18) << endl;   // 6
    cout << "LCM(12, 18) = " << sol.lcm(12, 18) << endl;   // 36

    cout << "GCD(54, 24) = " << sol.gcd(54, 24) << endl;    // 6
    cout << "LCM(54, 24) = " << sol.lcm(54, 24) << endl;    // 216

    cout << "GCD(7, 13) = " << sol.gcd(7, 13) << endl;      // 1 (coprime)
    cout << "LCM(7, 13) = " << sol.lcm(7, 13) << endl;      // 91

    cout << "GCD(0, 5) = " << sol.gcd(0, 5) << endl;        // 5
    cout << "GCD(5, 0) = " << sol.gcd(5, 0) << endl;        // 5
    cout << "GCD(100, 100) = " << sol.gcd(100, 100) << endl; // 100

    return 0;
}
```

### Dry Run
**GCD(54, 24):**

| Step | a | b | a % b |
|------|---|---|-------|
| 1 | 54 | 24 | 6 |
| 2 | 24 | 6 | 0 |
| 3 | 6 | 0 | STOP |

**GCD = 6**

**GCD(12, 18):**

| Step | a | b | a % b |
|------|---|---|-------|
| 1 | 12 | 18 | 12 |
| 2 | 18 | 12 | 6 |
| 3 | 12 | 6 | 0 |
| 4 | 6 | 0 | STOP |

**GCD = 6**, LCM = 12 * 18 / 6 = **36**

### Complexity Analysis
- **Time:** O(log(min(a,b))) -- the remainder decreases rapidly
- **Space:** O(1)

---

## Approach 3: Euclidean Algorithm (Recursive)

### Intuition
Same algorithm, expressed recursively.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    long long lcm(int a, int b) {
        return (long long)a / gcd(a, b) * b;
    }
};

int main() {
    Solution sol;
    cout << "GCD(12, 18) = " << sol.gcd(12, 18) << endl; // 6
    cout << "LCM(12, 18) = " << sol.lcm(12, 18) << endl; // 36

    cout << "GCD(48, 36) = " << sol.gcd(48, 36) << endl; // 12
    cout << "LCM(48, 36) = " << sol.lcm(48, 36) << endl; // 144

    // C++17 has __gcd() and C++17 also has std::gcd in <numeric>
    cout << "STL GCD: " << __gcd(12, 18) << endl; // 6
    return 0;
}
```

### Complexity Analysis
- **Time:** O(log(min(a,b)))
- **Space:** O(log(min(a,b))) -- recursion stack

---

## Common Mistakes
1. **LCM overflow:** Computing `a * b` before dividing by GCD causes overflow. Always do `a / gcd * b`
2. Not handling the case when a or b is 0 (GCD(0, n) = n)
3. Forgetting that GCD is always positive (take absolute values for negative inputs)
4. Confusing the order: GCD(a, b) = GCD(b, a%b), NOT GCD(a%b, b)

## Interview Tips
- The Euclidean algorithm is one of the oldest algorithms -- dates back to 300 BC
- C++17 provides `std::gcd` and `std::lcm` in `<numeric>`, and `__gcd` is available in GCC
- The relationship `a * b = GCD(a,b) * LCM(a,b)` is fundamental
- Extended Euclidean Algorithm finds x, y such that ax + by = GCD(a,b) -- useful for modular inverse
- For TCS NQT: this is a very frequently asked question, know both iterative and recursive
