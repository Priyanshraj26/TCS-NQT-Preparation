/*
 * Q008: Delete a Node (Given Only Pointer to It)
 * Question: DSA-Questions/Linked-Lists/Q008-delete-node.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Copy and Delete  | O(1)     | O(1)    |
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

// ==================== Approach: Copy and Delete (Only Approach) ====================
/*
 * Since we don't have access to the previous node, we can't do a traditional delete.
 * Trick: Copy the next node's value into the current node, then delete the next node.
 *
 * Dry Run: 4 -> 5 -> 1 -> 9, delete node 5
 *   Copy next value: node becomes 4 -> 1 -> 1 -> 9
 *   Delete next node: 4 -> 1 -> 9
 *   Done! Effectively "deleted" node 5.
 *
 * Note: This doesn't work for the tail node (no next to copy from).
 */
void deleteNode(ListNode* node) {
    // Copy next node's value
    node->val = node->next->val;
    // Delete next node
    ListNode* toDelete = node->next;
    node->next = toDelete->next;
    delete toDelete;
}

int main() {
    // Test Case 1: Delete node 5
    cout << "=== Test Case 1 ===" << endl;
    vector<int> a1 = {4, 5, 1, 9};
    ListNode* h1 = createList(a1);
    cout << "Before: "; printList(h1);
    // Find node with value 5
    ListNode* nodeToDelete = h1->next;  // node 5
    deleteNode(nodeToDelete);
    cout << "After deleting 5: "; printList(h1);
    freeList(h1);

    // Test Case 2: Delete node 1
    cout << "\n=== Test Case 2 ===" << endl;
    vector<int> a2 = {4, 5, 1, 9};
    ListNode* h2 = createList(a2);
    cout << "Before: "; printList(h2);
    nodeToDelete = h2->next->next;  // node 1
    deleteNode(nodeToDelete);
    cout << "After deleting 1: "; printList(h2);
    freeList(h2);

    // Test Case 3: Delete head's next (first non-head)
    cout << "\n=== Test Case 3 ===" << endl;
    vector<int> a3 = {1, 2, 3};
    ListNode* h3 = createList(a3);
    cout << "Before: "; printList(h3);
    deleteNode(h3);  // delete head node (value 1)
    cout << "After deleting head: "; printList(h3);
    freeList(h3);

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(1), Space: O(1)
 *
 * Common Mistakes:
 * 1. Trying to traverse from head (you don't have head!)
 * 2. Forgetting that this doesn't work for tail nodes
 * 3. Memory leak: not deleting the next node after copying
 *
 * Interview Tips:
 * - This is a trick question -- the "aha!" moment is realizing you copy, not traverse
 * - Mention the limitation: cannot delete the tail node
 * - Some interviewers ask "is the node truly deleted?" -- technically no,
 *   you deleted the NEXT node but it appears the same from outside
 */
