# Solution: Binary Search

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q006-binary-search.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Linear Search | O(n) | O(1) | ✗ |
| Binary Search (Iterative) | O(log n) | O(1) | ✓✓ |
| Binary Search (Recursive) | O(log n) | O(log n) | ✓ |

---

## Approach 1: Linear Search (Brute Force)

### Intuition
Scan every element from left to right until the target is found.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int linearSearch(vector<int>& arr, int target) {
        for (int i = 0; i < (int)arr.size(); i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {2, 3, 4, 10, 40};
    cout << sol.linearSearch(arr, 10) << endl; // 3
    cout << sol.linearSearch(arr, 5) << endl;  // -1
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Approach 2: Binary Search (Iterative)

### Intuition
For a sorted array, compare the target with the middle element. If equal, return the index. If target is smaller, search the left half. If larger, search the right half. Repeat until found or the search space is empty.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int binarySearch(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2; // prevents overflow

            if (arr[mid] == target)
                return mid;
            else if (arr[mid] < target)
                low = mid + 1;  // search right half
            else
                high = mid - 1; // search left half
        }
        return -1; // not found
    }
};

int main() {
    Solution sol;
    vector<int> arr = {2, 3, 4, 10, 40};
    cout << sol.binarySearch(arr, 10) << endl; // 3
    cout << sol.binarySearch(arr, 40) << endl; // 4
    cout << sol.binarySearch(arr, 2) << endl;  // 0
    cout << sol.binarySearch(arr, 5) << endl;  // -1

    vector<int> arr2 = {1};
    cout << sol.binarySearch(arr2, 1) << endl; // 0
    cout << sol.binarySearch(arr2, 2) << endl; // -1
    return 0;
}
```

### Dry Run
**Input:** arr = [2, 3, 4, 10, 40], target = 10

| Step | low | high | mid | arr[mid] | Action |
|------|-----|------|-----|----------|--------|
| 1 | 0 | 4 | 2 | 4 | 4 < 10 -> low = 3 |
| 2 | 3 | 4 | 3 | 10 | 10 == 10 -> return 3 |

**Output:** 3

**Input:** arr = [2, 3, 4, 10, 40], target = 5

| Step | low | high | mid | arr[mid] | Action |
|------|-----|------|-----|----------|--------|
| 1 | 0 | 4 | 2 | 4 | 4 < 5 -> low = 3 |
| 2 | 3 | 4 | 3 | 10 | 10 > 5 -> high = 2 |
| 3 | low=3 > high=2 | -- | -- | -- | STOP, return -1 |

### Complexity Analysis
- **Time:** O(log n) -- halves the search space each step
- **Space:** O(1) -- no extra space

---

## Approach 3: Binary Search (Recursive)

### Intuition
Same logic as iterative, but implemented with recursion. The search range is passed as parameters.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int binarySearchRecursive(vector<int>& arr, int low, int high, int target) {
        if (low > high) return -1;

        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            return binarySearchRecursive(arr, mid + 1, high, target);
        else
            return binarySearchRecursive(arr, low, mid - 1, target);
    }

    int search(vector<int>& arr, int target) {
        return binarySearchRecursive(arr, 0, arr.size() - 1, target);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cout << sol.search(arr, 7) << endl;  // 6
    cout << sol.search(arr, 1) << endl;  // 0
    cout << sol.search(arr, 10) << endl; // 9
    cout << sol.search(arr, 11) << endl; // -1
    return 0;
}
```

### Complexity Analysis
- **Time:** O(log n)
- **Space:** O(log n) -- recursion stack

---

## Common Mistakes
1. **Overflow:** Using `(low + high) / 2` instead of `low + (high - low) / 2`
2. **Infinite loop:** Using `low < high` instead of `low <= high` (misses the case when target is at the only remaining element)
3. **Off-by-one:** Using `high = mid` or `low = mid` instead of `mid-1`/`mid+1` (causes infinite loop)
4. Not checking if the array is sorted (binary search requires sorted input)

## Interview Tips
- Binary search is the most fundamental searching algorithm -- it appears in countless variations
- Always use `low + (high - low) / 2` to prevent integer overflow
- The iterative version is preferred in interviews (no stack overhead)
- Binary search can be applied beyond arrays: on answer spaces, functions, etc.
- Know the STL: `lower_bound()`, `upper_bound()`, `binary_search()` in C++
- TCS NQT frequently tests the ability to trace through binary search step by step
