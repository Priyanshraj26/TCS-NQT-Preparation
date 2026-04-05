# Solution: Palindrome Linked List

[← Back to Question](../../DSA-Questions/Linked-Lists/Q006-palindrome-linked-list.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Reverse second half and compare | O(n) | O(1) | Yes (interviews) |
| Stack-based | O(n) | O(n) | Simpler |

## Approach 1: Reverse Second Half and Compare

### Intuition

1. Find the middle of the list using slow/fast pointers.
2. Reverse the second half of the list.
3. Compare the first half with the reversed second half node by node.
4. (Optional) Restore the list by reversing the second half again.

### C++ Code

```cpp
#include <iostream>
#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

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

bool isPalindrome(ListNode* head) {
    if (!head || !head->next) return true;

    // Step 1: Find middle (slow ends at second middle for even lists)
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Step 2: Reverse second half
    ListNode* secondHalf = reverseList(slow);

    // Step 3: Compare
    ListNode* firstHalf = head;
    ListNode* secondCopy = secondHalf; // save for restoration
    bool result = true;
    while (secondHalf) {
        if (firstHalf->val != secondHalf->val) {
            result = false;
            break;
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }

    // Step 4: Restore (optional but good practice)
    reverseList(secondCopy);

    return result;
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

int main() {
    // Test 1: Odd palindrome
    int a1[] = {1, 2, 3, 2, 1};
    cout << "Test 1 (1,2,3,2,1): " << (isPalindrome(buildList(a1, 5)) ? "true" : "false") << endl;
    // Expected: true

    // Test 2: Even palindrome
    int a2[] = {1, 2, 2, 1};
    cout << "Test 2 (1,2,2,1): " << (isPalindrome(buildList(a2, 4)) ? "true" : "false") << endl;
    // Expected: true

    // Test 3: Not a palindrome
    int a3[] = {1, 2, 3};
    cout << "Test 3 (1,2,3): " << (isPalindrome(buildList(a3, 3)) ? "true" : "false") << endl;
    // Expected: false

    // Test 4: Single element
    int a4[] = {1};
    cout << "Test 4 (1): " << (isPalindrome(buildList(a4, 1)) ? "true" : "false") << endl;
    // Expected: true

    // Test 5: Two same elements
    int a5[] = {1, 1};
    cout << "Test 5 (1,1): " << (isPalindrome(buildList(a5, 2)) ? "true" : "false") << endl;
    // Expected: true

    // Test 6: Two different elements
    int a6[] = {1, 2};
    cout << "Test 6 (1,2): " << (isPalindrome(buildList(a6, 2)) ? "true" : "false") << endl;
    // Expected: false

    return 0;
}
```

### Dry Run

```
List: 1 -> 2 -> 3 -> 2 -> 1

Step 1 - Find middle:
  slow=1,fast=1 -> slow=2,fast=3 -> slow=3,fast=1(end)
  Middle = 3

Step 2 - Reverse from 3: 1 -> 2 -> 3 <- 2 <- 1
  Second half reversed: 1 -> 2 -> 3

Step 3 - Compare:
  first=1, second=1 => match
  first=2, second=2 => match
  first=3, second=3 => match
  second=null => DONE, palindrome = true
```

### Complexity Analysis

- **Time:** O(n) -- finding middle O(n) + reverse O(n/2) + compare O(n/2)
- **Space:** O(1) -- in-place reversal

## Approach 2: Stack-Based

### C++ Code

```cpp
bool isPalindromeStack(ListNode* head) {
    stack<int> st;
    ListNode* curr = head;
    while (curr) {
        st.push(curr->val);
        curr = curr->next;
    }
    curr = head;
    while (curr) {
        if (curr->val != st.top()) return false;
        st.pop();
        curr = curr->next;
    }
    return true;
}
```

### Complexity Analysis

- **Time:** O(n)
- **Space:** O(n) -- stack stores all values

## Common Mistakes

1. Not handling even vs odd length lists correctly when finding the middle
2. Forgetting to restore the list after checking (can cause issues if list is used later)
3. Comparing wrong halves or off-by-one in the comparison loop

## Interview Tips

- The O(1) space approach combines three fundamental techniques: finding middle, reversing a list, and comparing two lists
- Mention that the list is temporarily modified -- in a multi-threaded environment this could be a concern
- Always ask if the list needs to be preserved after the check
