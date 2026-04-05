# Solution: Merge Sort

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q004-merge-sort.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Merge Sort | O(n log n) | O(n) | ✓✓ |

---

## Approach 1: Merge Sort (Divide and Conquer)

### Intuition
1. **Divide:** Split the array into two halves.
2. **Conquer:** Recursively sort each half.
3. **Merge:** Combine two sorted halves into one sorted array.

The merge step is the key -- it combines two sorted arrays in O(n) time using a two-pointer technique.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // Create temporary arrays
        vector<int> L(n1), R(n2);
        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

        // Merge back
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j])  // <= makes it stable
                arr[k++] = L[i++];
            else
                arr[k++] = R[j++];
        }

        // Copy remaining elements
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    void mergeSort(vector<int>& arr, int left, int right) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);       // Sort left half
        mergeSort(arr, mid + 1, right);  // Sort right half
        merge(arr, left, mid, right);    // Merge sorted halves
    }

    void sort(vector<int>& arr) {
        if (arr.empty()) return;
        mergeSort(arr, 0, arr.size() - 1);
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> v1 = {38, 27, 43, 3, 9, 82, 10};
    sol.sort(v1);
    printArray(v1); // 3 9 10 27 38 43 82

    vector<int> v2 = {5, 2, 4, 6, 1, 3};
    sol.sort(v2);
    printArray(v2); // 1 2 3 4 5 6

    vector<int> v3 = {1};
    sol.sort(v3);
    printArray(v3); // 1

    vector<int> v4 = {4, 4, 2, 2, 1, 1};
    sol.sort(v4);
    printArray(v4); // 1 1 2 2 4 4

    return 0;
}
```

### Dry Run (Step-by-Step Visualization)
**Input:** [38, 27, 43, 3, 9, 82, 10]

```
                  [38, 27, 43, 3, 9, 82, 10]
                 /                           \
          [38, 27, 43, 3]              [9, 82, 10]
          /             \              /          \
      [38, 27]      [43, 3]       [9, 82]       [10]
      /      \      /     \       /     \          |
    [38]    [27]  [43]   [3]    [9]   [82]       [10]
      \      /      \     /       \     /          |
      [27, 38]     [3, 43]       [9, 82]         [10]
          \           /              \              /
       [3, 27, 38, 43]             [9, 10, 82]
                \                      /
          [3, 9, 10, 27, 38, 43, 82]
```

**Merge step example: merging [27, 38] and [3, 43]:**

| i | j | L[i] | R[j] | Pick | Result |
|---|---|------|------|------|--------|
| 0 | 0 | 27 | 3 | R[0]=3 | [3] |
| 0 | 1 | 27 | 43 | L[0]=27 | [3, 27] |
| 1 | 1 | 38 | 43 | L[1]=38 | [3, 27, 38] |
| - | 1 | -- | 43 | R[1]=43 | [3, 27, 38, 43] |

### Complexity Analysis
- **Time:** O(n log n) in all cases (always divides and merges)
- **Space:** O(n) for temporary arrays during merge
- **Stable:** Yes (equal elements maintain relative order using `<=`)
- **Not in-place:** Requires O(n) extra space

---

## Common Mistakes
1. Using `L[i] < R[j]` instead of `<=` (breaks stability)
2. Calculating mid as `(left + right) / 2` instead of `left + (right - left) / 2` (overflow for large indices)
3. Forgetting to copy remaining elements after the main merge loop
4. Wrong base case: using `left == right` misses the empty subarray case

## Interview Tips
- Merge sort guarantees O(n log n) -- unlike quicksort which can degrade to O(n^2)
- It is the preferred algorithm when **stability** is required
- The merge function is reusable: "merge two sorted arrays" is a standalone interview question
- Space overhead is the main disadvantage compared to quicksort
- Merge sort is the basis for **external sorting** (sorting data that does not fit in memory)
- Follow-up: count inversions during merge sort
