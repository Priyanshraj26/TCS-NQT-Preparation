/*
 * Q004: Next Greater Element
 * Question: ../../../DSA-Questions/Other-Topics/Q004-next-greater-element.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Brute Force (nested)  | O(n^2)    | O(1)    |
 * | Stack (monotonic)     | O(n)      | O(n)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <vector>
#include <stack>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Brute Force
// ===========================================
vector<int> ngeBrute(vector<int>& arr) {
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

// ===========================================
// Approach 2: Monotonic Stack (Right to Left)
// ===========================================
vector<int> ngeStack(vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n);
    stack<int> st; // stores elements, not indices

    for (int i = n - 1; i >= 0; i--) {
        // Pop elements smaller than or equal to current
        while (!st.empty() && st.top() <= arr[i]) {
            st.pop();
        }
        result[i] = st.empty() ? -1 : st.top();
        st.push(arr[i]);
    }
    return result;
}

// ===========================================
// Dry Run (arr = [4, 5, 2, 25])
// ===========================================
/*
 * Traverse right to left:
 * i=3 (25): stack=[], result[3]=-1, push 25. stack=[25]
 * i=2 (2):  stack=[25], 25>2 -> result[2]=25, push 2. stack=[25,2]
 * i=1 (5):  pop 2 (2<=5), stack=[25], 25>5 -> result[1]=25, push 5. stack=[25,5]
 * i=0 (4):  stack=[25,5], 5>4 -> result[0]=5, push 4. stack=[25,5,4]
 *
 * Result: [5, 25, 25, -1]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {4, 5, 2, 25};
    assert(ngeStack(v1) == (vector<int>{5, 25, 25, -1}));
    assert(ngeBrute(v1) == (vector<int>{5, 25, 25, -1}));

    vector<int> v2 = {13, 7, 6, 12};
    assert(ngeStack(v2) == (vector<int>{-1, 12, 12, -1}));

    vector<int> v3 = {1, 2, 3, 4};
    assert(ngeStack(v3) == (vector<int>{2, 3, 4, -1}));

    vector<int> v4 = {4, 3, 2, 1};
    assert(ngeStack(v4) == (vector<int>{-1, -1, -1, -1}));

    vector<int> v5 = {5};
    assert(ngeStack(v5) == (vector<int>{-1}));

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n;
    cout << "Enter n: ";
    cin >> n;
    vector<int> arr(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = ngeStack(arr);
    cout << "NGE: ";
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Stack approach: Time O(n), Space O(n)
 *   Each element is pushed and popped at most once.
 *
 * Common Mistakes:
 *   - Using < instead of <= in while condition (duplicates)
 *   - Traversing left to right instead of right to left
 *
 * Interview Tips:
 *   - Monotonic stack is the key pattern here
 *   - Variations: Next Smaller Element, Previous Greater Element
 *   - Circular variant: traverse array twice (2n iterations)
 *   - Stock span problem uses same pattern
 */
