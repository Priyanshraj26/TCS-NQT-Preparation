# Solution: Validate Binary Search Tree

[← Back to Question](../../DSA-Questions/Trees/Q006-check-bst.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Min/Max range check | O(n) | O(h) | Yes (interviews) |
| Inorder traversal check | O(n) | O(h) | Also great |

## Approach 1: Min/Max Range Check

### Intuition

For every node, define a valid range (min, max). The root can be anything. For the left child, the max is the parent's value. For the right child, the min is the parent's value. If any node violates its range, it is not a valid BST.

### C++ Code

```cpp
#include <iostream>
#include <climits>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Min/Max Range Approach ---
bool isValidBSTHelper(TreeNode* root, long long minVal, long long maxVal) {
    if (!root) return true;
    if (root->val <= minVal || root->val >= maxVal) return false;
    return isValidBSTHelper(root->left, minVal, root->val) &&
           isValidBSTHelper(root->right, root->val, maxVal);
}

bool isValidBST(TreeNode* root) {
    return isValidBSTHelper(root, LLONG_MIN, LLONG_MAX);
}

// --- Inorder Traversal Approach ---
bool isValidBSTInorder(TreeNode* root) {
    stack<TreeNode*> st;
    TreeNode* curr = root;
    TreeNode* prev = nullptr;

    while (curr || !st.empty()) {
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        curr = st.top();
        st.pop();
        // Inorder should be strictly increasing
        if (prev && curr->val <= prev->val) return false;
        prev = curr;
        curr = curr->right;
    }
    return true;
}

int main() {
    // Test 1: Valid BST
    //       5
    //      / \
    //     3   7
    //    / \ / \
    //   1  4 6  8
    TreeNode* t1 = new TreeNode(5);
    t1->left = new TreeNode(3);
    t1->right = new TreeNode(7);
    t1->left->left = new TreeNode(1);
    t1->left->right = new TreeNode(4);
    t1->right->left = new TreeNode(6);
    t1->right->right = new TreeNode(8);
    cout << "Test 1 (valid BST): " << (isValidBST(t1) ? "true" : "false") << endl;
    // Expected: true
    cout << "Test 1 (inorder):   " << (isValidBSTInorder(t1) ? "true" : "false") << endl;

    // Test 2: Invalid BST (4 is in right subtree of 5 but is less than 5)
    //       5
    //      / \
    //     1   6
    //        / \
    //       4   7    <- 4 < 5 but in right subtree!
    TreeNode* t2 = new TreeNode(5);
    t2->left = new TreeNode(1);
    t2->right = new TreeNode(6);
    t2->right->left = new TreeNode(4);
    t2->right->right = new TreeNode(7);
    cout << "Test 2 (invalid): " << (isValidBST(t2) ? "true" : "false") << endl;
    // Expected: false

    // Test 3: Single node
    cout << "Test 3 (single): " << (isValidBST(new TreeNode(1)) ? "true" : "false") << endl;
    // Expected: true

    // Test 4: Empty tree
    cout << "Test 4 (empty): " << (isValidBST(nullptr) ? "true" : "false") << endl;
    // Expected: true

    // Test 5: Equal values (not a valid BST)
    //    2
    //   / \
    //  2   2
    TreeNode* t5 = new TreeNode(2);
    t5->left = new TreeNode(2);
    t5->right = new TreeNode(2);
    cout << "Test 5 (equal vals): " << (isValidBST(t5) ? "true" : "false") << endl;
    // Expected: false (BST requires strictly less/greater)

    return 0;
}
```

### Dry Run

```
Tree:     5
         / \
        3   7

isValidBSTHelper(5, -INF, +INF) -> 5 in range? yes
  isValidBSTHelper(3, -INF, 5) -> 3 in range? yes
    isValidBSTHelper(null) -> true
    isValidBSTHelper(null) -> true
  isValidBSTHelper(7, 5, +INF) -> 7 in range? yes
    isValidBSTHelper(null) -> true
    isValidBSTHelper(null) -> true
All true => valid BST
```

### Complexity Analysis

- **Time:** O(n) -- visits every node once
- **Space:** O(h) -- recursion stack depth

## Common Mistakes

1. Only checking if left child < parent and right child > parent -- must check against the ENTIRE valid range
2. Using `int` for min/max bounds when node values can be INT_MIN or INT_MAX -- use `long long`
3. Not handling equal values correctly (BST typically requires strict inequality)
4. The tricky case: a node might be valid relative to its parent but invalid relative to a grandparent

## Interview Tips

- The min/max approach is cleaner and preferred for interviews
- The inorder approach is elegant: "a BST's inorder traversal is sorted"
- Always clarify: are duplicate values allowed? (usually not in standard BST)
- Use `long long` for bounds to avoid overflow with INT_MIN/INT_MAX node values
