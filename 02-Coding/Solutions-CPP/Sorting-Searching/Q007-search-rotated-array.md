# Solution: Search in Rotated Sorted Array

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q007-search-rotated-array.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Linear Search | O(n) | O(1) | ✗ |
| Modified Binary Search | O(log n) | O(1) | ✓✓ |

---

## Approach 1: Linear Search (Brute Force)

### Intuition
Simply scan all elements.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& arr, int target) {
        for (int i = 0; i < (int)arr.size(); i++)
            if (arr[i] == target) return i;
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {4, 5, 6, 7, 0, 1, 2};
    cout << sol.search(arr, 0) << endl; // 4
    cout << sol.search(arr, 3) << endl; // -1
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Approach 2: Modified Binary Search (Optimal)

### Intuition
In a rotated sorted array, at least one half (left or right of mid) is always sorted. Determine which half is sorted, then check if the target lies in that sorted half. If yes, search that half; otherwise, search the other half.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) return mid;

            // Left half is sorted
            if (arr[low] <= arr[mid]) {
                // Target is in the sorted left half
                if (arr[low] <= target && target < arr[mid])
                    high = mid - 1;
                else
                    low = mid + 1;
            }
            // Right half is sorted
            else {
                // Target is in the sorted right half
                if (arr[mid] < target && target <= arr[high])
                    low = mid + 1;
                else
                    high = mid - 1;
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;

    vector<int> v1 = {4, 5, 6, 7, 0, 1, 2};
    cout << sol.search(v1, 0) << endl;  // 4
    cout << sol.search(v1, 3) << endl;  // -1
    cout << sol.search(v1, 5) << endl;  // 1

    vector<int> v2 = {1};
    cout << sol.search(v2, 1) << endl;  // 0
    cout << sol.search(v2, 0) << endl;  // -1

    vector<int> v3 = {3, 1};
    cout << sol.search(v3, 1) << endl;  // 1

    // Not rotated (rotation by 0)
    vector<int> v4 = {1, 2, 3, 4, 5};
    cout << sol.search(v4, 3) << endl;  // 2

    return 0;
}
```

### Dry Run
**Input:** arr = [4, 5, 6, 7, 0, 1, 2], target = 0

| Step | low | high | mid | arr[mid] | Sorted half | target in sorted? | Action |
|------|-----|------|-----|----------|-------------|-------------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left [4,5,6,7] | 4<=0<7? No | low=4 |
| 2 | 4 | 6 | 5 | 1 | Right [1,2] | 1<0<=2? No | high=4 |
| 3 | 4 | 4 | 4 | 0 | Found! | -- | return 4 |

**Output:** 4

**Input:** arr = [4, 5, 6, 7, 0, 1, 2], target = 5

| Step | low | high | mid | arr[mid] | Sorted half | target in sorted? | Action |
|------|-----|------|-----|----------|-------------|-------------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left [4,5,6,7] | 4<=5<7? Yes | high=2 |
| 2 | 0 | 2 | 1 | 5 | Found! | -- | return 1 |

### Complexity Analysis
- **Time:** O(log n) -- standard binary search with modified conditions
- **Space:** O(1)

---

## Common Mistakes
1. Using `arr[low] < arr[mid]` instead of `arr[low] <= arr[mid]` (fails when low == mid)
2. Wrong boundary checks: must use `<=` and `<` correctly to include/exclude endpoints
3. Not handling the case when the array is not actually rotated
4. Confusing with the "find pivot" approach (this single-pass approach is cleaner)

## Interview Tips
- The key insight: **one half is always sorted** in a rotated sorted array
- This is one of the most popular binary search variations in interviews
- Follow-up: what if duplicates are allowed? Worst case becomes O(n) because you cannot distinguish halves when arr[low]==arr[mid]==arr[high]
- Follow-up: find the minimum element in rotated sorted array
- For TCS NQT, be prepared to trace through the algorithm step by step
