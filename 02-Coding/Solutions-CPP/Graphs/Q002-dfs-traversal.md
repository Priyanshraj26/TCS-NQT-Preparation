# Solution: DFS Traversal of Graph

[← Back to Question](../../DSA-Questions/Graphs/Q002-dfs-traversal.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Recursive DFS | O(V + E) | O(V) | Yes (interviews) |
| Iterative DFS (stack) | O(V + E) | O(V) | Good to know |

## Approach 1: Recursive DFS

### Intuition

Start from a source node, visit it, then recursively visit each unvisited neighbor. This explores as deep as possible along each branch before backtracking.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// --- Recursive DFS ---
void dfsRecursive(int node, const vector<vector<int>>& adj,
                  vector<bool>& visited, vector<int>& order) {
    visited[node] = true;
    order.push_back(node);
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfsRecursive(neighbor, adj, visited, order);
        }
    }
}

// --- Iterative DFS ---
vector<int> dfsIterative(int source, const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    vector<int> order;
    stack<int> st;

    st.push(source);
    while (!st.empty()) {
        int node = st.top();
        st.pop();

        if (visited[node]) continue;
        visited[node] = true;
        order.push_back(node);

        // Push neighbors in reverse order so smallest is processed first
        for (int i = (int)adj[node].size() - 1; i >= 0; i--) {
            if (!visited[adj[node][i]]) {
                st.push(adj[node][i]);
            }
        }
    }
    return order;
}

// --- DFS for disconnected graph ---
vector<int> dfsDisconnected(const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    vector<int> order;
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfsRecursive(i, adj, visited, order);
        }
    }
    return order;
}

void printVector(const vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    // Test 1: Connected graph
    //  0 -- 1 -- 2
    //  |         |
    //  3 -- 4 -- 5
    int V1 = 6;
    vector<vector<int>> adj1(V1);
    adj1[0] = {1, 3};
    adj1[1] = {0, 2};
    adj1[2] = {1, 5};
    adj1[3] = {0, 4};
    adj1[4] = {3, 5};
    adj1[5] = {2, 4};

    vector<bool> vis1(V1, false);
    vector<int> order1;
    dfsRecursive(0, adj1, vis1, order1);
    cout << "Test 1 (recursive from 0): ";
    printVector(order1);
    // Expected: [0, 1, 2, 5, 4, 3]

    cout << "Test 1 (iterative from 0): ";
    printVector(dfsIterative(0, adj1, V1));
    // Expected: [0, 1, 2, 5, 4, 3]

    // Test 2: Disconnected graph
    //  0 -- 1    2 -- 3    4
    int V2 = 5;
    vector<vector<int>> adj2(V2);
    adj2[0] = {1};
    adj2[1] = {0};
    adj2[2] = {3};
    adj2[3] = {2};

    cout << "Test 2 (disconnected): ";
    printVector(dfsDisconnected(adj2, V2));
    // Expected: [0, 1, 2, 3, 4]

    // Test 3: Single node
    int V3 = 1;
    vector<vector<int>> adj3(V3);
    cout << "Test 3 (single): ";
    printVector(dfsIterative(0, adj3, V3));
    // Expected: [0]

    // Test 4: Complete graph K4
    int V4 = 4;
    vector<vector<int>> adj4(V4);
    adj4[0] = {1, 2, 3};
    adj4[1] = {0, 2, 3};
    adj4[2] = {0, 1, 3};
    adj4[3] = {0, 1, 2};
    cout << "Test 4 (K4 from 0): ";
    printVector(dfsIterative(0, adj4, V4));
    // Expected: [0, 1, 2, 3]

    return 0;
}
```

### Dry Run (Recursive)

```
Graph: 0--1--2, 0--3
Source: 0

dfs(0): visit 0. Neighbors: 1, 3
  dfs(1): visit 1. Neighbors: 0(visited), 2
    dfs(2): visit 2. Neighbors: 1(visited)
      return
    return
  dfs(3): visit 3. Neighbors: 0(visited)
    return

Order: [0, 1, 2, 3]
```

### Complexity Analysis

- **Time:** O(V + E) -- each vertex visited once, each edge examined once
- **Space:** O(V) -- visited array + recursion stack (or explicit stack)

## Common Mistakes

1. Not checking `visited` before recursing -- causes infinite loops in cyclic graphs
2. Forgetting to handle disconnected graphs
3. Iterative DFS may visit nodes in different order than recursive due to stack LIFO order
4. Pushing visited nodes onto the stack in iterative version (wastes time, may cause issues)

## Interview Tips

- DFS is used for: cycle detection, topological sort, connected components, path finding
- Recursive is cleaner but can stack overflow for very deep graphs -- mention iterative as fallback
- BFS vs DFS: BFS for shortest path, DFS for exhaustive search / backtracking
- Time complexity is the same O(V + E) for both BFS and DFS
