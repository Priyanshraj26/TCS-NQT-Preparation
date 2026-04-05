# Solution: Prime Number Check

[← Back to Question](../../DSA-Questions/Other-Topics/Q008-prime-check.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive (Check all divisors) | O(n) | O(1) | ✗ |
| Check up to sqrt(n) | O(sqrt(n)) | O(1) | ✓✓ |
| Optimized (6k +/- 1) | O(sqrt(n)) | O(1) | ✓✓ |

---

## Approach 1: Naive (Check All Divisors)

### Intuition
Check if any number from 2 to n-1 divides n.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isPrime(2) << endl;  // true
    cout << sol.isPrime(7) << endl;  // true
    cout << sol.isPrime(10) << endl; // false
    cout << sol.isPrime(1) << endl;  // false
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Approach 2: Check up to sqrt(n) (Optimal)

### Intuition
If n has a factor greater than sqrt(n), it must also have a factor less than sqrt(n). So we only need to check divisors from 2 to sqrt(n).

### C++ Code
```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true; // 2 and 3 are prime

        for (int i = 2; i <= (int)sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isPrime(2) << endl;     // true
    cout << sol.isPrime(3) << endl;     // true
    cout << sol.isPrime(4) << endl;     // false
    cout << sol.isPrime(7) << endl;     // true
    cout << sol.isPrime(25) << endl;    // false (5*5)
    cout << sol.isPrime(29) << endl;    // true
    cout << sol.isPrime(97) << endl;    // true
    cout << sol.isPrime(100) << endl;   // false
    cout << sol.isPrime(1) << endl;     // false
    cout << sol.isPrime(0) << endl;     // false
    cout << sol.isPrime(-7) << endl;    // false
    return 0;
}
```

### Dry Run
**Input:** n = 29

sqrt(29) = 5.38, so check divisors 2, 3, 4, 5.

| i | 29 % i | Divisible? |
|---|--------|-----------|
| 2 | 1 | No |
| 3 | 2 | No |
| 4 | 1 | No |
| 5 | 4 | No |

No divisor found -> **true** (29 is prime)

**Input:** n = 25

sqrt(25) = 5, so check divisors 2, 3, 4, 5.

| i | 25 % i | Divisible? |
|---|--------|-----------|
| 2 | 1 | No |
| 3 | 1 | No |
| 4 | 1 | No |
| 5 | 0 | **Yes** -> return false |

### Complexity Analysis
- **Time:** O(sqrt(n))
- **Space:** O(1)

---

## Approach 3: Optimized with 6k +/- 1

### Intuition
All primes greater than 3 are of the form 6k+1 or 6k-1 (i.e., adjacent to multiples of 6). After checking 2 and 3, we only need to check numbers of the form 6k-1 and 6k+1. This skips about 2/3 of the candidates.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;

        // Check 6k-1 and 6k+1 up to sqrt(n)
        for (int i = 5; (long long)i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;
    cout << sol.isPrime(2) << endl;         // true
    cout << sol.isPrime(3) << endl;         // true
    cout << sol.isPrime(5) << endl;         // true
    cout << sol.isPrime(7) << endl;         // true
    cout << sol.isPrime(11) << endl;        // true
    cout << sol.isPrime(15) << endl;        // false (3*5)
    cout << sol.isPrime(49) << endl;        // false (7*7)
    cout << sol.isPrime(97) << endl;        // true
    cout << sol.isPrime(999999937) << endl; // true (large prime)
    return 0;
}
```

### Dry Run
**Input:** n = 49

- n > 3: yes
- n % 2 = 1 (not even)
- n % 3 = 1 (not divisible by 3)
- i = 5: 5*5 = 25 <= 49
  - 49 % 5 = 4 (no)
  - 49 % 7 = 0 -> **false** (49 = 7*7)

**Input:** n = 97

- Not even, not divisible by 3
- i=5: 97%5=2, 97%7=6
- i=11: 11*11=121 > 97 -> STOP

**Output:** true

### Complexity Analysis
- **Time:** O(sqrt(n)) but with ~3x fewer iterations than approach 2
- **Space:** O(1)

---

## Common Mistakes
1. Forgetting that 1 is NOT prime
2. Forgetting that 2 is the only even prime
3. Using `i < sqrt(n)` instead of `i <= sqrt(n)` (misses perfect squares like 25, 49)
4. Integer overflow when computing `i * i` for large n (use `(long long)i * i`)

## Interview Tips
- O(sqrt(n)) is the expected answer for primality testing in interviews
- The 6k +/- 1 optimization shows deeper understanding
- For checking many numbers: use Sieve of Eratosthenes instead
- For very large numbers: probabilistic tests like Miller-Rabin are used
- TCS NQT: this is a very common question, know the sqrt optimization and edge cases
