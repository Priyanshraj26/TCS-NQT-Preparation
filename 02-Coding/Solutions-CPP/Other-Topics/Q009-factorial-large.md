# Solution: Factorial of a Large Number

[← Back to Question](../../DSA-Questions/Other-Topics/Q009-factorial-large.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Using Data Types (limited) | O(n) | O(1) | ✗ (overflow) |
| Array-Based Multiplication | O(n * d) | O(d) | ✓✓ |
| String-Based | O(n * d) | O(d) | ✓ |

Where d = number of digits in the result.

---

## Approach 1: Simple Factorial (Overflows for Large n)

### Intuition
Standard loop multiplication. Works only for small values of n (up to ~20 for long long).

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    // Only works for n <= 20 (long long max ~ 9.2 * 10^18)
    long long factorialSmall(int n) {
        long long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.factorialSmall(5) << endl;  // 120
    cout << sol.factorialSmall(10) << endl; // 3628800
    cout << sol.factorialSmall(20) << endl; // 2432902008176640000
    // sol.factorialSmall(25) -> OVERFLOW!
    return 0;
}
```

---

## Approach 2: Array-Based Multiplication (Optimal for Large n)

### Intuition
Store the result as an array of digits. For each multiplication by `i`, process carry digit by digit, just like manual multiplication on paper. This handles numbers with hundreds of digits.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Multiply the number stored in result[] by x
    void multiply(vector<int>& result, int& size, int x) {
        int carry = 0;
        for (int i = 0; i < size; i++) {
            int prod = result[i] * x + carry;
            result[i] = prod % 10;  // store last digit
            carry = prod / 10;       // carry forward
        }
        // Add remaining carry digits
        while (carry > 0) {
            result[size] = carry % 10;
            carry /= 10;
            size++;
        }
    }

    string factorial(int n) {
        // Maximum digits in n! is roughly n*log10(n)
        vector<int> result(10000, 0);
        result[0] = 1;
        int size = 1;

        for (int x = 2; x <= n; x++) {
            multiply(result, size, x);
        }

        // Build result string (stored in reverse)
        string ans = "";
        for (int i = size - 1; i >= 0; i--) {
            ans += to_string(result[i]);
        }
        return ans;
    }
};

int main() {
    Solution sol;
    cout << sol.factorial(5) << endl;   // 120
    cout << sol.factorial(10) << endl;  // 3628800
    cout << sol.factorial(20) << endl;  // 2432902008176640000
    cout << sol.factorial(25) << endl;  // 15511210043330985984000000
    cout << sol.factorial(50) << endl;  // 30414093201713378043612608...
    cout << sol.factorial(100) << endl; // 93326215443944152681699238...

    return 0;
}
```

### Dry Run
**Input:** n = 5

**Initial:** result = [1], size = 1

**Multiply by 2:**

| i | result[i]*2+carry | digit | carry |
|---|-------------------|-------|-------|
| 0 | 1*2+0=2 | 2 | 0 |

result = [2], size = 1

**Multiply by 3:**

| i | result[i]*3+carry | digit | carry |
|---|-------------------|-------|-------|
| 0 | 2*3+0=6 | 6 | 0 |

result = [6], size = 1

**Multiply by 4:**

| i | result[i]*4+carry | digit | carry |
|---|-------------------|-------|-------|
| 0 | 6*4+0=24 | 4 | 2 |

carry=2 -> result[1]=2, size = 2. result = [4, 2] (represents 24)

**Multiply by 5:**

| i | result[i]*5+carry | digit | carry |
|---|-------------------|-------|-------|
| 0 | 4*5+0=20 | 0 | 2 |
| 1 | 2*5+2=12 | 2 | 1 |

carry=1 -> result[2]=1, size = 3. result = [0, 2, 1] (represents **120**)

**Output:** "120"

### Complexity Analysis
- **Time:** O(n * d) where d = number of digits in n! (approximately n * log10(n/e))
- **Space:** O(d)

---

## Approach 3: Using vector<int> (Cleaner Version)

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string factorial(int n) {
        vector<int> digits = {1}; // least significant digit first

        for (int x = 2; x <= n; x++) {
            int carry = 0;
            for (int i = 0; i < (int)digits.size(); i++) {
                int prod = digits[i] * x + carry;
                digits[i] = prod % 10;
                carry = prod / 10;
            }
            while (carry > 0) {
                digits.push_back(carry % 10);
                carry /= 10;
            }
        }

        // Reverse to get most significant digit first
        string result = "";
        for (int i = digits.size() - 1; i >= 0; i--) {
            result += to_string(digits[i]);
        }
        return result;
    }
};

int main() {
    Solution sol;
    cout << "5!  = " << sol.factorial(5) << endl;
    cout << "10! = " << sol.factorial(10) << endl;
    cout << "20! = " << sol.factorial(20) << endl;
    cout << "25! = " << sol.factorial(25) << endl;
    cout << "100! = " << sol.factorial(100) << endl;
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n * d)
- **Space:** O(d)

---

## Common Mistakes
1. Using `int` or `long long` for large factorials (overflows beyond 12! for int, 20! for long long)
2. Forgetting to process the remaining carry after the digit loop
3. Printing digits in the wrong order (they are stored least-significant-first)
4. Not allocating enough space for the result array

## Interview Tips
- This tests your ability to simulate multiplication manually, like grade-school arithmetic
- n! has approximately `n * log10(n/e) + 0.5 * log10(2*pi*n)` digits (Stirling's approximation)
- 100! has 158 digits, 1000! has 2568 digits
- In Python/Java, this is trivial due to big integers, but C++ requires manual implementation
- Alternative: use base-10000 instead of base-10 for each array element (4x fewer operations)
- TCS NQT: this is a classic question that tests both math and implementation skills
