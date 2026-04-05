# Solution: Selection Sort

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q002-selection-sort.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Selection Sort | O(n^2) | O(1) | ✓ |

---

## Approach 1: Selection Sort (Find Min and Swap)

### Intuition
Divide the array into sorted (left) and unsorted (right) parts. In each iteration, find the minimum element from the unsorted part and swap it with the first unsorted element.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void selectionSort(vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            // Find minimum in unsorted part
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap minimum with first unsorted element
            if (minIdx != i)
                swap(arr[i], arr[minIdx]);
        }
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> v1 = {64, 25, 12, 22, 11};
    sol.selectionSort(v1);
    printArray(v1); // 11 12 22 25 64

    vector<int> v2 = {29, 10, 14, 37, 13};
    sol.selectionSort(v2);
    printArray(v2); // 10 13 14 29 37

    vector<int> v3 = {1};
    sol.selectionSort(v3);
    printArray(v3); // 1

    vector<int> v4 = {3, 3, 3};
    sol.selectionSort(v4);
    printArray(v4); // 3 3 3

    return 0;
}
```

### Dry Run (Step-by-Step Visualization)
**Input:** [64, 25, 12, 22, 11]

**Pass 1 (i=0):**
```
Find min in [64, 25, 12, 22, 11] -> min = 11 at index 4
Swap arr[0] and arr[4]
[11, | 25, 12, 22, 64]
 ^sorted
```

**Pass 2 (i=1):**
```
Find min in [25, 12, 22, 64] -> min = 12 at index 2
Swap arr[1] and arr[2]
[11, 12, | 25, 22, 64]
 ^sorted^
```

**Pass 3 (i=2):**
```
Find min in [25, 22, 64] -> min = 22 at index 3
Swap arr[2] and arr[3]
[11, 12, 22, | 25, 64]
 ^--sorted--^
```

**Pass 4 (i=3):**
```
Find min in [25, 64] -> min = 25 at index 3 (itself)
No swap needed
[11, 12, 22, 25, | 64]
 ^----sorted----^
```

**Final:** [11, 12, 22, 25, 64]

| Pass | Array State | Min Found | Swap |
|------|-------------|-----------|------|
| 1 | [64, 25, 12, 22, 11] | 11 (idx 4) | arr[0] <-> arr[4] |
| 2 | [11, 25, 12, 22, 64] | 12 (idx 2) | arr[1] <-> arr[2] |
| 3 | [11, 12, 25, 22, 64] | 22 (idx 3) | arr[2] <-> arr[3] |
| 4 | [11, 12, 22, 25, 64] | 25 (idx 3) | no swap |

### Complexity Analysis
- **Time:** O(n^2) in all cases (always scans the entire unsorted portion)
- **Space:** O(1) in-place
- **Stable:** No (swapping can change relative order of equal elements)
- **Number of swaps:** O(n) -- minimum among simple sorting algorithms

---

## Common Mistakes
1. Forgetting the `if (minIdx != i)` check (unnecessary swap with itself)
2. Searching for min starting at `i`, not `i+1` (wastes one comparison)
3. Assuming selection sort is stable (it is NOT -- swapping disrupts order)

## Interview Tips
- Selection sort makes the **minimum number of swaps** (at most n-1) -- useful when writes are expensive
- It always does O(n^2) comparisons regardless of input order (no best-case advantage)
- Not stable in its standard form, but can be made stable using insertion instead of swap
- Compare with bubble sort: bubble sort can exit early, selection sort cannot
- TCS NQT often asks to trace through sorting algorithms step by step
