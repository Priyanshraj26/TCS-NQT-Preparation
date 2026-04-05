/*
 * Q002: DFS Traversal of Graph
 * Question: DSA-Questions/Graphs/Q002-dfs-traversal.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Recursive DFS    | O(V+E)   | O(V)    |
 * | Iterative DFS    | O(V+E)   | O(V)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// ==================== Approach 1: Recursive DFS ====================
/*
 * Dry Run: V=5, Edges: (0,1),(0,2),(1,3),(2,4), src=0
 *   dfs(0): visit 0, recurse on neighbor 1
 *     dfs(1): visit 1, recurse on neighbor 3
 *       dfs(3): visit 3, no unvisited neighbors, backtrack
 *     back to 1, no more unvisited, backtrack
 *   back to 0, recurse on neighbor 2
 *     dfs(2): visit 2, recurse on neighbor 4
 *       dfs(4): visit 4, backtrack
 *   Result: [0, 1, 3, 2, 4]
 */
void dfsRecursiveHelper(int node, vector<vector<int>>& adj,
                         vector<bool>& visited, vector<int>& result) {
    visited[node] = true;
    result.push_back(node);

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfsRecursiveHelper(neighbor, adj, visited, result);
        }
    }
}

vector<int> dfsRecursive(int V, vector<vector<int>>& adj, int src) {
    vector<int> result;
    vector<bool> visited(V, false);
    dfsRecursiveHelper(src, adj, visited, result);
    return result;
}

// ==================== Approach 2: Iterative DFS (Stack) ====================
/*
 * Similar to BFS but use a stack instead of queue.
 * Note: Order may differ slightly from recursive due to neighbor processing order.
 */
vector<int> dfsIterative(int V, vector<vector<int>>& adj, int src) {
    vector<int> result;
    vector<bool> visited(V, false);
    stack<int> st;

    st.push(src);

    while (!st.empty()) {
        int node = st.top();
        st.pop();

        if (visited[node]) continue;
        visited[node] = true;
        result.push_back(node);

        // Push neighbors in reverse order to match recursive order
        for (int i = adj[node].size() - 1; i >= 0; i--) {
            if (!visited[adj[node][i]]) {
                st.push(adj[node][i]);
            }
        }
    }

    return result;
}

// DFS for disconnected graph
vector<int> dfsDisconnected(int V, vector<vector<int>>& adj) {
    vector<int> result;
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfsRecursiveHelper(i, adj, visited, result);
        }
    }

    return result;
}

void printVector(vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    // Test Case 1: Connected graph
    cout << "=== Test Case 1: Connected ===" << endl;
    int V1 = 5;
    vector<vector<int>> adj1(V1);
    adj1[0].push_back(1); adj1[1].push_back(0);
    adj1[0].push_back(2); adj1[2].push_back(0);
    adj1[1].push_back(3); adj1[3].push_back(1);
    adj1[2].push_back(4); adj1[4].push_back(2);

    vector<int> r1 = dfsRecursive(V1, adj1, 0);
    cout << "DFS Recursive: "; printVector(r1);
    vector<int> r1b = dfsIterative(V1, adj1, 0);
    cout << "DFS Iterative: "; printVector(r1b);

    // Test Case 2: Disconnected graph
    cout << "\n=== Test Case 2: Disconnected ===" << endl;
    int V2 = 6;
    vector<vector<int>> adj2(V2);
    adj2[0].push_back(1); adj2[1].push_back(0);
    adj2[3].push_back(4); adj2[4].push_back(3);

    vector<int> r2 = dfsDisconnected(V2, adj2);
    cout << "DFS all components: "; printVector(r2);

    // Test Case 3: Graph with cycle
    cout << "\n=== Test Case 3: Cycle ===" << endl;
    int V3 = 4;
    vector<vector<int>> adj3(V3);
    adj3[0].push_back(1); adj3[1].push_back(0);
    adj3[1].push_back(2); adj3[2].push_back(1);
    adj3[2].push_back(3); adj3[3].push_back(2);
    adj3[3].push_back(0); adj3[0].push_back(3);

    vector<int> r3 = dfsRecursive(V3, adj3, 0);
    cout << "DFS: "; printVector(r3);

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(V + E) -- visit each vertex and edge once
 * - Space: O(V) for visited + recursion stack / explicit stack
 *
 * Common Mistakes:
 * 1. Not handling disconnected graphs (only visiting one component)
 * 2. Forgetting to mark visited (infinite loop with cycles)
 * 3. Stack overflow on very deep graphs with recursive approach
 *
 * Interview Tips:
 * - DFS is used for: cycle detection, topological sort, connected components,
 *   path finding, backtracking problems
 * - Recursive is cleaner, iterative handles deep graphs better
 * - Know when to use DFS vs BFS (DFS for exploring all paths, BFS for shortest path)
 */
