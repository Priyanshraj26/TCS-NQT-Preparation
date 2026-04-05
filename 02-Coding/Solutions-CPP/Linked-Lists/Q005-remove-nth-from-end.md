# Solution: Remove Nth Node From End of List

[← Back to Question](../../DSA-Questions/Linked-Lists/Q005-remove-nth-from-end.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Two pointer gap technique | O(n) | O(1) | Yes (interviews) |
| Two pass (count + delete) | O(n) | O(1) | Simpler but two passes |

## Approach 1: Two Pointer Gap Technique

### Intuition

Move the `fast` pointer n steps ahead first. Then move both `slow` and `fast` one step at a time. When `fast` reaches the end, `slow` is right before the node to remove. Use a dummy node to handle the edge case of removing the head.

### C++ Code

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0);
    dummy.next = head;
    ListNode* fast = &dummy;
    ListNode* slow = &dummy;

    // Move fast n+1 steps ahead (so slow lands BEFORE the target)
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }

    // Move both until fast reaches null
    while (fast) {
        fast = fast->next;
        slow = slow->next;
    }

    // Delete the node after slow
    ListNode* toDelete = slow->next;
    slow->next = toDelete->next;
    delete toDelete;

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
    // Test 1: Remove 2nd from end
    int a1[] = {1, 2, 3, 4, 5};
    ListNode* h1 = buildList(a1, 5);
    cout << "Test 1: ";
    printList(removeNthFromEnd(h1, 2));
    // Expected: 1 -> 2 -> 3 -> 5

    // Test 2: Remove last element (n=1)
    int a2[] = {1, 2, 3};
    ListNode* h2 = buildList(a2, 3);
    cout << "Test 2: ";
    printList(removeNthFromEnd(h2, 1));
    // Expected: 1 -> 2

    // Test 3: Remove head (n = length)
    int a3[] = {1, 2, 3};
    ListNode* h3 = buildList(a3, 3);
    cout << "Test 3: ";
    printList(removeNthFromEnd(h3, 3));
    // Expected: 2 -> 3

    // Test 4: Single element, remove it
    int a4[] = {1};
    ListNode* h4 = buildList(a4, 1);
    cout << "Test 4: ";
    printList(removeNthFromEnd(h4, 1));
    // Expected: (empty)

    return 0;
}
```

### Dry Run

```
List: 1 -> 2 -> 3 -> 4 -> 5, n = 2
dummy -> 1 -> 2 -> 3 -> 4 -> 5

Move fast n+1 = 3 steps:
  fast = dummy -> 1 -> 2 -> 3
  fast is at node 3

Move both:
  slow=dummy, fast=3
  slow=1,     fast=4
  slow=2,     fast=5
  slow=3,     fast=null => STOP

Delete slow->next = 4
Result: 1 -> 2 -> 3 -> 5
```

### Complexity Analysis

- **Time:** O(n) -- single pass
- **Space:** O(1)

## Common Mistakes

1. Forgetting the dummy node -- removing the head becomes a special case without it
2. Moving fast only n steps instead of n+1 (slow needs to be BEFORE the target)
3. Not freeing the deleted node (memory leak)
4. Assuming n is always valid -- in production, validate that n <= list length

## Interview Tips

- The dummy node pattern is critical -- it handles removing the head seamlessly
- The "gap" technique generalizes to many problems (kth from end, etc.)
- Always clarify: is n 0-indexed or 1-indexed? (usually 1-indexed)
- Mention that this is a single-pass solution, which is the key optimization over two-pass
