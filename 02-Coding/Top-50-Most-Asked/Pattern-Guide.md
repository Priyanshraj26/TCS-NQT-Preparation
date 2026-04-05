# Coding Patterns Guide — TCS NQT

Master these 10 patterns and you can solve 90% of TCS NQT coding questions.

---

## Pattern 1: Two Pointers

**When to use:** Sorted arrays, finding pairs, palindrome checks, partitioning

**Template:**
```cpp
int left = 0, right = n - 1;
while (left < right) {
    int sum = arr[left] + arr[right];
    if (sum == target) return {left, right};
    else if (sum < target) left++;
    else right--;
}
```

**Questions:** Two Sum (sorted), Sort 0s/1s/2s, Reverse Array, Move Negatives, Palindrome Check

**Key insight:** Reduces O(n²) brute force to O(n) by eliminating unnecessary comparisons.

---

## Pattern 2: Sliding Window

**When to use:** Subarray/substring problems with a condition (max/min length, sum, unique chars)

**Template:**
```cpp
int left = 0, result = 0;
for (int right = 0; right < n; right++) {
    // Add arr[right] to window
    while (/* window invalid */) {
        // Remove arr[left] from window
        left++;
    }
    result = max(result, right - left + 1);
}
```

**Questions:** Longest Substring Without Repeating, Subarray with Given Sum, Max Subarray (variant)

**Key insight:** Maintains a window that slides over data. O(n) because each element is added/removed at most once.

---

## Pattern 3: Hash Map / Hash Set

**When to use:** Need O(1) lookups — finding pairs, counting frequency, detecting duplicates

**Template:**
```cpp
unordered_map<int, int> mp;
for (int i = 0; i < n; i++) {
    if (mp.count(target - arr[i])) {
        // Found pair
    }
    mp[arr[i]] = i;
}
```

**Questions:** Two Sum, Contains Duplicate, First Non-Repeating Char, Anagram Check, Word Frequency

**Key insight:** Trade O(n) space for O(1) lookup time. Almost always worth it in interviews.

---

## Pattern 4: Binary Search

**When to use:** Sorted data, or when answer space is monotonic (can binary search on answer)

**Template:**
```cpp
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
return -1; // not found
```

**Variants:**
- Find first occurrence: when found, `hi = mid - 1` and track answer
- Find last occurrence: when found, `lo = mid + 1` and track answer
- Search on answer: binary search on possible answer range

**Questions:** Binary Search, Search Rotated Array, First & Last Position, Square Root, Count Occurrences

---

## Pattern 5: Kadane's Algorithm (Max Subarray)

**When to use:** Maximum/minimum subarray sum problems

**Template:**
```cpp
int maxSum = arr[0], current = arr[0];
for (int i = 1; i < n; i++) {
    current = max(arr[i], current + arr[i]);
    maxSum = max(maxSum, current);
}
```

**Key insight:** At each position, either extend the previous subarray or start a new one. O(n) time, O(1) space.

---

## Pattern 6: Stack (Monotonic Stack)

**When to use:** Next greater/smaller element, valid parentheses, expression evaluation

**Template (Next Greater Element):**
```cpp
stack<int> st;
vector<int> result(n, -1);
for (int i = 0; i < n; i++) {
    while (!st.empty() && arr[st.top()] < arr[i]) {
        result[st.top()] = arr[i];
        st.pop();
    }
    st.push(i);
}
```

**Questions:** Valid Parentheses, Next Greater Element, Trapping Rain Water (stack approach)

---

## Pattern 7: Recursion + Backtracking

**When to use:** Generate all permutations/combinations, solve puzzles, explore all possibilities

**Template:**
```cpp
void backtrack(vector<int>& path, vector<bool>& used) {
    if (path.size() == n) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.push_back(arr[i]);
        backtrack(path, used);
        path.pop_back();
        used[i] = false;
    }
}
```

**Questions:** All Permutations, Next Permutation, Subset Sum (backtrack approach)

---

## Pattern 8: Dynamic Programming

**When to use:** Overlapping subproblems + optimal substructure. Keywords: "minimum", "maximum", "count ways", "is possible"

**Steps to solve:**
1. Define state: `dp[i]` = answer for first i elements
2. Find recurrence: `dp[i] = f(dp[i-1], dp[i-2], ...)`
3. Identify base case: `dp[0] = ...`
4. Determine order: bottom-up (iterative) or top-down (memoized recursion)

**Template (Bottom-up):**
```cpp
vector<int> dp(n + 1, 0);
dp[0] = base_case;
for (int i = 1; i <= n; i++) {
    dp[i] = /* recurrence */;
}
return dp[n];
```

**Common DP types:**
- 1D: Fibonacci, Climbing Stairs, LIS, Max Sum No Adjacent
- 2D: LCS, Knapsack, Edit Distance, Matrix Chain
- On strings: LCS, Edit Distance, Palindromic Substring

---

## Pattern 9: BFS / DFS (Graph/Tree Traversal)

**BFS (Level-order, shortest path in unweighted graph):**
```cpp
queue<int> q;
vector<bool> visited(n, false);
q.push(start); visited[start] = true;
while (!q.empty()) {
    int node = q.front(); q.pop();
    for (int next : adj[node]) {
        if (!visited[next]) {
            visited[next] = true;
            q.push(next);
        }
    }
}
```

**DFS (Explore all paths, cycle detection, topological sort):**
```cpp
void dfs(int node) {
    visited[node] = true;
    for (int next : adj[node]) {
        if (!visited[next]) dfs(next);
    }
}
```

**Questions:** Tree traversals, Level Order, BFS/DFS of Graph, Cycle Detection, Connected Components, Topological Sort

---

## Pattern 10: Greedy

**When to use:** Making locally optimal choice leads to global optimum

**Questions:** Stock Buy & Sell, Merge Intervals (variant)

**Key insight:** Sort the data, then make the best local choice at each step. Prove the greedy choice property before using.

---

## Pattern Recognition Cheat Sheet

| If the problem says... | Try this pattern |
|------------------------|------------------|
| "Find pair with sum X" | Two Pointers / Hash Map |
| "Longest/shortest subarray" | Sliding Window |
| "Check duplicates/frequency" | Hash Set / Hash Map |
| "Sorted array + search" | Binary Search |
| "Maximum subarray sum" | Kadane's Algorithm |
| "Next greater/smaller" | Monotonic Stack |
| "All permutations/combinations" | Backtracking |
| "Minimum cost / count ways" | Dynamic Programming |
| "Shortest path / connected" | BFS / DFS |
| "Best local choice works" | Greedy |
| "Tree traversal" | DFS (recursive) or BFS (queue) |
| "Cycle detection" | Floyd's (linked list) / DFS coloring (graph) |
