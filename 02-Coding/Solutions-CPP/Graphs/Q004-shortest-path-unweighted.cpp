/*
 * Q004: Shortest Path in Unweighted Graph (BFS)
 * Question: DSA-Questions/Graphs/Q004-shortest-path-unweighted.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | BFS              | O(V+E)   | O(V)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// ==================== BFS Shortest Path ====================
/*
 * In an unweighted graph, BFS naturally finds the shortest path
 * because it explores nodes level by level (distance 1, then 2, etc.)
 *
 * Algorithm:
 * 1. Initialize dist[] = -1 for all vertices.
 * 2. Set dist[src] = 0, enqueue src.
 * 3. For each dequeued node, update neighbors: dist[neighbor] = dist[node] + 1.
 *
 * Dry Run: V=6, Edges: (0,1),(0,2),(1,3),(2,3),(3,4),(4,5),(2,5), src=0
 *   dist = [-1,-1,-1,-1,-1,-1], set dist[0]=0
 *   Process 0: neighbors 1,2. dist=[0,1,1,-1,-1,-1]
 *   Process 1: neighbor 3. dist=[0,1,1,2,-1,-1]
 *   Process 2: neighbor 3(skip,visited), 5. dist=[0,1,1,2,-1,2]
 *   Process 3: neighbor 4. dist=[0,1,1,2,3,2]
 *   Process 5: no new neighbors.
 *   Process 4: no new neighbors.
 *   Final: [0, 1, 1, 2, 3, 2]
 */
vector<int> shortestPath(int V, vector<vector<int>>& adj, int src) {
    vector<int> dist(V, -1);
    queue<int> q;

    dist[src] = 0;
    q.push(src);

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int neighbor : adj[node]) {
            if (dist[neighbor] == -1) {  // Not visited
                dist[neighbor] = dist[node] + 1;
                q.push(neighbor);
            }
        }
    }

    return dist;
}

// ==================== BFS Shortest Path with Path Reconstruction ====================
vector<int> shortestPathWithRoute(int V, vector<vector<int>>& adj, int src, int dest) {
    vector<int> dist(V, -1);
    vector<int> parent(V, -1);
    queue<int> q;

    dist[src] = 0;
    q.push(src);

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int neighbor : adj[node]) {
            if (dist[neighbor] == -1) {
                dist[neighbor] = dist[node] + 1;
                parent[neighbor] = node;
                q.push(neighbor);
            }
        }
    }

    // Reconstruct path from dest to src
    vector<int> path;
    if (dist[dest] == -1) return path;  // Unreachable

    for (int node = dest; node != -1; node = parent[node]) {
        path.push_back(node);
    }

    // Reverse to get src -> dest
    reverse(path.begin(), path.end());
    return path;
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
    // Test Case 1
    cout << "=== Test Case 1 ===" << endl;
    int V1 = 6;
    vector<vector<int>> adj1(V1);
    adj1[0].push_back(1); adj1[1].push_back(0);
    adj1[0].push_back(2); adj1[2].push_back(0);
    adj1[1].push_back(3); adj1[3].push_back(1);
    adj1[2].push_back(3); adj1[3].push_back(2);
    adj1[3].push_back(4); adj1[4].push_back(3);
    adj1[4].push_back(5); adj1[5].push_back(4);
    adj1[2].push_back(5); adj1[5].push_back(2);

    vector<int> dist1 = shortestPath(V1, adj1, 0);
    cout << "Distances from 0: "; printVector(dist1);
    // Expected: [0, 1, 1, 2, 3, 2]

    vector<int> path = shortestPathWithRoute(V1, adj1, 0, 5);
    cout << "Shortest path 0->5: "; printVector(path);
    // Expected: [0, 2, 5]

    // Test Case 2: Unreachable vertex
    cout << "\n=== Test Case 2: Unreachable ===" << endl;
    int V2 = 3;
    vector<vector<int>> adj2(V2);
    adj2[0].push_back(1); adj2[1].push_back(0);

    vector<int> dist2 = shortestPath(V2, adj2, 0);
    cout << "Distances from 0: "; printVector(dist2);
    // Expected: [0, 1, -1]

    // Test Case 3: Single vertex
    cout << "\n=== Test Case 3 ===" << endl;
    int V3 = 1;
    vector<vector<int>> adj3(V3);
    vector<int> dist3 = shortestPath(V3, adj3, 0);
    cout << "Distances: "; printVector(dist3);  // [0]

    return 0;
}

/*
 * Complexity Analysis:
 * - Time: O(V + E)
 * - Space: O(V) for dist array and queue
 *
 * Common Mistakes:
 * 1. Using DFS for shortest path (DFS does NOT guarantee shortest path)
 * 2. Not initializing distances to -1 / infinity
 * 3. Forgetting to handle unreachable vertices
 *
 * Interview Tips:
 * - BFS = shortest path for UNWEIGHTED graphs
 * - Dijkstra = shortest path for WEIGHTED graphs (non-negative weights)
 * - Path reconstruction using parent array is a common follow-up
 * - This is the foundation for many graph problems
 */
