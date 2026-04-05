/*
 * Q006: Binary Search
 * Question: ../../../DSA-Questions/Sorting-Searching/Q006-binary-search.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Linear Search         | O(n)      | O(1)    |
 * | Binary Search (iter)  | O(log n)  | O(1)    |
 * | Binary Search (recur) | O(log n)  | O(log n)|
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Linear Search (Brute Force)
// ===========================================
int linearSearch(vector<int>& arr, int target) {
    for (int i = 0; i < (int)arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

// ===========================================
// Approach 2: Binary Search (Iterative)
// ===========================================
int binarySearch(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

// ===========================================
// Approach 3: Binary Search (Recursive)
// ===========================================
int binarySearchRecursive(vector<int>& arr, int target, int low, int high) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) return binarySearchRecursive(arr, target, mid + 1, high);
    return binarySearchRecursive(arr, target, low, mid - 1);
}

// ===========================================
// Dry Run (arr = [-1, 0, 3, 5, 9, 12], target = 9)
// ===========================================
/*
 * low=0, high=5
 * Iteration 1: mid=2, arr[2]=3 < 9 -> low=3
 * Iteration 2: mid=4, arr[4]=9 == 9 -> return 4
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {-1, 0, 3, 5, 9, 12};
    assert(binarySearch(v1, 9) == 4);
    assert(binarySearch(v1, 2) == -1);
    assert(binarySearch(v1, -1) == 0);
    assert(binarySearch(v1, 12) == 5);

    assert(binarySearchRecursive(v1, 9, 0, v1.size() - 1) == 4);

    vector<int> v2 = {5};
    assert(binarySearch(v2, 5) == 0);
    assert(binarySearch(v2, 3) == -1);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n, target;
    cout << "Enter n and target: ";
    cin >> n >> target;
    vector<int> arr(n);
    cout << "Enter sorted elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "Index: " << binarySearch(arr, target) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Binary Search: Time O(log n), Space O(1) iterative / O(log n) recursive
 *
 * Common Mistakes:
 *   - Using (low + high) / 2 which can overflow; use low + (high - low) / 2
 *   - Using low < high instead of low <= high (misses single element)
 *   - Not updating low/high correctly (infinite loop)
 *
 * Interview Tips:
 *   - Foundation for many problems (search in rotated array, etc.)
 *   - Always verify: what happens with 0 elements? 1 element?
 *   - Iterative is preferred (no stack overhead)
 *   - Prerequisite: array MUST be sorted
 */
