# Solution: BFS Traversal of Graph

[← Back to Question](../../DSA-Questions/Graphs/Q001-bfs-traversal.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Queue-based BFS | O(V + E) | O(V) | Yes (standard) |

## Approach 1: Queue-Based BFS

### Intuition

Start from a source node, visit all its neighbors first, then visit their neighbors, and so on. Use a queue (FIFO) to maintain the order and a visited array to avoid revisiting nodes. This explores the graph level by level.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// --- BFS from a single source ---
vector<int> bfs(int source, const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    vector<int> order;
    queue<int> q;

    visited[source] = true;
    q.push(source);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order.push_back(node);

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
    return order;
}

// --- BFS for disconnected graph (visits all components) ---
vector<int> bfsDisconnected(const vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    vector<int> order;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            queue<int> q;
            visited[i] = true;
            q.push(i);
            while (!q.empty()) {
                int node = q.front();
                q.pop();
                order.push_back(node);
                for (int neighbor : adj[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
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

    cout << "Test 1 (from 0): ";
    printVector(bfs(0, adj1, V1));
    // Expected: [0, 1, 3, 2, 4, 5]

    cout << "Test 1 (from 2): ";
    printVector(bfs(2, adj1, V1));
    // Expected: [2, 1, 5, 0, 4, 3]

    // Test 2: Disconnected graph
    //  0 -- 1    2 -- 3
    int V2 = 4;
    vector<vector<int>> adj2(V2);
    adj2[0] = {1};
    adj2[1] = {0};
    adj2[2] = {3};
    adj2[3] = {2};

    cout << "Test 2 (disconnected): ";
    printVector(bfsDisconnected(adj2, V2));
    // Expected: [0, 1, 2, 3]

    // Test 3: Single node
    int V3 = 1;
    vector<vector<int>> adj3(V3);
    cout << "Test 3 (single): ";
    printVector(bfs(0, adj3, V3));
    // Expected: [0]

    // Test 4: Star graph
    //    1
    //    |
    // 2--0--3
    //    |
    //    4
    int V4 = 5;
    vector<vector<int>> adj4(V4);
    adj4[0] = {1, 2, 3, 4};
    adj4[1] = {0};
    adj4[2] = {0};
    adj4[3] = {0};
    adj4[4] = {0};
    cout << "Test 4 (star from 0): ";
    printVector(bfs(0, adj4, V4));
    // Expected: [0, 1, 2, 3, 4]

    return 0;
}
```

### Dry Run

```
Graph: 0--1--2, 0--3
Source: 0

Queue: [0], visited={0}
Pop 0, add to order. Neighbors: 1,3
  Mark 1 visited, push. Mark 3 visited, push.
Queue: [1, 3], order=[0]

Pop 1, add to order. Neighbors: 0,2
  0 already visited. Mark 2 visited, push.
Queue: [3, 2], order=[0, 1]

Pop 3, add to order. Neighbors: 0
  0 already visited.
Queue: [2], order=[0, 1, 3]

Pop 2, add to order. No unvisited neighbors.
Queue: [], order=[0, 1, 3, 2]
```

### Complexity Analysis

- **Time:** O(V + E) -- each vertex dequeued once, each edge examined once
- **Space:** O(V) -- visited array + queue

## Common Mistakes

1. Not marking a node as visited when pushing (not when popping) -- this causes duplicates in queue
2. Forgetting to handle disconnected graphs (need to loop through all vertices)
3. Using DFS (stack) instead of BFS (queue)
4. Not initializing the visited array

## Interview Tips

- BFS is the go-to for shortest path in unweighted graphs
- Mark visited WHEN PUSHING, not when popping -- this avoids duplicate entries
- BFS explores level by level -- useful for "minimum steps" type problems
- Always mention O(V + E) complexity -- interviewers look for this
