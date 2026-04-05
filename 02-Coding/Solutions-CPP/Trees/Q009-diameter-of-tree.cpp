/*
 * Q009: Diameter of Binary Tree
 * Question: DSA-Questions/Trees/Q009-diameter-of-tree.md
 *
 * Approach Overview:
 * +---------------------+----------+---------+
 * | Approach            | Time     | Space   |
 * +---------------------+----------+---------+
 * | DFS (single pass)   | O(n)     | O(h)    |
 * +---------------------+----------+---------+
 */

#include <iostream>
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

// ==================== Approach: DFS Computing Height + Diameter ====================
/*
 * At each node, the diameter passing through it = left_height + right_height.
 * The overall diameter = max diameter across all nodes.
 * We compute height and update diameter in a single DFS.
 *
 * Dry Run:      1
 *              / \
 *             2   3
 *            / \
 *           4   5
 *
 * height(4)=1, height(5)=1, diameter at 2 = 1+1=2
 * height(2)=2, height(3)=1, diameter at 1 = 2+1=3
 * Max diameter = 3
 */
int diameterHelper(TreeNode* root, int& maxDiameter) {
    if (!root) return 0;

    int leftHeight = diameterHelper(root->left, maxDiameter);
    int rightHeight = diameterHelper(root->right, maxDiameter);

    // Update diameter at this node
    maxDiameter = max(maxDiameter, leftHeight + rightHeight);

    // Return height
    return 1 + max(leftHeight, rightHeight);
}

int diameterOfBinaryTree(TreeNode* root) {
    int maxDiameter = 0;
    diameterHelper(root, maxDiameter);
    return maxDiameter;
}

int main() {
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    root1->left->left = new TreeNode(4);
    root1->left->right = new TreeNode(5);
    cout << "Diameter: " << diameterOfBinaryTree(root1) << endl;  // 3
    freeTree(root1);

    // Test Case 2: Diameter doesn't pass through root
    cout << "\n=== Test Case 2 ===" << endl;
    //        1
    //       /
    //      2
    //     / \
    //    4   5
    //   /     \
    //  6       7
    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->left->left = new TreeNode(4);
    root2->left->right = new TreeNode(5);
    root2->left->left->left = new TreeNode(6);
    root2->left->right->right = new TreeNode(7);
    cout << "Diameter: " << diameterOfBinaryTree(root2) << endl;  // 4 (6->4->2->5->7)
    freeTree(root2);

    // Test Case 3: Single node
    cout << "\n=== Test Case 3 ===" << endl;
    TreeNode* root3 = new TreeNode(1);
    cout << "Diameter: " << diameterOfBinaryTree(root3) << endl;  // 0
    freeTree(root3);

    // Test Case 4: Linear tree
    cout << "\n=== Test Case 4 ===" << endl;
    TreeNode* root4 = new TreeNode(1);
    root4->right = new TreeNode(2);
    cout << "Diameter: " << diameterOfBinaryTree(root4) << endl;  // 1
    freeTree(root4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(n) -- visit each node once
 * - Space: O(h) -- recursion stack
 *
 * Common Mistakes:
 * 1. Computing height separately for each node => O(n^2)
 * 2. Assuming diameter always passes through root
 * 3. Confusing edges vs nodes (diameter counts EDGES)
 *
 * Interview Tips:
 * - The key insight: compute height and diameter simultaneously
 * - This "compute two things in one DFS" pattern appears in many tree problems
 * - Always clarify: does the problem count edges or nodes?
 */
