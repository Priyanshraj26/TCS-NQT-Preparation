# Solution: Merge Two Sorted Linked Lists

[← Back to Question](../../DSA-Questions/Linked-Lists/Q003-merge-two-sorted.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Iterative (dummy node) | O(n + m) | O(1) | Yes (interviews) |
| Recursive | O(n + m) | O(n + m) stack | Clean but uses stack |

## Approach 1: Iterative with Dummy Node

### Intuition

Create a dummy head node to simplify edge cases. Use a tail pointer to build the merged list by always choosing the smaller of the two current heads. After one list is exhausted, attach the remainder of the other.

### C++ Code

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// --- Iterative Merge ---
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;

    while (l1 && l2) {
        if (l1->val <= l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy.next;
}

ListNode* buildList(int arr[], int n) {
    if (n == 0) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* curr = head;
    for (int i = 1; i < n; i++) {
        curr->next = new ListNode(arr[i]);
        curr = curr->next;
    }
    return head;
}

void printList(ListNode* head) {
    while (head) {
        cout << head->val;
        if (head->next) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Test 1: Normal merge
    int a1[] = {1, 3, 5};
    int a2[] = {2, 4, 6};
    ListNode* l1 = buildList(a1, 3);
    ListNode* l2 = buildList(a2, 3);
    cout << "Test 1: ";
    printList(mergeTwoLists(l1, l2));
    // Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6

    // Test 2: One empty list
    int a3[] = {1, 2, 3};
    ListNode* l3 = buildList(a3, 3);
    cout << "Test 2: ";
    printList(mergeTwoLists(l3, nullptr));
    // Expected: 1 -> 2 -> 3

    // Test 3: Both empty
    cout << "Test 3: ";
    printList(mergeTwoLists(nullptr, nullptr));
    // Expected: (empty)

    // Test 4: Overlapping values
    int a4[] = {1, 1, 3};
    int a5[] = {1, 2, 4};
    ListNode* l4 = buildList(a4, 3);
    ListNode* l5 = buildList(a5, 3);
    cout << "Test 4: ";
    printList(mergeTwoLists(l4, l5));
    // Expected: 1 -> 1 -> 1 -> 2 -> 3 -> 4

    // Test 5: Unequal lengths
    int a6[] = {5};
    int a7[] = {1, 2, 3, 4};
    ListNode* l6 = buildList(a6, 1);
    ListNode* l7 = buildList(a7, 4);
    cout << "Test 5: ";
    printList(mergeTwoLists(l6, l7));
    // Expected: 1 -> 2 -> 3 -> 4 -> 5

    return 0;
}
```

### Dry Run

```
l1: 1 -> 3 -> 5
l2: 2 -> 4 -> 6
dummy -> ?

Step 1: 1 <= 2, pick 1.  dummy -> 1    l1=3
Step 2: 3 > 2,  pick 2.  dummy -> 1 -> 2    l2=4
Step 3: 3 <= 4, pick 3.  dummy -> 1 -> 2 -> 3    l1=5
Step 4: 5 > 4,  pick 4.  dummy -> 1 -> 2 -> 3 -> 4    l2=6
Step 5: 5 <= 6, pick 5.  dummy -> 1 -> 2 -> 3 -> 4 -> 5    l1=null
Attach remaining l2: -> 6

Result: 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

### Complexity Analysis

- **Time:** O(n + m) -- each node visited once
- **Space:** O(1) -- only relinks existing nodes

## Approach 2: Recursive

### Intuition

At each call, compare the heads. The smaller one becomes the head of the result, and its `next` is the merge of the remaining lists.

### C++ Code

```cpp
ListNode* mergeTwoListsRecursive(ListNode* l1, ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;

    if (l1->val <= l2->val) {
        l1->next = mergeTwoListsRecursive(l1->next, l2);
        return l1;
    } else {
        l2->next = mergeTwoListsRecursive(l1, l2->next);
        return l2;
    }
}
```

### Complexity Analysis

- **Time:** O(n + m)
- **Space:** O(n + m) -- recursion stack

## Common Mistakes

1. Forgetting to handle when one or both lists are empty
2. Creating new nodes instead of relinking existing ones (wastes memory)
3. Losing the reference to the merged list head (the dummy node pattern prevents this)
4. Not advancing the pointer after picking a node

## Interview Tips

- The dummy node trick eliminates special-case handling for the first node
- Mention this is the core merge step in merge sort for linked lists
- If asked about stability: this merge is stable (equal elements preserve order)
- Start with iterative -- it is preferred for O(1) space
