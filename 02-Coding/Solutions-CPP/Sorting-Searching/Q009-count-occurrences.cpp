/*
 * Q009: Count Occurrences in Sorted Array
 * Question: ../../../DSA-Questions/Sorting-Searching/Q009-count-occurrences.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Linear Count          | O(n)      | O(1)    |
 * | Binary Search         | O(log n)  | O(1)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Linear Count (Brute Force)
// ===========================================
int countLinear(vector<int>& arr, int target) {
    int count = 0;
    for (int x : arr) {
        if (x == target) count++;
    }
    return count;
}

// ===========================================
// Approach 2: Binary Search (Optimized)
// ===========================================
int findFirst(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) { result = mid; high = mid - 1; }
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return result;
}

int findLast(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) { result = mid; low = mid + 1; }
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return result;
}

int countOccurrences(vector<int>& arr, int target) {
    int first = findFirst(arr, target);
    if (first == -1) return 0;
    int last = findLast(arr, target);
    return last - first + 1;
}

// ===========================================
// Dry Run (arr = [1,1,2,2,2,2,3], target = 2)
// ===========================================
/*
 * findFirst(2): returns 2 (first 2 at index 2)
 * findLast(2):  returns 5 (last 2 at index 5)
 * count = 5 - 2 + 1 = 4
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {1, 1, 2, 2, 2, 2, 3};
    assert(countOccurrences(v1, 2) == 4);
    assert(countOccurrences(v1, 4) == 0);
    assert(countOccurrences(v1, 1) == 2);
    assert(countOccurrences(v1, 3) == 1);

    vector<int> v2 = {8, 9, 10, 12, 12, 12};
    assert(countOccurrences(v2, 12) == 3);

    vector<int> v3 = {5};
    assert(countOccurrences(v3, 5) == 1);
    assert(countOccurrences(v3, 3) == 0);

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
    cout << "Count: " << countOccurrences(arr, target) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(log n), Space: O(1)
 *
 * Common Mistakes:
 *   - Using linear scan instead of binary search
 *   - Off-by-one: count = last - first + 1, not last - first
 *
 * Interview Tips:
 *   - Builds on Q008 (first and last position)
 *   - C++ shortcut: upper_bound - lower_bound gives count
 *   - Very commonly asked in TCS NQT
 */
