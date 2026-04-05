# Solution: Preorder Traversal of Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q002-preorder-traversal.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive | O(n) | O(h) stack | Easy to write |
| Iterative (stack) | O(n) | O(h) | Yes (interviews) |

## Approach 1: Recursive

### Intuition

Preorder visits: Root first, then Left subtree, then Right subtree. This is useful for creating a copy of the tree or serializing it.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Recursive ---
void preorderRecursive(TreeNode* root, vector<int>& result) {
    if (!root) return;
    result.push_back(root->val);
    preorderRecursive(root->left, result);
    preorderRecursive(root->right, result);
}

// --- Iterative (stack) ---
vector<int> preorderIterative(TreeNode* root) {
    vector<int> result;
    if (!root) return result;

    stack<TreeNode*> st;
    st.push(root);

    while (!st.empty()) {
        TreeNode* node = st.top();
        st.pop();
        result.push_back(node->val);
        // Push right first so left is processed first (LIFO)
        if (node->right) st.push(node->right);
        if (node->left) st.push(node->left);
    }
    return result;
}

void printVector(const vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    //       1
    //      / \
    //     2   3
    //    / \   \
    //   4   5   6
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(6);

    // Test 1: Recursive
    vector<int> res1;
    preorderRecursive(root, res1);
    cout << "Recursive: ";
    printVector(res1);
    // Expected: [1, 2, 4, 5, 3, 6]

    // Test 2: Iterative
    cout << "Iterative: ";
    printVector(preorderIterative(root));
    // Expected: [1, 2, 4, 5, 3, 6]

    // Test 3: Empty tree
    cout << "Empty: ";
    printVector(preorderIterative(nullptr));
    // Expected: []

    // Test 4: Single node
    cout << "Single: ";
    printVector(preorderIterative(new TreeNode(99)));
    // Expected: [99]

    // Test 5: Right-skewed
    TreeNode* skew = new TreeNode(1);
    skew->right = new TreeNode(2);
    skew->right->right = new TreeNode(3);
    cout << "Right-skewed: ";
    printVector(preorderIterative(skew));
    // Expected: [1, 2, 3]

    return 0;
}
```

### Dry Run (Iterative)

```
Tree:     1
         / \
        2   3

Stack: [1]
Pop 1, add 1. Push right(3), left(2). Stack: [3, 2]
Pop 2, add 2. No children. Stack: [3]
Pop 3, add 3. No children. Stack: []

Result: [1, 2, 3]
```

### Complexity Analysis

- **Time:** O(n) -- every node visited once
- **Space:** O(h) -- stack depth is the height of the tree

## Common Mistakes

1. In the iterative version, pushing left before right -- this processes right first due to LIFO
2. Not checking for null children before pushing to stack
3. Confusing preorder with inorder -- remember: preorder processes root FIRST

## Interview Tips

- Preorder iterative is the simplest of the three iterative traversals
- The key trick: push right child first, then left, so left is popped first
- Preorder is used in: tree serialization, copying trees, prefix expression evaluation
- Always mention both recursive and iterative to show completeness
