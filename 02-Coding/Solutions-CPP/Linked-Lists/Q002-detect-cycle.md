# Solution: Detect Cycle in Linked List

[← Back to Question](../../DSA-Questions/Linked-Lists/Q002-detect-cycle.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Floyd's Cycle Detection (slow/fast) | O(n) | O(1) | Yes (interviews) |
| Hash Set | O(n) | O(n) | Simpler but more space |

## Approach 1: Floyd's Cycle Detection (Tortoise and Hare)

### Intuition

Use two pointers moving at different speeds. The slow pointer moves one step at a time, the fast pointer moves two steps. If there is a cycle, the fast pointer will eventually catch up to the slow pointer inside the cycle. If there is no cycle, the fast pointer reaches the end.

### C++ Code

```cpp
#include <iostream>
#include <unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// --- Floyd's Cycle Detection ---
bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

// --- Find the start of the cycle ---
ListNode* detectCycleStart(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            // Reset slow to head, move both one step at a time
            slow = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow; // start of cycle
        }
    }
    return nullptr; // no cycle
}

int main() {
    // Test 1: List with cycle
    // 1 -> 2 -> 3 -> 4 -> 2 (cycle back to node 2)
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    ListNode* n4 = new ListNode(4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n2; // cycle here
    cout << "Test 1 (has cycle): " << (hasCycle(n1) ? "true" : "false") << endl;
    // Expected: true
    ListNode* start = detectCycleStart(n1);
    cout << "Cycle starts at node with value: " << start->val << endl;
    // Expected: 2

    // Test 2: No cycle
    ListNode* a1 = new ListNode(1);
    ListNode* a2 = new ListNode(2);
    ListNode* a3 = new ListNode(3);
    a1->next = a2;
    a2->next = a3;
    cout << "Test 2 (no cycle): " << (hasCycle(a1) ? "true" : "false") << endl;
    // Expected: false

    // Test 3: Single node, no cycle
    ListNode* single = new ListNode(1);
    cout << "Test 3 (single node): " << (hasCycle(single) ? "true" : "false") << endl;
    // Expected: false

    // Test 4: Single node with self-loop
    ListNode* selfLoop = new ListNode(1);
    selfLoop->next = selfLoop;
    cout << "Test 4 (self-loop): " << (hasCycle(selfLoop) ? "true" : "false") << endl;
    // Expected: true

    // Test 5: Empty list
    cout << "Test 5 (empty): " << (hasCycle(nullptr) ? "true" : "false") << endl;
    // Expected: false

    return 0;
}
```

### Dry Run

```
List: 1 -> 2 -> 3 -> 4 -> (back to 2)

Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=2 (fast went 3->4->2)
Step 3: slow=4, fast=4 (fast went 2->3->4)
        slow == fast => CYCLE DETECTED

Finding cycle start:
  Reset slow=1, fast=4
  Step 1: slow=2, fast=2 (fast went 4->2)
  slow == fast => cycle starts at node 2
```

### Complexity Analysis

- **Time:** O(n) -- at most 2n steps before they meet
- **Space:** O(1) -- only two pointers

## Approach 2: Hash Set

### C++ Code

```cpp
bool hasCycleHashSet(ListNode* head) {
    unordered_set<ListNode*> visited;
    ListNode* curr = head;
    while (curr) {
        if (visited.count(curr)) return true;
        visited.insert(curr);
        curr = curr->next;
    }
    return false;
}
```

### Complexity Analysis

- **Time:** O(n)
- **Space:** O(n) -- stores all visited node addresses

## Common Mistakes

1. Checking `fast->next` without first checking `fast != nullptr`
2. Comparing node values instead of node pointers (two nodes can have the same value)
3. Moving both pointers at the same speed -- they will never meet in a cycle
4. Forgetting the edge case of an empty list or single node

## Interview Tips

- Always mention Floyd's algorithm by name -- it shows you know the classic technique
- Be ready to explain *why* the two pointers meet (math: the distance closes by 1 each step)
- The follow-up "find the start of the cycle" is very commonly asked
- Mention the Hash Set approach as a simpler alternative, then optimize to Floyd's
