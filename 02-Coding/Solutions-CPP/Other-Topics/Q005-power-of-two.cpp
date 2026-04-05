/*
 * Q005: Check if Number is Power of 2
 * Question: ../../../DSA-Questions/Other-Topics/Q005-power-of-two.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Loop (divide by 2)    | O(log n)  | O(1)    |
 * | Bit Manipulation      | O(1)      | O(1)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Loop (Brute Force)
// ===========================================
bool isPowerOfTwoLoop(int n) {
    if (n <= 0) return false;
    while (n > 1) {
        if (n % 2 != 0) return false;
        n /= 2;
    }
    return true;
}

// ===========================================
// Approach 2: Bit Manipulation (Optimal)
// ===========================================
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

// ===========================================
// Dry Run
// ===========================================
/*
 * n = 16 = 10000 (binary)
 * n-1 = 15 = 01111
 * n & (n-1) = 10000 & 01111 = 00000 = 0
 * -> Power of 2: YES
 *
 * n = 12 = 1100
 * n-1 = 11 = 1011
 * n & (n-1) = 1100 & 1011 = 1000 = 8 != 0
 * -> Power of 2: NO
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(isPowerOfTwo(1) == true);   // 2^0
    assert(isPowerOfTwo(2) == true);   // 2^1
    assert(isPowerOfTwo(4) == true);   // 2^2
    assert(isPowerOfTwo(16) == true);  // 2^4
    assert(isPowerOfTwo(1024) == true);// 2^10
    assert(isPowerOfTwo(3) == false);
    assert(isPowerOfTwo(6) == false);
    assert(isPowerOfTwo(12) == false);
    assert(isPowerOfTwo(0) == false);

    // Cross-check with loop
    for (int i = 1; i <= 10000; i++) {
        assert(isPowerOfTwo(i) == isPowerOfTwoLoop(i));
    }

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << (isPowerOfTwo(n) ? "YES" : "NO") << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Bit Manipulation: Time O(1), Space O(1)
 *
 * Common Mistakes:
 *   - Not checking n > 0 (0 is not a power of 2)
 *   - Using n & (n-1) without understanding it clears lowest set bit
 *
 * Interview Tips:
 *   - n & (n-1) is a must-know bit trick
 *   - Alternative: __builtin_popcount(n) == 1
 *   - Related: check if power of 4, power of 8, etc.
 */
