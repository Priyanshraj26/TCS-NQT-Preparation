# Solution: Next Greater Element

[← Back to Question](../../DSA-Questions/Other-Topics/Q004-next-greater-element.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Brute Force (Nested Loop) | O(n^2) | O(1) | ✗ |
| Monotonic Stack | O(n) | O(n) | ✓✓ |

---

## Approach 1: Brute Force (Nested Loop)

### Intuition
For each element, scan all elements to its right and find the first one that is greater.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n, -1);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[i]) {
                    result[i] = arr[j];
                    break;
                }
            }
        }
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {4, 5, 2, 25};
    auto res = sol.nextGreaterElement(arr);
    for (int x : res) cout << x << " ";
    cout << endl; // 5 25 25 -1
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n^2)
- **Space:** O(1) extra (excluding output)

---

## Approach 2: Monotonic Stack (Optimal)

### Intuition
Traverse the array from **right to left**. Maintain a stack of elements seen so far (in decreasing order from bottom to top). For each element:
1. Pop all stack elements smaller than or equal to the current element (they cannot be the NGE for any element to the left).
2. If the stack is not empty, the top is the next greater element.
3. Push the current element onto the stack.

The stack maintains a **monotonically decreasing** order (from bottom to top).

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n);
        stack<int> st; // stores values (not indices)

        // Traverse from right to left
        for (int i = n - 1; i >= 0; i--) {
            // Remove all elements <= current (they can't be NGE)
            while (!st.empty() && st.top() <= arr[i]) {
                st.pop();
            }

            // If stack has elements, top is the NGE
            result[i] = st.empty() ? -1 : st.top();

            // Push current element for future elements
            st.push(arr[i]);
        }
        return result;
    }
};

int main() {
    Solution sol;

    vector<int> v1 = {4, 5, 2, 25};
    auto r1 = sol.nextGreaterElement(v1);
    for (int x : r1) cout << x << " ";
    cout << endl; // 5 25 25 -1

    vector<int> v2 = {13, 7, 6, 12};
    auto r2 = sol.nextGreaterElement(v2);
    for (int x : r2) cout << x << " ";
    cout << endl; // -1 12 12 -1

    vector<int> v3 = {1, 2, 3, 4};
    auto r3 = sol.nextGreaterElement(v3);
    for (int x : r3) cout << x << " ";
    cout << endl; // 2 3 4 -1

    vector<int> v4 = {4, 3, 2, 1};
    auto r4 = sol.nextGreaterElement(v4);
    for (int x : r4) cout << x << " ";
    cout << endl; // -1 -1 -1 -1

    return 0;
}
```

### Dry Run
**Input:** [4, 5, 2, 25]

Processing right to left:

| i | arr[i] | Stack before | Pop | result[i] | Stack after |
|---|--------|-------------|-----|-----------|-------------|
| 3 | 25 | (empty) | -- | -1 | [25] |
| 2 | 2 | [25] | -- | 25 | [2, 25] |
| 1 | 5 | [2, 25] | pop 2 | 25 | [5, 25] |
| 0 | 4 | [5, 25] | -- | 5 | [4, 5, 25] |

**Output:** [5, 25, 25, -1]

**Input:** [13, 7, 6, 12]

| i | arr[i] | Stack before | Pop | result[i] | Stack after |
|---|--------|-------------|-----|-----------|-------------|
| 3 | 12 | (empty) | -- | -1 | [12] |
| 2 | 6 | [12] | -- | 12 | [6, 12] |
| 1 | 7 | [6, 12] | pop 6 | 12 | [7, 12] |
| 0 | 13 | [7, 12] | pop 7, pop 12 | -1 | [13] |

**Output:** [-1, 12, 12, -1]

### Complexity Analysis
- **Time:** O(n) -- each element is pushed and popped at most once
- **Space:** O(n) -- stack can hold all n elements

---

## Common Mistakes
1. Traversing left to right instead of right to left (requires index-based stack, more complex)
2. Using `<` instead of `<=` when popping (fails when elements are equal)
3. Forgetting that each element is pushed/popped at most once -- the total work is O(n), not O(n^2)

## Interview Tips
- The **monotonic stack** is a powerful pattern that appears in many problems
- Related problems: next smaller element, stock span, largest rectangle in histogram, trapping rain water
- Left-to-right approach works too (push indices, resolve when you find a greater element) but right-to-left is more intuitive
- Time complexity justification: amortized O(1) per element since each is pushed/popped at most once
- For TCS NQT: be ready to explain why the stack approach is O(n) despite the while loop inside the for loop
