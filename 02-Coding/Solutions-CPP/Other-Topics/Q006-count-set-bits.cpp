/*
 * Q006: Count Set Bits (Brian Kernighan's Algorithm)
 * Question: ../../../DSA-Questions/Other-Topics/Q006-count-set-bits.md
 *
 * Approach Overview:
 * +----------------------------+-----------+---------+
 * | Approach                   | Time      | Space   |
 * +----------------------------+-----------+---------+
 * | Bit-by-bit check           | O(32)     | O(1)    |
 * | Brian Kernighan            | O(k)      | O(1)    |
 * +----------------------------+-----------+---------+
 * k = number of set bits
 */

#include <iostream>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Bit-by-bit (Brute Force)
// ===========================================
int countSetBitsBrute(int n) {
    int count = 0;
    while (n > 0) {
        count += (n & 1);
        n >>= 1;
    }
    return count;
}

// ===========================================
// Approach 2: Brian Kernighan's Algorithm
// ===========================================
int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        n = n & (n - 1); // clear rightmost set bit
        count++;
    }
    return count;
}

// ===========================================
// Dry Run (n = 13 = 1101)
// ===========================================
/*
 * Iteration 1: n=1101, n-1=1100, n&(n-1)=1100, count=1
 * Iteration 2: n=1100, n-1=1011, n&(n-1)=1000, count=2
 * Iteration 3: n=1000, n-1=0111, n&(n-1)=0000, count=3
 * n=0 -> return 3
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(countSetBits(0) == 0);
    assert(countSetBits(1) == 1);
    assert(countSetBits(7) == 3);   // 111
    assert(countSetBits(13) == 3);  // 1101
    assert(countSetBits(255) == 8); // 11111111
    assert(countSetBits(1024) == 1);// 10000000000

    // Cross-check with brute force
    for (int i = 0; i <= 10000; i++) {
        assert(countSetBits(i) == countSetBitsBrute(i));
    }

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "Set bits: " << countSetBits(n) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Brian Kernighan: Time O(k) where k = number of set bits, Space O(1)
 *   Worst case k=32 for 32-bit int
 *
 * Common Mistakes:
 *   - Using n > 0 for signed negative numbers (use n != 0 or unsigned)
 *   - Confusing with counting total bits vs set bits
 *
 * Interview Tips:
 *   - C++ builtin: __builtin_popcount(n)
 *   - Brian Kernighan trick: n & (n-1) clears the lowest set bit
 *   - Applications: Hamming distance, subset enumeration
 *   - Very commonly asked in TCS NQT
 */
