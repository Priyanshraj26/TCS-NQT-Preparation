/*
 * Q002: Selection Sort Implementation
 * Question: ../../../DSA-Questions/Sorting-Searching/Q002-selection-sort.md
 *
 * Approach Overview:
 * +-----------------------+----------+--------+---------+
 * | Approach              | Best     | Worst  | Space   |
 * +-----------------------+----------+--------+---------+
 * | Selection Sort        | O(n^2)   | O(n^2) | O(1)    |
 * +-----------------------+----------+--------+---------+
 * Stable: No | In-place: Yes
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Selection Sort
// ===========================================
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
        }
    }
}

// ===========================================
// Dry Run: Step-by-Step Visualization
// arr = [64, 25, 12, 22, 11]
// ===========================================
/*
 * Pass 1 (i=0): Find min in [64, 25, 12, 22, 11] -> min=11 at idx 4
 *   Swap arr[0] and arr[4]: [11, 25, 12, 22, 64]
 *   Sorted: [11 | 25, 12, 22, 64]
 *
 * Pass 2 (i=1): Find min in [25, 12, 22, 64] -> min=12 at idx 2
 *   Swap arr[1] and arr[2]: [11, 12, 25, 22, 64]
 *   Sorted: [11, 12 | 25, 22, 64]
 *
 * Pass 3 (i=2): Find min in [25, 22, 64] -> min=22 at idx 3
 *   Swap arr[2] and arr[3]: [11, 12, 22, 25, 64]
 *   Sorted: [11, 12, 22 | 25, 64]
 *
 * Pass 4 (i=3): Find min in [25, 64] -> min=25 at idx 3
 *   No swap needed.
 *   Sorted: [11, 12, 22, 25 | 64]
 *
 * Result: [11, 12, 22, 25, 64]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {64, 25, 12, 22, 11};
    selectionSort(v1);
    assert(v1 == (vector<int>{11, 12, 22, 25, 64}));

    vector<int> v2 = {29, 10, 14, 37, 13};
    selectionSort(v2);
    assert(v2 == (vector<int>{10, 13, 14, 29, 37}));

    vector<int> v3 = {1, 2, 3};
    selectionSort(v3);
    assert(v3 == (vector<int>{1, 2, 3}));

    vector<int> v4 = {3, 2, 1};
    selectionSort(v4);
    assert(v4 == (vector<int>{1, 2, 3}));

    vector<int> v5 = {1};
    selectionSort(v5);
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
    selectionSort(arr);
    cout << "Sorted: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(n^2) always (no best case optimization)
 *   Space: O(1) - in-place
 *   Comparisons: n*(n-1)/2 always
 *   Swaps: O(n) - at most n-1 swaps (advantage over bubble sort)
 *
 * Common Mistakes:
 *   - Using j = i instead of j = i + 1 in inner loop
 *   - Swapping inside inner loop instead of after finding minimum
 *
 * Interview Tips:
 *   - Minimizes number of swaps (useful when writes are expensive)
 *   - NOT stable (can make stable with linked list)
 *   - Always O(n^2) -- no early termination
 */
