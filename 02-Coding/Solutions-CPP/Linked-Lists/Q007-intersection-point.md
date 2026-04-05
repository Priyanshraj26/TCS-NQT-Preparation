# Solution: Intersection Point of Two Linked Lists

[← Back to Question](../../DSA-Questions/Linked-Lists/Q007-intersection-point.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Two pointer (switch heads) | O(n + m) | O(1) | Yes (elegant) |
| Length difference technique | O(n + m) | O(1) | Also good |
| Hash Set | O(n + m) | O(n) | Simple but extra space |

## Approach 1: Two Pointer (Switch Heads)

### Intuition

Use two pointers starting at the heads of both lists. When a pointer reaches the end of its list, redirect it to the head of the other list. Both pointers traverse the same total distance (lenA + lenB), so they will meet at the intersection point (or both reach `nullptr` if no intersection).

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

// --- Two Pointer Switch Heads ---
ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
    if (!headA || !headB) return nullptr;
    ListNode* pA = headA;
    ListNode* pB = headB;
    while (pA != pB) {
        pA = pA ? pA->next : headB;
        pB = pB ? pB->next : headA;
    }
    return pA; // either intersection node or nullptr
}

int main() {
    // Test 1: Lists intersect
    // A: 1 -> 2 -\
    //              -> 6 -> 7
    // B: 3 -> 4 -> 5 -/
    ListNode* common = new ListNode(6);
    common->next = new ListNode(7);

    ListNode* headA = new ListNode(1);
    headA->next = new ListNode(2);
    headA->next->next = common;

    ListNode* headB = new ListNode(3);
    headB->next = new ListNode(4);
    headB->next->next = new ListNode(5);
    headB->next->next->next = common;

    ListNode* result = getIntersectionNode(headA, headB);
    cout << "Test 1: Intersection at " << (result ? to_string(result->val) : "null") << endl;
    // Expected: 6

    // Test 2: No intersection
    ListNode* a = new ListNode(1);
    a->next = new ListNode(2);
    ListNode* b = new ListNode(3);
    b->next = new ListNode(4);
    result = getIntersectionNode(a, b);
    cout << "Test 2: " << (result ? to_string(result->val) : "null") << endl;
    // Expected: null

    // Test 3: One list is empty
    result = getIntersectionNode(nullptr, headB);
    cout << "Test 3: " << (result ? to_string(result->val) : "null") << endl;
    // Expected: null

    // Test 4: Intersection at head
    ListNode* shared = new ListNode(10);
    shared->next = new ListNode(20);
    result = getIntersectionNode(shared, shared);
    cout << "Test 4: Intersection at " << (result ? to_string(result->val) : "null") << endl;
    // Expected: 10

    return 0;
}
```

### Dry Run

```
A: 1 -> 2 -> 6 -> 7       (length 4)
B: 3 -> 4 -> 5 -> 6 -> 7  (length 5)

pA=1, pB=3
pA=2, pB=4
pA=6, pB=5
pA=7, pB=6
pA=null, pB=7
pA=headB=3, pB=null
pA=4, pB=headA=1
pA=5, pB=2
pA=6, pB=6  => pA == pB => INTERSECTION at 6

Total steps each: 4 + 5 = 9 (same for both)
```

### Complexity Analysis

- **Time:** O(n + m) -- each pointer traverses at most n + m nodes
- **Space:** O(1)

## Approach 2: Length Difference

### C++ Code

```cpp
ListNode* getIntersectionByLength(ListNode* headA, ListNode* headB) {
    int lenA = 0, lenB = 0;
    ListNode* curr = headA;
    while (curr) { lenA++; curr = curr->next; }
    curr = headB;
    while (curr) { lenB++; curr = curr->next; }

    // Advance the longer list by the difference
    ListNode* pA = headA;
    ListNode* pB = headB;
    while (lenA > lenB) { pA = pA->next; lenA--; }
    while (lenB > lenA) { pB = pB->next; lenB--; }

    // Move together until they meet
    while (pA != pB) {
        pA = pA->next;
        pB = pB->next;
    }
    return pA;
}
```

### Complexity Analysis

- **Time:** O(n + m)
- **Space:** O(1)

## Common Mistakes

1. Comparing node values instead of node pointers -- two nodes can have the same value but be different
2. Infinite loop if you don't handle the no-intersection case (both must be allowed to become null)
3. In the switch-heads approach, using `pA->next` instead of `pA` in the null check -- this skips the null step and breaks the algorithm

## Interview Tips

- The two-pointer switch approach is elegant and impressive in interviews
- Explain the math: pointer A travels lenA + lenB, pointer B travels lenB + lenA -- equal total distance
- Clarify that intersection means the same node in memory, not just same value
- The Hash Set approach is a valid mention for showing alternatives
