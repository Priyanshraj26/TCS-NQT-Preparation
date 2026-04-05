# Solution: First and Last Position of Element in Sorted Array

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q008-first-last-position.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Linear Scan | O(n) | O(1) | ✗ |
| Two Binary Searches | O(log n) | O(1) | ✓✓ |

---

## Approach 1: Linear Scan (Brute Force)

### Intuition
Scan left to right to find the first occurrence, then right to left for the last.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& arr, int target) {
        int first = -1, last = -1;
        for (int i = 0; i < (int)arr.size(); i++) {
            if (arr[i] == target) {
                if (first == -1) first = i;
                last = i;
            }
        }
        return {first, last};
    }
};

int main() {
    Solution sol;
    vector<int> arr = {5, 7, 7, 8, 8, 10};
    auto res = sol.searchRange(arr, 8);
    cout << res[0] << " " << res[1] << endl; // 3 4
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Approach 2: Two Binary Searches (Optimal)

### Intuition
Run binary search twice:
1. **Find first occurrence:** When `arr[mid] == target`, do not stop -- continue searching left (`high = mid - 1`) to find an earlier occurrence.
2. **Find last occurrence:** When `arr[mid] == target`, continue searching right (`low = mid + 1`) to find a later occurrence.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findFirst(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1, result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) {
                result = mid;       // record this position
                high = mid - 1;     // keep searching left
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return result;
    }

    int findLast(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1, result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) {
                result = mid;       // record this position
                low = mid + 1;      // keep searching right
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return result;
    }

    vector<int> searchRange(vector<int>& arr, int target) {
        return {findFirst(arr, target), findLast(arr, target)};
    }
};

int main() {
    Solution sol;

    vector<int> v1 = {5, 7, 7, 8, 8, 10};
    auto r1 = sol.searchRange(v1, 8);
    cout << r1[0] << " " << r1[1] << endl; // 3 4

    auto r2 = sol.searchRange(v1, 6);
    cout << r2[0] << " " << r2[1] << endl; // -1 -1

    vector<int> v3 = {1, 1, 1, 1, 1};
    auto r3 = sol.searchRange(v3, 1);
    cout << r3[0] << " " << r3[1] << endl; // 0 4

    vector<int> v4 = {};
    auto r4 = sol.searchRange(v4, 0);
    cout << r4[0] << " " << r4[1] << endl; // -1 -1

    vector<int> v5 = {1};
    auto r5 = sol.searchRange(v5, 1);
    cout << r5[0] << " " << r5[1] << endl; // 0 0

    return 0;
}
```

### Dry Run
**Input:** arr = [5, 7, 7, 8, 8, 10], target = 8

**findFirst(8):**

| Step | low | high | mid | arr[mid] | Action | result |
|------|-----|------|-----|----------|--------|--------|
| 1 | 0 | 5 | 2 | 7 | 7<8, low=3 | -1 |
| 2 | 3 | 5 | 4 | 8 | match, high=3 | 4 |
| 3 | 3 | 3 | 3 | 8 | match, high=2 | 3 |
| 4 | low=3 > high=2 | STOP | | | | **3** |

**findLast(8):**

| Step | low | high | mid | arr[mid] | Action | result |
|------|-----|------|-----|----------|--------|--------|
| 1 | 0 | 5 | 2 | 7 | 7<8, low=3 | -1 |
| 2 | 3 | 5 | 4 | 8 | match, low=5 | 4 |
| 3 | 5 | 5 | 5 | 10 | 10>8, high=4 | 4 |
| 4 | low=5 > high=4 | STOP | | | | **4** |

**Output:** [3, 4]

### Complexity Analysis
- **Time:** O(log n) -- two binary searches, each O(log n)
- **Space:** O(1)

---

## Common Mistakes
1. Stopping at the first match instead of continuing to search for first/last
2. Not recording `result = mid` before narrowing the search
3. Using a single binary search and then scanning linearly (degrades to O(n) for all-same arrays)

## Interview Tips
- This is equivalent to using `lower_bound` and `upper_bound` from C++ STL
- STL approach: `first = lower_bound(arr, target)`, `last = upper_bound(arr, target) - 1`
- The trick of "don't stop when found, keep searching" is a general binary search pattern
- Follow-up: count the number of occurrences = last - first + 1
- This problem is a building block for many advanced binary search problems
