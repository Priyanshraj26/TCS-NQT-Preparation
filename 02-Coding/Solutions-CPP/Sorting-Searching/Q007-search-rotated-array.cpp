/*
 * Q007: Search in Rotated Sorted Array
 * Question: ../../../DSA-Questions/Sorting-Searching/Q007-search-rotated-array.md
 *
 * Approach Overview:
 * +-----------------------+-----------+---------+
 * | Approach              | Time      | Space   |
 * +-----------------------+-----------+---------+
 * | Linear Search         | O(n)      | O(1)    |
 * | Modified Binary Search| O(log n)  | O(1)    |
 * +-----------------------+-----------+---------+
 */

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// ===========================================
// Approach 1: Linear Search (Brute Force)
// ===========================================
int searchLinear(vector<int>& nums, int target) {
    for (int i = 0; i < (int)nums.size(); i++) {
        if (nums[i] == target) return i;
    }
    return -1;
}

// ===========================================
// Approach 2: Modified Binary Search
// ===========================================
int searchRotated(vector<int>& nums, int target) {
    int low = 0, high = nums.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (nums[mid] == target) return mid;

        // Left half is sorted
        if (nums[low] <= nums[mid]) {
            if (target >= nums[low] && target < nums[mid]) {
                high = mid - 1; // target is in sorted left half
            } else {
                low = mid + 1;  // target is in right half
            }
        }
        // Right half is sorted
        else {
            if (target > nums[mid] && target <= nums[high]) {
                low = mid + 1;  // target is in sorted right half
            } else {
                high = mid - 1; // target is in left half
            }
        }
    }
    return -1;
}

// ===========================================
// Dry Run (arr = [4,5,6,7,0,1,2], target = 0)
// ===========================================
/*
 * low=0, high=6
 *
 * Iter 1: mid=3, nums[3]=7 != 0
 *   Left sorted (nums[0]=4 <= nums[3]=7)
 *   target=0 in [4,7)? No -> low=4
 *
 * Iter 2: low=4, high=6, mid=5, nums[5]=1 != 0
 *   Left sorted? nums[4]=0 <= nums[5]=1 -> Yes
 *   target=0 in [0,1)? Yes -> high=4
 *
 * Iter 3: low=4, high=4, mid=4, nums[4]=0 == 0 -> return 4
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    vector<int> v1 = {4, 5, 6, 7, 0, 1, 2};
    assert(searchRotated(v1, 0) == 4);
    assert(searchRotated(v1, 3) == -1);
    assert(searchRotated(v1, 4) == 0);
    assert(searchRotated(v1, 2) == 6);

    vector<int> v2 = {1};
    assert(searchRotated(v2, 0) == -1);
    assert(searchRotated(v2, 1) == 0);

    vector<int> v3 = {3, 1};
    assert(searchRotated(v3, 1) == 1);
    assert(searchRotated(v3, 3) == 0);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    int n, target;
    cout << "Enter n and target: ";
    cin >> n >> target;
    vector<int> arr(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "Index: " << searchRotated(arr, target) << endl;
    return 0;
}

/*
 * Complexity Analysis:
 *   Time: O(log n), Space: O(1)
 *
 * Common Mistakes:
 *   - Using < instead of <= in nums[low] <= nums[mid]
 *   - Not handling edge cases (single element, two elements)
 *   - Getting confused with which half is sorted
 *
 * Interview Tips:
 *   - Key insight: at least one half is always sorted
 *   - Check if target is in the sorted half; if yes, go there; else go other side
 *   - Variation: with duplicates, worst case becomes O(n)
 */
