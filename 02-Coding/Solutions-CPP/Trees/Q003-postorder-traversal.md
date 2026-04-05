# Solution: Postorder Traversal of Binary Tree

[← Back to Question](../../DSA-Questions/Trees/Q003-postorder-traversal.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive | O(n) | O(h) stack | Easy to write |
| Iterative (two stacks) | O(n) | O(n) | Good for interviews |
| Iterative (one stack) | O(n) | O(h) | Advanced |

## Approach 1: Recursive

### Intuition

Postorder visits: Left subtree, Right subtree, then Root. This is useful for deleting a tree (delete children before parent) and evaluating postfix expressions.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- Recursive ---
void postorderRecursive(TreeNode* root, vector<int>& result) {
    if (!root) return;
    postorderRecursive(root->left, result);
    postorderRecursive(root->right, result);
    result.push_back(root->val);
}

// --- Iterative (Two Stacks) ---
vector<int> postorderTwoStacks(TreeNode* root) {
    vector<int> result;
    if (!root) return result;

    stack<TreeNode*> s1, s2;
    s1.push(root);

    while (!s1.empty()) {
        TreeNode* node = s1.top();
        s1.pop();
        s2.push(node);
        // Push left first, then right (right will be processed first in s1,
        // but s2 reverses the order)
        if (node->left) s1.push(node->left);
        if (node->right) s1.push(node->right);
    }

    while (!s2.empty()) {
        result.push_back(s2.top()->val);
        s2.pop();
    }
    return result;
}

// --- Iterative (Modified Preorder + Reverse) ---
vector<int> postorderReverse(TreeNode* root) {
    vector<int> result;
    if (!root) return result;

    stack<TreeNode*> st;
    st.push(root);

    while (!st.empty()) {
        TreeNode* node = st.top();
        st.pop();
        result.push_back(node->val);
        // Push left first, then right (opposite of preorder)
        if (node->left) st.push(node->left);
        if (node->right) st.push(node->right);
    }
    // This gives Root, Right, Left -- reverse to get Left, Right, Root
    reverse(result.begin(), result.end());
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
    postorderRecursive(root, res1);
    cout << "Recursive:   ";
    printVector(res1);
    // Expected: [4, 5, 2, 6, 3, 1]

    // Test 2: Two stacks
    cout << "Two stacks:  ";
    printVector(postorderTwoStacks(root));
    // Expected: [4, 5, 2, 6, 3, 1]

    // Test 3: Reverse method
    cout << "Reverse:     ";
    printVector(postorderReverse(root));
    // Expected: [4, 5, 2, 6, 3, 1]

    // Test 4: Empty tree
    cout << "Empty: ";
    printVector(postorderTwoStacks(nullptr));
    // Expected: []

    // Test 5: Single node
    cout << "Single: ";
    printVector(postorderTwoStacks(new TreeNode(42)));
    // Expected: [42]

    return 0;
}
```

### Dry Run (Two Stacks)

```
Tree:     1
         / \
        2   3

s1: [1]
Pop 1 -> s2: [1]. Push left(2), right(3) to s1. s1: [2, 3]
Pop 3 -> s2: [1, 3]. No children. s1: [2]
Pop 2 -> s2: [1, 3, 2]. No children. s1: []

Pop s2: 2, 3, 1 => Result: [2, 3, 1]
```

### Complexity Analysis

- **Time:** O(n) -- every node processed once
- **Space:** O(n) -- two stacks can hold up to n nodes total

## Common Mistakes

1. In two-stack method, pushing children in wrong order
2. Confusing postorder (L, R, Root) with inorder (L, Root, R)
3. Forgetting that the reverse method gives Root-Right-Left which needs to be reversed

## Interview Tips

- Postorder is the hardest of the three to do iteratively -- practice it well
- The "modified preorder + reverse" trick is easy to remember
- Postorder is used in: tree deletion, expression evaluation, calculating directory sizes
- Mention the two-stack approach as the clearest iterative method
