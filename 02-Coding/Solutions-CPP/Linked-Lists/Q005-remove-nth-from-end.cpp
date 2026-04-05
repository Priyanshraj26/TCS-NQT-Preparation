/*
 * Q005: Remove Nth Node from End of List
 * Question: DSA-Questions/Linked-Lists/Q005-remove-nth-from-end.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Two-pass         | O(n)     | O(1)    |
 * | One-pass         | O(n)     | O(1)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* createList(vector<int>& arr) {
    if (arr.empty()) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* curr = head;
    for (int i = 1; i < (int)arr.size(); i++) {
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
    cout << " -> NULL" << endl;
}

void freeList(ListNode* head) {
    while (head) { ListNode* t = head; head = head->next; delete t; }
}

// ==================== Approach 1: Two-Pass ====================
ListNode* removeNthTwoPass(ListNode* head, int n) {
    int len = 0;
    ListNode* curr = head;
    while (curr) { len++; curr = curr->next; }

    // If removing the head
    if (n == len) {
        ListNode* newHead = head->next;
        delete head;
        return newHead;
    }

    curr = head;
    for (int i = 1; i < len - n; i++) {
        curr = curr->next;
    }
    ListNode* toDelete = curr->next;
    curr->next = toDelete->next;
    delete toDelete;
    return head;
}

// ==================== Approach 2: One-Pass with Two Pointers (Optimal) ====================
/*
 * Use a dummy node + two pointers spaced n+1 apart.
 * When fast reaches NULL, slow is just before the target.
 *
 * Dry Run: 1->2->3->4->5, n=2
 *   dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL
 *   fast advances n+1=3 steps: fast at node 3
 *   Move both until fast=NULL:
 *     slow=1, fast=4
 *     slow=2, fast=5
 *     slow=3, fast=NULL => stop
 *   Remove slow->next (node 4): 1->2->3->5
 */
ListNode* removeNthOnePass(ListNode* head, int n) {
    ListNode dummy(0);
    dummy.next = head;
    ListNode* fast = &dummy;
    ListNode* slow = &dummy;

    // Advance fast by n+1 steps
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }

    // Move both until fast reaches end
    while (fast != nullptr) {
        fast = fast->next;
        slow = slow->next;
    }

    // Remove the node after slow
    ListNode* toDelete = slow->next;
    slow->next = toDelete->next;
    delete toDelete;

    return dummy.next;
}

int main() {
    // Test Case 1: Remove from middle
    cout << "=== Test Case 1 ===" << endl;
    vector<int> a1 = {1, 2, 3, 4, 5};
    ListNode* h1 = createList(a1);
    cout << "Original: "; printList(h1);
    h1 = removeNthOnePass(h1, 2);
    cout << "Remove 2nd from end: "; printList(h1);
    freeList(h1);

    // Test Case 2: Remove only element
    cout << "\n=== Test Case 2 ===" << endl;
    vector<int> a2 = {1};
    ListNode* h2 = createList(a2);
    h2 = removeNthOnePass(h2, 1);
    cout << "Remove 1st from end: ";
    if (!h2) cout << "NULL" << endl; else printList(h2);

    // Test Case 3: Remove head
    cout << "\n=== Test Case 3 ===" << endl;
    vector<int> a3 = {1, 2};
    ListNode* h3 = createList(a3);
    cout << "Original: "; printList(h3);
    h3 = removeNthOnePass(h3, 2);
    cout << "Remove 2nd from end (head): "; printList(h3);
    freeList(h3);

    // Test Case 4: Remove tail
    cout << "\n=== Test Case 4 ===" << endl;
    vector<int> a4 = {1, 2, 3};
    ListNode* h4 = createList(a4);
    cout << "Original: "; printList(h4);
    h4 = removeNthOnePass(h4, 1);
    cout << "Remove 1st from end (tail): "; printList(h4);
    freeList(h4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Both approaches: O(n) time, O(1) space
 * - One-pass is preferred in interviews for elegance
 *
 * Common Mistakes:
 * 1. Off-by-one: not using dummy node and failing when removing the head
 * 2. Advancing fast by n instead of n+1 (slow ends up ON the target, not before it)
 * 3. Not handling edge case: single node list
 *
 * Interview Tips:
 * - The dummy node trick is essential -- avoids special-casing head removal
 * - Mention that you can do it in one pass to impress the interviewer
 * - Clarify: is n guaranteed to be valid? (usually yes)
 */
