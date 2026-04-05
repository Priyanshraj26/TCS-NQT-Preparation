# Solution: Topological Sort

[← Back to Question](../../DSA-Questions/Graphs/Q006-topological-sort.md)

## Approach Overview

| Approach | Time | Space | Recommended |
|----------|------|-------|-------------|
| Kahn's Algorithm (BFS) | O(V + E) | O(V) | Yes (interviews, also detects cycles) |
| DFS-based | O(V + E) | O(V) | Also good |

## Approach 1: Kahn's Algorithm (BFS with Indegree)

### Intuition

Compute the in-degree (number of incoming edges) for every vertex. Start with all vertices that have in-degree 0 (no dependencies). Process them, reduce the in-degree of their neighbors, and add any neighbor whose in-degree becomes 0. If all vertices are processed, the order is a valid topological sort. If not, a cycle exists.

### C++ Code

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

// --- Kahn's Algorithm (BFS) ---
vector<int> topologicalSortKahn(const vector<vector<int>>& adj, int V) {
    vector<int> indegree(V, 0);

    // Compute in-degrees
    for (int u = 0; u < V; u++) {
        for (int v : adj[u]) {
            indegree[v]++;
        }
    }

    // Enqueue all vertices with in-degree 0
    queue<int> q;
    for (int i = 0; i < V; i++) {
        if (indegree[i] == 0) q.push(i);
    }

    vector<int> order;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order.push_back(node);
        for (int neighbor : adj[node]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    // If order doesn't contain all vertices, there's a cycle
    if ((int)order.size() != V) {
        cout << "  [CYCLE DETECTED - no valid topological order]" << endl;
        return {};
    }
    return order;
}

// --- DFS-based Topological Sort ---
bool dfsTopo(int node, const vector<vector<int>>& adj,
             vector<int>& state, stack<int>& st) {
    state[node] = 1; // visiting (gray)
    for (int neighbor : adj[node]) {
        if (state[neighbor] == 1) return false; // back edge => cycle
        if (state[neighbor] == 0) {
            if (!dfsTopo(neighbor, adj, state, st)) return false;
        }
    }
    state[node] = 2; // done (black)
    st.push(node);
    return true;
}

vector<int> topologicalSortDFS(const vector<vector<int>>& adj, int V) {
    vector<int> state(V, 0); // 0=unvisited, 1=visiting, 2=done
    stack<int> st;

    for (int i = 0; i < V; i++) {
        if (state[i] == 0) {
            if (!dfsTopo(i, adj, state, st)) {
                cout << "  [CYCLE DETECTED]" << endl;
                return {};
            }
        }
    }

    vector<int> order;
    while (!st.empty()) {
        order.push_back(st.top());
        st.pop();
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
    // Test 1: DAG (course prerequisites)
    // 0 -> 1 -> 3
    // 0 -> 2 -> 3
    //       2 -> 4
    int V1 = 5;
    vector<vector<int>> adj1(V1);
    adj1[0] = {1, 2};
    adj1[1] = {3};
    adj1[2] = {3, 4};

    cout << "Test 1 (Kahn): ";
    printVector(topologicalSortKahn(adj1, V1));
    // Expected: [0, 1, 2, 3, 4] or [0, 2, 1, 4, 3] etc. (any valid order)

    cout << "Test 1 (DFS):  ";
    printVector(topologicalSortDFS(adj1, V1));

    // Test 2: Linear chain
    // 0 -> 1 -> 2 -> 3
    int V2 = 4;
    vector<vector<int>> adj2(V2);
    adj2[0] = {1};
    adj2[1] = {2};
    adj2[2] = {3};

    cout << "Test 2 (Kahn): ";
    printVector(topologicalSortKahn(adj2, V2));
    // Expected: [0, 1, 2, 3]

    // Test 3: Graph with cycle
    // 0 -> 1 -> 2 -> 0
    int V3 = 3;
    vector<vector<int>> adj3(V3);
    adj3[0] = {1};
    adj3[1] = {2};
    adj3[2] = {0};

    cout << "Test 3 (Kahn): ";
    printVector(topologicalSortKahn(adj3, V3));
    // Expected: [] with cycle detected message

    cout << "Test 3 (DFS):  ";
    printVector(topologicalSortDFS(adj3, V3));
    // Expected: [] with cycle detected message

    // Test 4: Independent vertices
    int V4 = 3;
    vector<vector<int>> adj4(V4);
    cout << "Test 4 (Kahn): ";
    printVector(topologicalSortKahn(adj4, V4));
    // Expected: [0, 1, 2] (any order is valid)

    // Test 5: Diamond dependency
    //    0
    //   / \
    //  1   2
    //   \ /
    //    3
    int V5 = 4;
    vector<vector<int>> adj5(V5);
    adj5[0] = {1, 2};
    adj5[1] = {3};
    adj5[2] = {3};
    cout << "Test 5 (Kahn): ";
    printVector(topologicalSortKahn(adj5, V5));
    // Expected: [0, 1, 2, 3] or [0, 2, 1, 3]

    return 0;
}
```

### Dry Run (Kahn's)

```
DAG: 0->1->3, 0->2->3, 2->4

In-degrees: [0:0, 1:1, 2:1, 3:2, 4:1]

Queue: [0] (indegree 0)
Pop 0, order=[0]. Reduce neighbors 1,2:
  indegree[1]=0, indegree[2]=0. Queue: [1, 2]

Pop 1, order=[0,1]. Reduce neighbor 3:
  indegree[3]=1. Queue: [2]

Pop 2, order=[0,1,2]. Reduce neighbors 3,4:
  indegree[3]=0, indegree[4]=0. Queue: [3, 4]

Pop 3, order=[0,1,2,3]. No neighbors with reduced indegree.
Pop 4, order=[0,1,2,3,4].

Result: [0, 1, 2, 3, 4]
```

### Complexity Analysis

- **Time:** O(V + E) -- compute indegrees O(E), BFS O(V + E)
- **Space:** O(V) -- indegree array + queue

## Common Mistakes

1. Applying topological sort to undirected graphs -- it only applies to DAGs (directed acyclic graphs)
2. Forgetting to check for cycles (order.size() != V in Kahn's)
3. In DFS approach, forgetting to push to stack after processing all neighbors (post-order)
4. Confusing the 3 states in DFS: unvisited, visiting (in current path), done

## Interview Tips

- Kahn's algorithm is generally easier to implement and also detects cycles naturally
- DFS approach: the key is to push to stack in post-order and reverse at the end
- Topological sort has many applications: build systems, course scheduling, task ordering
- Multiple valid topological orders may exist -- any one is acceptable
- If the interviewer asks for lexicographically smallest order, use a min-heap instead of queue in Kahn's
