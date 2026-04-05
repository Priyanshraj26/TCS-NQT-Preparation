# Solution: Quick Sort

[← Back to Question](../../DSA-Questions/Sorting-Searching/Q005-quick-sort.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Lomuto Partition | O(n log n) avg, O(n^2) worst | O(log n) | ✓ |
| Hoare Partition | O(n log n) avg, O(n^2) worst | O(log n) | ✓✓ |

---

## Approach 1: Quick Sort with Lomuto Partition

### Intuition
Choose the last element as pivot. Partition the array so that all elements less than or equal to the pivot are on the left, and all greater are on the right. The pivot ends up in its final sorted position. Recursively sort the left and right partitions.

**Lomuto scheme:** Maintain an index `i` that tracks where the next smaller element should go.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int lomutoPartition(vector<int>& arr, int low, int high) {
        int pivot = arr[high]; // last element as pivot
        int i = low - 1;       // index of smaller element boundary

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]); // place pivot in correct position
        return i + 1;                // pivot index
    }

    void quickSort(vector<int>& arr, int low, int high) {
        if (low < high) {
            int pi = lomutoPartition(arr, low, high);
            quickSort(arr, low, pi - 1);  // sort left of pivot
            quickSort(arr, pi + 1, high); // sort right of pivot
        }
    }

    void sort(vector<int>& arr) {
        if (arr.empty()) return;
        quickSort(arr, 0, arr.size() - 1);
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> v1 = {10, 7, 8, 9, 1, 5};
    sol.sort(v1);
    printArray(v1); // 1 5 7 8 9 10

    vector<int> v2 = {3, 6, 8, 10, 1, 2, 1};
    sol.sort(v2);
    printArray(v2); // 1 1 2 3 6 8 10

    vector<int> v3 = {5, 4, 3, 2, 1};
    sol.sort(v3);
    printArray(v3); // 1 2 3 4 5

    return 0;
}
```

### Dry Run (Lomuto Partition Visualization)
**Input:** [10, 7, 8, 9, 1, 5], pivot = 5

| j | arr[j] | arr[j]<=5? | i | Swap | Array State |
|---|--------|-----------|---|------|-------------|
| 0 | 10 | No | -1 | -- | [10, 7, 8, 9, 1, 5] |
| 1 | 7 | No | -1 | -- | [10, 7, 8, 9, 1, 5] |
| 2 | 8 | No | -1 | -- | [10, 7, 8, 9, 1, 5] |
| 3 | 9 | No | -1 | -- | [10, 7, 8, 9, 1, 5] |
| 4 | 1 | Yes | 0 | arr[0]<->arr[4] | [1, 7, 8, 9, 10, 5] |

Final: swap arr[1] with arr[5] (pivot): **[1, 5, 8, 9, 10, 7]**, pivot at index 1

---

## Approach 2: Quick Sort with Hoare Partition

### Intuition
Use two pointers starting from both ends. Move them toward each other, swapping elements that are on the wrong side. Hoare partition is more efficient in practice as it does fewer swaps on average.

### C++ Code
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int hoarePartition(vector<int>& arr, int low, int high) {
        int pivot = arr[low]; // first element as pivot
        int i = low - 1;
        int j = high + 1;

        while (true) {
            // Move i right until we find element >= pivot
            do { i++; } while (arr[i] < pivot);

            // Move j left until we find element <= pivot
            do { j--; } while (arr[j] > pivot);

            if (i >= j) return j; // partition point

            swap(arr[i], arr[j]);
        }
    }

    void quickSort(vector<int>& arr, int low, int high) {
        if (low < high) {
            int p = hoarePartition(arr, low, high);
            quickSort(arr, low, p);      // NOTE: p, not p-1
            quickSort(arr, p + 1, high);
        }
    }

    void sort(vector<int>& arr) {
        if (arr.empty()) return;
        quickSort(arr, 0, arr.size() - 1);
    }
};

void printArray(vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> v1 = {10, 7, 8, 9, 1, 5};
    sol.sort(v1);
    printArray(v1); // 1 5 7 8 9 10

    vector<int> v2 = {3, 6, 8, 10, 1, 2, 1};
    sol.sort(v2);
    printArray(v2); // 1 1 2 3 6 8 10

    vector<int> v3 = {1, 2, 3, 4, 5};
    sol.sort(v3);
    printArray(v3); // 1 2 3 4 5

    vector<int> v4 = {4, 2, 4, 2, 4};
    sol.sort(v4);
    printArray(v4); // 2 2 4 4 4

    return 0;
}
```

### Dry Run (Hoare Partition Visualization)
**Input:** [10, 7, 8, 9, 1, 5], pivot = 10 (first element)

| Step | i | j | arr[i] | arr[j] | Action | Array |
|------|---|---|--------|--------|--------|-------|
| 1 | 0 | 5 | 10 | 5 | i finds 10>=10, j finds 5<=10 | swap -> [5, 7, 8, 9, 1, 10] |
| 2 | 1 | 4 | 7 | 1 | i finds... i moves to 5 (10>=10), j moves to 4 (1<=10) | i=5, j=4, i>=j STOP |

Return j = 4. Partition: [5,7,8,9,1] and [10].

### Complexity Analysis
- **Time:** O(n log n) average, O(n^2) worst case (sorted input with bad pivot)
- **Space:** O(log n) average (recursion stack), O(n) worst case
- **Stable:** No
- **In-place:** Yes (only O(log n) stack space)

---

## Common Mistakes
1. **Lomuto:** Off-by-one with `i` initialization (should be `low - 1`)
2. **Hoare:** Using `quickSort(arr, low, p-1)` instead of `quickSort(arr, low, p)` -- Hoare partition returns differently than Lomuto
3. Infinite recursion when all elements are equal (need proper handling)
4. Not handling the case when `low >= high` in the base case

## Interview Tips
- Quicksort is the fastest in practice due to cache efficiency and small constant factors
- Worst case O(n^2) occurs with sorted input and first/last element as pivot
- **Randomized quicksort** (random pivot) gives expected O(n log n) -- always mention this
- Hoare partition does ~3x fewer swaps than Lomuto on average
- C++ `std::sort` uses IntroSort (quicksort + heapsort fallback + insertion sort for small arrays)
- Know the difference between Lomuto and Hoare for interviews
