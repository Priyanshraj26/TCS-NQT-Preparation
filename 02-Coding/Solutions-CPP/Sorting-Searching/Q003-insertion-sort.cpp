/*
 * Q003: Insertion Sort Implementation
 * Question: ../../../DSA-Questions/Sorting-Searching/Q003-insertion-sort.md
 *
 * Approach Overview:
 * +-----------------------+----------+--------+---------+
 * | Approach              | Best     | Worst  | Space   |
 * +-----------------------+----------+--------+---------+
 * | Insertion Sort        | O(n)     | O(n^2) | O(1)    |
 * +-----------------------+----------+--------+---------+
 * Stable: Yes | In-place: Yes | Adaptive: Yes
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Insertion Sort
// ===========================================
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        // Shift elements greater than key to the right
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// ===========================================
// Dry Run: Step-by-Step Visualization
// arr = [12, 11, 13, 5, 6]
// ===========================================
/*
 * Initial: [12, 11, 13, 5, 6]
 *
 * i=1, key=11:
 *   Compare 12 > 11 -> shift 12 right: [12, 12, 13, 5, 6]
 *   Insert 11 at position 0: [11, 12, 13, 5, 6]
 *   Sorted part: [11, 12 | 13, 5, 6]
 *
 * i=2, key=13:
 *   Compare 12 > 13? No -> stop
 *   Insert 13 at position 2: [11, 12, 13, 5, 6]
 *   Sorted part: [11, 12, 13 | 5, 6]
 *
 * i=3, key=5:
 *   Compare 13 > 5 -> shift: [11, 12, 13, 13, 6]
 *   Compare 12 > 5 -> shift: [11, 12, 12, 13, 6]
 *   Compare 11 > 5 -> shift: [11, 11, 12, 13, 6]
 *   Insert 5 at position 0: [5, 11, 12, 13, 6]
 *   Sorted part: [5, 11, 12, 13 | 6]
 *
 * i=4, key=6:
 *   Compare 13 > 6 -> shift: [5, 11, 12, 13, 13]
 *   Compare 12 > 6 -> shift: [5, 11, 12, 12, 13]
 *   Compare 11 > 6 -> shift: [5, 11, 11, 12, 13]
 *   Compare 5 > 6? No -> stop
 *   Insert 6 at position 1: [5, 6, 11, 12, 13]
 *
 * Result: [5, 6, 11, 12, 13]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {12, 11, 13, 5, 6};
    insertionSort(v1);
    assert(v1 == (vector<int>{5, 6, 11, 12, 13}));

    vector<int> v2 = {4, 3, 2, 10, 12, 1, 5, 6};
    insertionSort(v2);
    assert(v2 == (vector<int>{1, 2, 3, 4, 5, 6, 10, 12}));

    vector<int> v3 = {1, 2, 3, 4, 5}; // already sorted
    insertionSort(v3);
    assert(v3 == (vector<int>{1, 2, 3, 4, 5}));

    vector<int> v4 = {5, 4, 3, 2, 1}; // reverse
    insertionSort(v4);
    assert(v4 == (vector<int>{1, 2, 3, 4, 5}));

    vector<int> v5 = {1};
    insertionSort(v5);
    assert(v5 == (vector<int>{1}));

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
    insertionSort(arr);
    cout << "Sorted: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Best Case: O(n) - already sorted (inner while never executes)
 *   Worst Case: O(n^2) - reverse sorted
 *   Space: O(1) - in-place
 *
 * Common Mistakes:
 *   - Starting outer loop from 0 instead of 1
 *   - Not saving key before shifting
 *   - Off-by-one in placement: arr[j+1] = key, not arr[j] = key
 *
 * Interview Tips:
 *   - Best for small arrays or nearly sorted data
 *   - Used as base case in hybrid sorts (TimSort, IntroSort)
 *   - Stable and adaptive
 *   - Online algorithm (can sort as data arrives)
 */
