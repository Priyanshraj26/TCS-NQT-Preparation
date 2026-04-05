# Solution: Diameter of a Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q009-diameter-of-tree.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| DFS tracking max path | O(n) | O(h) | Yes (interviews) |
| Naive (height at each node) | O(n^2) | O(h) | Too slow |

## Approach 1: DFS Tracking Max Path

### Intuition

The diameter is the longest path between any two nodes (measured in edges). The key insight: the longest path through any node equals the height of its left subtree plus the height of its right subtree. Compute heights recursively and track the maximum diameter seen so far.

### C++ Code

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Single DFS O(n) ---
int diameterHelper(TreeNode* root, int& maxDiameter) {
    if (!root) return 0;

    int leftHeight = diameterHelper(root->left, maxDiameter);
    int rightHeight = diameterHelper(root->right, maxDiameter);

    // Diameter through this node = leftHeight + rightHeight
    maxDiameter = max(maxDiameter, leftHeight + rightHeight);

    // Return height of this subtree
    return 1 + max(leftHeight, rightHeight);
}

int diameter(TreeNode* root) {
    int maxDiameter = 0;
    diameterHelper(root, maxDiameter);
    return maxDiameter;
}

int main() {
    // Test 1: Diameter passes through root
    //       1
    //      / \
    //     2   3
    //    / \
    //   4   5
    TreeNode* t1 = new TreeNode(1);
    t1->left = new TreeNode(2);
    t1->right = new TreeNode(3);
    t1->left->left = new TreeNode(4);
    t1->left->right = new TreeNode(5);
    cout << "Test 1: " << diameter(t1) << endl;
    // Expected: 3 (path: 4->2->1->3 or 5->2->1->3)

    // Test 2: Diameter does NOT pass through root
    //       1
    //      /
    //     2
    //    / \
    //   4   5
    //  /     \
    // 6       7
    TreeNode* t2 = new TreeNode(1);
    t2->left = new TreeNode(2);
    t2->left->left = new TreeNode(4);
    t2->left->right = new TreeNode(5);
    t2->left->left->left = new TreeNode(6);
    t2->left->right->right = new TreeNode(7);
    cout << "Test 2: " << diameter(t2) << endl;
    // Expected: 4 (path: 6->4->2->5->7)

    // Test 3: Single node
    cout << "Test 3: " << diameter(new TreeNode(1)) << endl;
    // Expected: 0

    // Test 4: Empty tree
    cout << "Test 4: " << diameter(nullptr) << endl;
    // Expected: 0

    // Test 5: Linear chain
    //  1 -> 2 -> 3 -> 4
    TreeNode* t5 = new TreeNode(1);
    t5->right = new TreeNode(2);
    t5->right->right = new TreeNode(3);
    t5->right->right->right = new TreeNode(4);
    cout << "Test 5: " << diameter(t5) << endl;
    // Expected: 3

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

diameterHelper(4): left=0, right=0, maxD=max(0,0)=0, return 1
diameterHelper(5): left=0, right=0, maxD=max(0,0)=0, return 1
diameterHelper(2): left=1, right=1, maxD=max(0,2)=2, return 2
diameterHelper(3): left=0, right=0, maxD=max(2,0)=2, return 1
diameterHelper(1): left=2, right=1, maxD=max(2,3)=3, return 3

Diameter = 3
```

### Complexity Analysis

- **Time:** O(n) -- single DFS, each node visited once
- **Space:** O(h) -- recursion stack

## Approach 2: Naive (O(n^2))

```cpp
// Computes height separately at each node -- DO NOT use this in interviews
int heightNaive(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(heightNaive(root->left), heightNaive(root->right));
}

int diameterNaive(TreeNode* root) {
    if (!root) return 0;
    int throughRoot = heightNaive(root->left) + heightNaive(root->right);
    int leftDia = diameterNaive(root->left);
    int rightDia = diameterNaive(root->right);
    return max({throughRoot, leftDia, rightDia});
}
```

This is O(n^2) because height is computed repeatedly. Mentioned only to understand why the optimized approach is better.

## Common Mistakes

1. Assuming the diameter always passes through the root -- it may not (Test 2 above)
2. Returning height instead of diameter from the main function
3. Confusing diameter in edges vs in nodes (edges = nodes on path - 1)
4. Using the naive O(n^2) approach when O(n) is expected

## Interview Tips

- The trick is combining height computation with diameter tracking in a single DFS
- This pattern of "return one thing, track another via reference" is common in tree problems
- Always mention that diameter may not pass through the root
- This same pattern applies to: maximum path sum, balanced tree check, etc.
