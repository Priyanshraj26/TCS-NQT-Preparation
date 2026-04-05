/*
 * Q001: BFS Traversal of Graph
 * Question: DSA-Questions/Graphs/Q001-bfs-traversal.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | BFS (Queue)      | O(V+E)   | O(V)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// ==================== Graph using Adjacency List ====================
/*
 * We represent the graph as an adjacency list: vector<vector<int>> adj
 * adj[u] contains all neighbors of vertex u.
 */

// ==================== BFS Traversal ====================
/*
 * Algorithm:
 * 1. Create a visited array, initialize all to false.
 * 2. Create a queue, enqueue source, mark visited.
 * 3. While queue not empty:
 *    a. Dequeue front vertex.
 *    b. Process it (add to result).
 *    c. Enqueue all unvisited neighbors, mark them visited.
 *
 * Dry Run: V=5, Edges: (0,1),(0,2),(1,3),(2,4), src=0
 *   Queue: [0], visited={0}
 *   Dequeue 0, process. Enqueue 1,2. Queue: [1,2], visited={0,1,2}
 *   Dequeue 1, process. Enqueue 3. Queue: [2,3], visited={0,1,2,3}
 *   Dequeue 2, process. Enqueue 4. Queue: [3,4], visited={0,1,2,3,4}
 *   Dequeue 3, process. No new neighbors. Queue: [4]
 *   Dequeue 4, process. Queue: []
 *   Result: [0, 1, 2, 3, 4]
 */
vector<int> bfs(int V, vector<vector<int>>& adj, int src) {
    vector<int> result;
    vector<bool> visited(V, false);
    queue<int> q;

    visited[src] = true;
    q.push(src);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        result.push_back(node);

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    return result;
}

// BFS for disconnected graph (visit all components)
vector<int> bfsDisconnected(int V, vector<vector<int>>& adj) {
    vector<int> result;
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            queue<int> q;
            visited[i] = true;
            q.push(i);

            while (!q.empty()) {
                int node = q.front();
                q.pop();
                result.push_back(node);

                for (int neighbor : adj[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
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
    // Add undirected edges
    adj1[0].push_back(1); adj1[1].push_back(0);
    adj1[0].push_back(2); adj1[2].push_back(0);
    adj1[1].push_back(3); adj1[3].push_back(1);
    adj1[2].push_back(4); adj1[4].push_back(2);

    vector<int> r1 = bfs(V1, adj1, 0);
    cout << "BFS from 0: "; printVector(r1);  // [0, 1, 2, 3, 4]

    // Test Case 2: Disconnected graph
    cout << "\n=== Test Case 2: Disconnected ===" << endl;
    int V2 = 6;
    vector<vector<int>> adj2(V2);
    adj2[0].push_back(1); adj2[1].push_back(0);
    adj2[0].push_back(2); adj2[2].push_back(0);
    adj2[3].push_back(4); adj2[4].push_back(3);
    // Vertex 5 is isolated

    vector<int> r2 = bfsDisconnected(V2, adj2);
    cout << "BFS all: "; printVector(r2);  // [0, 1, 2, 3, 4, 5]

    // Test Case 3: Single vertex
    cout << "\n=== Test Case 3: Single ===" << endl;
    int V3 = 1;
    vector<vector<int>> adj3(V3);
    vector<int> r3 = bfs(V3, adj3, 0);
    cout << "BFS: "; printVector(r3);  // [0]

    // Test Case 4: Graph with cycle
    cout << "\n=== Test Case 4: Cycle ===" << endl;
    int V4 = 4;
    vector<vector<int>> adj4(V4);
    adj4[0].push_back(1); adj4[1].push_back(0);
    adj4[1].push_back(2); adj4[2].push_back(1);
    adj4[2].push_back(3); adj4[3].push_back(2);
    adj4[3].push_back(0); adj4[0].push_back(3);

    vector<int> r4 = bfs(V4, adj4, 0);
    cout << "BFS: "; printVector(r4);  // [0, 1, 3, 2]

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(V + E) -- visit each vertex and edge once
 * - Space: O(V) for visited array and queue
 *
 * Common Mistakes:
 * 1. Not marking visited BEFORE enqueuing (can lead to duplicates in queue)
 * 2. Forgetting to handle disconnected graphs
 * 3. Using adjacency matrix instead of list (wastes space for sparse graphs)
 *
 * Interview Tips:
 * - BFS gives shortest path in unweighted graphs
 * - BFS visits nodes level by level (similar to tree level-order)
 * - Always mark visited when ENQUEUEING, not when dequeuing
 * - Know the difference between BFS and DFS use cases
 */
