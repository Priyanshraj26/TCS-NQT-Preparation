/*
 * Q010: Square Root using Binary Search
 * Question: ../../../DSA-Questions/Sorting-Searching/Q010-square-root.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Brute Force           | O(sqrt(x))| O(1)    |
 * | Binary Search         | O(log x)  | O(1)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Brute Force
// ===========================================
int sqrtBrute(int x) {
    if (x == 0) return 0;
    long long i = 1;
    while (i * i <= x) i++;
    return (int)(i - 1);
}

// ===========================================
// Approach 2: Binary Search (Optimized)
// ===========================================
int mySqrt(int x) {
    if (x == 0) return 0;
    long long low = 1, high = x, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (mid * mid == x) {
            return (int)mid;
        } else if (mid * mid < x) {
            ans = mid;       // mid might be the answer
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return (int)ans;
}

// ===========================================
// Dry Run (x = 8)
// ===========================================
/*
 * low=1, high=8
 * Iter 1: mid=4, 4*4=16 > 8 -> high=3
 * Iter 2: mid=2, 2*2=4 < 8 -> ans=2, low=3
 * Iter 3: mid=3, 3*3=9 > 8 -> high=2
 * low=3 > high=2 -> return ans=2
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(mySqrt(0) == 0);
    assert(mySqrt(1) == 1);
    assert(mySqrt(4) == 2);
    assert(mySqrt(8) == 2);
    assert(mySqrt(9) == 3);
    assert(mySqrt(15) == 3);
    assert(mySqrt(16) == 4);
    assert(mySqrt(100) == 10);
    assert(mySqrt(2147395599) == 46339); // large input test

    // Cross-check with brute force
    for (int i = 0; i <= 1000; i++) {
        assert(mySqrt(i) == sqrtBrute(i));
    }

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int x;
    cout << "Enter x: ";
    cin >> x;
    cout << "sqrt(" << x << ") = " << mySqrt(x) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(log x), Space: O(1)
 *
 * Common Mistakes:
 *   - Integer overflow: mid*mid can overflow int (use long long)
 *   - Not handling x=0 separately
 *   - Returning mid instead of ans when mid*mid < x
 *
 * Interview Tips:
 *   - Classic binary search on answer space
 *   - Same pattern: find nth root, find minimum speed, etc.
 *   - Newton's method is O(log x) too but harder to implement
 */
