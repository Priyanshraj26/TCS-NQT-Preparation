/*
 * Q007: GCD and LCM
 * Question: ../../../DSA-Questions/Other-Topics/Q007-gcd-lcm.md
 *
 * Approach Overview:
 * +---------------------------+-----------+---------+
 * | Approach                  | Time      | Space   |
 * +---------------------------+-----------+---------+
 * | Brute Force               | O(min(a,b))| O(1)  |
 * | Euclidean (recursive)     | O(log(min))| O(log) |
 * | Euclidean (iterative)     | O(log(min))| O(1)  |
 * +---------------------------+-----------+---------+
 */

#include <iostream>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Brute Force GCD
// ===========================================
long long gcdBrute(long long a, long long b) {
    long long result = 1;
    for (long long i = 1; i <= min(a, b); i++) {
        if (a % i == 0 && b % i == 0) {
            result = i;
        }
    }
    return result;
}

// ===========================================
// Approach 2: Euclidean Algorithm (Recursive)
// ===========================================
long long gcdRecursive(long long a, long long b) {
    if (b == 0) return a;
    return gcdRecursive(b, a % b);
}

// ===========================================
// Approach 3: Euclidean Algorithm (Iterative)
// ===========================================
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// ===========================================
// LCM using GCD
// ===========================================
long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b; // divide first to avoid overflow
}

// ===========================================
// Dry Run (a=12, b=18)
// ===========================================
/*
 * GCD(12, 18):
 *   a=12, b=18 -> a=18, b=12%18? No, swap logic:
 *   Actually: a=12, b=18
 *   Iter 1: temp=18, b=12%18=12, a=18 -> Wait, let's be precise:
 *
 *   a=12, b=18
 *   Iter 1: temp=18, b=12%18=12, a=18  -> a=18, b=12
 *   Iter 2: temp=12, b=18%12=6, a=12   -> a=12, b=6
 *   Iter 3: temp=6, b=12%6=0, a=6      -> a=6, b=0
 *   Return 6
 *
 * LCM(12, 18) = (12/6) * 18 = 2 * 18 = 36
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(gcd(12, 18) == 6);
    assert(lcm(12, 18) == 36);

    assert(gcd(7, 13) == 1);
    assert(lcm(7, 13) == 91);

    assert(gcd(20, 20) == 20);
    assert(lcm(20, 20) == 20);

    assert(gcd(1, 1000000000) == 1);
    assert(gcd(0, 5) == 5);

    // Cross-check with recursive
    assert(gcdRecursive(12, 18) == 6);
    assert(gcdRecursive(7, 13) == 1);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    long long a, b;
    cout << "Enter a and b: ";
    cin >> a >> b;
    cout << "GCD: " << gcd(a, b) << endl;
    cout << "LCM: " << lcm(a, b) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Euclidean (iterative): Time O(log(min(a,b))), Space O(1)
 *
 * Common Mistakes:
 *   - Computing LCM as a*b/gcd which can overflow; use (a/gcd)*b
 *   - Not handling a=0 or b=0 edge cases
 *
 * Interview Tips:
 *   - C++17 has __gcd() and std::gcd() in <numeric>
 *   - Euclidean algorithm is one of the oldest algorithms known
 *   - Extended Euclidean: also finds x, y such that ax + by = gcd(a,b)
 *   - Very frequently asked in TCS NQT
 */
