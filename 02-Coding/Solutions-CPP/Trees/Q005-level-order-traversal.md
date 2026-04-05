# Solution: Level Order Traversal (BFS)

[← Back to Question](../../DSA-Questions/Trees/Q005-level-order-traversal.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| BFS with queue | O(n) | O(w) | Yes (interviews) |
| DFS with level tracking | O(n) | O(h) | Alternative |

## Approach 1: BFS with Queue

### Intuition

Use a queue to process nodes level by level. For each level, process all nodes currently in the queue, and add their children. The size of the queue at the start of each iteration gives the number of nodes in the current level.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// --- BFS Level Order ---
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;

        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            currentLevel.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(currentLevel);
    }
    return result;
}

// --- DFS with Level Tracking ---
void dfsLevelOrder(TreeNode* root, int level, vector<vector<int>>& result) {
    if (!root) return;
    if (level == (int)result.size()) {
        result.push_back({});
    }
    result[level].push_back(root->val);
    dfsLevelOrder(root->left, level + 1, result);
    dfsLevelOrder(root->right, level + 1, result);
}

void printLevels(const vector<vector<int>>& levels) {
    for (int i = 0; i < (int)levels.size(); i++) {
        cout << "  Level " << i << ": [";
        for (int j = 0; j < (int)levels[i].size(); j++) {
            cout << levels[i][j];
            if (j < (int)levels[i].size() - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
}

int main() {
    //       3
    //      / \
    //     9  20
    //       /  \
    //      15   7
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    // Test 1: BFS
    cout << "Test 1 (BFS):" << endl;
    printLevels(levelOrder(root));
    // Expected:
    //   Level 0: [3]
    //   Level 1: [9, 20]
    //   Level 2: [15, 7]

    // Test 2: DFS approach
    vector<vector<int>> dfsResult;
    dfsLevelOrder(root, 0, dfsResult);
    cout << "Test 2 (DFS):" << endl;
    printLevels(dfsResult);
    // Expected: same as above

    // Test 3: Empty tree
    cout << "Test 3 (empty):" << endl;
    printLevels(levelOrder(nullptr));
    // Expected: (nothing)

    // Test 4: Single node
    cout << "Test 4 (single):" << endl;
    printLevels(levelOrder(new TreeNode(1)));
    // Expected: Level 0: [1]

    // Test 5: Complete binary tree
    //       1
    //      / \
    //     2   3
    //    / \ / \
    //   4  5 6  7
    TreeNode* complete = new TreeNode(1);
    complete->left = new TreeNode(2);
    complete->right = new TreeNode(3);
    complete->left->left = new TreeNode(4);
    complete->left->right = new TreeNode(5);
    complete->right->left = new TreeNode(6);
    complete->right->right = new TreeNode(7);
    cout << "Test 5 (complete):" << endl;
    printLevels(levelOrder(complete));
    // Expected:
    //   Level 0: [1]
    //   Level 1: [2, 3]
    //   Level 2: [4, 5, 6, 7]

    return 0;
}
```

### Dry Run

```
Tree:     3
         / \
        9  20

Queue: [3]
Level 0: size=1, pop 3, add children 9,20. result=[[3]]
Queue: [9, 20]
Level 1: size=2, pop 9 (no children), pop 20 (no children). result=[[3],[9,20]]
Queue: []
Done.

Result: [[3], [9, 20]]
```

### Complexity Analysis

- **Time:** O(n) -- every node processed once
- **Space:** O(w) where w = max width of tree. Worst case O(n/2) = O(n) for last level of complete tree

## Common Mistakes

1. Not capturing `q.size()` before the for-loop -- the queue size changes as you push children
2. Forgetting to check for null before pushing children
3. Using a stack instead of a queue (gives DFS, not BFS)

## Interview Tips

- This is the most important tree traversal to know for interviews
- Many variations: zigzag level order, right side view, average of levels -- all build on this
- The DFS approach is useful when you need to avoid BFS memory overhead
- Always mention O(w) space for the queue where w is the maximum width
