# Solution: Insertion Sort

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q003-insertion-sort.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Insertion Sort | O(n^2) worst, O(n) best | O(1) | ✓ |

---

## Approach 1: Insertion Sort (Insert in Sorted Position)

### Intuition
Build the sorted array one element at a time. For each new element, shift larger elements to the right and insert the new element in its correct position in the sorted portion.

Think of it like sorting playing cards in your hand -- you pick each card and slide it into the right spot.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void insertionSort(vector<int>& arr) {
        int n = arr.size();
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            // Shift elements greater than key to the right
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key; // Insert key at correct position
        }
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> v1 = {12, 11, 13, 5, 6};
    sol.insertionSort(v1);
    printArray(v1); // 5 6 11 12 13

    vector<int> v2 = {5, 2, 4, 6, 1, 3};
    sol.insertionSort(v2);
    printArray(v2); // 1 2 3 4 5 6

    // Already sorted (best case)
    vector<int> v3 = {1, 2, 3, 4, 5};
    sol.insertionSort(v3);
    printArray(v3); // 1 2 3 4 5

    // Reverse sorted (worst case)
    vector<int> v4 = {5, 4, 3, 2, 1};
    sol.insertionSort(v4);
    printArray(v4); // 1 2 3 4 5

    return 0;
}
```

### Dry Run (Step-by-Step Visualization)
**Input:** [12, 11, 13, 5, 6]

**Step 1 (i=1): key = 11**
```
Sorted part: [12]  |  key = 11
12 > 11 -> shift 12 right
Insert 11 at position 0
Result: [11, 12, | 13, 5, 6]
```

**Step 2 (i=2): key = 13**
```
Sorted part: [11, 12]  |  key = 13
12 < 13 -> no shift needed
Insert 13 at position 2
Result: [11, 12, 13, | 5, 6]
```

**Step 3 (i=3): key = 5**
```
Sorted part: [11, 12, 13]  |  key = 5
13 > 5 -> shift 13 right  -> [11, 12, _, 13]
12 > 5 -> shift 12 right  -> [11, _, 12, 13]
11 > 5 -> shift 11 right  -> [_, 11, 12, 13]
Insert 5 at position 0
Result: [5, 11, 12, 13, | 6]
```

**Step 4 (i=4): key = 6**
```
Sorted part: [5, 11, 12, 13]  |  key = 6
13 > 6 -> shift -> [5, 11, 12, _, 13]
12 > 6 -> shift -> [5, 11, _, 12, 13]
11 > 6 -> shift -> [5, _, 11, 12, 13]
5 < 6  -> stop
Insert 6 at position 1
Result: [5, 6, 11, 12, 13]
```

| Step | key | Shifts | Array After |
|------|-----|--------|-------------|
| i=1 | 11 | 12 right | [11, 12, 13, 5, 6] |
| i=2 | 13 | none | [11, 12, 13, 5, 6] |
| i=3 | 5 | 13, 12, 11 right | [5, 11, 12, 13, 6] |
| i=4 | 6 | 13, 12, 11 right | [5, 6, 11, 12, 13] |

### Complexity Analysis
- **Time:** O(n^2) worst/average case, **O(n) best case** (already sorted)
- **Space:** O(1) in-place
- **Stable:** Yes
- **Adaptive:** Yes (fewer operations on nearly-sorted data)

---

## Common Mistakes
1. Starting the outer loop at `i=0` instead of `i=1`
2. Forgetting to save the `key` before shifting (overwrites the value)
3. Wrong placement: `arr[j] = key` instead of `arr[j+1] = key`

## Interview Tips
- Insertion sort is the **best simple sorting algorithm** for nearly sorted data -- O(n) in best case
- It is **stable** and **in-place** -- preferred over selection sort when stability matters
- Used as the base case in hybrid algorithms (TimSort uses insertion sort for small subarrays)
- Total number of shifts = number of inversions in the array
- For TCS NQT: know the step-by-step trace and complexity analysis
