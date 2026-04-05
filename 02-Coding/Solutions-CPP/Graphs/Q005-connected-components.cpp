/*
 * Q005: Number of Connected Components
 * Question: DSA-Questions/Graphs/Q005-connected-components.md
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
 * For each unvisited vertex, start a DFS -- this explores one full component.
 * Count the number of DFS calls = number of components.
 *
 * Dry Run: V=5, Edges: (0,1),(1,2),(3,4)
 *   i=0: unvisited, DFS from 0 -> visits {0,1,2}. components=1
 *   i=1: visited, skip
 *   i=2: visited, skip
 *   i=3: unvisited, DFS from 3 -> visits {3,4}. components=2
 *   i=4: visited, skip
 *   Answer: 2
 */
void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adj, visited);
        }
    }
}

int countComponentsDFS(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    int components = 0;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfs(i, adj, visited);
            components++;
        }
    }

    return components;
}

// ==================== Approach 2: BFS ====================
int countComponentsBFS(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    int components = 0;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            components++;
            queue<int> q;
            visited[i] = true;
            q.push(i);

            while (!q.empty()) {
                int node = q.front();
                q.pop();
                for (int neighbor : adj[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
        }
    }

    return components;
}

int main() {
    // Test Case 1: Two components
    cout << "=== Test Case 1: Two components ===" << endl;
    int V1 = 5;
    vector<vector<int>> adj1(V1);
    adj1[0].push_back(1); adj1[1].push_back(0);
    adj1[1].push_back(2); adj1[2].push_back(1);
    adj1[3].push_back(4); adj1[4].push_back(3);

    cout << "DFS: " << countComponentsDFS(V1, adj1) << endl;  // 2
    cout << "BFS: " << countComponentsBFS(V1, adj1) << endl;  // 2

    // Test Case 2: All isolated (no edges)
    cout << "\n=== Test Case 2: All isolated ===" << endl;
    int V2 = 4;
    vector<vector<int>> adj2(V2);
    cout << "Components: " << countComponentsDFS(V2, adj2) << endl;  // 4

    // Test Case 3: Fully connected
    cout << "\n=== Test Case 3: Fully connected ===" << endl;
    int V3 = 4;
    vector<vector<int>> adj3(V3);
    adj3[0].push_back(1); adj3[1].push_back(0);
    adj3[1].push_back(2); adj3[2].push_back(1);
    adj3[2].push_back(3); adj3[3].push_back(2);
    adj3[3].push_back(0); adj3[0].push_back(3);

    cout << "Components: " << countComponentsDFS(V3, adj3) << endl;  // 1

    // Test Case 4: Three components
    cout << "\n=== Test Case 4: Three components ===" << endl;
    int V4 = 7;
    vector<vector<int>> adj4(V4);
    adj4[0].push_back(1); adj4[1].push_back(0);  // {0,1}
    adj4[2].push_back(3); adj4[3].push_back(2);   // {2,3}
    adj4[4].push_back(5); adj4[5].push_back(4);
    adj4[5].push_back(6); adj4[6].push_back(5);   // {4,5,6}

    cout << "Components: " << countComponentsDFS(V4, adj4) << endl;  // 3

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(V + E) -- visit each vertex and edge once
 * - Space: O(V) for visited array
 *
 * Common Mistakes:
 * 1. Only running DFS from vertex 0 (missing other components)
 * 2. Not iterating through ALL vertices to find unvisited ones
 *
 * Interview Tips:
 * - This is one of the most fundamental graph problems
 * - Same pattern is used for: number of islands, friend circles, etc.
 * - Can also be solved with Union-Find (Disjoint Set Union)
 * - For large graphs, Union-Find may be more efficient
 */
