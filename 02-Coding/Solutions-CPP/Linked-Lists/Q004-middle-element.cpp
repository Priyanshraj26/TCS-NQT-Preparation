/*
 * Q004: Find Middle Element of Linked List
 * Question: DSA-Questions/Linked-Lists/Q004-middle-element.md
 *
 * Approach Overview:
 * +---------------------+----------+---------+
 * | Approach            | Time     | Space   |
 * +---------------------+----------+---------+
 * | Two-pass (count)    | O(n)     | O(1)    |
 * | Slow-Fast pointer   | O(n)     | O(1)    |
 * +---------------------+----------+---------+
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

void freeList(ListNode* head) {
    while (head) { ListNode* t = head; head = head->next; delete t; }
}

// ==================== Approach 1: Two-Pass (Brute Force) ====================
ListNode* middleBruteForce(ListNode* head) {
    int count = 0;
    ListNode* curr = head;
    while (curr) { count++; curr = curr->next; }

    curr = head;
    for (int i = 0; i < count / 2; i++) {
        curr = curr->next;
    }
    return curr;
}

// ==================== Approach 2: Slow-Fast Pointer (Optimal) ====================
/*
 * Slow moves 1 step, fast moves 2 steps.
 * When fast reaches end, slow is at the middle.
 *
 * Dry Run (odd): 1 -> 2 -> 3 -> 4 -> 5
 *   Start: slow=1, fast=1
 *   Step 1: slow=2, fast=3
 *   Step 2: slow=3, fast=5
 *   fast->next is NULL, stop. Return slow = 3 (correct!)
 *
 * Dry Run (even): 1 -> 2 -> 3 -> 4 -> 5 -> 6
 *   Start: slow=1, fast=1
 *   Step 1: slow=2, fast=3
 *   Step 2: slow=3, fast=5
 *   Step 3: slow=4, fast=NULL (fast went past end)
 *   fast is NULL, stop. Return slow = 4 (second middle, correct!)
 */
ListNode* middleOptimal(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}

int main() {
    // Test Case 1: Odd length
    cout << "=== Test Case 1: Odd length ===" << endl;
    vector<int> a1 = {1, 2, 3, 4, 5};
    ListNode* h1 = createList(a1);
    ListNode* mid = middleOptimal(h1);
    cout << "List: 1->2->3->4->5" << endl;
    cout << "Middle: " << mid->val << endl;  // Expected: 3
    freeList(h1);

    // Test Case 2: Even length
    cout << "\n=== Test Case 2: Even length ===" << endl;
    vector<int> a2 = {1, 2, 3, 4, 5, 6};
    ListNode* h2 = createList(a2);
    mid = middleOptimal(h2);
    cout << "List: 1->2->3->4->5->6" << endl;
    cout << "Middle: " << mid->val << endl;  // Expected: 4
    freeList(h2);

    // Test Case 3: Single element
    cout << "\n=== Test Case 3: Single element ===" << endl;
    vector<int> a3 = {1};
    ListNode* h3 = createList(a3);
    mid = middleOptimal(h3);
    cout << "Middle: " << mid->val << endl;  // Expected: 1
    freeList(h3);

    // Test Case 4: Two elements
    cout << "\n=== Test Case 4: Two elements ===" << endl;
    vector<int> a4 = {1, 2};
    ListNode* h4 = createList(a4);
    mid = middleOptimal(h4);
    cout << "Middle: " << mid->val << endl;  // Expected: 2
    freeList(h4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Both approaches: O(n) time, O(1) space
 * - Slow-fast is preferred: single pass, elegant
 *
 * Common Mistakes:
 * 1. Off-by-one error for even-length lists (returning first vs second middle)
 * 2. Not handling single-node lists
 *
 * Interview Tips:
 * - The slow-fast pointer technique is used in MANY linked list problems
 * - For "first middle" (even list), check fast->next->next instead
 * - This is a building block for palindrome check and merge sort
 */
