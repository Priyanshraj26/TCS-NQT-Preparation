# Solution: Reverse a Linked List

[← Back to Question](../../DSA-Questions/Linked-Lists/Q001-reverse-linked-list.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Iterative (3 pointers) | O(n) | O(1) | Yes (interviews) |
| Recursive | O(n) | O(n) stack | Good to know |

## Approach 1: Iterative (Three Pointers)

### Intuition

Maintain three pointers -- `prev`, `curr`, and `next`. At each step, reverse the `next` pointer of the current node to point to the previous node, then advance all three pointers forward by one position.

### C++ Code

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// --- Iterative Approach ---
ListNode* reverseListIterative(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* nextTemp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}

// Helper: build list from array
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

// Helper: print list
void printList(ListNode* head) {
    while (head) {
        cout << head->val;
        if (head->next) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Test 1: Normal list
    int arr1[] = {1, 2, 3, 4, 5};
    ListNode* head1 = buildList(arr1, 5);
    cout << "Original: ";
    printList(head1);
    head1 = reverseListIterative(head1);
    cout << "Reversed: ";
    printList(head1);
    // Expected: 5 -> 4 -> 3 -> 2 -> 1

    // Test 2: Single element
    int arr2[] = {42};
    ListNode* head2 = buildList(arr2, 1);
    head2 = reverseListIterative(head2);
    cout << "Single element reversed: ";
    printList(head2);
    // Expected: 42

    // Test 3: Empty list
    ListNode* head3 = nullptr;
    head3 = reverseListIterative(head3);
    cout << "Empty list reversed: ";
    printList(head3);
    // Expected: (empty)

    // Test 4: Two elements
    int arr4[] = {1, 2};
    ListNode* head4 = buildList(arr4, 2);
    head4 = reverseListIterative(head4);
    cout << "Two elements reversed: ";
    printList(head4);
    // Expected: 2 -> 1

    return 0;
}
```

### Dry Run

```
Input: 1 -> 2 -> 3 -> nullptr

Step 0: prev=null, curr=1, next=2
        1->null         prev=1, curr=2
Step 1: prev=1,   curr=2, next=3
        2->1->null      prev=2, curr=3
Step 2: prev=2,   curr=3, next=null
        3->2->1->null   prev=3, curr=null

Return prev = 3 -> 2 -> 1 -> null
```

### Complexity Analysis

- **Time:** O(n) -- single pass through the list
- **Space:** O(1) -- only three extra pointers

## Approach 2: Recursive

### Intuition

Recursively reverse the rest of the list, then make the current node's next node point back to the current node. Set the current node's next to `nullptr` to avoid cycles.

### C++ Code

```cpp
ListNode* reverseListRecursive(ListNode* head) {
    // Base case: empty list or single node
    if (!head || !head->next) return head;

    ListNode* newHead = reverseListRecursive(head->next);
    head->next->next = head;  // make next node point back to current
    head->next = nullptr;     // break forward link
    return newHead;
}
```

### Dry Run

```
reverseListRecursive(1)
  reverseListRecursive(2)
    reverseListRecursive(3) -> returns 3 (base case, no next)
    2->next->next = 2  =>  3->next = 2
    2->next = null
    return 3
  1->next->next = 1  =>  2->next = 1
  1->next = null
  return 3

Result: 3 -> 2 -> 1 -> null
```

### Complexity Analysis

- **Time:** O(n) -- visits each node once
- **Space:** O(n) -- recursion stack depth

## Common Mistakes

1. Forgetting to save `curr->next` before overwriting it in the iterative approach
2. Not handling the empty list (`head == nullptr`) case
3. In the recursive approach, forgetting `head->next = nullptr` which causes a cycle
4. Returning `head` instead of `prev` (iterative) or `newHead` (recursive)

## Interview Tips

- Start with the iterative approach -- it is O(1) space and interviewers prefer it
- Draw the pointer diagram on the whiteboard to avoid confusion
- Mention both approaches to show depth of knowledge
- This is a building block for many other problems (palindrome check, reorder list, etc.)
