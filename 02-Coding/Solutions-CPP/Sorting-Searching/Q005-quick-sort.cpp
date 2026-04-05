/*
 * Q005: Quick Sort Implementation
 * Question: ../../../DSA-Questions/Sorting-Searching/Q005-quick-sort.md
 *
 * Approach Overview:
 * +-----------------------+------------+-----------+---------+
 * | Approach              | Best       | Worst     | Space   |
 * +-----------------------+------------+-----------+---------+
 * | Quick Sort (Lomuto)   | O(n log n) | O(n^2)    | O(log n)|
 * +-----------------------+------------+-----------+---------+
 * Stable: No | In-place: Yes
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Lomuto Partition Scheme
// ===========================================
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high]; // pivot is last element
    int i = low - 1;       // index of smaller element boundary

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// ===========================================
// Quick Sort
// ===========================================
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void quickSort(vector<int>& arr) {
    if (arr.empty()) return;
    quickSort(arr, 0, arr.size() - 1);
}

// ===========================================
// Dry Run: Step-by-Step Visualization
// arr = [10, 80, 30, 90, 40, 50, 70]
// ===========================================
/*
 * partition(arr, 0, 6), pivot = 70
 *   i = -1
 *   j=0: 10 <= 70 -> i=0, swap(arr[0],arr[0]) -> [10, 80, 30, 90, 40, 50, 70]
 *   j=1: 80 <= 70? No
 *   j=2: 30 <= 70 -> i=1, swap(arr[1],arr[2]) -> [10, 30, 80, 90, 40, 50, 70]
 *   j=3: 90 <= 70? No
 *   j=4: 40 <= 70 -> i=2, swap(arr[2],arr[4]) -> [10, 30, 40, 90, 80, 50, 70]
 *   j=5: 50 <= 70 -> i=3, swap(arr[3],arr[5]) -> [10, 30, 40, 50, 80, 90, 70]
 *   swap(arr[4], arr[6]) -> [10, 30, 40, 50, 70, 90, 80]
 *   Pivot 70 is at index 4
 *
 * Left:  quickSort([10, 30, 40, 50], 0, 3)
 * Right: quickSort([90, 80], 5, 6)
 *   ... continues recursively until sorted
 *
 * Result: [10, 30, 40, 50, 70, 80, 90]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {10, 80, 30, 90, 40, 50, 70};
    quickSort(v1);
    assert(v1 == (vector<int>{10, 30, 40, 50, 70, 80, 90}));

    vector<int> v2 = {10, 7, 8, 9, 1, 5};
    quickSort(v2);
    assert(v2 == (vector<int>{1, 5, 7, 8, 9, 10}));

    vector<int> v3 = {1, 2, 3, 4, 5};
    quickSort(v3);
    assert(v3 == (vector<int>{1, 2, 3, 4, 5}));

    vector<int> v4 = {5, 4, 3, 2, 1};
    quickSort(v4);
    assert(v4 == (vector<int>{1, 2, 3, 4, 5}));

    vector<int> v5 = {1};
    quickSort(v5);
    assert(v5 == (vector<int>{1}));

    vector<int> v6 = {3, 3, 3};
    quickSort(v6);
    assert(v6 == (vector<int>{3, 3, 3}));

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
    quickSort(arr);
    cout << "Sorted: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Best/Average: O(n log n)
 *   Worst: O(n^2) - when already sorted and pivot is last element
 *   Space: O(log n) recursion stack (average), O(n) worst case
 *
 * Common Mistakes:
 *   - Wrong partition logic (i should start at low-1)
 *   - Not placing pivot in correct position after partition
 *   - Stack overflow on sorted input (use randomized pivot)
 *
 * Interview Tips:
 *   - Fastest in practice for most inputs (cache-friendly)
 *   - Use randomized pivot to avoid O(n^2) worst case
 *   - NOT stable (merge sort is preferred when stability needed)
 *   - In-place (unlike merge sort) -- O(log n) stack space
 *   - Know both Lomuto and Hoare partition schemes
 */
