/*
 * Q003: Binary Tree Postorder Traversal
 * Question: DSA-Questions/Trees/Q003-postorder-traversal.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive        | O(n)     | O(h)    |
 * | Iterative        | O(n)     | O(n)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <stack>
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

void printVector(vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

// ==================== Approach 1: Recursive ====================
// Postorder: Left -> Right -> Root
void postorderHelper(TreeNode* root, vector<int>& result) {
    if (!root) return;
    postorderHelper(root->left, result);
    postorderHelper(root->right, result);
    result.push_back(root->val);
}

vector<int> postorderRecursive(TreeNode* root) {
    vector<int> result;
    postorderHelper(root, result);
    return result;
}

// ==================== Approach 2: Iterative (Modified Preorder + Reverse) ====================
/*
 * Trick: Postorder = reverse of (Root -> Right -> Left)
 * Do a modified preorder: Root -> Right -> Left, then reverse.
 *
 * Dry Run:      1
 *              / \
 *             2   3
 *            / \
 *           4   5
 * Modified preorder (Root-Right-Left): [1, 3, 2, 5, 4]
 * Reverse: [4, 5, 2, 3, 1] = Postorder!
 */
vector<int> postorderIterative(TreeNode* root) {
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

    reverse(result.begin(), result.end());
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

    vector<int> r1 = postorderRecursive(root1);
    cout << "Recursive: "; printVector(r1);  // [4, 5, 2, 3, 1]
    vector<int> r1b = postorderIterative(root1);
    cout << "Iterative: "; printVector(r1b);
    freeTree(root1);

    // Test Case 2: Right-skewed
    cout << "\n=== Test Case 2 ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    root2->right = new TreeNode(2);
    root2->right->left = new TreeNode(3);
    vector<int> r2 = postorderIterative(root2);
    cout << "Postorder: "; printVector(r2);  // [3, 2, 1]
    freeTree(root2);

    // Test Case 3: Single node
    cout << "\n=== Test Case 3 ===" << endl;
    TreeNode* root3 = new TreeNode(1);
    vector<int> r3 = postorderIterative(root3);
    cout << "Postorder: "; printVector(r3);  // [1]
    freeTree(root3);

    return 0;
}

/*
 * Complexity Analysis:
 * - Recursive: O(n) time, O(h) space
 * - Iterative: O(n) time, O(n) space (result vector for reverse)
 *
 * Common Mistakes:
 * 1. Confusing push order in iterative approach
 * 2. Forgetting to reverse in the iterative method
 *
 * Interview Tips:
 * - Postorder is used for: deleting a tree, evaluating expression trees
 * - The "modified preorder + reverse" trick is clever for interviews
 * - Know all three traversals and their iterative versions
 */
