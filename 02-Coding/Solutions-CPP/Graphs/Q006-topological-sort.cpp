/*
 * Q006: Topological Sort (Kahn's / DFS)
 * Question: DSA-Questions/Graphs/Q006-topological-sort.md
 *
 * Approach Overview:
 * +------------------+----------+---------+
 * | Approach         | Time     | Space   |
 * +------------------+----------+---------+
 * | Kahn's (BFS)     | O(V+E)   | O(V)    |
 * | DFS              | O(V+E)   | O(V)    |
 * +------------------+----------+---------+
 */

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

// ==================== Approach 1: Kahn's Algorithm (BFS) ====================
/*
 * Algorithm:
 * 1. Compute in-degree for each vertex.
 * 2. Add all vertices with in-degree 0 to a queue.
 * 3. While queue not empty:
 *    a. Dequeue vertex, add to result.
 *    b. Reduce in-degree of all neighbors by 1.
 *    c. If any neighbor's in-degree becomes 0, enqueue it.
 * 4. If result size != V, graph has a cycle (not a DAG).
 *
 * Dry Run: V=6, Edges: (5,2),(5,0),(4,0),(4,1),(2,3),(3,1)
 *   In-degrees: [2,2,1,1,0,0]
 *   Queue: [4,5] (in-degree 0)
 *   Process 4: reduce in-degree of 0,1. In-degrees: [1,1,1,1,-,-]
 *   Process 5: reduce in-degree of 2,0. In-degrees: [0,1,0,1,-,-]
 *   Queue gets: 0,2
 *   Process 0: (no outgoing). Process 2: reduce 3. In-degrees: [-,1,-,0,-,-]
 *   Queue gets: 3
 *   Process 3: reduce 1. In-degrees: [-,0,-,-,-,-]
 *   Queue gets: 1. Process 1.
 *   Result: [4, 5, 0, 2, 3, 1]
 */
vector<int> topologicalSortKahn(int V, vector<vector<int>>& adj) {
    vector<int> inDegree(V, 0);
    vector<int> result;

    // Compute in-degrees
    for (int u = 0; u < V; u++) {
        for (int v : adj[u]) {
            inDegree[v]++;
        }
    }

    // Enqueue vertices with in-degree 0
    queue<int> q;
    for (int i = 0; i < V; i++) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        result.push_back(node);

        for (int neighbor : adj[node]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    // If result size != V, there's a cycle
    if ((int)result.size() != V) {
        cout << "  WARNING: Graph has a cycle! Not a DAG." << endl;
        return {};
    }

    return result;
}

// ==================== Approach 2: DFS ====================
/*
 * Post-order DFS: after processing all descendants, push current node to stack.
 * Stack gives reverse topological order.
 */
void dfsHelper(int node, vector<vector<int>>& adj, vector<bool>& visited,
               stack<int>& st) {
    visited[node] = true;

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfsHelper(neighbor, adj, visited, st);
        }
    }

    st.push(node);  // Post-order: push after all descendants
}

vector<int> topologicalSortDFS(int V, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    stack<int> st;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfsHelper(i, adj, visited, st);
        }
    }

    vector<int> result;
    while (!st.empty()) {
        result.push_back(st.top());
        st.pop();
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
    // Test Case 1: Classic DAG
    cout << "=== Test Case 1 ===" << endl;
    int V1 = 6;
    vector<vector<int>> adj1(V1);
    adj1[5].push_back(2); adj1[5].push_back(0);
    adj1[4].push_back(0); adj1[4].push_back(1);
    adj1[2].push_back(3); adj1[3].push_back(1);

    vector<int> r1 = topologicalSortKahn(V1, adj1);
    cout << "Kahn's: "; printVector(r1);
    vector<int> r1b = topologicalSortDFS(V1, adj1);
    cout << "DFS:    "; printVector(r1b);

    // Test Case 2: Linear chain (0 -> 1 -> 2)
    cout << "\n=== Test Case 2: Linear ===" << endl;
    int V2 = 3;
    vector<vector<int>> adj2(V2);
    adj2[0].push_back(1);
    adj2[1].push_back(2);

    vector<int> r2 = topologicalSortKahn(V2, adj2);
    cout << "Kahn's: "; printVector(r2);  // [0, 1, 2]

    // Test Case 3: No edges (all independent)
    cout << "\n=== Test Case 3: Independent ===" << endl;
    int V3 = 4;
    vector<vector<int>> adj3(V3);
    vector<int> r3 = topologicalSortKahn(V3, adj3);
    cout << "Kahn's: "; printVector(r3);  // Any permutation of [0,1,2,3]

    // Test Case 4: Course schedule style
    cout << "\n=== Test Case 4: Course schedule ===" << endl;
    // 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
    int V4 = 4;
    vector<vector<int>> adj4(V4);
    adj4[0].push_back(1); adj4[0].push_back(2);
    adj4[1].push_back(3); adj4[2].push_back(3);

    vector<int> r4 = topologicalSortKahn(V4, adj4);
    cout << "Kahn's: "; printVector(r4);  // [0, 1, 2, 3] or [0, 2, 1, 3]

    return 0;
}

/*
 * Complexity Analysis:
 * - Both: O(V + E) time, O(V) space
 *
 * Common Mistakes:
 * 1. Applying topological sort to a graph with cycles (only works on DAGs)
 * 2. In DFS approach, not pushing to stack in POST-order
 * 3. Forgetting to iterate all vertices (disconnected DAG)
 *
 * Interview Tips:
 * - Kahn's can detect cycles (if result.size() != V, cycle exists)
 * - Used in: course scheduling, build systems, task ordering
 * - LeetCode #207 (Course Schedule) and #210 (Course Schedule II) use this
 * - Kahn's is generally easier to implement and explain in interviews
 */
