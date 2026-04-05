/*
 * Q004: Merge Sort Implementation
 * Question: ../../../DSA-Questions/Sorting-Searching/Q004-merge-sort.md
 *
 * Approach Overview:
 * +-----------------------+------------+--------+---------+
 * | Approach              | Best       | Worst  | Space   |
 * +-----------------------+------------+--------+---------+
 * | Merge Sort            | O(n log n) |O(n log n)| O(n)  |
 * +-----------------------+------------+--------+---------+
 * Stable: Yes | In-place: No
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Merge Function
// ===========================================
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

// ===========================================
// Merge Sort
// ===========================================
void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

void mergeSort(vector<int>& arr) {
    if (arr.empty()) return;
    mergeSort(arr, 0, arr.size() - 1);
}

// ===========================================
// Dry Run: Step-by-Step Visualization
// arr = [38, 27, 43, 3]
// ===========================================
/*
 * mergeSort([38, 27, 43, 3], 0, 3)
 *   mid = 1
 *   mergeSort([38, 27], 0, 1)
 *     mid = 0
 *     mergeSort([38], 0, 0) -> base case
 *     mergeSort([27], 1, 1) -> base case
 *     merge([38], [27]) -> [27, 38]
 *   mergeSort([43, 3], 2, 3)
 *     mid = 2
 *     mergeSort([43], 2, 2) -> base case
 *     mergeSort([3], 3, 3)  -> base case
 *     merge([43], [3]) -> [3, 43]
 *   merge([27, 38], [3, 43]):
 *     Compare 27, 3 -> pick 3   -> [3, ...]
 *     Compare 27, 43 -> pick 27 -> [3, 27, ...]
 *     Compare 38, 43 -> pick 38 -> [3, 27, 38, ...]
 *     Remaining: 43           -> [3, 27, 38, 43]
 *
 * Result: [3, 27, 38, 43]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(v1);
    assert(v1 == (vector<int>{3, 9, 10, 27, 38, 43, 82}));

    vector<int> v2 = {5, 2, 4, 7, 1, 3, 2, 6};
    mergeSort(v2);
    assert(v2 == (vector<int>{1, 2, 2, 3, 4, 5, 6, 7}));

    vector<int> v3 = {1, 2, 3};
    mergeSort(v3);
    assert(v3 == (vector<int>{1, 2, 3}));

    vector<int> v4 = {3, 2, 1};
    mergeSort(v4);
    assert(v4 == (vector<int>{1, 2, 3}));

    vector<int> v5 = {1};
    mergeSort(v5);
    assert(v5 == (vector<int>{1}));

    vector<int> v6 = {};
    mergeSort(v6);
    assert(v6.empty());

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
    mergeSort(arr);
    cout << "Sorted: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(n log n) in all cases
 *   Space: O(n) for temporary arrays
 *   Recurrence: T(n) = 2T(n/2) + O(n)
 *
 * Common Mistakes:
 *   - Not copying remaining elements after main merge loop
 *   - Wrong mid calculation (use left + (right-left)/2 to avoid overflow)
 *   - Using arr.size()-1 when arr is empty (unsigned underflow)
 *
 * Interview Tips:
 *   - Guaranteed O(n log n) -- unlike quicksort
 *   - Stable sort -- preferred when stability matters
 *   - Extra O(n) space is the main drawback
 *   - Used in external sorting (large files)
 */
