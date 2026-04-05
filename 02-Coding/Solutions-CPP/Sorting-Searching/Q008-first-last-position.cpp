/*
 * Q008: First and Last Position of Element in Sorted Array
 * Question: ../../../DSA-Questions/Sorting-Searching/Q008-first-last-position.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Linear Scan           | O(n)      | O(1)    |
 * | Two Binary Searches   | O(log n)  | O(1)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Find First Occurrence
// ===========================================
int findFirst(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            result = mid;
            high = mid - 1; // keep searching left
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
}

// ===========================================
// Find Last Occurrence
// ===========================================
int findLast(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            result = mid;
            low = mid + 1; // keep searching right
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
}

// ===========================================
// Combined Solution
// ===========================================
pair<int, int> searchRange(vector<int>& arr, int target) {
    return {findFirst(arr, target), findLast(arr, target)};
}

// ===========================================
// Dry Run (arr = [5,7,7,8,8,10], target = 8)
// ===========================================
/*
 * findFirst(target=8):
 *   low=0, high=5, mid=2, arr[2]=7 < 8 -> low=3
 *   low=3, high=5, mid=4, arr[4]=8 == 8 -> result=4, high=3
 *   low=3, high=3, mid=3, arr[3]=8 == 8 -> result=3, high=2
 *   low=3 > high=2 -> return 3
 *
 * findLast(target=8):
 *   low=0, high=5, mid=2, arr[2]=7 < 8 -> low=3
 *   low=3, high=5, mid=4, arr[4]=8 == 8 -> result=4, low=5
 *   low=5, high=5, mid=5, arr[5]=10 > 8 -> high=4
 *   low=5 > high=4 -> return 4
 *
 * Answer: [3, 4]
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {5, 7, 7, 8, 8, 10};
    assert(searchRange(v1, 8) == make_pair(3, 4));
    assert(searchRange(v1, 6) == make_pair(-1, -1));
    assert(searchRange(v1, 7) == make_pair(1, 2));
    assert(searchRange(v1, 5) == make_pair(0, 0));
    assert(searchRange(v1, 10) == make_pair(5, 5));

    vector<int> v2 = {};
    assert(searchRange(v2, 0) == make_pair(-1, -1));

    vector<int> v3 = {1, 1, 1, 1, 1};
    assert(searchRange(v3, 1) == make_pair(0, 4));

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
    auto [first, last] = searchRange(arr, target);
    cout << "First: " << first << ", Last: " << last << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(log n) - two binary searches
 *   Space: O(1)
 *
 * Common Mistakes:
 *   - Stopping at first match instead of continuing to search
 *   - Using one binary search and linear scan (degrades to O(n))
 *
 * Interview Tips:
 *   - This is a template for "lower_bound" and "upper_bound"
 *   - C++ STL: lower_bound() and upper_bound() do exactly this
 *   - Can also use: count = last - first + 1
 */
