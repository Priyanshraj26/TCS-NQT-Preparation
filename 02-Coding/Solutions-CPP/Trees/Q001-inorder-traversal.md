# Solution: Inorder Traversal of Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q001-inorder-traversal.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive | O(n) | O(h) stack | Easy to write |
| Iterative (stack) | O(n) | O(h) | Yes (interviews) |

## Approach 1: Recursive

### Intuition

Inorder traversal visits nodes in the order: Left subtree, Root, Right subtree. For a BST, this produces sorted output.

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
void inorderRecursive(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorderRecursive(root->left, result);
    result.push_back(root->val);
    inorderRecursive(root->right, result);
}

// --- Iterative (stack) ---
vector<int> inorderIterative(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> st;
    TreeNode* curr = root;

    while (curr || !st.empty()) {
        // Go all the way left
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        // Process the top
        curr = st.top();
        st.pop();
        result.push_back(curr->val);
        // Move to right subtree
        curr = curr->right;
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
    // Build tree:
    //       4
    //      / \
    //     2   6
    //    / \ / \
    //   1  3 5  7
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(7);

    // Test 1: Recursive
    vector<int> res1;
    inorderRecursive(root, res1);
    cout << "Recursive: ";
    printVector(res1);
    // Expected: [1, 2, 3, 4, 5, 6, 7]

    // Test 2: Iterative
    cout << "Iterative: ";
    printVector(inorderIterative(root));
    // Expected: [1, 2, 3, 4, 5, 6, 7]

    // Test 3: Empty tree
    cout << "Empty tree: ";
    printVector(inorderIterative(nullptr));
    // Expected: []

    // Test 4: Single node
    TreeNode* single = new TreeNode(42);
    cout << "Single node: ";
    printVector(inorderIterative(single));
    // Expected: [42]

    // Test 5: Left-skewed tree (1 <- 2 <- 3)
    TreeNode* skewed = new TreeNode(3);
    skewed->left = new TreeNode(2);
    skewed->left->left = new TreeNode(1);
    cout << "Left-skewed: ";
    printVector(inorderIterative(skewed));
    // Expected: [1, 2, 3]

    return 0;
}
```

### Dry Run (Iterative)

```
Tree:     4
         / \
        2   6
       / \
      1   3

Stack: []     curr=4
Push 4,2,1    curr=null
Pop 1, add 1  curr=null (1 has no right)
Pop 2, add 2  curr=3
Push 3        curr=null
Pop 3, add 3  curr=null
Pop 4, add 4  curr=6
Push 6        curr=null (6 has no left)
Pop 6, add 6  curr=null

Result: [1, 2, 3, 4, 6]
```

### Complexity Analysis

- **Time:** O(n) -- visits every node once
- **Space:** O(h) -- stack holds at most h nodes (h = height), worst case O(n) for skewed tree

## Common Mistakes

1. Forgetting the base case `if (!root) return` in recursive version
2. In the iterative version, using only `!st.empty()` without `curr` check -- misses the initial push phase
3. Confusing inorder (L, Root, R) with preorder (Root, L, R) or postorder (L, R, Root)

## Interview Tips

- For BST problems, mention that inorder gives sorted output
- The iterative version is frequently asked -- practice until it is natural
- Morris Traversal can do it in O(1) space but is rarely asked in TCS-NQT
- Know how to convert between all three traversals quickly
