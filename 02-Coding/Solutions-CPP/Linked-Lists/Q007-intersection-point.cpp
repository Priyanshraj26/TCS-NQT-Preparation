/*
 * Q007: Intersection Point of Two Linked Lists
 * Question: DSA-Questions/Linked-Lists/Q007-intersection-point.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Brute Force      | O(m*n)   | O(1)    |
 * | Hash Set         | O(m+n)   | O(m)    |
 * | Two Pointers     | O(m+n)   | O(1)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// ==================== Approach 1: Hash Set ====================
ListNode* intersectionHashSet(ListNode* headA, ListNode* headB) {
    unordered_set<ListNode*> visited;
    while (headA) {
        visited.insert(headA);
        headA = headA->next;
    }
    while (headB) {
        if (visited.count(headB)) return headB;
        headB = headB->next;
    }
    return nullptr;
}

// ==================== Approach 2: Two Pointers (Optimal) ====================
/*
 * Idea: Pointer A traverses listA then listB. Pointer B traverses listB then listA.
 * Both travel the same total distance (m + n). If lists intersect, they will
 * meet at the intersection. If not, both reach NULL simultaneously.
 *
 * Dry Run: A = 4->1->8->4->5, B = 5->6->1->8->4->5 (intersect at 8)
 *   pA: 4,1,8,4,5,NULL,5,6,1,8  <-- meets here
 *   pB: 5,6,1,8,4,5,NULL,4,1,8  <-- meets here
 *   Both travel 10 steps total, meet at node 8.
 */
ListNode* intersectionTwoPointers(ListNode* headA, ListNode* headB) {
    if (!headA || !headB) return nullptr;

    ListNode* pA = headA;
    ListNode* pB = headB;

    while (pA != pB) {
        pA = pA ? pA->next : headB;
        pB = pB ? pB->next : headA;
    }

    return pA;  // Either intersection node or NULL
}

int main() {
    // Test Case 1: Lists intersect at node with value 8
    cout << "=== Test Case 1: Intersection exists ===" << endl;
    // Common part: 8 -> 4 -> 5
    ListNode* common = new ListNode(8);
    common->next = new ListNode(4);
    common->next->next = new ListNode(5);

    // List A: 4 -> 1 -> [8 -> 4 -> 5]
    ListNode* headA = new ListNode(4);
    headA->next = new ListNode(1);
    headA->next->next = common;

    // List B: 5 -> 6 -> 1 -> [8 -> 4 -> 5]
    ListNode* headB = new ListNode(5);
    headB->next = new ListNode(6);
    headB->next->next = new ListNode(1);
    headB->next->next->next = common;

    ListNode* result = intersectionTwoPointers(headA, headB);
    cout << "Intersection at: " << (result ? to_string(result->val) : "NULL") << endl;

    // Test Case 2: No intersection
    cout << "\n=== Test Case 2: No intersection ===" << endl;
    ListNode* h1 = new ListNode(2);
    h1->next = new ListNode(6);
    h1->next->next = new ListNode(4);

    ListNode* h2 = new ListNode(1);
    h2->next = new ListNode(5);

    result = intersectionTwoPointers(h1, h2);
    cout << "Intersection at: " << (result ? to_string(result->val) : "NULL") << endl;

    // Cleanup (simplified -- not freeing shared nodes twice)
    delete headA->next; delete headA;
    delete headB->next->next; delete headB->next; delete headB;
    delete common->next->next; delete common->next; delete common;
    delete h1->next->next; delete h1->next; delete h1;
    delete h2->next; delete h2;

    return 0;
}

/*
 * Complexity Analysis:
 * - Two Pointers: O(m+n) time, O(1) space -- best approach
 * - Hash Set: O(m+n) time, O(m) space
 *
 * Common Mistakes:
 * 1. Comparing node VALUES instead of node POINTERS (two nodes can have same value but be different)
 * 2. Infinite loop if not handling the NULL redirect correctly
 * 3. Forgetting that intersection means shared nodes from that point onwards
 *
 * Interview Tips:
 * - The two-pointer trick is elegant and often impresses interviewers
 * - Explain WHY it works: both pointers travel m+n distance
 * - Clarify: intersection means same NODE (by reference), not same value
 */
