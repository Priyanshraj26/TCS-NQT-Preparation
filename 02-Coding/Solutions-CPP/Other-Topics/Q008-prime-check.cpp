/*
 * Q008: Check if Number is Prime
 * Question: ../../../DSA-Questions/Other-Topics/Q008-prime-check.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Brute Force (1 to n)  | O(n)      | O(1)    |
 * | Check up to sqrt(n)   | O(sqrt(n))| O(1)    |
 * | Optimized (6k +/- 1)  | O(sqrt(n))| O(1)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <cmath>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Brute Force
// ===========================================
bool isPrimeBrute(int n) {
    if (n <= 1) return false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// ===========================================
// Approach 2: Check up to sqrt(n)
// ===========================================
bool isPrimeSqrt(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0) return false;

    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// ===========================================
// Approach 3: Optimized (6k +/- 1)
// ===========================================
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    // All primes > 3 are of the form 6k +/- 1
    for (int i = 5; (long long)i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

// ===========================================
// Dry Run (n = 29)
// ===========================================
/*
 * 29 > 3: OK
 * 29 % 2 = 1: not even
 * 29 % 3 = 2: not divisible by 3
 * i=5: 5*5=25 <= 29, 29%5=4, 29%7=1 -> continue
 * i=11: 11*11=121 > 29 -> stop
 * Return true (29 is prime)
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(isPrime(1) == false);
    assert(isPrime(2) == true);
    assert(isPrime(3) == true);
    assert(isPrime(4) == false);
    assert(isPrime(7) == true);
    assert(isPrime(10) == false);
    assert(isPrime(29) == true);
    assert(isPrime(97) == true);
    assert(isPrime(100) == false);
    assert(isPrime(999999937) == true); // large prime

    // Cross-check
    for (int i = 1; i <= 1000; i++) {
        assert(isPrime(i) == isPrimeBrute(i));
    }

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << (isPrime(n) ? "YES" : "NO") << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Optimized: Time O(sqrt(n)), Space O(1)
 *   6k+/-1 optimization reduces checks by ~3x vs checking all odds
 *
 * Common Mistakes:
 *   - Forgetting that 1 is NOT prime
 *   - Forgetting that 2 IS prime (only even prime)
 *   - Using i*i which can overflow for large n (use long long)
 *   - Checking up to n instead of sqrt(n)
 *
 * Interview Tips:
 *   - sqrt(n) check is a must-know optimization
 *   - For multiple queries, use Sieve of Eratosthenes
 *   - 6k+/-1 optimization shows deeper understanding
 *   - Very frequently asked in TCS NQT
 */
