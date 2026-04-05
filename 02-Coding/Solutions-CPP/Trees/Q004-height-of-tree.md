# Solution: Height of a Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q004-height-of-tree.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive DFS | O(n) | O(h) stack | Yes (interviews) |
| Iterative BFS (level order) | O(n) | O(w) | Alternative |

## Approach 1: Recursive DFS

### Intuition

The height of a tree is 1 + max(height of left subtree, height of right subtree). Base case: an empty tree has height -1 (or 0, depending on convention -- clarify with the interviewer).

Convention used here: height = number of edges on the longest root-to-leaf path. So a single node has height 0, and an empty tree has height -1.

### C++ Code

```cpp
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Recursive (height = edges) ---
int height(TreeNode* root) {
    if (!root) return -1; // empty tree
    return 1 + max(height(root->left), height(root->right));
}

// --- Alternative: height as number of nodes on longest path ---
int heightNodes(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(heightNodes(root->left), heightNodes(root->right));
}

// --- Iterative BFS ---
int heightBFS(TreeNode* root) {
    if (!root) return -1;
    queue<TreeNode*> q;
    q.push(root);
    int h = -1;
    while (!q.empty()) {
        int levelSize = q.size();
        h++;
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
    return h;
}

int main() {
    //       1
    //      / \
    //     2   3
    //    / \
    //   4   5
    //  /
    // 6
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->left->left->left = new TreeNode(6);

    cout << "Test 1 (edges): " << height(root) << endl;
    // Expected: 3  (path: 1->2->4->6)
    cout << "Test 1 (nodes): " << heightNodes(root) << endl;
    // Expected: 4
    cout << "Test 1 (BFS):   " << heightBFS(root) << endl;
    // Expected: 3

    // Test 2: Single node
    TreeNode* single = new TreeNode(1);
    cout << "Test 2 (single): " << height(single) << endl;
    // Expected: 0

    // Test 3: Empty tree
    cout << "Test 3 (empty): " << height(nullptr) << endl;
    // Expected: -1

    // Test 4: Right-skewed
    TreeNode* skew = new TreeNode(1);
    skew->right = new TreeNode(2);
    skew->right->right = new TreeNode(3);
    cout << "Test 4 (skewed): " << height(skew) << endl;
    // Expected: 2

    // Test 5: Balanced
    TreeNode* bal = new TreeNode(1);
    bal->left = new TreeNode(2);
    bal->right = new TreeNode(3);
    cout << "Test 5 (balanced): " << height(bal) << endl;
    // Expected: 1

    return 0;
}
```

### Dry Run

```
Tree:     1
         / \
        2   3
       /
      4

height(1)
  = 1 + max(height(2), height(3))
  = 1 + max(1 + max(height(4), height(null)),  0)
  = 1 + max(1 + max(0, -1),  0)
  = 1 + max(1 + 0,  0)
  = 1 + max(1, 0)
  = 1 + 1 = 2
```

### Complexity Analysis

- **Time:** O(n) -- visits every node once
- **Space:** O(h) -- recursion stack, worst case O(n) for skewed tree

## Common Mistakes

1. Confusing height (edges) vs depth (also edges but from root) vs number of levels
2. Returning 0 for empty tree when using edge-based convention (should be -1)
3. Not considering that a skewed tree has O(n) height

## Interview Tips

- Always clarify the convention: height in edges or height in nodes
- This is a fundamental building block for many tree problems (balanced check, diameter, etc.)
- The recursive solution is clean and preferred for interviews
- Mention the BFS approach as an alternative for iterative solutions
