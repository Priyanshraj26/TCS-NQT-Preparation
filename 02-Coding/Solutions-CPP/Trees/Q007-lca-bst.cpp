/*
 * Q007: Lowest Common Ancestor in BST
 * Question: DSA-Questions/Trees/Q007-lca-bst.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive        | O(h)     | O(h)    |
 * | Iterative        | O(h)     | O(1)    |
 * +------------------+----------+---------+
 */

#include <iostream>
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

// ==================== Approach 1: Recursive ====================
/*
 * Exploit BST property:
 * - If both p,q < root: LCA is in left subtree
 * - If both p,q > root: LCA is in right subtree
 * - Otherwise: root is the LCA (split point)
 *
 * Dry Run:       6
 *               / \
 *              2   8
 *             / \ / \
 *            0  4 7  9
 *              / \
 *             3   5
 *   p=2, q=8: 2<6 and 8>6 => split, LCA=6
 *   p=2, q=4: both < 6, go left. At 2: 2<=2 and 4>2 => split, LCA=2
 */
TreeNode* lcaRecursive(TreeNode* root, int p, int q) {
    if (!root) return nullptr;

    if (p < root->val && q < root->val) {
        return lcaRecursive(root->left, p, q);
    }
    if (p > root->val && q > root->val) {
        return lcaRecursive(root->right, p, q);
    }

    return root;  // Split point = LCA
}

// ==================== Approach 2: Iterative (Optimal) ====================
TreeNode* lcaIterative(TreeNode* root, int p, int q) {
    while (root) {
        if (p < root->val && q < root->val) {
            root = root->left;
        } else if (p > root->val && q > root->val) {
            root = root->right;
        } else {
            return root;
        }
    }
    return nullptr;
}

int main() {
    // Build BST:       6
    //                 / \
    //                2   8
    //               / \ / \
    //              0  4 7  9
    //                / \
    //               3   5
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(2);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(9);
    root->left->right->left = new TreeNode(3);
    root->left->right->right = new TreeNode(5);

    // Test Case 1: p=2, q=8
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* lca1 = lcaRecursive(root, 2, 8);
    cout << "LCA(2,8) = " << lca1->val << endl;  // 6

    // Test Case 2: p=2, q=4
    cout << "\n=== Test Case 2 ===" << endl;
    TreeNode* lca2 = lcaIterative(root, 2, 4);
    cout << "LCA(2,4) = " << lca2->val << endl;  // 2

    // Test Case 3: p=3, q=5
    cout << "\n=== Test Case 3 ===" << endl;
    TreeNode* lca3 = lcaRecursive(root, 3, 5);
    cout << "LCA(3,5) = " << lca3->val << endl;  // 4

    // Test Case 4: p=7, q=9
    cout << "\n=== Test Case 4 ===" << endl;
    TreeNode* lca4 = lcaIterative(root, 7, 9);
    cout << "LCA(7,9) = " << lca4->val << endl;  // 8

    freeTree(root);
    return 0;
}

/*
 * Complexity Analysis:
 * - Recursive: O(h) time, O(h) space
 * - Iterative: O(h) time, O(1) space -- preferred
 *
 * Common Mistakes:
 * 1. Not exploiting BST property (using generic binary tree LCA approach)
 * 2. Forgetting that a node can be its own ancestor
 * 3. Comparing values when you should be comparing nodes (or vice versa)
 *
 * Interview Tips:
 * - For BST, LCA is much simpler than for a general binary tree
 * - The key insight: LCA is the first node where p and q diverge (split point)
 * - If asked for general binary tree LCA, use a different approach (recursion checking both subtrees)
 */
