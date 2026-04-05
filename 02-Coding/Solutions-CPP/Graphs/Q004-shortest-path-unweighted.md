# Solution: Shortest Path in Unweighted Graph

[← Back to Question](../../DSA-Questions/Graphs/Q004-shortest-path-unweighted.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| BFS | O(V + E) | O(V) | Yes (optimal for unweighted) |

## Approach 1: BFS Shortest Path

### Intuition

In an unweighted graph, BFS naturally finds the shortest path because it explores all vertices at distance d before exploring vertices at distance d+1. Maintain a `dist[]` array initialized to -1 (unvisited). The distance of the source is 0. When we visit a neighbor, its distance is parent's distance + 1.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// --- BFS Shortest Path (distances only) ---
vector<int> shortestPath(int source, const vector<vector<int>>& adj, int V) {
    vector<int> dist(V, -1); // -1 means unreachable
    queue<int> q;

    dist[source] = 0;
    q.push(source);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        for (int neighbor : adj[node]) {
            if (dist[neighbor] == -1) { // not visited
                dist[neighbor] = dist[node] + 1;
                q.push(neighbor);
            }
        }
    }
    return dist;
}

// --- BFS Shortest Path (with path reconstruction) ---
vector<int> shortestPathWithRoute(int source, int target,
                                   const vector<vector<int>>& adj, int V) {
    vector<int> dist(V, -1);
    vector<int> parent(V, -1);
    queue<int> q;

    dist[source] = 0;
    q.push(source);

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

    // Reconstruct path from target to source
    vector<int> path;
    if (dist[target] == -1) return path; // unreachable

    for (int node = target; node != -1; node = parent[node]) {
        path.push_back(node);
    }
    // Reverse to get source -> target
    reverse(path.begin(), path.end());
    return path;
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

    cout << "Test 1 - Distances from 0: ";
    printVector(shortestPath(0, adj1, V1));
    // Expected: [0, 1, 2, 1, 2, 3]

    cout << "Test 1 - Path 0 to 5: ";
    printVector(shortestPathWithRoute(0, 5, adj1, V1));
    // Expected: [0, 1, 2, 5]

    // Test 2: Disconnected graph
    //  0 -- 1    2 -- 3
    int V2 = 4;
    vector<vector<int>> adj2(V2);
    adj2[0] = {1};
    adj2[1] = {0};
    adj2[2] = {3};
    adj2[3] = {2};

    cout << "Test 2 - Distances from 0: ";
    printVector(shortestPath(0, adj2, V2));
    // Expected: [0, 1, -1, -1] (-1 = unreachable)

    cout << "Test 2 - Path 0 to 3: ";
    printVector(shortestPathWithRoute(0, 3, adj2, V2));
    // Expected: [] (unreachable)

    // Test 3: Single node
    int V3 = 1;
    vector<vector<int>> adj3(V3);
    cout << "Test 3 - Single node: ";
    printVector(shortestPath(0, adj3, V3));
    // Expected: [0]

    // Test 4: Linear graph
    //  0 -- 1 -- 2 -- 3 -- 4
    int V4 = 5;
    vector<vector<int>> adj4(V4);
    adj4[0] = {1};
    adj4[1] = {0, 2};
    adj4[2] = {1, 3};
    adj4[3] = {2, 4};
    adj4[4] = {3};
    cout << "Test 4 - Distances from 0: ";
    printVector(shortestPath(0, adj4, V4));
    // Expected: [0, 1, 2, 3, 4]

    cout << "Test 4 - Path 0 to 4: ";
    printVector(shortestPathWithRoute(0, 4, adj4, V4));
    // Expected: [0, 1, 2, 3, 4]

    return 0;
}
```

### Dry Run

```
Graph: 0--1--2, 0--3--4--5--2
Source: 0

dist = [-1,-1,-1,-1,-1,-1]
dist[0]=0, Queue: [0]

Pop 0 (dist=0): neighbors 1,3
  dist[1]=1, dist[3]=1. Queue: [1, 3]

Pop 1 (dist=1): neighbors 0(visited), 2
  dist[2]=2. Queue: [3, 2]

Pop 3 (dist=1): neighbors 0(visited), 4
  dist[4]=2. Queue: [2, 4]

Pop 2 (dist=2): neighbors 1(visited), 5
  dist[5]=3. Queue: [4, 5]

Pop 4 (dist=2): neighbors 3(visited), 5(visited)
Pop 5 (dist=3): no unvisited

dist = [0, 1, 2, 1, 2, 3]
```

### Complexity Analysis

- **Time:** O(V + E) -- standard BFS
- **Space:** O(V) -- dist array + queue + parent array

## Common Mistakes

1. Using DFS for shortest path -- DFS does NOT guarantee shortest path in general graphs
2. Not initializing distances to -1 or infinity
3. Forgetting that BFS only works for unweighted graphs -- use Dijkstra for weighted graphs
4. Not handling unreachable nodes (dist remains -1)

## Interview Tips

- BFS = shortest path in unweighted graphs. This is a fundamental fact to state.
- Path reconstruction using parent array is a common follow-up
- For weighted graphs, mention Dijkstra's algorithm as the alternative
- This is the foundation for many problems: word ladder, maze solving, network delay, etc.
