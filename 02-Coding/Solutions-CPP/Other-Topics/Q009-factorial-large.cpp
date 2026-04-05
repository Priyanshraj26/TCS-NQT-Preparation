/*
 * Q009: Factorial of Large Numbers
 * Question: ../../../DSA-Questions/Other-Topics/Q009-factorial-large.md
 *
 * Approach Overview:
 * +-----------------------+------------+---------+
 * | Approach              | Time       | Space   |
 * +-----------------------+------------+---------+
 * | Big Integer (array)   | O(n * d)   | O(d)    |
 * | String multiplication | O(n * d)   | O(d)    |
 * +-----------------------+------------+---------+
 * d = number of digits in result
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
using namespace std;

// ===========================================
// Approach: Big Integer using Vector
// ===========================================
string factorial(int n) {
    if (n == 0 || n == 1) return "1";

    // Store result as digits in reverse order (least significant first)
    vector<int> result;
    result.push_back(1);

    for (int x = 2; x <= n; x++) {
        int carry = 0;
        for (int i = 0; i < (int)result.size(); i++) {
            int prod = result[i] * x + carry;
            result[i] = prod % 10;
            carry = prod / 10;
        }
        while (carry > 0) {
            result.push_back(carry % 10);
            carry /= 10;
        }
    }

    // Convert to string (reverse since we stored least significant first)
    string ans = "";
    for (int i = result.size() - 1; i >= 0; i--) {
        ans += to_string(result[i]);
    }
    return ans;
}

// ===========================================
// Dry Run (n = 5)
// ===========================================
/*
 * result = [1]
 *
 * x=2: [1]*2 = [2], carry=0 -> result = [2]         = "2"
 * x=3: [2]*3 = [6], carry=0 -> result = [6]         = "6"
 * x=4: [6]*4 = [4], carry=2 -> result = [4,2]       = "24"
 * x=5: [4]*5+0=20 -> result[0]=0, carry=2
 *       [2]*5+2=12 -> result[1]=2, carry=1
 *       carry=1 -> result = [0,2,1]                  = "120"
 *
 * Reverse: "120"
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    assert(factorial(0) == "1");
    assert(factorial(1) == "1");
    assert(factorial(5) == "120");
    assert(factorial(10) == "3628800");
    assert(factorial(20) == "2432902008176640000");
    assert(factorial(25) == "15511210043330985984000000");

    // Check that 100! has 158 digits
    string f100 = factorial(100);
    assert(f100.size() == 158);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << n << "! = " << factorial(n) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(n * d) where d = number of digits in result
 *   Space: O(d)
 *   Note: d for n! is approximately n*log10(n/e) + 0.5*log10(2*pi*n)
 *
 * Common Mistakes:
 *   - Forgetting to reverse the result
 *   - Not handling carry after the inner loop
 *   - Using int/long long (overflows for n > 20)
 *
 * Interview Tips:
 *   - Shows ability to handle big integers
 *   - In Python, this is trivial (built-in big integers)
 *   - In C++/Java, need manual implementation or BigInteger class
 *   - Frequently asked in TCS NQT coding round
 */
