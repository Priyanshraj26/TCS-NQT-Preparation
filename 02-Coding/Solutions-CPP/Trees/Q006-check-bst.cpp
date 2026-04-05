/*
 * Q006: Check if Tree is BST
 * Question: DSA-Questions/Trees/Q006-check-bst.md
 *
 * Approach Overview:
 * +---------------------+----------+---------+
 * | Approach            | Time     | Space   |
 * +---------------------+----------+---------+
 * | Range checking      | O(n)     | O(h)    |
 * | Inorder traversal   | O(n)     | O(h)    |
 * +---------------------+----------+---------+
 */

#include <iostream>
#include <climits>
#include <vector>
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

// ==================== Approach 1: Range Checking (Optimal) ====================
/*
 * Each node must be within a valid range [min, max].
 * Left child: range becomes [min, parent_val)
 * Right child: range becomes (parent_val, max]
 *
 * Dry Run:     5
 *             / \
 *            1   4     <-- 4 is NOT > 5, so invalid
 *               / \
 *              3   6
 *
 * isValid(5, -INF, INF) -> check left isValid(1, -INF, 5) OK
 *                       -> check right isValid(4, 5, INF) -> 4 < 5, FAIL!
 */
bool isValidBSTHelper(TreeNode* root, long long minVal, long long maxVal) {
    if (!root) return true;

    if (root->val <= minVal || root->val >= maxVal) {
        return false;
    }

    return isValidBSTHelper(root->left, minVal, root->val) &&
           isValidBSTHelper(root->right, root->val, maxVal);
}

bool isValidBST(TreeNode* root) {
    return isValidBSTHelper(root, LLONG_MIN, LLONG_MAX);
}

// ==================== Approach 2: Inorder Traversal ====================
/*
 * Inorder traversal of BST gives sorted (strictly increasing) order.
 * Track previous value and check if current > previous.
 */
bool isValidBSTInorder(TreeNode* root, long long& prev) {
    if (!root) return true;

    // Check left subtree
    if (!isValidBSTInorder(root->left, prev)) return false;

    // Check current node
    if (root->val <= prev) return false;
    prev = root->val;

    // Check right subtree
    return isValidBSTInorder(root->right, prev);
}

bool isValidBSTInorder(TreeNode* root) {
    long long prev = LLONG_MIN;
    return isValidBSTInorder(root, prev);
}

int main() {
    // Test Case 1: Valid BST
    cout << "=== Test Case 1: Valid BST ===" << endl;
    TreeNode* root1 = new TreeNode(2);
    root1->left = new TreeNode(1);
    root1->right = new TreeNode(3);
    cout << "Range: " << (isValidBST(root1) ? "true" : "false") << endl;      // true
    cout << "Inorder: " << (isValidBSTInorder(root1) ? "true" : "false") << endl;
    freeTree(root1);

    // Test Case 2: Invalid BST
    cout << "\n=== Test Case 2: Invalid BST ===" << endl;
    TreeNode* root2 = new TreeNode(5);
    root2->left = new TreeNode(1);
    root2->right = new TreeNode(4);
    root2->right->left = new TreeNode(3);
    root2->right->right = new TreeNode(6);
    cout << "Range: " << (isValidBST(root2) ? "true" : "false") << endl;      // false
    cout << "Inorder: " << (isValidBSTInorder(root2) ? "true" : "false") << endl;
    freeTree(root2);

    // Test Case 3: Tricky case -- left subtree has node > root
    cout << "\n=== Test Case 3: Tricky case ===" << endl;
    //      5
    //     / \
    //    3   7
    //   / \
    //  2   6   <-- 6 > 5, invalid BST even though 6 < 3 is wrong
    TreeNode* root3 = new TreeNode(5);
    root3->left = new TreeNode(3);
    root3->right = new TreeNode(7);
    root3->left->left = new TreeNode(2);
    root3->left->right = new TreeNode(6);  // 6 > 5, violates BST
    cout << "Range: " << (isValidBST(root3) ? "true" : "false") << endl;  // false
    freeTree(root3);

    // Test Case 4: Single node
    cout << "\n=== Test Case 4: Single node ===" << endl;
    TreeNode* root4 = new TreeNode(1);
    cout << "Valid: " << (isValidBST(root4) ? "true" : "false") << endl;  // true
    freeTree(root4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Both approaches: O(n) time, O(h) space
 *
 * Common Mistakes:
 * 1. Only checking immediate children (left < root < right) -- WRONG!
 *    Must check entire subtree range.
 * 2. Using int for min/max bounds (overflow with INT_MIN/MAX node values)
 *    Use long long.
 * 3. Not handling equal values (BST requires strictly less/greater)
 *
 * Interview Tips:
 * - The range-based approach is cleaner and more intuitive
 * - Mention the "wrong approach" (checking only children) to show awareness
 * - Use long long for bounds to avoid edge cases
 */
