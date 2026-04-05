/*
 * Q006: Check if Linked List is Palindrome
 * Question: DSA-Questions/Linked-Lists/Q006-palindrome-linked-list.md
 *
 * Approach Overview:
 * +---------------------------+----------+---------+
 * | Approach                  | Time     | Space   |
 * +---------------------------+----------+---------+
 * | Copy to array             | O(n)     | O(n)    |
 * | Reverse second half       | O(n)     | O(1)    |
 * +---------------------------+----------+---------+
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

// ==================== Approach 1: Copy to Array (Brute Force) ====================
bool isPalindromeBruteForce(ListNode* head) {
    vector<int> vals;
    while (head) {
        vals.push_back(head->val);
        head = head->next;
    }

    int left = 0, right = vals.size() - 1;
    while (left < right) {
        if (vals[left] != vals[right]) return false;
        left++;
        right--;
    }
    return true;
}

// ==================== Approach 2: Reverse Second Half (Optimal) ====================
/*
 * Steps:
 * 1. Find middle using slow-fast pointers
 * 2. Reverse the second half
 * 3. Compare first half with reversed second half
 * 4. (Optional) Restore the list
 *
 * Dry Run: 1 -> 2 -> 2 -> 1
 *   Middle: slow at node 2 (2nd node), fast at node 1 (4th node)
 *   Reverse from slow: 1 -> 2   and   1 -> 2
 *   Compare: 1==1, 2==2 => palindrome!
 */
ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    while (head) {
        ListNode* next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

bool isPalindromeOptimal(ListNode* head) {
    if (!head || !head->next) return true;

    // Step 1: Find middle
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Step 2: Reverse second half (starting from slow->next)
    ListNode* secondHalf = reverseList(slow->next);
    slow->next = nullptr;  // Cut the list

    // Step 3: Compare both halves
    ListNode* p1 = head;
    ListNode* p2 = secondHalf;
    bool result = true;
    while (p2) {
        if (p1->val != p2->val) {
            result = false;
            break;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    // Step 4: Restore (optional but good practice)
    slow->next = reverseList(secondHalf);

    return result;
}

int main() {
    // Test Case 1: Even palindrome
    cout << "=== Test Case 1 ===" << endl;
    vector<int> a1 = {1, 2, 2, 1};
    ListNode* h1 = createList(a1);
    cout << "1->2->2->1: " << (isPalindromeOptimal(h1) ? "true" : "false") << endl;
    freeList(h1);

    // Test Case 2: Not palindrome
    cout << "\n=== Test Case 2 ===" << endl;
    vector<int> a2 = {1, 2};
    ListNode* h2 = createList(a2);
    cout << "1->2: " << (isPalindromeOptimal(h2) ? "true" : "false") << endl;
    freeList(h2);

    // Test Case 3: Odd palindrome
    cout << "\n=== Test Case 3 ===" << endl;
    vector<int> a3 = {1, 2, 3, 2, 1};
    ListNode* h3 = createList(a3);
    cout << "1->2->3->2->1: " << (isPalindromeOptimal(h3) ? "true" : "false") << endl;
    freeList(h3);

    // Test Case 4: Single element
    cout << "\n=== Test Case 4 ===" << endl;
    vector<int> a4 = {1};
    ListNode* h4 = createList(a4);
    cout << "1: " << (isPalindromeOptimal(h4) ? "true" : "false") << endl;
    freeList(h4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Brute Force: O(n) time, O(n) space
 * - Optimal: O(n) time, O(1) space
 *
 * Common Mistakes:
 * 1. Getting the middle wrong for odd vs even length lists
 * 2. Forgetting to compare only the shorter half (second half may be 1 shorter)
 * 3. Not restoring the list (some problems require it)
 *
 * Interview Tips:
 * - This combines three techniques: find middle + reverse list + compare
 * - Practice each sub-problem separately first
 * - Mention the O(1) space advantage of the optimal approach
 */
