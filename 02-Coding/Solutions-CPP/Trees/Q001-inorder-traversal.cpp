/*
 * Q001: Binary Tree Inorder Traversal
 * Question: DSA-Questions/Trees/Q001-inorder-traversal.md
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

// ==================== TreeNode Definition ====================
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Helper: Build tree from array (level-order, -1 = null)
TreeNode* buildTree(vector<int>& arr, int i) {
    if (i >= (int)arr.size() || arr[i] == -1) return nullptr;
    TreeNode* node = new TreeNode(arr[i]);
    node->left = buildTree(arr, 2 * i + 1);
    node->right = buildTree(arr, 2 * i + 2);
    return node;
}

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
/*
 * Inorder: Left -> Root -> Right
 * Simply recurse left, add current, recurse right.
 */
void inorderRecursiveHelper(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorderRecursiveHelper(root->left, result);
    result.push_back(root->val);
    inorderRecursiveHelper(root->right, result);
}

vector<int> inorderRecursive(TreeNode* root) {
    vector<int> result;
    inorderRecursiveHelper(root, result);
    return result;
}

// ==================== Approach 2: Iterative (Stack) ====================
/*
 * Use a stack to simulate recursion.
 * Push all left children, then pop and process, then go right.
 *
 * Dry Run for tree:    4
 *                     / \
 *                    2   6
 *                   / \
 *                  1   3
 *
 * Stack operations:
 *   Push 4, Push 2, Push 1 (go left until null)
 *   Pop 1, add to result. Go right (null).
 *   Pop 2, add to result. Go right to 3.
 *   Push 3. Pop 3, add to result. Go right (null).
 *   Pop 4, add to result. Go right to 6.
 *   Push 6. Pop 6, add to result.
 *   Result: [1, 2, 3, 4, 6]
 */
vector<int> inorderIterative(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> st;
    TreeNode* curr = root;

    while (curr || !st.empty()) {
        // Push all left children
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        // Process top of stack
        curr = st.top();
        st.pop();
        result.push_back(curr->val);
        // Go right
        curr = curr->right;
    }

    return result;
}

int main() {
    // Test Case 1: BST
    cout << "=== Test Case 1: BST ===" << endl;
    vector<int> arr1 = {4, 2, 6, 1, 3, 5, 7};
    TreeNode* root1 = buildTree(arr1, 0);
    vector<int> res1 = inorderRecursive(root1);
    cout << "Recursive: "; printVector(res1);
    vector<int> res1b = inorderIterative(root1);
    cout << "Iterative: "; printVector(res1b);
    freeTree(root1);

    // Test Case 2: Skewed tree (1 -> 2 -> 3)
    cout << "\n=== Test Case 2: Right-skewed ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    root2->right = new TreeNode(2);
    root2->right->left = new TreeNode(3);
    vector<int> res2 = inorderRecursive(root2);
    cout << "Inorder: "; printVector(res2);  // [1, 3, 2]
    freeTree(root2);

    // Test Case 3: Single node
    cout << "\n=== Test Case 3: Single node ===" << endl;
    TreeNode* root3 = new TreeNode(1);
    vector<int> res3 = inorderIterative(root3);
    cout << "Inorder: "; printVector(res3);  // [1]
    freeTree(root3);

    // Test Case 4: Empty tree
    cout << "\n=== Test Case 4: Empty ===" << endl;
    vector<int> res4 = inorderIterative(nullptr);
    cout << "Inorder: "; printVector(res4);  // []

    return 0;
}

/*
 * Complexity Analysis:
 * - Both: O(n) time, O(h) space where h = height
 *
 * Common Mistakes:
 * 1. Forgetting base case (null check)
 * 2. In iterative, not handling the "go right" step properly
 * 3. Confusing inorder with preorder/postorder
 *
 * Interview Tips:
 * - Know all three traversals cold -- they're building blocks
 * - Inorder of BST gives SORTED output (key insight)
 * - Be ready to write iterative version -- shows deeper understanding
 */
