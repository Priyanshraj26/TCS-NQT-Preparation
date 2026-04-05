# C++ Quick Reference for TCS NQT Coding

## Compilation & Execution
```bash
g++ -std=c++17 -O2 -Wall solution.cpp -o solution
./solution
./solution < input.txt          # from file
echo "5 1 2 3 4 5" | ./solution  # pipe input
```

---

## Input/Output Template
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    // Solution here
    
    cout << result << endl;
    return 0;
}
```

---

## STL Containers — Time Complexities

### vector
```cpp
vector<int> v;
v.push_back(x);       // O(1) amortized
v.pop_back();          // O(1)
v[i];                  // O(1)
v.size();              // O(1)
v.empty();             // O(1)
v.begin(), v.end();    // iterators
v.insert(pos, val);    // O(n)
v.erase(pos);          // O(n)
sort(v.begin(), v.end()); // O(n log n)
```

### string
```cpp
string s = "hello";
s.length();  s.size();    // O(1)
s[i];                     // O(1)
s.substr(pos, len);       // O(len)
s.find("sub");            // O(n*m)
s += "world";             // O(m) amortized
reverse(s.begin(), s.end()); // O(n)
to_string(42);            // int to string
stoi("42");               // string to int
```

### unordered_map / unordered_set
```cpp
unordered_map<int, int> mp;
mp[key] = val;                  // O(1) avg
mp.find(key) != mp.end();      // O(1) avg — check exists
mp.count(key);                  // O(1) avg — 0 or 1
mp.erase(key);                  // O(1) avg
for (auto& [k, v] : mp) {}     // iterate

unordered_set<int> st;
st.insert(x);                   // O(1) avg
st.count(x);                    // O(1) avg
```

### map / set (Ordered — Red-Black Tree)
```cpp
map<int, int> mp;      // sorted by key
mp[key] = val;         // O(log n)
mp.find(key);          // O(log n)
mp.lower_bound(key);   // O(log n) — first >= key
mp.upper_bound(key);   // O(log n) — first > key

set<int> st;
st.insert(x);          // O(log n)
st.lower_bound(x);     // O(log n)
```

### priority_queue (Heap)
```cpp
priority_queue<int> maxHeap;              // max at top
priority_queue<int, vector<int>, greater<int>> minHeap; // min at top
maxHeap.push(x);    // O(log n)
maxHeap.top();       // O(1)
maxHeap.pop();       // O(log n)
```

### stack / queue / deque
```cpp
stack<int> st;
st.push(x); st.top(); st.pop(); st.empty(); // all O(1)

queue<int> q;
q.push(x); q.front(); q.back(); q.pop(); // all O(1)

deque<int> dq;
dq.push_front(x); dq.push_back(x);  // O(1)
dq.pop_front(); dq.pop_back();      // O(1)
dq[i];                                // O(1)
```

---

## Common Algorithms

### Sorting
```cpp
sort(v.begin(), v.end());                    // ascending
sort(v.begin(), v.end(), greater<int>());    // descending
sort(v.begin(), v.end(), [](int a, int b) {  // custom
    return a > b;
});
```

### Binary Search
```cpp
// Array must be sorted
binary_search(v.begin(), v.end(), target);   // true/false
lower_bound(v.begin(), v.end(), target);     // iter to first >= target
upper_bound(v.begin(), v.end(), target);     // iter to first > target
```

### GCD / LCM
```cpp
__gcd(a, b);           // GCD (built-in)
// LCM = (a / gcd(a,b)) * b   (avoid overflow)
```

### Power
```cpp
// Fast exponentiation O(log n)
long long power(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}
```

### String Operations
```cpp
// Reverse
reverse(s.begin(), s.end());

// Convert case
transform(s.begin(), s.end(), s.begin(), ::tolower);
transform(s.begin(), s.end(), s.begin(), ::toupper);

// Split by space
stringstream ss(s);
string word;
while (ss >> word) { /* process word */ }

// Check if char is digit/alpha
isdigit(c); isalpha(c); isalnum(c);
```

---

## Common Patterns

### Two Pointers
```cpp
int left = 0, right = n - 1;
while (left < right) {
    // process arr[left] and arr[right]
    left++; right--;
}
```

### Sliding Window
```cpp
int left = 0, maxLen = 0;
for (int right = 0; right < n; right++) {
    // expand window by including arr[right]
    while (/* window invalid */) {
        // shrink from left
        left++;
    }
    maxLen = max(maxLen, right - left + 1);
}
```

### Prefix Sum
```cpp
vector<int> prefix(n + 1, 0);
for (int i = 0; i < n; i++)
    prefix[i + 1] = prefix[i] + arr[i];
// sum of arr[l..r] = prefix[r+1] - prefix[l]
```

### BFS Template
```cpp
queue<int> q;
vector<bool> visited(n, false);
q.push(start);
visited[start] = true;
while (!q.empty()) {
    int node = q.front(); q.pop();
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            visited[neighbor] = true;
            q.push(neighbor);
        }
    }
}
```

### DFS Template
```cpp
void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adj, visited);
        }
    }
}
```

### DP Template (Tabulation)
```cpp
vector<int> dp(n + 1, 0);
dp[0] = base_case;
for (int i = 1; i <= n; i++) {
    dp[i] = /* recurrence relation using dp[i-1], dp[i-2], etc. */;
}
return dp[n];
```

---

## Useful Tricks

```cpp
// Swap without temp
swap(a, b);

// Min/Max of multiple values
int m = min({a, b, c, d});

// INT_MAX, INT_MIN, LLONG_MAX
#include <climits>

// Infinity for algorithms
const int INF = 1e9;

// Modular arithmetic
const int MOD = 1e9 + 7;

// Check if power of 2
bool isPow2 = (n > 0) && (n & (n - 1)) == 0;

// Count set bits
__builtin_popcount(n);      // for int
__builtin_popcountll(n);    // for long long

// Floor/Ceil division
int floorDiv = a / b;
int ceilDiv = (a + b - 1) / b;

// Iterate all subsets of a bitmask
for (int mask = 0; mask < (1 << n); mask++) {
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) { /* i-th element included */ }
    }
}
```

---

## Complexity Cheat Sheet

| Algorithm | Time | Space |
|-----------|------|-------|
| Binary Search | O(log n) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg | O(log n) |
| Heap Sort | O(n log n) | O(1) |
| BFS/DFS | O(V + E) | O(V) |
| Dijkstra | O(E log V) | O(V) |
| DP (typical) | O(n * states) | O(states) |
| Hash Map ops | O(1) avg | O(n) |
| BST ops | O(log n) avg | O(n) |
