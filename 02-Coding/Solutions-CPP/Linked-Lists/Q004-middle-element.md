# Solution: Find Middle Element of Linked List

[← Back to Question](../../DSA-Questions/Linked-Lists/Q004-middle-element.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Slow/Fast pointer | O(n) | O(1) | Yes (interviews) |
| Count then traverse | O(n) | O(1) | Two-pass, less elegant |

## Approach 1: Slow and Fast Pointer

### Intuition

Use two pointers: slow moves one step, fast moves two steps. When fast reaches the end, slow is at the middle. For even-length lists, this gives the second middle node.

### C++ Code

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// --- Slow/Fast Pointer ---
ListNode* findMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

// --- If you need the FIRST middle (even length) ---
ListNode* findFirstMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
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

int main() {
    // Test 1: Odd length
    int a1[] = {1, 2, 3, 4, 5};
    ListNode* h1 = buildList(a1, 5);
    cout << "Test 1 (odd): Middle = " << findMiddle(h1)->val << endl;
    // Expected: 3

    // Test 2: Even length (returns second middle)
    int a2[] = {1, 2, 3, 4, 5, 6};
    ListNode* h2 = buildList(a2, 6);
    cout << "Test 2 (even, second middle): " << findMiddle(h2)->val << endl;
    // Expected: 4
    cout << "Test 2 (even, first middle): " << findFirstMiddle(h2)->val << endl;
    // Expected: 3

    // Test 3: Single element
    int a3[] = {42};
    ListNode* h3 = buildList(a3, 1);
    cout << "Test 3 (single): Middle = " << findMiddle(h3)->val << endl;
    // Expected: 42

    // Test 4: Two elements
    int a4[] = {1, 2};
    ListNode* h4 = buildList(a4, 2);
    cout << "Test 4 (two elements): Middle = " << findMiddle(h4)->val << endl;
    // Expected: 2

    return 0;
}
```

### Dry Run

```
List: 1 -> 2 -> 3 -> 4 -> 5

Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=5
fast->next = null => STOP

Middle = slow = 3
```

```
List: 1 -> 2 -> 3 -> 4 -> 5 -> 6

Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=5
Step 3: slow=4, fast=null (went past 6)
fast = null => STOP

Second middle = 4
```

### Complexity Analysis

- **Time:** O(n) -- fast pointer traverses the list once
- **Space:** O(1) -- only two pointers

## Approach 2: Count Then Traverse

### C++ Code

```cpp
ListNode* findMiddleTwoPass(ListNode* head) {
    int count = 0;
    ListNode* curr = head;
    while (curr) {
        count++;
        curr = curr->next;
    }
    curr = head;
    for (int i = 0; i < count / 2; i++) {
        curr = curr->next;
    }
    return curr;
}
```

### Complexity Analysis

- **Time:** O(n) -- two passes
- **Space:** O(1)

## Common Mistakes

1. Confusing which middle to return for even-length lists (first vs second)
2. Not handling single-node lists
3. Off-by-one errors in the while condition (`fast->next` vs `fast->next->next`)

## Interview Tips

- The slow/fast pointer technique is a fundamental pattern -- master it
- This is used as a subroutine in merge sort for linked lists and palindrome checking
- Clarify with the interviewer which middle to return for even-length lists
- This pattern is also called the "tortoise and hare" technique
