# Solution: Lowest Common Ancestor in BST

[← Back to Question](../../DSA-Questions/Trees/Q007-lca-bst.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| BST property (iterative) | O(h) | O(1) | Yes (interviews) |
| BST property (recursive) | O(h) | O(h) stack | Also good |

## Approach 1: BST Property Based (Iterative)

### Intuition

In a BST, if both nodes are smaller than the current node, the LCA must be in the left subtree. If both are larger, the LCA is in the right subtree. If one is on each side (or one equals the current node), the current node is the LCA.

### C++ Code

```cpp
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Iterative O(h) time, O(1) space ---
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    while (root) {
        if (p->val < root->val && q->val < root->val) {
            root = root->left;   // both in left subtree
        } else if (p->val > root->val && q->val > root->val) {
            root = root->right;  // both in right subtree
        } else {
            return root;         // split point = LCA
        }
    }
    return nullptr;
}

// --- Recursive ---
TreeNode* lcaRecursive(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root) return nullptr;
    if (p->val < root->val && q->val < root->val)
        return lcaRecursive(root->left, p, q);
    if (p->val > root->val && q->val > root->val)
        return lcaRecursive(root->right, p, q);
    return root;
}

// Helper: find node in BST
TreeNode* findNode(TreeNode* root, int val) {
    while (root) {
        if (val == root->val) return root;
        if (val < root->val) root = root->left;
        else root = root->right;
    }
    return nullptr;
}

int main() {
    //         6
    //        / \
    //       2   8
    //      / \ / \
    //     0  4 7  9
    //       / \
    //      3   5
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(2);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(9);
    root->left->right->left = new TreeNode(3);
    root->left->right->right = new TreeNode(5);

    // Test 1: LCA of 2 and 8
    TreeNode* p = findNode(root, 2);
    TreeNode* q = findNode(root, 8);
    cout << "Test 1: LCA(2, 8) = " << lowestCommonAncestor(root, p, q)->val << endl;
    // Expected: 6

    // Test 2: LCA of 2 and 4
    p = findNode(root, 2);
    q = findNode(root, 4);
    cout << "Test 2: LCA(2, 4) = " << lowestCommonAncestor(root, p, q)->val << endl;
    // Expected: 2 (ancestor is itself)

    // Test 3: LCA of 3 and 5
    p = findNode(root, 3);
    q = findNode(root, 5);
    cout << "Test 3: LCA(3, 5) = " << lowestCommonAncestor(root, p, q)->val << endl;
    // Expected: 4

    // Test 4: LCA of 0 and 5
    p = findNode(root, 0);
    q = findNode(root, 5);
    cout << "Test 4: LCA(0, 5) = " << lowestCommonAncestor(root, p, q)->val << endl;
    // Expected: 2

    // Test 5: LCA of 7 and 9
    p = findNode(root, 7);
    q = findNode(root, 9);
    cout << "Test 5: LCA(7, 9) = " << lowestCommonAncestor(root, p, q)->val << endl;
    // Expected: 8

    return 0;
}
```

### Dry Run

```
BST:      6
         / \
        2   8

LCA(2, 8):
  root=6: 2 < 6 and 8 > 6 => split point => return 6

LCA(3, 5):
  root=6: 3 < 6 and 5 < 6 => go left
  root=2: 3 > 2 and 5 > 2 => go right
  root=4: 3 < 4 and 5 > 4 => split point => return 4
```

### Complexity Analysis

- **Time:** O(h) where h is the height of the BST. O(log n) for balanced, O(n) for skewed
- **Space:** O(1) iterative, O(h) recursive

## Common Mistakes

1. Using a generic binary tree LCA algorithm (O(n)) instead of leveraging the BST property (O(h))
2. Forgetting that a node can be an ancestor of itself
3. Not handling the case where both values are equal (same node)

## Interview Tips

- Emphasize that this is O(h), not O(n) -- the BST property is the key optimization
- For a general binary tree (not BST), the approach is different (recursive check both subtrees)
- Always ask if the tree is a BST or general binary tree -- the approach changes significantly
- The iterative version is preferred since it uses O(1) space
