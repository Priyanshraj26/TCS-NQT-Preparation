/*
 * Q003: Detect Cycle in Undirected Graph
 * Question: DSA-Questions/Graphs/Q003-detect-cycle-undirected.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | DFS              | O(V+E)   | O(V)    |
 * | BFS              | O(V+E)   | O(V)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// ==================== Approach 1: DFS ====================
/*
 * Key insight: In DFS, if we visit a neighbor that is already visited
 * AND it is NOT the parent of the current node, then we found a cycle.
 *
 * Why check parent? Because in undirected graph, edge (u,v) means
 * v is in adj[u] and u is in adj[v]. When we go from u to v,
 * v's neighbor list includes u (the parent). That is NOT a cycle.
 *
 * Dry Run: 0-1-2-3-0 (cycle)
 *   dfs(0, -1): visit 0, go to 1
 *     dfs(1, 0): visit 1, go to 2
 *       dfs(2, 1): visit 2, go to 3
 *         dfs(3, 2): visit 3, neighbor 0 is visited and != parent(2) => CYCLE!
 */
bool dfsCycleCheck(int node, int parent, vector<vector<int>>& adj,
                    vector<bool>& visited) {
    visited[node] = true;

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            if (dfsCycleCheck(neighbor, node, adj, visited)) {
                return true;
            }
        } else if (neighbor != parent) {
            return true;  // Visited neighbor that is not parent => cycle
        }
    }

    return false;
}

bool hasCycleDFS(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);

    // Check all components
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            if (dfsCycleCheck(i, -1, adj, visited)) {
                return true;
            }
        }
    }

    return false;
}

// ==================== Approach 2: BFS ====================
/*
 * Similar logic using BFS. Track parent for each node.
 * If a visited neighbor is not the parent, cycle found.
 */
bool hasCycleBFS(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++) {
        if (visited[i]) continue;

        queue<pair<int, int>> q;  // {node, parent}
        visited[i] = true;
        q.push({i, -1});

        while (!q.empty()) {
            auto [node, parent] = q.front();
            q.pop();

            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push({neighbor, node});
                } else if (neighbor != parent) {
                    return true;  // Cycle found
                }
            }
        }
    }

    return false;
}

int main() {
    // Test Case 1: Graph with cycle (0-1-2-3-0)
    cout << "=== Test Case 1: Has cycle ===" << endl;
    int V1 = 4;
    vector<vector<int>> adj1(V1);
    adj1[0].push_back(1); adj1[1].push_back(0);
    adj1[1].push_back(2); adj1[2].push_back(1);
    adj1[2].push_back(3); adj1[3].push_back(2);
    adj1[3].push_back(0); adj1[0].push_back(3);

    cout << "DFS: " << (hasCycleDFS(V1, adj1) ? "true" : "false") << endl;  // true
    cout << "BFS: " << (hasCycleBFS(V1, adj1) ? "true" : "false") << endl;  // true

    // Test Case 2: No cycle (tree)
    cout << "\n=== Test Case 2: No cycle ===" << endl;
    int V2 = 3;
    vector<vector<int>> adj2(V2);
    adj2[0].push_back(1); adj2[1].push_back(0);
    adj2[1].push_back(2); adj2[2].push_back(1);

    cout << "DFS: " << (hasCycleDFS(V2, adj2) ? "true" : "false") << endl;  // false
    cout << "BFS: " << (hasCycleBFS(V2, adj2) ? "true" : "false") << endl;  // false

    // Test Case 3: Disconnected, one component has cycle
    cout << "\n=== Test Case 3: Disconnected with cycle ===" << endl;
    int V3 = 6;
    vector<vector<int>> adj3(V3);
    adj3[0].push_back(1); adj3[1].push_back(0);  // Component 1: 0-1 (no cycle)
    adj3[2].push_back(3); adj3[3].push_back(2);   // Component 2: 2-3-4-2 (cycle)
    adj3[3].push_back(4); adj3[4].push_back(3);
    adj3[4].push_back(2); adj3[2].push_back(4);

    cout << "DFS: " << (hasCycleDFS(V3, adj3) ? "true" : "false") << endl;  // true

    // Test Case 4: Single node
    cout << "\n=== Test Case 4: Single ===" << endl;
    int V4 = 1;
    vector<vector<int>> adj4(V4);
    cout << "DFS: " << (hasCycleDFS(V4, adj4) ? "true" : "false") << endl;  // false

    return 0;
}

/*
 * Complexity Analysis:
 * - Both DFS and BFS: O(V + E) time, O(V) space
 *
 * Common Mistakes:
 * 1. Not checking parent -- every edge creates a "back" connection that is NOT a cycle
 * 2. Only checking one component (forgetting disconnected graphs)
 * 3. Confusing undirected cycle detection with directed cycle detection
 *    (directed uses different algorithm: coloring / back-edge detection)
 *
 * Interview Tips:
 * - For undirected: check visited neighbor != parent
 * - For directed: use coloring (white/gray/black) or track recursion stack
 * - Always handle disconnected graphs
 * - A tree with V vertices has exactly V-1 edges. If E >= V, cycle exists.
 */
