# Solution: Count Occurrences in Sorted Array

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q009-count-occurrences.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Linear Count | O(n) | O(1) | ✗ |
| Binary Search (upper - lower bound) | O(log n) | O(1) | ✓✓ |

---

## Approach 1: Linear Count (Brute Force)

### Intuition
Scan the entire array and count how many times the target appears.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int countOccurrences(vector<int>& arr, int target) {
        int count = 0;
        for (int x : arr) {
            if (x == target) count++;
        }
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 1, 2, 2, 2, 2, 3};
    cout << sol.countOccurrences(arr, 2) << endl; // 4
    cout << sol.countOccurrences(arr, 4) << endl; // 0
    return 0;
}
```

### Complexity Analysis
- **Time:** O(n)
- **Space:** O(1)

---

## Approach 2: Using upper_bound - lower_bound (Optimal)

### Intuition
In a sorted array, all occurrences of a target are contiguous. Find the first position using `lower_bound` and the position just after the last using `upper_bound`. The count = upper_bound - lower_bound.

- **lower_bound(target):** first index where `arr[idx] >= target`
- **upper_bound(target):** first index where `arr[idx] > target`

### C++ Code (Using STL)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int countOccurrences(vector<int>& arr, int target) {
        auto lb = lower_bound(arr.begin(), arr.end(), target);
        auto ub = upper_bound(arr.begin(), arr.end(), target);
        return ub - lb;
    }
};

int main() {
    Solution sol;

    vector<int> v1 = {1, 1, 2, 2, 2, 2, 3};
    cout << sol.countOccurrences(v1, 2) << endl; // 4
    cout << sol.countOccurrences(v1, 1) << endl; // 2
    cout << sol.countOccurrences(v1, 3) << endl; // 1
    cout << sol.countOccurrences(v1, 4) << endl; // 0

    vector<int> v2 = {5, 5, 5, 5, 5};
    cout << sol.countOccurrences(v2, 5) << endl; // 5

    vector<int> v3 = {};
    cout << sol.countOccurrences(v3, 1) << endl; // 0

    return 0;
}
```

### C++ Code (Manual Binary Search Implementation)
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Returns index of first element >= target
    int lowerBound(vector<int>& arr, int target) {
        int low = 0, high = arr.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < target)
                low = mid + 1;
            else
                high = mid;
        }
        return low;
    }

    // Returns index of first element > target
    int upperBound(vector<int>& arr, int target) {
        int low = 0, high = arr.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] <= target)
                low = mid + 1;
            else
                high = mid;
        }
        return low;
    }

    int countOccurrences(vector<int>& arr, int target) {
        return upperBound(arr, target) - lowerBound(arr, target);
    }
};

int main() {
    Solution sol;

    vector<int> v1 = {1, 1, 2, 2, 2, 2, 3};
    cout << sol.countOccurrences(v1, 2) << endl; // 4
    cout << sol.countOccurrences(v1, 1) << endl; // 2
    cout << sol.countOccurrences(v1, 4) << endl; // 0

    vector<int> v2 = {2, 2, 2, 2, 2};
    cout << sol.countOccurrences(v2, 2) << endl; // 5

    return 0;
}
```

### Dry Run
**Input:** arr = [1, 1, 2, 2, 2, 2, 3], target = 2

**lowerBound(2):**

| Step | low | high | mid | arr[mid] | Action |
|------|-----|------|-----|----------|--------|
| 1 | 0 | 7 | 3 | 2 | 2>=2, high=3 |
| 2 | 0 | 3 | 1 | 1 | 1<2, low=2 |
| 3 | 2 | 3 | 2 | 2 | 2>=2, high=2 |
| 4 | low=2 == high=2 | STOP | | | return **2** |

**upperBound(2):**

| Step | low | high | mid | arr[mid] | Action |
|------|-----|------|-----|----------|--------|
| 1 | 0 | 7 | 3 | 2 | 2<=2, low=4 |
| 2 | 4 | 7 | 5 | 2 | 2<=2, low=6 |
| 3 | 6 | 7 | 6 | 3 | 3>2, high=6 |
| 4 | low=6 == high=6 | STOP | | | return **6** |

**Count:** 6 - 2 = **4**

### Complexity Analysis
- **Time:** O(log n) -- two binary searches
- **Space:** O(1)

---

## Common Mistakes
1. Confusing `lower_bound` (`<` vs `>=`) and `upper_bound` (`<=` vs `>`)
2. Using `high = arr.size() - 1` instead of `high = arr.size()` (the bound can be past the last element)
3. Using `low <= high` instead of `low < high` in bound searches (different loop invariant than standard binary search)

## Interview Tips
- This is one of the most practical binary search applications
- The STL one-liner is acceptable in interviews, but be ready to implement manually
- Key difference: `lower_bound` uses `<` to compare, `upper_bound` uses `<=`
- The `high = arr.size()` (not `size()-1`) is crucial -- the answer can be one past the end
- This pattern extends to: "count elements in range [a, b]" = lowerBound(b+1) - lowerBound(a)
