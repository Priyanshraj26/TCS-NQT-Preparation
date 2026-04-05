# Solution: Mirror (Invert) a Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q008-mirror-tree.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive swap | O(n) | O(h) | Yes (interviews) |
| Iterative BFS | O(n) | O(w) | Alternative |

## Approach 1: Recursive Swap

### Intuition

For each node, swap its left and right children, then recursively mirror both subtrees. This is a simple post-order or pre-order operation -- the order doesn't matter as long as you swap at every node.

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
TreeNode* mirrorTree(TreeNode* root) {
    if (!root) return nullptr;
    // Swap left and right
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;
    // Recurse
    mirrorTree(root->left);
    mirrorTree(root->right);
    return root;
}

// --- Iterative BFS ---
TreeNode* mirrorTreeBFS(TreeNode* root) {
    if (!root) return nullptr;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        // Swap children
        TreeNode* temp = node->left;
        node->left = node->right;
        node->right = temp;
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    return root;
}

// Helper: print level order for verification
void printLevelOrder(TreeNode* root) {
    if (!root) { cout << "[]" << endl; return; }
    queue<TreeNode*> q;
    q.push(root);
    cout << "[";
    bool first = true;
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        if (!first) cout << ", ";
        cout << node->val;
        first = false;
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    cout << "]" << endl;
}

int main() {
    // Test 1: Normal tree
    //       4              4
    //      / \    =>      / \
    //     2   7          7   2
    //    / \ / \        / \ / \
    //   1  3 6  9      9  6 3  1
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(7);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(9);

    cout << "Before: ";
    printLevelOrder(root);
    mirrorTree(root);
    cout << "After:  ";
    printLevelOrder(root);
    // Expected: [4, 7, 2, 9, 6, 3, 1]

    // Test 2: Single node
    TreeNode* single = new TreeNode(1);
    mirrorTree(single);
    cout << "Single: ";
    printLevelOrder(single);
    // Expected: [1]

    // Test 3: Empty tree
    TreeNode* empty = mirrorTree(nullptr);
    cout << "Empty: ";
    printLevelOrder(empty);
    // Expected: []

    // Test 4: Left-only tree -> becomes right-only
    //    1           1
    //   /     =>      \
    //  2               2
    //   \             /
    //    3           3
    TreeNode* leftOnly = new TreeNode(1);
    leftOnly->left = new TreeNode(2);
    leftOnly->left->right = new TreeNode(3);
    mirrorTree(leftOnly);
    cout << "Left->Right: ";
    printLevelOrder(leftOnly);
    // Expected: [1, 2, 3]

    return 0;
}
```

### Dry Run

```
Tree:     4
         / \
        2   7

mirrorTree(4):
  swap: left=7, right=2
  mirrorTree(7):
    swap: left=null, right=null (no-op)
  mirrorTree(2):
    swap: left=null, right=null (no-op)

Result:   4
         / \
        7   2
```

### Complexity Analysis

- **Time:** O(n) -- visits every node once
- **Space:** O(h) -- recursion stack (O(n) worst case for skewed tree)

## Common Mistakes

1. Returning a new tree instead of modifying in place (or vice versa -- clarify with interviewer)
2. Only swapping one level instead of recursing through the entire tree
3. Using `swap(root->left->val, root->right->val)` -- this only swaps values, not subtrees

## Interview Tips

- This is famously the problem Max Howell (creator of Homebrew) couldn't solve in a Google interview
- The solution is simple but interviewers look for clean recursive thinking
- Mention both recursive and iterative approaches
- Clarify: should the tree be modified in place or should a new tree be returned?
