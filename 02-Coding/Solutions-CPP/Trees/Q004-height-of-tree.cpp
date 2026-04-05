/*
 * Q004: Height/Depth of Binary Tree
 * Question: DSA-Questions/Trees/Q004-height-of-tree.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive DFS    | O(n)     | O(h)    |
 * | BFS (levels)     | O(n)     | O(w)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

// ==================== Approach 1: Recursive DFS (Optimal) ====================
/*
 * Height = 1 + max(height of left, height of right)
 * Base case: null node has height 0
 *
 * Dry Run:      3
 *              / \
 *             9  20
 *               /  \
 *              15   7
 *
 * height(15)=1, height(7)=1
 * height(20) = 1 + max(1,1) = 2
 * height(9) = 1
 * height(3) = 1 + max(1,2) = 3
 */
int maxDepthRecursive(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepthRecursive(root->left),
                   maxDepthRecursive(root->right));
}

// ==================== Approach 2: BFS (Level Count) ====================
/*
 * Count the number of levels using BFS.
 * Each complete level processing = depth + 1.
 */
int maxDepthBFS(TreeNode* root) {
    if (!root) return 0;

    queue<TreeNode*> q;
    q.push(root);
    int depth = 0;

    while (!q.empty()) {
        int levelSize = q.size();
        depth++;
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }

    return depth;
}

int main() {
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    cout << "Height (Recursive): " << maxDepthRecursive(root1) << endl;  // 3
    cout << "Height (BFS): " << maxDepthBFS(root1) << endl;              // 3
    freeTree(root1);

    // Test Case 2: Skewed
    cout << "\n=== Test Case 2: Skewed ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    root2->right = new TreeNode(2);
    cout << "Height: " << maxDepthRecursive(root2) << endl;  // 2
    freeTree(root2);

    // Test Case 3: Empty
    cout << "\n=== Test Case 3: Empty ===" << endl;
    cout << "Height: " << maxDepthRecursive(nullptr) << endl;  // 0

    // Test Case 4: Single node
    cout << "\n=== Test Case 4: Single ===" << endl;
    TreeNode* root4 = new TreeNode(1);
    cout << "Height: " << maxDepthRecursive(root4) << endl;  // 1
    freeTree(root4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Recursive: O(n) time, O(h) space
 * - BFS: O(n) time, O(w) space where w = max width
 *
 * Common Mistakes:
 * 1. Confusing height (edges) vs depth (nodes). LeetCode counts nodes.
 * 2. Forgetting base case: null returns 0
 *
 * Interview Tips:
 * - This is a fundamental building block for many tree problems
 * - Recursive solution is clean and elegant -- interviewers love it
 * - Mention both approaches to show versatility
 */
