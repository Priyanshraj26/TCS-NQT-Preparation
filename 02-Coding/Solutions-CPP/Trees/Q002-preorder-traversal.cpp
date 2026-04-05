/*
 * Q002: Binary Tree Preorder Traversal
 * Question: DSA-Questions/Trees/Q002-preorder-traversal.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive        | O(n)     | O(h)    |
 * | Iterative        | O(n)     | O(h)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <stack>
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

void printVector(vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

// ==================== Approach 1: Recursive ====================
// Preorder: Root -> Left -> Right
void preorderHelper(TreeNode* root, vector<int>& result) {
    if (!root) return;
    result.push_back(root->val);    // Process root
    preorderHelper(root->left, result);  // Left
    preorderHelper(root->right, result); // Right
}

vector<int> preorderRecursive(TreeNode* root) {
    vector<int> result;
    preorderHelper(root, result);
    return result;
}

// ==================== Approach 2: Iterative (Stack) ====================
/*
 * Push root to stack.
 * Pop, process, push RIGHT first, then LEFT (so left is processed first).
 *
 * Dry Run:      1
 *              / \
 *             2   3
 *            / \
 *           4   5
 *
 * Stack: [1] -> pop 1, push 3,2 -> [3,2]
 * Pop 2, push 5,4 -> [3,5,4]
 * Pop 4 -> [3,5]
 * Pop 5 -> [3]
 * Pop 3 -> []
 * Result: [1, 2, 4, 5, 3]
 */
vector<int> preorderIterative(TreeNode* root) {
    vector<int> result;
    if (!root) return result;

    stack<TreeNode*> st;
    st.push(root);

    while (!st.empty()) {
        TreeNode* node = st.top();
        st.pop();
        result.push_back(node->val);

        // Push right first so left is processed first
        if (node->right) st.push(node->right);
        if (node->left) st.push(node->left);
    }

    return result;
}

int main() {
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    root1->left->left = new TreeNode(4);
    root1->left->right = new TreeNode(5);

    vector<int> r1 = preorderRecursive(root1);
    cout << "Recursive: "; printVector(r1);  // [1, 2, 4, 5, 3]
    vector<int> r1b = preorderIterative(root1);
    cout << "Iterative: "; printVector(r1b);
    freeTree(root1);

    // Test Case 2: Right-skewed
    cout << "\n=== Test Case 2 ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    root2->right = new TreeNode(2);
    root2->right->left = new TreeNode(3);
    vector<int> r2 = preorderIterative(root2);
    cout << "Preorder: "; printVector(r2);  // [1, 2, 3]
    freeTree(root2);

    // Test Case 3: Empty tree
    cout << "\n=== Test Case 3 ===" << endl;
    vector<int> r3 = preorderIterative(nullptr);
    cout << "Preorder: "; printVector(r3);  // []

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(n) for both approaches
 * - Space: O(h) -- O(log n) balanced, O(n) skewed
 *
 * Common Mistakes:
 * 1. In iterative, pushing left before right (wrong order)
 * 2. Forgetting null check before pushing children
 *
 * Interview Tips:
 * - Preorder is the most intuitive traversal (process node as you visit)
 * - Used in: tree serialization, copying a tree, prefix expression
 * - The iterative version is simpler than inorder iterative
 */
