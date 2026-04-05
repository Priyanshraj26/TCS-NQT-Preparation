/*
 * Q001: Bubble Sort Implementation
 * Question: ../../../DSA-Questions/Sorting-Searching/Q001-bubble-sort.md
 *
 * Approach Overview:
 * +-----------------------+----------+--------+---------+
 * | Approach              | Best     | Worst  | Space   |
 * +-----------------------+----------+--------+---------+
 * | Basic Bubble Sort     | O(n^2)   | O(n^2) | O(1)    |
 * | Optimized (early stop)| O(n)     | O(n^2) | O(1)    |
 * +-----------------------+----------+--------+---------+
 * Stable: Yes | In-place: Yes
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Basic Bubble Sort (Brute Force)
// ===========================================
void bubbleSortBasic(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// ===========================================
// Approach 2: Optimized Bubble Sort
// ===========================================
void bubbleSortOptimized(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break; // Array is already sorted
    }
}

// ===========================================
// Dry Run: Step-by-Step Visualization
// arr = [5, 1, 4, 2, 8]
// ===========================================
/*
 * Pass 1 (i=0):
 *   [5, 1, 4, 2, 8] -> compare 5,1 -> swap -> [1, 5, 4, 2, 8]
 *   [1, 5, 4, 2, 8] -> compare 5,4 -> swap -> [1, 4, 5, 2, 8]
 *   [1, 4, 5, 2, 8] -> compare 5,2 -> swap -> [1, 4, 2, 5, 8]
 *   [1, 4, 2, 5, 8] -> compare 5,8 -> no swap
 *   After pass 1: [1, 4, 2, 5, 8]  (8 is in place)
 *
 * Pass 2 (i=1):
 *   [1, 4, 2, 5, 8] -> compare 1,4 -> no swap
 *   [1, 4, 2, 5, 8] -> compare 4,2 -> swap -> [1, 2, 4, 5, 8]
 *   [1, 2, 4, 5, 8] -> compare 4,5 -> no swap
 *   After pass 2: [1, 2, 4, 5, 8]  (5 is in place)
 *
 * Pass 3 (i=2):
 *   No swaps -> swapped = false -> BREAK (early termination)
 *
 * Result: [1, 2, 4, 5, 8]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {64, 34, 25, 12, 22, 11, 90};
    bubbleSortOptimized(v1);
    assert(v1 == (vector<int>{11, 12, 22, 25, 34, 64, 90}));

    vector<int> v2 = {5, 1, 4, 2, 8};
    bubbleSortOptimized(v2);
    assert(v2 == (vector<int>{1, 2, 4, 5, 8}));

    vector<int> v3 = {1, 2, 3, 4, 5}; // already sorted
    bubbleSortOptimized(v3);
    assert(v3 == (vector<int>{1, 2, 3, 4, 5}));

    vector<int> v4 = {5, 4, 3, 2, 1}; // reverse sorted
    bubbleSortOptimized(v4);
    assert(v4 == (vector<int>{1, 2, 3, 4, 5}));

    vector<int> v5 = {1};
    bubbleSortOptimized(v5);
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
    bubbleSortOptimized(arr);
    cout << "Sorted: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Best Case: O(n) - already sorted, one pass with no swaps
 *   Worst Case: O(n^2) - reverse sorted
 *   Space: O(1) - in-place
 *
 * Common Mistakes:
 *   - Inner loop going up to n-1 instead of n-1-i
 *   - Forgetting the optimization (early break when no swaps)
 *
 * Interview Tips:
 *   - Simplest sorting algorithm to implement
 *   - Stable sort (preserves relative order of equal elements)
 *   - Mention it is adaptive with the swapped flag optimization
 *   - Not practical for large datasets
 */
