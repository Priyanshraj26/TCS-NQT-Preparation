# Solution: Bubble Sort

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q001-bubble-sort.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Standard Bubble Sort | O(n^2) | O(1) | ✗ |
| Optimized (Early Exit) | O(n^2) worst, O(n) best | O(1) | ✓ |

---

## Approach 1: Standard Bubble Sort

### Intuition
Repeatedly swap adjacent elements if they are in the wrong order. After each pass, the largest unsorted element "bubbles up" to its correct position.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void bubbleSort(vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> v1 = {64, 34, 25, 12, 22, 11, 90};
    sol.bubbleSort(v1);
    printArray(v1); // 11 12 22 25 34 64 90

    vector<int> v2 = {5, 1, 4, 2, 8};
    sol.bubbleSort(v2);
    printArray(v2); // 1 2 4 5 8

    return 0;
}
```

### Dry Run (Step-by-Step Visualization)
**Input:** [5, 1, 4, 2, 8]

**Pass 1 (i=0):**
```
[5, 1, 4, 2, 8]  -> compare 5,1 -> swap -> [1, 5, 4, 2, 8]
[1, 5, 4, 2, 8]  -> compare 5,4 -> swap -> [1, 4, 5, 2, 8]
[1, 4, 5, 2, 8]  -> compare 5,2 -> swap -> [1, 4, 2, 5, 8]
[1, 4, 2, 5, 8]  -> compare 5,8 -> no swap
Result: [1, 4, 2, 5, | 8]  (8 is in place)
```

**Pass 2 (i=1):**
```
[1, 4, 2, 5, 8]  -> compare 1,4 -> no swap
[1, 4, 2, 5, 8]  -> compare 4,2 -> swap -> [1, 2, 4, 5, 8]
[1, 2, 4, 5, 8]  -> compare 4,5 -> no swap
Result: [1, 2, 4, | 5, 8]  (5 is in place)
```

**Pass 3 (i=2):**
```
[1, 2, 4, 5, 8]  -> compare 1,2 -> no swap
[1, 2, 4, 5, 8]  -> compare 2,4 -> no swap
Result: [1, 2, | 4, 5, 8]  (4 is in place)
```

**Pass 4 (i=3):**
```
[1, 2, 4, 5, 8]  -> compare 1,2 -> no swap
Result: [1, | 2, 4, 5, 8]  (sorted!)
```

### Complexity Analysis
- **Time:** O(n^2) always (even for sorted input)
- **Space:** O(1) in-place

---

## Approach 2: Optimized Bubble Sort (Early Exit)

### Intuition
If no swaps occur during a pass, the array is already sorted. Add a flag to detect this and exit early. This makes best-case O(n) for an already-sorted array.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void bubbleSortOptimized(vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n - 1; i++) {
            bool swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    swapped = true;
                }
            }
            // If no swaps in this pass, array is sorted
            if (!swapped) break;
        }
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    // Test 1: Random order
    vector<int> v1 = {64, 34, 25, 12, 22, 11, 90};
    sol.bubbleSortOptimized(v1);
    printArray(v1); // 11 12 22 25 34 64 90

    // Test 2: Already sorted (benefits from early exit)
    vector<int> v2 = {1, 2, 3, 4, 5};
    sol.bubbleSortOptimized(v2);
    printArray(v2); // 1 2 3 4 5

    // Test 3: Reverse sorted (worst case)
    vector<int> v3 = {5, 4, 3, 2, 1};
    sol.bubbleSortOptimized(v3);
    printArray(v3); // 1 2 3 4 5

    // Test 4: Single element
    vector<int> v4 = {1};
    sol.bubbleSortOptimized(v4);
    printArray(v4); // 1

    return 0;
}
```

### Dry Run (Step-by-Step Visualization)
**Input:** [1, 2, 3, 5, 4] (nearly sorted)

**Pass 1 (i=0):**
```
[1, 2, 3, 5, 4]  -> 1<2 ok -> 2<3 ok -> 3<5 ok -> 5>4 swap
Result: [1, 2, 3, 4, | 5]  swapped = true
```

**Pass 2 (i=1):**
```
[1, 2, 3, 4, 5]  -> 1<2 ok -> 2<3 ok -> 3<4 ok
Result: [1, 2, 3, | 4, 5]  swapped = false -> BREAK!
```

Only 2 passes needed instead of 4.

### Complexity Analysis
- **Time:** O(n^2) worst case, **O(n) best case** (already sorted)
- **Space:** O(1) in-place
- **Stable:** Yes (equal elements maintain relative order)

---

## Common Mistakes
1. Inner loop bound should be `n-1-i`, not `n-1` (optimization to avoid re-checking sorted end)
2. Forgetting to reset the `swapped` flag at the start of each pass
3. Using `arr[j] >= arr[j+1]` instead of `>` (makes it unstable)

## Interview Tips
- Bubble sort is the simplest sorting algorithm -- good for explaining sorting concepts
- Always mention the optimized version with the `swapped` flag
- Properties: **stable**, **in-place**, **adaptive** (with optimization)
- Practical use: when data is nearly sorted and n is small
- In TCS NQT, you may be asked to trace through the algorithm step by step
