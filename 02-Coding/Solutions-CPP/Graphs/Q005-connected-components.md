# Solution: Count Connected Components

[← Back to Question](../../DSA-Questions/Graphs/Q005-connected-components.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| DFS | O(V + E) | O(V) | Yes (interviews) |
| BFS | O(V + E) | O(V) | Also good |
| Union-Find | O(E * alpha(V)) | O(V) | Advanced |

## Approach 1: DFS Counting Components

### Intuition

Iterate through all vertices. For each unvisited vertex, start a DFS/BFS to mark all reachable vertices as visited. Each time we start a new DFS from an unvisited vertex, we have found a new connected component.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// --- DFS helper ---
void dfs(int node, const vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adj, visited);
        }
    }
}

// --- Count components using DFS ---
int countComponentsDFS(const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    int count = 0;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfs(i, adj, visited);
            count++;
        }
    }
    return count;
}

// --- Count components using BFS ---
int countComponentsBFS(const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    int count = 0;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
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
            count++;
        }
    }
    return count;
}

// --- Union-Find approach ---
class UnionFind {
    vector<int> parent, rank_;
public:
    UnionFind(int n) : parent(n), rank_(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank_[px] < rank_[py]) swap(px, py);
        parent[py] = px;
        if (rank_[px] == rank_[py]) rank_[px]++;
        return true;
    }
};

int countComponentsUF(const vector<vector<int>>& adj, int V) {
    UnionFind uf(V);
    int components = V;
    for (int u = 0; u < V; u++) {
        for (int v : adj[u]) {
            if (u < v && uf.unite(u, v)) { // u < v to avoid double counting
                components--;
            }
        }
    }
    return components;
}

int main() {
    // Test 1: Three components
    //  0 -- 1    2 -- 3    4
    int V1 = 5;
    vector<vector<int>> adj1(V1);
    adj1[0] = {1};
    adj1[1] = {0};
    adj1[2] = {3};
    adj1[3] = {2};

    cout << "Test 1 (DFS): " << countComponentsDFS(adj1, V1) << endl;
    cout << "Test 1 (BFS): " << countComponentsBFS(adj1, V1) << endl;
    cout << "Test 1 (UF):  " << countComponentsUF(adj1, V1) << endl;
    // Expected: 3

    // Test 2: Fully connected
    //  0 -- 1 -- 2 -- 3
    int V2 = 4;
    vector<vector<int>> adj2(V2);
    adj2[0] = {1};
    adj2[1] = {0, 2};
    adj2[2] = {1, 3};
    adj2[3] = {2};
    cout << "Test 2: " << countComponentsDFS(adj2, V2) << endl;
    // Expected: 1

    // Test 3: All isolated
    int V3 = 4;
    vector<vector<int>> adj3(V3);
    cout << "Test 3: " << countComponentsDFS(adj3, V3) << endl;
    // Expected: 4

    // Test 4: Single node
    int V4 = 1;
    vector<vector<int>> adj4(V4);
    cout << "Test 4: " << countComponentsDFS(adj4, V4) << endl;
    // Expected: 1

    // Test 5: Two components with cycles
    //  0 -- 1     3 -- 4
    //  |    |     |    |
    //  2 ---+     5 ---+
    int V5 = 6;
    vector<vector<int>> adj5(V5);
    adj5[0] = {1, 2};
    adj5[1] = {0, 2};
    adj5[2] = {0, 1};
    adj5[3] = {4, 5};
    adj5[4] = {3, 5};
    adj5[5] = {3, 4};
    cout << "Test 5: " << countComponentsDFS(adj5, V5) << endl;
    // Expected: 2

    return 0;
}
```

### Dry Run

```
Graph: 0--1  2--3  4  (V=5)

i=0: not visited. DFS(0) visits {0, 1}. count=1
i=1: visited, skip
i=2: not visited. DFS(2) visits {2, 3}. count=2
i=3: visited, skip
i=4: not visited. DFS(4) visits {4}. count=3

Result: 3 components
```

### Complexity Analysis

- **Time:** O(V + E) -- each vertex and edge visited at most once
- **Space:** O(V) -- visited array + recursion/queue

## Common Mistakes

1. Not iterating through ALL vertices -- only starting DFS from vertex 0 misses disconnected components
2. Forgetting that isolated vertices (no edges) are each their own component
3. In Union-Find, processing undirected edges twice (from both endpoints)

## Interview Tips

- This is a fundamental graph problem -- many advanced problems reduce to connected components
- The number of components = V - (number of edges in a spanning forest)
- For dynamic graphs (edges added/removed), Union-Find is better than repeated DFS
- Related problems: number of islands (grid), friend circles, accounts merge
