# Solution: Detect Cycle in Undirected Graph

[← Back to Question](../../DSA-Questions/Graphs/Q003-detect-cycle-undirected.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| DFS with parent tracking | O(V + E) | O(V) | Yes (interviews) |
| BFS with parent tracking | O(V + E) | O(V) | Alternative |
| Union-Find | O(E * alpha(V)) | O(V) | Advanced |

## Approach 1: DFS with Parent Tracking

### Intuition

During DFS, if we encounter a neighbor that is already visited AND is not the parent of the current node, then a cycle exists. We track the parent because in an undirected graph, the edge back to the parent does not count as a cycle.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// --- DFS Cycle Detection ---
bool dfsCycle(int node, int parent, const vector<vector<int>>& adj,
              vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            if (dfsCycle(neighbor, node, adj, visited))
                return true;
        } else if (neighbor != parent) {
            return true; // visited neighbor that is NOT parent => cycle
        }
    }
    return false;
}

bool hasCycleDFS(const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            if (dfsCycle(i, -1, adj, visited))
                return true;
        }
    }
    return false;
}

// --- BFS Cycle Detection ---
bool hasCycleBFS(const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    for (int i = 0; i < V; i++) {
        if (visited[i]) continue;
        queue<pair<int, int>> q; // {node, parent}
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
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    // Test 1: Graph with cycle
    //  0 -- 1
    //  |    |
    //  3 -- 2
    int V1 = 4;
    vector<vector<int>> adj1(V1);
    adj1[0] = {1, 3};
    adj1[1] = {0, 2};
    adj1[2] = {1, 3};
    adj1[3] = {2, 0};
    cout << "Test 1 (cycle, DFS): " << (hasCycleDFS(adj1, V1) ? "true" : "false") << endl;
    cout << "Test 1 (cycle, BFS): " << (hasCycleBFS(adj1, V1) ? "true" : "false") << endl;
    // Expected: true, true

    // Test 2: Tree (no cycle)
    //  0 -- 1 -- 2
    //       |
    //       3
    int V2 = 4;
    vector<vector<int>> adj2(V2);
    adj2[0] = {1};
    adj2[1] = {0, 2, 3};
    adj2[2] = {1};
    adj2[3] = {1};
    cout << "Test 2 (tree, DFS): " << (hasCycleDFS(adj2, V2) ? "true" : "false") << endl;
    cout << "Test 2 (tree, BFS): " << (hasCycleBFS(adj2, V2) ? "true" : "false") << endl;
    // Expected: false, false

    // Test 3: Disconnected, one component has cycle
    //  0 -- 1    2 -- 3
    //             |  /
    //             4
    int V3 = 5;
    vector<vector<int>> adj3(V3);
    adj3[0] = {1};
    adj3[1] = {0};
    adj3[2] = {3, 4};
    adj3[3] = {2, 4};
    adj3[4] = {2, 3};
    cout << "Test 3 (disconnected+cycle): " << (hasCycleDFS(adj3, V3) ? "true" : "false") << endl;
    // Expected: true

    // Test 4: Single node
    int V4 = 1;
    vector<vector<int>> adj4(V4);
    cout << "Test 4 (single): " << (hasCycleDFS(adj4, V4) ? "true" : "false") << endl;
    // Expected: false

    // Test 5: Two nodes, one edge (no cycle)
    int V5 = 2;
    vector<vector<int>> adj5(V5);
    adj5[0] = {1};
    adj5[1] = {0};
    cout << "Test 5 (two nodes): " << (hasCycleDFS(adj5, V5) ? "true" : "false") << endl;
    // Expected: false

    return 0;
}
```

### Dry Run

```
Graph: 0--1--2--3--0 (cycle)

dfsCycle(0, parent=-1):
  visit 0. Neighbors: 1, 3
  dfsCycle(1, parent=0):
    visit 1. Neighbors: 0(visited, parent=skip), 2
    dfsCycle(2, parent=1):
      visit 2. Neighbors: 1(visited, parent=skip), 3
      dfsCycle(3, parent=2):
        visit 3. Neighbors: 2(visited, parent=skip), 0
        0 is visited and NOT parent(2) => CYCLE FOUND!
```

### Complexity Analysis

- **Time:** O(V + E) -- standard DFS/BFS traversal
- **Space:** O(V) -- visited array + recursion stack

## Common Mistakes

1. Not tracking the parent -- every undirected edge creates a "back edge" to the parent, which is not a cycle
2. Forgetting to handle disconnected graphs (must iterate through all vertices)
3. For multigraphs (multiple edges between same pair), parent tracking alone is insufficient -- need to track edge IDs
4. Confusing directed and undirected cycle detection (directed needs coloring: white/gray/black)

## Interview Tips

- For undirected: parent tracking is sufficient
- For directed: you need a different approach (DFS with 3 colors or detect back edges)
- Union-Find is an alternative that processes edges one by one -- useful for dynamic graphs
- A tree is a connected acyclic graph with exactly V-1 edges
