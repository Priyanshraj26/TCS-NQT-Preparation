/*
 * Q010: Count Leaf Nodes
 * Question: DSA-Questions/Trees/Q010-count-leaf-nodes.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive DFS    | O(n)     | O(h)    |
 * | Iterative BFS    | O(n)     | O(w)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <queue>
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

// ==================== Approach 1: Recursive DFS ====================
/*
 * A leaf has no children. Count leaves in left + right subtrees.
 *
 * Dry Run:      1
 *              / \
 *             2   3
 *            / \
 *           4   5
 * countLeaves(4)=1, countLeaves(5)=1
 * countLeaves(2) = 1+1 = 2
 * countLeaves(3) = 1 (leaf)
 * countLeaves(1) = 2+1 = 3
 */
int countLeavesRecursive(TreeNode* root) {
    if (!root) return 0;

    // Leaf node
    if (!root->left && !root->right) return 1;

    return countLeavesRecursive(root->left) + countLeavesRecursive(root->right);
}

// ==================== Approach 2: Iterative BFS ====================
int countLeavesBFS(TreeNode* root) {
    if (!root) return 0;

    int count = 0;
    queue<TreeNode*> q;
    q.push(root);

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
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    root1->left->left = new TreeNode(4);
    root1->left->right = new TreeNode(5);
    cout << "Leaf count (Recursive): " << countLeavesRecursive(root1) << endl;  // 3
    cout << "Leaf count (BFS): " << countLeavesBFS(root1) << endl;              // 3
    freeTree(root1);

    // Test Case 2: Single node (is itself a leaf)
    cout << "\n=== Test Case 2 ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    cout << "Leaf count: " << countLeavesRecursive(root2) << endl;  // 1
    freeTree(root2);

    // Test Case 3: Empty tree
    cout << "\n=== Test Case 3 ===" << endl;
    cout << "Leaf count: " << countLeavesRecursive(nullptr) << endl;  // 0

    // Test Case 4: Complete binary tree
    cout << "\n=== Test Case 4 ===" << endl;
    TreeNode* root4 = new TreeNode(1);
    root4->left = new TreeNode(2);
    root4->right = new TreeNode(3);
    root4->left->left = new TreeNode(4);
    root4->left->right = new TreeNode(5);
    root4->right->left = new TreeNode(6);
    root4->right->right = new TreeNode(7);
    cout << "Leaf count: " << countLeavesRecursive(root4) << endl;  // 4
    freeTree(root4);

    // Test Case 5: Skewed tree
    cout << "\n=== Test Case 5 ===" << endl;
    TreeNode* root5 = new TreeNode(1);
    root5->right = new TreeNode(2);
    root5->right->right = new TreeNode(3);
    cout << "Leaf count: " << countLeavesRecursive(root5) << endl;  // 1
    freeTree(root5);

    return 0;
}

/*
 * Complexity Analysis:
 * - Both: O(n) time
 * - Recursive: O(h) space, BFS: O(w) space
 *
 * Common Mistakes:
 * 1. Forgetting to check for null root
 * 2. Counting internal nodes as leaves
 *
 * Interview Tips:
 * - Simple but tests basic tree understanding
 * - A leaf is defined as: node->left == NULL && node->right == NULL
 * - Can be extended to: count nodes at level k, count internal nodes, etc.
 */
