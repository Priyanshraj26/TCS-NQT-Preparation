/*
 * Q010: Sieve of Eratosthenes
 * Question: ../../../DSA-Questions/Other-Topics/Q010-sieve-eratosthenes.md
 *
 * Approach Overview:
 * +---------------------------+---------------+---------+
 * | Approach                  | Time          | Space   |
 * +---------------------------+---------------+---------+
 * | Brute Force (per number)  | O(n*sqrt(n))  | O(1)    |
 * | Sieve of Eratosthenes     | O(n*log(logn))| O(n)    |
 * +---------------------------+---------------+---------+
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Brute Force
// ===========================================
vector<int> primesBrute(int n) {
    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) { isPrime = false; break; }
        }
        if (isPrime) primes.push_back(i);
    }
    return primes;
}

// ===========================================
// Approach 2: Sieve of Eratosthenes
// ===========================================
vector<int> sieveOfEratosthenes(int n) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; (long long)i * i <= n; i++) {
        if (isPrime[i]) {
            // Mark all multiples of i starting from i*i
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) primes.push_back(i);
    }
    return primes;
}

// ===========================================
// Dry Run (n = 30)
// ===========================================
/*
 * Initial: all true (2 to 30)
 *
 * i=2: mark 4,6,8,10,12,14,16,18,20,22,24,26,28,30 as false
 * i=3: mark 9,12,15,18,21,24,27,30 as false
 * i=5: mark 25 as false
 * i=6: 6*6=36 > 30, stop
 *
 * Remaining true: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
 *
 * Visualization (T=prime, F=not prime):
 * Index: 2  3  4  5  6  7  8  9  10 11 12 13 14 15
 *        T  T  F  T  F  T  F  F  F  T  F  T  F  F
 * Index: 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
 *        F  T  F  T  F  F  F  T  F  F  F  F  F  T  F
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> p10 = sieveOfEratosthenes(10);
    assert(p10 == (vector<int>{2, 3, 5, 7}));

    vector<int> p30 = sieveOfEratosthenes(30);
    assert(p30 == (vector<int>{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}));

    vector<int> p2 = sieveOfEratosthenes(2);
    assert(p2 == (vector<int>{2}));

    // Cross-check with brute force
    assert(sieveOfEratosthenes(100) == primesBrute(100));
    assert(sieveOfEratosthenes(1000) == primesBrute(1000));

    // Count primes up to 100 should be 25
    assert(sieveOfEratosthenes(100).size() == 25);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    vector<int> primes = sieveOfEratosthenes(n);
    cout << "Primes up to " << n << ": ";
    for (int p : primes) cout << p << " ";
    cout << endl;
    cout << "Count: " << primes.size() << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(n * log(log(n))) - nearly linear
 *   Space: O(n)
 *
 * Common Mistakes:
 *   - Starting inner loop from 2*i instead of i*i
 *   - Forgetting to mark 0 and 1 as non-prime
 *   - Integer overflow: i*i can overflow (use long long check)
 *
 * Interview Tips:
 *   - Most efficient way to find all primes up to n
 *   - For single prime check, use trial division
 *   - Segmented sieve for very large ranges
 *   - Prime Factorization can use smallest prime factor from sieve
 *   - Frequently asked in TCS NQT
 */
