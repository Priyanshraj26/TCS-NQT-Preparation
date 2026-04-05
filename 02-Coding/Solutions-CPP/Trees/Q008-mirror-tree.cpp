/*
 * Q008: Mirror/Invert a Binary Tree
 * Question: DSA-Questions/Trees/Q008-mirror-tree.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive        | O(n)     | O(h)    |
 * | Iterative BFS    | O(n)     | O(w)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
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

// Print level order for verification
void printLevelOrder(TreeNode* root) {
    if (!root) { cout << "[]" << endl; return; }
    queue<TreeNode*> q;
    q.push(root);
    cout << "[";
    bool first = true;
    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        if (!first) cout << ", ";
        first = false;
        if (node) {
            cout << node->val;
            q.push(node->left);
            q.push(node->right);
        } else {
            cout << "null";
        }
    }
    cout << "]" << endl;
}

// ==================== Approach 1: Recursive (Optimal) ====================
/*
 * Swap left and right children, then recursively invert subtrees.
 *
 * Dry Run:      4            4
 *              / \   =>     / \
 *             2   7        7   2
 *            / \ / \      / \ / \
 *           1  3 6  9    9  6 3  1
 */
TreeNode* invertRecursive(TreeNode* root) {
    if (!root) return nullptr;

    // Swap children
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;

    // Recursively invert subtrees
    invertRecursive(root->left);
    invertRecursive(root->right);

    return root;
}

// ==================== Approach 2: Iterative BFS ====================
TreeNode* invertIterative(TreeNode* root) {
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

int main() {
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(7);
    root1->left->left = new TreeNode(1);
    root1->left->right = new TreeNode(3);
    root1->right->left = new TreeNode(6);
    root1->right->right = new TreeNode(9);
    cout << "Before: "; printLevelOrder(root1);
    invertRecursive(root1);
    cout << "After:  "; printLevelOrder(root1);
    freeTree(root1);

    // Test Case 2: Single node
    cout << "\n=== Test Case 2 ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    invertRecursive(root2);
    cout << "Single node: "; printLevelOrder(root2);
    freeTree(root2);

    // Test Case 3: Empty
    cout << "\n=== Test Case 3 ===" << endl;
    TreeNode* root3 = invertRecursive(nullptr);
    cout << "Empty: "; printLevelOrder(root3);

    // Test Case 4: Iterative approach
    cout << "\n=== Test Case 4 (Iterative) ===" << endl;
    TreeNode* root4 = new TreeNode(2);
    root4->left = new TreeNode(1);
    root4->right = new TreeNode(3);
    cout << "Before: "; printLevelOrder(root4);
    invertIterative(root4);
    cout << "After:  "; printLevelOrder(root4);
    freeTree(root4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Both: O(n) time, O(h) or O(w) space
 *
 * Common Mistakes:
 * 1. Trying to swap values instead of subtrees
 * 2. Not returning the root
 *
 * Interview Tips:
 * - This is the famous "Homebrew incident" question
 * - Extremely simple but tests understanding of tree recursion
 * - Can be done in 3 lines of code
 */
