# Solution: Count Leaf Nodes in a Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q010-count-leaf-nodes.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive DFS | O(n) | O(h) | Yes (interviews) |
| Iterative BFS | O(n) | O(w) | Alternative |

## Approach 1: Recursive DFS

### Intuition

A leaf node has no left or right child. Recursively count: if the current node is a leaf, return 1. Otherwise, return the sum of leaf counts in the left and right subtrees.

### C++ Code

```cpp
#include <iostream>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Recursive ---
int countLeaves(TreeNode* root) {
    if (!root) return 0;
    if (!root->left && !root->right) return 1; // leaf
    return countLeaves(root->left) + countLeaves(root->right);
}

// --- Iterative BFS ---
int countLeavesBFS(TreeNode* root) {
    if (!root) return 0;
    queue<TreeNode*> q;
    q.push(root);
    int count = 0;
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        if (!node->left && !node->right) {
            count++;
        }
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    return count;
}

int main() {
    // Test 1: Normal tree
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

    cout << "Test 1 (recursive): " << countLeaves(root) << endl;
    // Expected: 3 (nodes 4, 5, 6)
    cout << "Test 1 (BFS):       " << countLeavesBFS(root) << endl;
    // Expected: 3

    // Test 2: Full binary tree
    //       1
    //      / \
    //     2   3
    //    / \ / \
    //   4  5 6  7
    TreeNode* full = new TreeNode(1);
    full->left = new TreeNode(2);
    full->right = new TreeNode(3);
    full->left->left = new TreeNode(4);
    full->left->right = new TreeNode(5);
    full->right->left = new TreeNode(6);
    full->right->right = new TreeNode(7);
    cout << "Test 2 (full): " << countLeaves(full) << endl;
    // Expected: 4 (nodes 4, 5, 6, 7)

    // Test 3: Single node (is itself a leaf)
    cout << "Test 3 (single): " << countLeaves(new TreeNode(1)) << endl;
    // Expected: 1

    // Test 4: Empty tree
    cout << "Test 4 (empty): " << countLeaves(nullptr) << endl;
    // Expected: 0

    // Test 5: Skewed tree (only last node is leaf)
    TreeNode* skew = new TreeNode(1);
    skew->left = new TreeNode(2);
    skew->left->left = new TreeNode(3);
    skew->left->left->left = new TreeNode(4);
    cout << "Test 5 (skewed): " << countLeaves(skew) << endl;
    // Expected: 1

    return 0;
}
```

### Dry Run

```
Tree:     1
         / \
        2   3
       / \
      4   5

countLeaves(1)
  = countLeaves(2) + countLeaves(3)
  = (countLeaves(4) + countLeaves(5)) + 1
  = (1 + 1) + 1
  = 3
```

### Complexity Analysis

- **Time:** O(n) -- visits every node
- **Space:** O(h) -- recursion stack, worst case O(n)

## Common Mistakes

1. Counting all nodes instead of only leaf nodes (forgetting the leaf check)
2. Returning 1 for a null node instead of 0
3. Only checking one child for null (a leaf has BOTH children null)

## Interview Tips

- This is one of the simplest tree recursion problems -- use it to warm up
- The pattern generalizes: count internal nodes, count nodes at depth k, etc.
- For a full binary tree with n leaves, there are n-1 internal nodes (useful property)
- A single root with no children is considered a leaf
