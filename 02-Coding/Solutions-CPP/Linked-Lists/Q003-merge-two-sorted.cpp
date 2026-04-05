/*
 * Q003: Merge Two Sorted Linked Lists
 * Question: DSA-Questions/Linked-Lists/Q003-merge-two-sorted.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Iterative        | O(n+m)   | O(1)    |
 * | Recursive        | O(n+m)   | O(n+m)  |
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
    while (head) {
        ListNode* t = head; head = head->next; delete t;
    }
}

// ==================== Approach 1: Iterative (Optimal) ====================
/*
 * Use a dummy node as the starting point. Compare heads of both lists,
 * attach the smaller one, and advance that list's pointer.
 *
 * Dry Run: list1 = 1->2->4, list2 = 1->3->4
 *   dummy -> 1(L1) -> 1(L2) -> 2(L1) -> 3(L2) -> 4(L1) -> 4(L2) -> NULL
 */
ListNode* mergeIterative(ListNode* l1, ListNode* l2) {
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

    // Attach remaining nodes
    tail->next = l1 ? l1 : l2;

    return dummy.next;
}

// ==================== Approach 2: Recursive ====================
/*
 * Compare heads: the smaller one becomes the head of the merged list.
 * Recursively merge the rest.
 */
ListNode* mergeRecursive(ListNode* l1, ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;

    if (l1->val <= l2->val) {
        l1->next = mergeRecursive(l1->next, l2);
        return l1;
    } else {
        l2->next = mergeRecursive(l1, l2->next);
        return l2;
    }
}

int main() {
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    vector<int> a1 = {1, 2, 4}, b1 = {1, 3, 4};
    ListNode* l1 = createList(a1);
    ListNode* l2 = createList(b1);
    cout << "List1: "; printList(l1);
    cout << "List2: "; printList(l2);
    ListNode* merged = mergeIterative(l1, l2);
    cout << "Merged (Iterative): "; printList(merged);
    freeList(merged);

    // Test Case 2: One empty list
    cout << "\n=== Test Case 2 ===" << endl;
    vector<int> a2 = {}, b2 = {0};
    ListNode* l3 = createList(a2);
    ListNode* l4 = createList(b2);
    merged = mergeRecursive(l3, l4);
    cout << "Merged (Recursive): "; printList(merged);
    freeList(merged);

    // Test Case 3: Both empty
    cout << "\n=== Test Case 3 ===" << endl;
    merged = mergeIterative(nullptr, nullptr);
    cout << "Merged: ";
    if (!merged) cout << "NULL" << endl;

    // Test Case 4: Different lengths
    cout << "\n=== Test Case 4 ===" << endl;
    vector<int> a4 = {1, 5, 10}, b4 = {2, 3};
    ListNode* l5 = createList(a4);
    ListNode* l6 = createList(b4);
    merged = mergeIterative(l5, l6);
    cout << "Merged: "; printList(merged);
    freeList(merged);

    return 0;
}

/*
 * Complexity Analysis:
 * - Iterative: Time O(n+m), Space O(1) -- only rearranges pointers
 * - Recursive: Time O(n+m), Space O(n+m) due to recursion stack
 *
 * Common Mistakes:
 * 1. Forgetting to handle when one list is empty
 * 2. Not attaching the remaining list after one is exhausted
 * 3. Creating new nodes instead of reusing existing ones (wastes memory)
 *
 * Interview Tips:
 * - The dummy node trick avoids special-casing the head
 * - This is a building block for Merge Sort on linked lists
 * - Mention that iterative is better for space
 */
