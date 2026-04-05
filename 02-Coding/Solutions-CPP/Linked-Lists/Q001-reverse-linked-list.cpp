/*
 * Q001: Reverse a Linked List
 * Question: DSA-Questions/Linked-Lists/Q001-reverse-linked-list.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Iterative        | O(n)     | O(1)    |
 * | Recursive        | O(n)     | O(n)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
using namespace std;

// ==================== ListNode Definition ====================
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// ==================== Helper Functions ====================
ListNode* createList(vector<int>& arr) {
    if (arr.empty()) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* curr = head;
    for (int i = 1; i < arr.size(); i++) {
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
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

// ==================== Approach 1: Iterative (Optimal) ====================
/*
 * Idea: Use three pointers (prev, curr, next).
 * At each step, reverse the current node's pointer to point to prev.
 *
 * Dry Run: 1 -> 2 -> 3 -> NULL
 *   Step 0: prev=NULL, curr=1
 *   Step 1: next=2, 1->NULL, prev=1, curr=2
 *   Step 2: next=3, 2->1, prev=2, curr=3
 *   Step 3: next=NULL, 3->2, prev=3, curr=NULL
 *   Return prev = 3 -> 2 -> 1 -> NULL
 */
ListNode* reverseIterative(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;

    while (curr != nullptr) {
        ListNode* next = curr->next;  // Save next
        curr->next = prev;            // Reverse link
        prev = curr;                  // Move prev forward
        curr = next;                  // Move curr forward
    }

    return prev;  // prev is the new head
}

// ==================== Approach 2: Recursive ====================
/*
 * Idea: Recursively reverse the rest of the list, then fix the head pointer.
 *
 * For list 1 -> 2 -> 3:
 *   reverse(1): calls reverse(2)
 *     reverse(2): calls reverse(3)
 *       reverse(3): base case, return 3
 *     Now: 3 -> NULL, fix: 2->next->next = 2, so 3->2, set 2->next = NULL
 *     Return 3 (new head)
 *   Now: 3 -> 2 -> NULL, fix: 1->next->next = 1, so 2->1, set 1->next = NULL
 *   Return 3 (new head)
 * Result: 3 -> 2 -> 1 -> NULL
 */
ListNode* reverseRecursive(ListNode* head) {
    // Base case: empty list or single node
    if (head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode* newHead = reverseRecursive(head->next);
    head->next->next = head;  // Make next node point back to current
    head->next = nullptr;     // Remove old forward link

    return newHead;
}

// ==================== Main with Test Cases ====================
int main() {
    // Test Case 1: Normal list
    cout << "=== Test Case 1 ===" << endl;
    vector<int> arr1 = {1, 2, 3, 4, 5};
    ListNode* head1 = createList(arr1);
    cout << "Original: ";
    printList(head1);
    head1 = reverseIterative(head1);
    cout << "Reversed (Iterative): ";
    printList(head1);
    freeList(head1);

    // Test Case 2: Two elements
    cout << "\n=== Test Case 2 ===" << endl;
    vector<int> arr2 = {1, 2};
    ListNode* head2 = createList(arr2);
    cout << "Original: ";
    printList(head2);
    head2 = reverseRecursive(head2);
    cout << "Reversed (Recursive): ";
    printList(head2);
    freeList(head2);

    // Test Case 3: Single element
    cout << "\n=== Test Case 3 ===" << endl;
    vector<int> arr3 = {1};
    ListNode* head3 = createList(arr3);
    cout << "Original: ";
    printList(head3);
    head3 = reverseIterative(head3);
    cout << "Reversed: ";
    printList(head3);
    freeList(head3);

    // Test Case 4: Empty list
    cout << "\n=== Test Case 4 ===" << endl;
    ListNode* head4 = nullptr;
    cout << "Original: NULL" << endl;
    head4 = reverseIterative(head4);
    cout << "Reversed: ";
    if (!head4) cout << "NULL" << endl;

    return 0;
}

/*
 * Complexity Analysis:
 * - Iterative: Time O(n), Space O(1) -- best for interviews
 * - Recursive: Time O(n), Space O(n) due to call stack
 *
 * Common Mistakes:
 * 1. Forgetting to save curr->next before reversing the link
 * 2. Not handling empty list or single node
 * 3. Returning head instead of prev in iterative approach
 *
 * Interview Tips:
 * - Start with the iterative approach -- it's O(1) space and interviewers prefer it
 * - Draw the pointer changes on paper before coding
 * - Mention both approaches to show breadth of knowledge
 * - This is the MOST frequently asked linked list question
 */
