# Solution: Sieve of Eratosthenes

[← Back to Question](../../DSA-Questions/Other-Topics/Q010-sieve-eratosthenes.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Naive (Check each number) | O(n * sqrt(n)) | O(1) | ✗ |
| Sieve of Eratosthenes | O(n log log n) | O(n) | ✓✓ |

---

## Approach 1: Naive (Check Each Number Individually)

### Intuition
For each number from 2 to n, check if it is prime using the O(sqrt(n)) primality test.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; (long long)i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    vector<int> findPrimes(int n) {
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i))
                primes.push_back(i);
        }
        return primes;
    }
};

int main() {
    Solution sol;
    auto primes = sol.findPrimes(30);
    for (int p : primes) cout << p << " ";
    cout << endl; // 2 3 5 7 11 13 17 19 23 29
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n * sqrt(n))
- **Space:** O(1) extra (excluding output)

---

## Approach 2: Sieve of Eratosthenes (Optimal)

### Intuition
1. Create a boolean array of size n+1, initially all set to `true`.
2. Start from the smallest prime (2). Mark all its multiples as `false` (not prime).
3. Move to the next unmarked number and repeat.
4. Continue until we have processed up to sqrt(n).
5. All numbers still marked `true` are primes.

The key insight: when we reach a prime p, we start marking from p*p (all smaller multiples have already been marked by smaller primes).

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sieveOfEratosthenes(int n) {
        // Step 1: Create boolean array
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;

        // Step 2: Mark multiples of each prime
        for (int i = 2; (long long)i * i <= n; i++) {
            if (isPrime[i]) {
                // Mark all multiples of i starting from i*i
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        // Step 3: Collect all primes
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i])
                primes.push_back(i);
        }
        return primes;
    }

    int countPrimes(int n) {
        if (n < 2) return 0;
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; (long long)i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i)
                    isPrime[j] = false;
            }
        }
        int count = 0;
        for (int i = 2; i <= n; i++)
            if (isPrime[i]) count++;
        return count;
    }
};

int main() {
    Solution sol;

    // Print all primes up to 50
    auto primes = sol.sieveOfEratosthenes(50);
    cout << "Primes up to 50: ";
    for (int p : primes) cout << p << " ";
    cout << endl;
    // 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

    // Count primes
    cout << "Primes up to 10: " << sol.countPrimes(10) << endl;     // 4
    cout << "Primes up to 100: " << sol.countPrimes(100) << endl;   // 25
    cout << "Primes up to 1000: " << sol.countPrimes(1000) << endl; // 168

    // Small cases
    auto p1 = sol.sieveOfEratosthenes(1);
    cout << "Primes up to 1: " << p1.size() << endl; // 0

    auto p2 = sol.sieveOfEratosthenes(2);
    cout << "Primes up to 2: ";
    for (int p : p2) cout << p << " ";
    cout << endl; // 2

    return 0;
}
```

### Dry Run (Step-by-Step Visualization)
**Input:** n = 30

**Initial array (indices 2-30, all true):**
```
2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T  T
```

**i=2 (prime): Mark multiples starting from 4:**
```
2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
T  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F
         ^     ^     ^     ^     ^     ^     ^     ^     ^     ^     ^     ^     ^     ^
```

**i=3 (prime): Mark multiples starting from 9:**
```
2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
T  T  F  T  F  T  F  F  F  T  F  T  F  F  F  T  F  T  F  F  F  T  F  T  F  F  F  T  F
                        ^           ^        ^           ^        ^           ^
```

**i=4: already marked false, skip**

**i=5: 5*5=25 <= 30. Mark multiples starting from 25:**
```
Mark 25 (already done by 5's not needed - 25 is new!)
25 -> F (was T, now F)
30 -> already F
```

**i=6: 6*6=36 > 30, STOP**

**Final primes:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

| Step | i | Marks (j = i*i, i*i+i, ...) |
|------|---|----------------------------|
| 1 | 2 | 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30 |
| 2 | 3 | 9, 12, 15, 18, 21, 24, 27, 30 |
| 3 | 5 | 25, 30 |
| STOP | 6*6=36>30 | |

### Complexity Analysis
- **Time:** O(n log log n) -- proven by Mertens' theorem
- **Space:** O(n) for the boolean array

---

## Common Mistakes
1. Starting the inner loop from `2*i` instead of `i*i` (correct but slower)
2. Not marking 0 and 1 as non-prime
3. Using `int j = i*i` which overflows for large i -- use `(long long)i*i <= n`
4. Off-by-one: the sieve array should be of size `n+1` to include index n

## Interview Tips
- The Sieve of Eratosthenes is the most efficient way to find all primes up to n
- O(n log log n) is nearly linear -- excellent for n up to 10^7
- For n up to 10^9: use a segmented sieve (processes in sqrt(n)-sized blocks)
- Space optimization: use a bitset instead of bool array (8x less memory)
- Applications: finding prime factors, Euler's totient, Mobius function
- The "start from i*i" optimization is important to mention in interviews
- TCS NQT: know the algorithm, be able to trace it step by step, and state the time complexity
