/*
 * Q005: Level Order Traversal (BFS)
 * Question: DSA-Questions/Trees/Q005-level-order-traversal.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | BFS (Queue)      | O(n)     | O(w)    |
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

// ==================== Approach: BFS with Queue ====================
/*
 * Use a queue. For each level, process all nodes currently in the queue
 * (tracked by queue size at the start of each level).
 *
 * Dry Run:      3
 *              / \
 *             9  20
 *               /  \
 *              15   7
 *
 * Level 0: queue=[3], process 3, enqueue 9,20 -> result=[[3]]
 * Level 1: queue=[9,20], process 9(no children), process 20(enqueue 15,7)
 *          -> result=[[3],[9,20]]
 * Level 2: queue=[15,7], process both -> result=[[3],[9,20],[15,7]]
 */
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

void printResult(vector<vector<int>>& res) {
    cout << "[";
    for (int i = 0; i < (int)res.size(); i++) {
        cout << "[";
        for (int j = 0; j < (int)res[i].size(); j++) {
            cout << res[i][j];
            if (j < (int)res[i].size() - 1) cout << ", ";
        }
        cout << "]";
        if (i < (int)res.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    TreeNode* root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    vector<vector<int>> r1 = levelOrder(root1);
    cout << "Level Order: "; printResult(r1);
    // Expected: [[3], [9, 20], [15, 7]]
    freeTree(root1);

    // Test Case 2: Single node
    cout << "\n=== Test Case 2 ===" << endl;
    TreeNode* root2 = new TreeNode(1);
    vector<vector<int>> r2 = levelOrder(root2);
    cout << "Level Order: "; printResult(r2);  // [[1]]
    freeTree(root2);

    // Test Case 3: Empty
    cout << "\n=== Test Case 3 ===" << endl;
    vector<vector<int>> r3 = levelOrder(nullptr);
    cout << "Level Order: "; printResult(r3);  // []

    // Test Case 4: Complete binary tree
    cout << "\n=== Test Case 4 ===" << endl;
    TreeNode* root4 = new TreeNode(1);
    root4->left = new TreeNode(2);
    root4->right = new TreeNode(3);
    root4->left->left = new TreeNode(4);
    root4->left->right = new TreeNode(5);
    root4->right->left = new TreeNode(6);
    root4->right->right = new TreeNode(7);
    vector<vector<int>> r4 = levelOrder(root4);
    cout << "Level Order: "; printResult(r4);
    // Expected: [[1], [2, 3], [4, 5, 6, 7]]
    freeTree(root4);

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(n) -- visit each node once
 * - Space: O(w) where w = maximum width (up to n/2 for complete tree)
 *
 * Common Mistakes:
 * 1. Not using levelSize to separate levels (just doing BFS without grouping)
 * 2. Forgetting the empty tree check
 *
 * Interview Tips:
 * - BFS is the natural choice for level-order problems
 * - This pattern (queue + level size) is used in MANY variations:
 *   zigzag traversal, right side view, average of levels, etc.
 * - Know this pattern cold
 */
