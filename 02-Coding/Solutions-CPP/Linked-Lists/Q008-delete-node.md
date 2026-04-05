# Solution: Delete Node Without Head Pointer

[← Back to Question](../../DSA-Questions/Linked-Lists/Q008-delete-node.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Copy next node's data and delete next | O(1) | O(1) | Yes (only way) |

## Approach 1: Copy and Delete Next

### Intuition

Since we don't have access to the previous node, we cannot unlink the given node directly. Instead, copy the value from the next node into the current node, then delete the next node. This effectively "becomes" the next node.

**Constraint:** This approach cannot delete the last node (it has no next node to copy from).

### C++ Code

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// --- Delete node (given only pointer to that node) ---
void deleteNode(ListNode* node) {
    // Assumption: node is NOT the last node
    ListNode* nextNode = node->next;
    node->val = nextNode->val;
    node->next = nextNode->next;
    delete nextNode;
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

// Helper: find node by value
ListNode* findNode(ListNode* head, int val) {
    while (head) {
        if (head->val == val) return head;
        head = head->next;
    }
    return nullptr;
}

int main() {
    // Test 1: Delete middle node
    int a1[] = {1, 2, 3, 4, 5};
    ListNode* h1 = buildList(a1, 5);
    cout << "Before: ";
    printList(h1);
    deleteNode(findNode(h1, 3));
    cout << "After deleting 3: ";
    printList(h1);
    // Expected: 1 -> 2 -> 4 -> 5

    // Test 2: Delete first node
    int a2[] = {10, 20, 30};
    ListNode* h2 = buildList(a2, 3);
    deleteNode(h2); // delete head node
    cout << "After deleting head (10): ";
    printList(h2);
    // Expected: 20 -> 30

    // Test 3: Delete second of two nodes
    // Note: cannot delete the LAST node with this technique
    int a3[] = {1, 2, 3};
    ListNode* h3 = buildList(a3, 3);
    deleteNode(findNode(h3, 2));
    cout << "After deleting 2: ";
    printList(h3);
    // Expected: 1 -> 3

    return 0;
}
```

### Dry Run

```
List: 1 -> 2 -> [3] -> 4 -> 5
Delete node with value 3.

Step 1: Copy next node's value (4) into current node
        1 -> 2 -> [4] -> 4 -> 5

Step 2: Point current node's next to next->next
        1 -> 2 -> [4] -> 5

Step 3: Free the old next node
        Result: 1 -> 2 -> 4 -> 5
```

### Complexity Analysis

- **Time:** O(1) -- constant time, no traversal needed
- **Space:** O(1)

## Common Mistakes

1. Trying to delete the last node -- this technique does not work for the tail
2. Not deleting (freeing) the next node after copying, causing a memory leak
3. Forgetting to update `node->next` to skip the next node
4. Assuming you need the head pointer -- this problem specifically gives you only the node to delete

## Interview Tips

- This is a classic trick question -- the key insight is "copy and delete next"
- Always mention the limitation: cannot delete the last node
- If the interviewer asks about deleting the last node, mention you would need to mark it as a "dummy" or sentinel, or you need the head pointer
- This is O(1) time which is the key advantage -- a normal linked list deletion is O(n) since you need to find the previous node
- Mention that this changes the node's identity -- if external code holds pointers to the "next" node, those pointers become dangling
