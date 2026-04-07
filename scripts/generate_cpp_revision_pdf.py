#!/usr/bin/env python3
"""
Generate Comprehensive C++ Revision PDF for TCS NQT Preparation.
Covers all libraries, syntax, STL, constants, and patterns needed for coding.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.pdf_generator import TCSNQTPDFGenerator


def code(text):
    """Format text as code (escape XML and use Courier font)."""
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = text.replace('\n', '<br/>').replace(' ', '&nbsp;')
    return f"<font face='Courier' size='9'>{text}</font>"


def main():
    output_path = os.path.join(
        os.path.dirname(__file__), '..',
        '06-Study-Resources', 'CPP-Complete-Revision.pdf'
    )

    pdf = TCSNQTPDFGenerator(
        output_path=output_path,
        title="C++ Complete Revision Guide",
        subject="Libraries, Syntax, STL, Constants & Everything for Coding"
    )

    pdf.add_cover_page()

    # ════════════════════════════════════════════════════════════
    # 1. ESSENTIAL HEADERS / LIBRARIES
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header(
        "1. Essential C++ Headers / Libraries",
        "Header files you need to include for various functionalities."
    )

    pdf.add_subtopic_header("1.1 The Universal Header")
    pdf.add_text("For competitive programming, one header includes everything:")
    pdf.add_text(code("#include <bits/stdc++.h>\nusing namespace std;"))
    pdf.add_tip("This includes ALL standard libraries. Use it for contests/practice. For production code, include specific headers.")

    pdf.add_subtopic_header("1.2 Specific Headers (Production Style)")
    pdf.add_table([
        ["Header", "Purpose", "Example Use"],
        ["<iostream>", "Input/Output streams", "cin, cout, cerr, endl"],
        ["<vector>", "Dynamic arrays", "vector<int>"],
        ["<string>", "String class", "string s = \"hello\""],
        ["<algorithm>", "Sort, search, reverse", "sort(), reverse(), find()"],
        ["<map>", "Ordered map (RB tree)", "map<int,int>"],
        ["<unordered_map>", "Hash map", "unordered_map<int,int>"],
        ["<set>", "Ordered set", "set<int>"],
        ["<unordered_set>", "Hash set", "unordered_set<int>"],
        ["<queue>", "Queue & priority queue", "queue<int>, priority_queue<int>"],
        ["<stack>", "Stack", "stack<int>"],
        ["<deque>", "Double-ended queue", "deque<int>"],
        ["<list>", "Doubly linked list", "list<int>"],
        ["<utility>", "pair, swap, move", "pair<int,int>"],
        ["<tuple>", "Tuple type", "tuple<int,int,int>"],
        ["<climits>", "INT_MAX, INT_MIN, etc.", "INT_MAX, LLONG_MAX"],
        ["<cmath>", "Math functions", "sqrt, pow, abs, log"],
        ["<cstdlib>", "atoi, malloc, rand", "atoi(), rand()"],
        ["<cstring>", "C string functions", "strlen, strcpy, memset"],
        ["<numeric>", "accumulate, gcd, lcm", "accumulate(), __gcd()"],
        ["<bitset>", "Fixed-size bit array", "bitset<32>"],
        ["<sstream>", "String streams", "stringstream"],
        ["<iomanip>", "I/O formatting", "setprecision, setw"],
        ["<functional>", "Function objects", "greater<int>, less<int>"],
        ["<chrono>", "Time measurements", "chrono::steady_clock"],
    ])

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 2. BASIC PROGRAM STRUCTURE
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("2. Basic Program Structure")

    pdf.add_subtopic_header("2.1 Minimal Template")
    pdf.add_text(code(
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n"
        "\n"
        "int main() {\n"
        "    // Your code here\n"
        "    return 0;\n"
        "}"
    ))

    pdf.add_subtopic_header("2.2 Fast I/O Template (Recommended)")
    pdf.add_text(code(
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n"
        "\n"
        "int main() {\n"
        "    ios_base::sync_with_stdio(false);\n"
        "    cin.tie(NULL);\n"
        "    \n"
        "    int n;\n"
        "    cin >> n;\n"
        "    \n"
        "    vector<int> arr(n);\n"
        "    for (int i = 0; i < n; i++) cin >> arr[i];\n"
        "    \n"
        "    // Solve\n"
        "    \n"
        "    return 0;\n"
        "}"
    ))
    pdf.add_tip("sync_with_stdio(false) makes cin/cout 5-10x faster. Use this for large inputs.")

    pdf.add_subtopic_header("2.3 Multiple Test Cases Template")
    pdf.add_text(code(
        "int main() {\n"
        "    int t;\n"
        "    cin >> t;\n"
        "    while (t--) {\n"
        "        // Solve each test case\n"
        "    }\n"
        "    return 0;\n"
        "}"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 3. DATA TYPES
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("3. Data Types & Sizes")

    pdf.add_subtopic_header("3.1 Primitive Types")
    pdf.add_table([
        ["Type", "Size (bytes)", "Range", "Format Specifier"],
        ["bool", "1", "true / false", "%d"],
        ["char", "1", "-128 to 127", "%c"],
        ["unsigned char", "1", "0 to 255", "%c"],
        ["short", "2", "-32,768 to 32,767", "%hd"],
        ["int", "4", "-2.1*10^9 to 2.1*10^9", "%d"],
        ["unsigned int", "4", "0 to 4.2*10^9", "%u"],
        ["long", "4 or 8", "Platform dependent", "%ld"],
        ["long long", "8", "-9.2*10^18 to 9.2*10^18", "%lld"],
        ["unsigned long long", "8", "0 to 1.8*10^19", "%llu"],
        ["float", "4", "~6 decimal digits", "%f"],
        ["double", "8", "~15 decimal digits", "%lf"],
        ["long double", "12 or 16", "~18 decimal digits", "%Lf"],
    ])

    pdf.add_subtopic_header("3.2 When to use which type")
    pdf.add_tip("Use 'int' for normal integers (up to ~2 billion).")
    pdf.add_tip("Use 'long long' when values exceed 2*10^9 (e.g., factorials, products).")
    pdf.add_tip("Use 'double' for floating point (more precision than float).")
    pdf.add_tip("Use 'long long' for sums of large arrays to avoid overflow.")

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 4. CONSTANTS - INT_MAX, INT_MIN, etc.
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("4. Constants (climits, cfloat)")

    pdf.add_subtopic_header("4.1 Integer Limits (#include <climits>)")
    pdf.add_table([
        ["Constant", "Value", "Description"],
        ["CHAR_MIN", "-128", "Minimum char value"],
        ["CHAR_MAX", "127", "Maximum char value"],
        ["UCHAR_MAX", "255", "Max unsigned char"],
        ["SHRT_MIN", "-32768", "Minimum short"],
        ["SHRT_MAX", "32767", "Maximum short"],
        ["USHRT_MAX", "65535", "Max unsigned short"],
        ["INT_MIN", "-2,147,483,648", "Minimum int (-2^31)"],
        ["INT_MAX", "2,147,483,647", "Maximum int (2^31 - 1)"],
        ["UINT_MAX", "4,294,967,295", "Max unsigned int (2^32-1)"],
        ["LONG_MIN", "-2^31 or -2^63", "Minimum long"],
        ["LONG_MAX", "2^31-1 or 2^63-1", "Maximum long"],
        ["LLONG_MIN", "-9.2 * 10^18", "Minimum long long (-2^63)"],
        ["LLONG_MAX", "9.2 * 10^18", "Maximum long long (2^63-1)"],
        ["ULLONG_MAX", "1.8 * 10^19", "Max unsigned long long"],
    ])

    pdf.add_subtopic_header("4.2 Float Limits (#include <cfloat>)")
    pdf.add_table([
        ["Constant", "Description"],
        ["FLT_MAX", "Maximum float (~3.4 * 10^38)"],
        ["FLT_MIN", "Minimum positive float"],
        ["DBL_MAX", "Maximum double (~1.7 * 10^308)"],
        ["DBL_MIN", "Minimum positive double"],
        ["FLT_EPSILON", "Smallest float such that 1.0 + EPSILON != 1.0"],
        ["DBL_EPSILON", "Same for double (~2.2 * 10^-16)"],
    ])

    pdf.add_subtopic_header("4.3 Custom Infinity Constants (Common Practice)")
    pdf.add_text(code(
        "const int INF = 1e9;            // ~2*10^9 (fits in int)\n"
        "const long long LLINF = 1e18;   // For long long\n"
        "const int MOD = 1e9 + 7;        // Common prime modulus\n"
        "const double EPS = 1e-9;        // For floating point comparison\n"
        "const double PI = 3.14159265358979323846;"
    ))
    pdf.add_tip("Don't use INT_MAX as INF when adding values - it will overflow! Use 1e9 instead.")

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 5. INPUT / OUTPUT
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("5. Input / Output")

    pdf.add_subtopic_header("5.1 Basic cin / cout")
    pdf.add_text(code(
        "int n;\n"
        "cin >> n;                      // Read integer\n"
        "cout << n << endl;             // Print with newline\n"
        "cout << n << \"\\n\";             // Faster than endl\n"
        "\n"
        "string s;\n"
        "cin >> s;                      // Reads single word (no spaces)\n"
        "getline(cin, s);               // Reads entire line\n"
        "\n"
        "// Reading multiple values\n"
        "int a, b, c;\n"
        "cin >> a >> b >> c;"
    ))

    pdf.add_subtopic_header("5.2 Reading Until EOF")
    pdf.add_text(code(
        "int x;\n"
        "while (cin >> x) {\n"
        "    // Process x\n"
        "}"
    ))

    pdf.add_subtopic_header("5.3 Reading a Line After Integer")
    pdf.add_text(code(
        "int n;\n"
        "cin >> n;\n"
        "cin.ignore();  // Skip newline left in buffer\n"
        "string line;\n"
        "getline(cin, line);"
    ))

    pdf.add_subtopic_header("5.4 Output Formatting")
    pdf.add_text(code(
        "#include <iomanip>\n"
        "\n"
        "cout << fixed << setprecision(2) << 3.14159;  // 3.14\n"
        "cout << setw(10) << 42;                        // Right-aligned width 10\n"
        "cout << setfill('0') << setw(5) << 42;         // 00042\n"
        "cout << hex << 255 << endl;                    // ff\n"
        "cout << oct << 8 << endl;                      // 10\n"
        "cout << dec << 10 << endl;                     // back to decimal"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 6. STL CONTAINERS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("6. STL Containers")

    pdf.add_subtopic_header("6.1 vector - Dynamic Array")
    pdf.add_text(code(
        "#include <vector>\n"
        "\n"
        "vector<int> v;                 // Empty vector\n"
        "vector<int> v(10);             // Size 10, all zeros\n"
        "vector<int> v(10, 5);          // Size 10, all 5s\n"
        "vector<int> v = {1, 2, 3};     // Initializer list\n"
        "vector<vector<int>> mat(n, vector<int>(m, 0));  // 2D vector n*m\n"
        "\n"
        "// Operations (Time Complexity)\n"
        "v.push_back(x);                // O(1) amortized\n"
        "v.pop_back();                  // O(1)\n"
        "v[i];                          // O(1)\n"
        "v.at(i);                       // O(1) with bounds check\n"
        "v.size();                      // O(1)\n"
        "v.empty();                     // O(1)\n"
        "v.clear();                     // O(n)\n"
        "v.front();                     // O(1) - first element\n"
        "v.back();                      // O(1) - last element\n"
        "v.insert(v.begin()+i, x);      // O(n)\n"
        "v.erase(v.begin()+i);          // O(n)\n"
        "v.resize(newSize);             // O(n)\n"
        "v.begin(), v.end();            // Iterators"
    ))

    pdf.add_subtopic_header("6.2 string")
    pdf.add_text(code(
        "#include <string>\n"
        "\n"
        "string s = \"hello\";\n"
        "s.length();  s.size();         // O(1)\n"
        "s[i];                          // O(1)\n"
        "s.substr(start, len);          // O(len)\n"
        "s.find(\"sub\");                 // O(n*m), returns string::npos if not found\n"
        "s.find('c');                   // Find character\n"
        "s += \"world\";                  // O(m) amortized\n"
        "s.append(\"abc\");               // Same as +=\n"
        "s.insert(pos, \"abc\");          // O(n)\n"
        "s.erase(pos, len);             // O(n)\n"
        "s.replace(pos, len, \"abc\");    // O(n)\n"
        "s.compare(s2);                 // 0 if equal\n"
        "\n"
        "// Conversions\n"
        "int x = stoi(\"42\");            // string to int\n"
        "long long y = stoll(\"42\");     // string to long long\n"
        "double d = stod(\"3.14\");       // string to double\n"
        "string s = to_string(42);      // any number to string"
    ))

    pdf.add_subtopic_header("6.3 pair & tuple")
    pdf.add_text(code(
        "#include <utility>\n"
        "\n"
        "pair<int, string> p = {1, \"abc\"};\n"
        "p.first;                       // 1\n"
        "p.second;                      // \"abc\"\n"
        "make_pair(1, \"abc\");\n"
        "\n"
        "// Tuple (3+ elements)\n"
        "#include <tuple>\n"
        "tuple<int, string, double> t = {1, \"abc\", 3.14};\n"
        "get<0>(t);                     // 1\n"
        "get<1>(t);                     // \"abc\"\n"
        "auto [a, b, c] = t;            // C++17 structured binding"
    ))

    pdf.add_page_break()

    pdf.add_subtopic_header("6.4 map & unordered_map")
    pdf.add_text(code(
        "#include <map>\n"
        "#include <unordered_map>\n"
        "\n"
        "// map - ordered (Red-Black Tree), O(log n) operations\n"
        "map<string, int> m;\n"
        "m[\"key\"] = 10;                // Insert/update O(log n)\n"
        "m.count(\"key\");                // 0 or 1\n"
        "m.find(\"key\") != m.end();      // Check existence\n"
        "m.erase(\"key\");                // O(log n)\n"
        "m.size();\n"
        "for (auto& [k, v] : m) { ... } // Iterate (sorted by key)\n"
        "m.lower_bound(\"abc\");          // First key >= \"abc\"\n"
        "m.upper_bound(\"abc\");          // First key > \"abc\"\n"
        "\n"
        "// unordered_map - hash table, O(1) average\n"
        "unordered_map<string, int> um;\n"
        "// Same operations as map but O(1) average, no ordering"
    ))
    pdf.add_tip("Use unordered_map by default for speed. Use map when you need keys sorted.")

    pdf.add_subtopic_header("6.5 set & unordered_set")
    pdf.add_text(code(
        "#include <set>\n"
        "#include <unordered_set>\n"
        "\n"
        "set<int> s;                    // Ordered, unique, O(log n)\n"
        "s.insert(5);                   // O(log n)\n"
        "s.erase(5);                    // O(log n)\n"
        "s.count(5);                    // 0 or 1\n"
        "s.find(5);                     // Returns iterator or s.end()\n"
        "s.size(); s.empty();\n"
        "*s.begin();                    // Smallest element\n"
        "*s.rbegin();                   // Largest element\n"
        "s.lower_bound(5);              // First >= 5\n"
        "s.upper_bound(5);              // First > 5\n"
        "\n"
        "// multiset - allows duplicates\n"
        "multiset<int> ms;\n"
        "\n"
        "// unordered_set - hash, O(1) average\n"
        "unordered_set<int> us;"
    ))

    pdf.add_subtopic_header("6.6 stack")
    pdf.add_text(code(
        "#include <stack>\n"
        "\n"
        "stack<int> st;\n"
        "st.push(x);                    // O(1)\n"
        "st.top();                      // O(1) - peek\n"
        "st.pop();                      // O(1) - removes top\n"
        "st.size(); st.empty();"
    ))

    pdf.add_subtopic_header("6.7 queue & deque")
    pdf.add_text(code(
        "#include <queue>\n"
        "\n"
        "queue<int> q;                  // FIFO\n"
        "q.push(x);                     // O(1) - add to back\n"
        "q.front();                     // O(1) - peek front\n"
        "q.back();                      // O(1) - peek back\n"
        "q.pop();                       // O(1) - removes front\n"
        "\n"
        "// deque - double-ended queue\n"
        "#include <deque>\n"
        "deque<int> dq;\n"
        "dq.push_front(x);              // O(1)\n"
        "dq.push_back(x);               // O(1)\n"
        "dq.pop_front();                // O(1)\n"
        "dq.pop_back();                 // O(1)\n"
        "dq[i];                         // O(1) random access"
    ))

    pdf.add_page_break()

    pdf.add_subtopic_header("6.8 priority_queue (Heap)")
    pdf.add_text(code(
        "#include <queue>\n"
        "\n"
        "// Max-heap (default)\n"
        "priority_queue<int> maxHeap;\n"
        "maxHeap.push(x);               // O(log n)\n"
        "maxHeap.top();                 // O(1) - largest\n"
        "maxHeap.pop();                 // O(log n)\n"
        "\n"
        "// Min-heap\n"
        "priority_queue<int, vector<int>, greater<int>> minHeap;\n"
        "\n"
        "// Custom comparator (max-heap by second element of pair)\n"
        "auto cmp = [](pair<int,int> a, pair<int,int> b) {\n"
        "    return a.second < b.second;  // < for max-heap\n"
        "};\n"
        "priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);"
    ))

    pdf.add_subtopic_header("6.9 list & forward_list")
    pdf.add_text(code(
        "#include <list>\n"
        "list<int> lst;                 // Doubly linked list\n"
        "lst.push_back(x); lst.push_front(x);\n"
        "lst.pop_back(); lst.pop_front();\n"
        "lst.insert(it, x);             // O(1) given iterator\n"
        "lst.erase(it);                 // O(1) given iterator\n"
        "lst.sort();                    // O(n log n)\n"
        "lst.reverse();                 // O(n)\n"
        "lst.unique();                  // Remove consecutive duplicates"
    ))

    pdf.add_subtopic_header("6.10 bitset")
    pdf.add_text(code(
        "#include <bitset>\n"
        "bitset<32> bs;                 // 32 bits, all zero\n"
        "bitset<8> b(\"10110010\");      // From string\n"
        "bitset<8> b2(42);              // From integer\n"
        "bs.set(i);                     // Set bit i to 1\n"
        "bs.reset(i);                   // Set bit i to 0\n"
        "bs.flip(i);                    // Toggle bit i\n"
        "bs.count();                    // Number of 1 bits\n"
        "bs.test(i);                    // Check if bit i is set\n"
        "bs.to_string();                // Convert to string\n"
        "bs.to_ulong();                 // Convert to unsigned long"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 7. STL ALGORITHMS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("7. STL Algorithms (#include <algorithm>)")

    pdf.add_subtopic_header("7.1 Sorting")
    pdf.add_text(code(
        "vector<int> v = {3, 1, 4, 1, 5};\n"
        "\n"
        "sort(v.begin(), v.end());                  // Ascending\n"
        "sort(v.begin(), v.end(), greater<int>());  // Descending\n"
        "\n"
        "// Custom comparator (lambda)\n"
        "sort(v.begin(), v.end(), [](int a, int b) {\n"
        "    return a > b;  // Descending\n"
        "});\n"
        "\n"
        "// Sort by absolute value\n"
        "sort(v.begin(), v.end(), [](int a, int b) {\n"
        "    return abs(a) < abs(b);\n"
        "});\n"
        "\n"
        "stable_sort(v.begin(), v.end());           // Maintains order of equal elements\n"
        "partial_sort(v.begin(), v.begin()+k, v.end()); // First k smallest sorted\n"
        "nth_element(v.begin(), v.begin()+k, v.end());  // kth element in place"
    ))

    pdf.add_subtopic_header("7.2 Searching")
    pdf.add_text(code(
        "// Linear search\n"
        "auto it = find(v.begin(), v.end(), target);\n"
        "if (it != v.end()) { /* found */ }\n"
        "\n"
        "// Binary search (array MUST be sorted)\n"
        "binary_search(v.begin(), v.end(), target);   // returns bool\n"
        "auto lb = lower_bound(v.begin(), v.end(), x); // first >= x\n"
        "auto ub = upper_bound(v.begin(), v.end(), x); // first > x\n"
        "\n"
        "// Convert iterator to index\n"
        "int idx = lb - v.begin();\n"
        "\n"
        "// Count occurrences in sorted array\n"
        "int cnt = upper_bound(...) - lower_bound(...);"
    ))

    pdf.add_subtopic_header("7.3 Min / Max")
    pdf.add_text(code(
        "min(a, b);                     // Min of two\n"
        "max(a, b);                     // Max of two\n"
        "min({a, b, c, d});             // Min of multiple (C++11)\n"
        "max({a, b, c, d});             // Max of multiple\n"
        "\n"
        "// Min/max element in a range\n"
        "auto it = min_element(v.begin(), v.end());\n"
        "auto it = max_element(v.begin(), v.end());\n"
        "int idx = min_element(v.begin(), v.end()) - v.begin();\n"
        "\n"
        "// Both at once\n"
        "auto [mn, mx] = minmax_element(v.begin(), v.end());"
    ))

    pdf.add_subtopic_header("7.4 Modifying Operations")
    pdf.add_text(code(
        "reverse(v.begin(), v.end());               // Reverse in place\n"
        "rotate(v.begin(), v.begin()+k, v.end());   // Rotate left by k\n"
        "fill(v.begin(), v.end(), 0);               // Fill with value\n"
        "iota(v.begin(), v.end(), 1);               // Fill with 1, 2, 3, ...\n"
        "\n"
        "// Remove duplicates (sorted array)\n"
        "v.erase(unique(v.begin(), v.end()), v.end());\n"
        "\n"
        "// Remove all occurrences of value\n"
        "v.erase(remove(v.begin(), v.end(), val), v.end());\n"
        "\n"
        "// Permutations\n"
        "next_permutation(v.begin(), v.end());\n"
        "prev_permutation(v.begin(), v.end());\n"
        "\n"
        "// Random shuffle (C++17+)\n"
        "random_shuffle(v.begin(), v.end());"
    ))

    pdf.add_page_break()

    pdf.add_subtopic_header("7.5 Numeric Operations (#include <numeric>)")
    pdf.add_text(code(
        "// Sum of elements\n"
        "int sum = accumulate(v.begin(), v.end(), 0);\n"
        "long long sum = accumulate(v.begin(), v.end(), 0LL); // Use 0LL for long long\n"
        "\n"
        "// Product\n"
        "int prod = accumulate(v.begin(), v.end(), 1, multiplies<int>());\n"
        "\n"
        "// Prefix sum\n"
        "vector<int> prefix(v.size());\n"
        "partial_sum(v.begin(), v.end(), prefix.begin());\n"
        "\n"
        "// Adjacent differences\n"
        "vector<int> diff(v.size());\n"
        "adjacent_difference(v.begin(), v.end(), diff.begin());\n"
        "\n"
        "// GCD and LCM (C++17)\n"
        "int g = gcd(12, 18);           // 6\n"
        "int l = lcm(12, 18);           // 36\n"
        "int g = __gcd(12, 18);         // Built-in (also works pre-C++17)"
    ))

    pdf.add_subtopic_header("7.6 Counting & Predicates")
    pdf.add_text(code(
        "count(v.begin(), v.end(), x);              // Count occurrences of x\n"
        "count_if(v.begin(), v.end(), [](int n) {\n"
        "    return n > 0;\n"
        "});\n"
        "\n"
        "all_of(v.begin(), v.end(), [](int n) { return n > 0; });\n"
        "any_of(v.begin(), v.end(), [](int n) { return n > 0; });\n"
        "none_of(v.begin(), v.end(), [](int n) { return n > 0; });\n"
        "\n"
        "// Find with predicate\n"
        "auto it = find_if(v.begin(), v.end(), [](int n) {\n"
        "    return n % 2 == 0;\n"
        "});"
    ))

    pdf.add_subtopic_header("7.7 Set Operations (Sorted Ranges)")
    pdf.add_text(code(
        "vector<int> a = {1, 2, 3, 4};\n"
        "vector<int> b = {3, 4, 5, 6};\n"
        "vector<int> result;\n"
        "\n"
        "set_union(a.begin(), a.end(), b.begin(), b.end(),\n"
        "          back_inserter(result));         // {1,2,3,4,5,6}\n"
        "\n"
        "set_intersection(a.begin(), a.end(), b.begin(), b.end(),\n"
        "                 back_inserter(result));  // {3,4}\n"
        "\n"
        "set_difference(a.begin(), a.end(), b.begin(), b.end(),\n"
        "               back_inserter(result));    // {1,2}"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 8. MATH FUNCTIONS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("8. Math Functions (#include <cmath>)")

    pdf.add_text(code(
        "abs(-5);                       // 5 (works for int, long, double)\n"
        "fabs(-3.14);                   // 3.14 (for floating point)\n"
        "\n"
        "sqrt(16);                      // 4.0\n"
        "cbrt(27);                      // 3.0\n"
        "pow(2, 10);                    // 1024.0\n"
        "pow(2.5, 3);                   // 15.625\n"
        "\n"
        "exp(1);                        // e (2.718...)\n"
        "log(e);                        // 1 (natural log)\n"
        "log2(8);                       // 3\n"
        "log10(100);                    // 2\n"
        "\n"
        "ceil(3.2);                     // 4.0\n"
        "floor(3.8);                    // 3.0\n"
        "round(3.5);                    // 4.0\n"
        "trunc(3.7);                    // 3.0\n"
        "\n"
        "sin(x); cos(x); tan(x);\n"
        "asin(x); acos(x); atan(x);\n"
        "atan2(y, x);                   // Angle in correct quadrant\n"
        "\n"
        "fmod(10.5, 3);                 // 1.5 (floating point modulo)\n"
        "hypot(3, 4);                   // 5 (sqrt(3^2 + 4^2))"
    ))

    pdf.add_subtopic_header("8.1 Integer Math Tricks")
    pdf.add_text(code(
        "// Avoid using sqrt for integer square root (loss of precision)\n"
        "int isqrt = (int)sqrt((double)n + 0.5);\n"
        "\n"
        "// Integer power (manual)\n"
        "long long power(long long base, long long exp) {\n"
        "    long long res = 1;\n"
        "    while (exp > 0) {\n"
        "        if (exp & 1) res *= base;\n"
        "        base *= base;\n"
        "        exp >>= 1;\n"
        "    }\n"
        "    return res;\n"
        "}\n"
        "\n"
        "// Modular exponentiation\n"
        "long long powMod(long long b, long long e, long long m) {\n"
        "    long long res = 1; b %= m;\n"
        "    while (e > 0) {\n"
        "        if (e & 1) res = res * b % m;\n"
        "        b = b * b % m;\n"
        "        e >>= 1;\n"
        "    }\n"
        "    return res;\n"
        "}\n"
        "\n"
        "// Ceiling division\n"
        "int ceilDiv = (a + b - 1) / b;"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 9. BIT MANIPULATION
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("9. Bit Manipulation")

    pdf.add_subtopic_header("9.1 Basic Operators")
    pdf.add_table([
        ["Operator", "Name", "Example"],
        ["&", "AND", "5 & 3 = 1"],
        ["|", "OR", "5 | 3 = 7"],
        ["^", "XOR", "5 ^ 3 = 6"],
        ["~", "NOT", "~5 = -6"],
        ["<<", "Left shift", "5 << 1 = 10 (multiply by 2)"],
        [">>", "Right shift", "5 >> 1 = 2 (divide by 2)"],
    ])

    pdf.add_subtopic_header("9.2 Common Bit Tricks")
    pdf.add_text(code(
        "// Check if bit i is set\n"
        "bool isSet = (n >> i) & 1;\n"
        "bool isSet = n & (1 << i);\n"
        "\n"
        "// Set bit i\n"
        "n |= (1 << i);\n"
        "\n"
        "// Clear bit i\n"
        "n &= ~(1 << i);\n"
        "\n"
        "// Toggle bit i\n"
        "n ^= (1 << i);\n"
        "\n"
        "// Check if power of 2\n"
        "bool isPow2 = (n > 0) && ((n & (n - 1)) == 0);\n"
        "\n"
        "// Lowest set bit\n"
        "int lsb = n & (-n);\n"
        "\n"
        "// Clear lowest set bit\n"
        "n = n & (n - 1);\n"
        "\n"
        "// Count of set bits\n"
        "__builtin_popcount(n);         // for int\n"
        "__builtin_popcountll(n);       // for long long\n"
        "\n"
        "// Number of leading zeros\n"
        "__builtin_clz(n);              // int\n"
        "__builtin_clzll(n);            // long long\n"
        "\n"
        "// Number of trailing zeros\n"
        "__builtin_ctz(n);\n"
        "\n"
        "// Parity (1 if odd number of bits, else 0)\n"
        "__builtin_parity(n);\n"
        "\n"
        "// XOR swap (no temp variable)\n"
        "a ^= b; b ^= a; a ^= b;"
    ))

    pdf.add_subtopic_header("9.3 Iterating All Subsets of a Set")
    pdf.add_text(code(
        "// Iterate all subsets of n elements\n"
        "for (int mask = 0; mask < (1 << n); mask++) {\n"
        "    for (int i = 0; i < n; i++) {\n"
        "        if (mask & (1 << i)) {\n"
        "            // i-th element is in subset\n"
        "        }\n"
        "    }\n"
        "}"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 10. STRINGS - DETAILED
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("10. String Operations - Detailed")

    pdf.add_text(code(
        "string s = \"Hello World\";\n"
        "\n"
        "// Length\n"
        "int len = s.length();          // 11\n"
        "int len = s.size();            // same\n"
        "\n"
        "// Access\n"
        "char c = s[0];                 // 'H'\n"
        "s[0] = 'h';                    // Modify\n"
        "\n"
        "// Substring\n"
        "string sub = s.substr(6);      // \"World\" (from index 6 to end)\n"
        "string sub = s.substr(6, 3);   // \"Wor\" (3 chars from index 6)\n"
        "\n"
        "// Find\n"
        "int pos = s.find(\"World\");     // 6 (or string::npos if not found)\n"
        "if (s.find(\"xyz\") == string::npos) { /* not found */ }\n"
        "\n"
        "// Replace\n"
        "s.replace(6, 5, \"There\");      // \"Hello There\"\n"
        "\n"
        "// Insert\n"
        "s.insert(5, \" beautiful\");\n"
        "\n"
        "// Erase\n"
        "s.erase(5, 6);                 // Remove 6 chars from index 5\n"
        "\n"
        "// Reverse\n"
        "reverse(s.begin(), s.end());\n"
        "\n"
        "// Convert case\n"
        "transform(s.begin(), s.end(), s.begin(), ::tolower);\n"
        "transform(s.begin(), s.end(), s.begin(), ::toupper);\n"
        "\n"
        "// Character checks (#include <cctype>)\n"
        "isalpha(c); isdigit(c); isalnum(c);\n"
        "isupper(c); islower(c); isspace(c);\n"
        "tolower(c); toupper(c);\n"
        "\n"
        "// Split string by space\n"
        "stringstream ss(s);\n"
        "string word;\n"
        "vector<string> words;\n"
        "while (ss >> word) words.push_back(word);"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 11. ITERATORS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("11. Iterators")

    pdf.add_text(code(
        "vector<int> v = {1, 2, 3, 4, 5};\n"
        "\n"
        "// Forward iteration\n"
        "for (auto it = v.begin(); it != v.end(); ++it) {\n"
        "    cout << *it << \" \";\n"
        "}\n"
        "\n"
        "// Reverse iteration\n"
        "for (auto it = v.rbegin(); it != v.rend(); ++it) {\n"
        "    cout << *it << \" \";\n"
        "}\n"
        "\n"
        "// Range-based for loop (C++11+) - PREFERRED\n"
        "for (int x : v) cout << x << \" \";\n"
        "for (auto& x : v) x *= 2;          // By reference to modify\n"
        "for (const auto& x : v) ...;       // Read-only, no copy\n"
        "\n"
        "// With index\n"
        "for (int i = 0; i < (int)v.size(); i++) {\n"
        "    cout << i << \": \" << v[i] << endl;\n"
        "}\n"
        "\n"
        "// Iterator arithmetic (random access only)\n"
        "auto it = v.begin() + 2;       // Points to v[2]\n"
        "int idx = it - v.begin();      // 2"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 12. LAMBDA FUNCTIONS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("12. Lambda Functions (C++11+)")

    pdf.add_text(code(
        "// Basic lambda\n"
        "auto add = [](int a, int b) { return a + b; };\n"
        "int x = add(3, 4);             // 7\n"
        "\n"
        "// Capture by value\n"
        "int multiplier = 10;\n"
        "auto times = [multiplier](int x) { return x * multiplier; };\n"
        "\n"
        "// Capture by reference\n"
        "int counter = 0;\n"
        "auto inc = [&counter]() { counter++; };\n"
        "\n"
        "// Capture all by value / reference\n"
        "auto f1 = [=]() { /* all variables by value */ };\n"
        "auto f2 = [&]() { /* all variables by reference */ };\n"
        "\n"
        "// Lambda as comparator\n"
        "sort(v.begin(), v.end(), [](int a, int b) {\n"
        "    return a > b;  // descending\n"
        "});\n"
        "\n"
        "// Recursive lambda (C++14+)\n"
        "function<int(int)> fact = [&](int n) {\n"
        "    return n <= 1 ? 1 : n * fact(n - 1);\n"
        "};"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 13. CLASSES AND STRUCTS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("13. Classes and Structs")

    pdf.add_subtopic_header("13.1 Basic Class")
    pdf.add_text(code(
        "class Point {\n"
        "private:\n"
        "    int x, y;\n"
        "public:\n"
        "    // Constructor\n"
        "    Point() : x(0), y(0) {}\n"
        "    Point(int a, int b) : x(a), y(b) {}\n"
        "    \n"
        "    // Member functions\n"
        "    int getX() const { return x; }\n"
        "    int getY() const { return y; }\n"
        "    void setX(int a) { x = a; }\n"
        "    \n"
        "    // Destructor\n"
        "    ~Point() {}\n"
        "};\n"
        "\n"
        "Point p(3, 4);\n"
        "Point* pp = new Point(5, 6);\n"
        "delete pp;"
    ))

    pdf.add_subtopic_header("13.2 Struct (for DSA)")
    pdf.add_text(code(
        "// Linked List Node\n"
        "struct ListNode {\n"
        "    int val;\n"
        "    ListNode* next;\n"
        "    ListNode() : val(0), next(nullptr) {}\n"
        "    ListNode(int x) : val(x), next(nullptr) {}\n"
        "    ListNode(int x, ListNode* n) : val(x), next(n) {}\n"
        "};\n"
        "\n"
        "// Tree Node\n"
        "struct TreeNode {\n"
        "    int val;\n"
        "    TreeNode* left;\n"
        "    TreeNode* right;\n"
        "    TreeNode() : val(0), left(nullptr), right(nullptr) {}\n"
        "    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n"
        "};"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 14. POINTERS AND REFERENCES
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("14. Pointers and References")

    pdf.add_text(code(
        "int a = 10;\n"
        "int* p = &a;                   // Pointer to a\n"
        "cout << *p;                    // 10 (dereference)\n"
        "*p = 20;                       // a is now 20\n"
        "\n"
        "// Null pointer\n"
        "int* p = nullptr;              // C++11+ (preferred)\n"
        "int* p = NULL;                 // C-style\n"
        "\n"
        "// Reference (alias)\n"
        "int& ref = a;                  // ref is another name for a\n"
        "ref = 30;                      // a is now 30\n"
        "\n"
        "// Pass by reference (avoid copy)\n"
        "void modify(vector<int>& v) {  // No copy, can modify\n"
        "    v.push_back(1);\n"
        "}\n"
        "\n"
        "// Pass by const reference (no copy, read-only)\n"
        "void print(const vector<int>& v) {\n"
        "    for (int x : v) cout << x;\n"
        "}\n"
        "\n"
        "// Dynamic memory\n"
        "int* arr = new int[10];        // Allocate array of 10 ints\n"
        "delete[] arr;                  // Free array\n"
        "\n"
        "int* x = new int(5);           // Single int initialized to 5\n"
        "delete x;\n"
        "\n"
        "// Smart pointers (C++11+) - prefer these\n"
        "#include <memory>\n"
        "unique_ptr<int> up = make_unique<int>(10);  // C++14\n"
        "shared_ptr<int> sp = make_shared<int>(10);"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 15. COMMON CODING PATTERNS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("15. Common Coding Patterns")

    pdf.add_subtopic_header("15.1 Two Pointers")
    pdf.add_text(code(
        "int left = 0, right = n - 1;\n"
        "while (left < right) {\n"
        "    if (condition) left++;\n"
        "    else right--;\n"
        "}"
    ))

    pdf.add_subtopic_header("15.2 Sliding Window")
    pdf.add_text(code(
        "int left = 0, sum = 0, ans = 0;\n"
        "for (int right = 0; right < n; right++) {\n"
        "    sum += arr[right];\n"
        "    while (sum > target) {\n"
        "        sum -= arr[left++];\n"
        "    }\n"
        "    ans = max(ans, right - left + 1);\n"
        "}"
    ))

    pdf.add_subtopic_header("15.3 Binary Search")
    pdf.add_text(code(
        "int lo = 0, hi = n - 1;\n"
        "while (lo <= hi) {\n"
        "    int mid = lo + (hi - lo) / 2;  // Avoid overflow\n"
        "    if (arr[mid] == target) return mid;\n"
        "    else if (arr[mid] < target) lo = mid + 1;\n"
        "    else hi = mid - 1;\n"
        "}\n"
        "return -1;"
    ))

    pdf.add_subtopic_header("15.4 BFS Template")
    pdf.add_text(code(
        "queue<int> q;\n"
        "vector<bool> visited(n, false);\n"
        "q.push(start);\n"
        "visited[start] = true;\n"
        "while (!q.empty()) {\n"
        "    int node = q.front(); q.pop();\n"
        "    for (int next : adj[node]) {\n"
        "        if (!visited[next]) {\n"
        "            visited[next] = true;\n"
        "            q.push(next);\n"
        "        }\n"
        "    }\n"
        "}"
    ))

    pdf.add_subtopic_header("15.5 DFS Template (Recursive)")
    pdf.add_text(code(
        "void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited) {\n"
        "    visited[node] = true;\n"
        "    for (int next : adj[node]) {\n"
        "        if (!visited[next]) {\n"
        "            dfs(next, adj, visited);\n"
        "        }\n"
        "    }\n"
        "}"
    ))

    pdf.add_subtopic_header("15.6 Prefix Sum")
    pdf.add_text(code(
        "vector<int> prefix(n + 1, 0);\n"
        "for (int i = 0; i < n; i++)\n"
        "    prefix[i + 1] = prefix[i] + arr[i];\n"
        "// Sum of arr[l..r] = prefix[r+1] - prefix[l]"
    ))

    pdf.add_subtopic_header("15.7 DP Template")
    pdf.add_text(code(
        "// 1D DP\n"
        "vector<int> dp(n + 1, 0);\n"
        "dp[0] = base_case;\n"
        "for (int i = 1; i <= n; i++)\n"
        "    dp[i] = /* recurrence */;\n"
        "\n"
        "// 2D DP\n"
        "vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 16. COMPLEXITY CHEAT SHEET
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("16. Time Complexity Cheat Sheet")

    pdf.add_subtopic_header("16.1 Common Algorithms")
    pdf.add_table([
        ["Algorithm", "Best", "Average", "Worst", "Space"],
        ["Linear Search", "O(1)", "O(n)", "O(n)", "O(1)"],
        ["Binary Search", "O(1)", "O(log n)", "O(log n)", "O(1)"],
        ["Bubble Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)"],
        ["Selection Sort", "O(n^2)", "O(n^2)", "O(n^2)", "O(1)"],
        ["Insertion Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)"],
        ["Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)"],
        ["Quick Sort", "O(n log n)", "O(n log n)", "O(n^2)", "O(log n)"],
        ["Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)"],
        ["Counting Sort", "O(n+k)", "O(n+k)", "O(n+k)", "O(k)"],
        ["Radix Sort", "O(nk)", "O(nk)", "O(nk)", "O(n+k)"],
    ])

    pdf.add_subtopic_header("16.2 STL Operations")
    pdf.add_table([
        ["Container", "Access", "Search", "Insert", "Delete"],
        ["vector", "O(1)", "O(n)", "O(1) end", "O(1) end"],
        ["deque", "O(1)", "O(n)", "O(1) ends", "O(1) ends"],
        ["list", "O(n)", "O(n)", "O(1)*", "O(1)*"],
        ["set/map", "-", "O(log n)", "O(log n)", "O(log n)"],
        ["unordered_set/map", "-", "O(1) avg", "O(1) avg", "O(1) avg"],
        ["stack/queue", "O(1) end", "-", "O(1)", "O(1)"],
        ["priority_queue", "O(1) top", "-", "O(log n)", "O(log n)"],
    ])
    pdf.add_text("(* with iterator)")

    pdf.add_subtopic_header("16.3 What's Acceptable for Different N")
    pdf.add_table([
        ["Input Size n", "Acceptable Complexity"],
        ["n <= 10", "O(n!) - permutations OK"],
        ["n <= 20", "O(2^n) - subsets OK"],
        ["n <= 500", "O(n^3)"],
        ["n <= 5,000", "O(n^2)"],
        ["n <= 10^6", "O(n log n)"],
        ["n <= 10^8", "O(n) or O(log n)"],
        ["n > 10^8", "O(log n) or O(1)"],
    ])

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 17. COMMON PITFALLS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("17. Common Pitfalls & Mistakes")

    pdf.add_text("<b>1. Integer Overflow</b>")
    pdf.add_text(code(
        "// WRONG: int overflows for large n\n"
        "int n = 1000000;\n"
        "int result = n * n;            // OVERFLOW!\n"
        "\n"
        "// CORRECT: use long long\n"
        "long long result = (long long)n * n;"
    ))

    pdf.add_text("<b>2. Array Index Out of Bounds</b>")
    pdf.add_text(code(
        "// WRONG: comparing signed/unsigned\n"
        "for (int i = 0; i < v.size() - 1; i++)  // If v is empty, size()-1 underflows!\n"
        "\n"
        "// CORRECT\n"
        "for (int i = 0; i + 1 < (int)v.size(); i++)"
    ))

    pdf.add_text("<b>3. Modifying Container While Iterating</b>")
    pdf.add_text(code(
        "// WRONG\n"
        "for (auto x : v) {\n"
        "    if (x == 0) v.erase(...);   // Invalidates iterator!\n"
        "}\n"
        "\n"
        "// CORRECT - use erase-remove idiom\n"
        "v.erase(remove(v.begin(), v.end(), 0), v.end());"
    ))

    pdf.add_text("<b>4. Uninitialized Variables</b>")
    pdf.add_text(code(
        "int x;                         // Garbage value!\n"
        "int x = 0;                     // OK\n"
        "vector<int> v(10);             // All zeros (vector initializes)\n"
        "int arr[10];                   // Garbage values\n"
        "int arr[10] = {0};             // All zeros"
    ))

    pdf.add_text("<b>5. Comparing Floating Point</b>")
    pdf.add_text(code(
        "// WRONG\n"
        "if (a == b) ...                // May fail due to precision\n"
        "\n"
        "// CORRECT\n"
        "if (abs(a - b) < EPS) ..."
    ))

    pdf.add_text("<b>6. Recursive Stack Overflow</b>")
    pdf.add_text("Default stack size is ~1 MB. Deep recursion (>10^5) may overflow. Use iterative or increase stack.")

    pdf.add_text("<b>7. Forgetting to Reset Global State</b>")
    pdf.add_text("In multi-test-case problems, reset global vectors/arrays before each test case.")

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 18. COMPILATION & DEBUGGING
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("18. Compilation & Debugging")

    pdf.add_subtopic_header("18.1 Compilation Commands")
    pdf.add_text(code(
        "# Basic compilation\n"
        "g++ solution.cpp -o solution\n"
        "\n"
        "# Recommended (with optimizations and warnings)\n"
        "g++ -std=c++17 -O2 -Wall -Wextra solution.cpp -o solution\n"
        "\n"
        "# Debug build\n"
        "g++ -std=c++17 -g -Wall solution.cpp -o solution_debug\n"
        "\n"
        "# Run\n"
        "./solution\n"
        "./solution &lt; input.txt              # Input from file\n"
        "./solution &lt; input.txt &gt; output.txt  # I/O from files\n"
        "\n"
        "# C++ standards\n"
        "-std=c++11   # C++11 (auto, lambda, range-for)\n"
        "-std=c++14   # Adds generic lambdas\n"
        "-std=c++17   # Adds structured bindings, if-init\n"
        "-std=c++20   # Adds concepts, ranges"
    ))

    pdf.add_subtopic_header("18.2 Debug Macros")
    pdf.add_text(code(
        "// Debug print macro\n"
        "#define debug(x) cerr &lt;&lt; #x &lt;&lt; \" = \" &lt;&lt; x &lt;&lt; endl\n"
        "\n"
        "// Use:\n"
        "int x = 42;\n"
        "debug(x);                      // x = 42\n"
        "\n"
        "// Print vector\n"
        "for (int v : vec) cerr &lt;&lt; v &lt;&lt; \" \"; cerr &lt;&lt; endl;"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 19. USEFUL ONE-LINERS
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("19. Useful One-Liners & Snippets")

    pdf.add_text(code(
        "// Sum of vector\n"
        "long long sum = accumulate(v.begin(), v.end(), 0LL);\n"
        "\n"
        "// Max in vector\n"
        "int mx = *max_element(v.begin(), v.end());\n"
        "\n"
        "// Min in vector\n"
        "int mn = *min_element(v.begin(), v.end());\n"
        "\n"
        "// Sort descending\n"
        "sort(v.rbegin(), v.rend());\n"
        "\n"
        "// Unique elements (sort first!)\n"
        "sort(v.begin(), v.end());\n"
        "v.erase(unique(v.begin(), v.end()), v.end());\n"
        "\n"
        "// Frequency map\n"
        "unordered_map&lt;int, int&gt; freq;\n"
        "for (int x : v) freq[x]++;\n"
        "\n"
        "// Check if element exists\n"
        "if (find(v.begin(), v.end(), x) != v.end()) ...\n"
        "\n"
        "// Convert vector to set\n"
        "set&lt;int&gt; s(v.begin(), v.end());\n"
        "\n"
        "// Reverse string\n"
        "reverse(s.begin(), s.end());\n"
        "\n"
        "// String to char array\n"
        "const char* cstr = s.c_str();\n"
        "\n"
        "// 2D vector initialization\n"
        "vector&lt;vector&lt;int&gt;&gt; mat(n, vector&lt;int&gt;(m, 0));\n"
        "\n"
        "// Print all elements\n"
        "for (int x : v) cout &lt;&lt; x &lt;&lt; \" \";\n"
        "cout &lt;&lt; endl;\n"
        "\n"
        "// Random number\n"
        "#include &lt;random&gt;\n"
        "random_device rd;\n"
        "mt19937 gen(rd());\n"
        "uniform_int_distribution&lt;&gt; dis(1, 100);\n"
        "int r = dis(gen);"
    ))

    pdf.add_page_break()

    # ════════════════════════════════════════════════════════════
    # 20. KEYWORDS REFERENCE
    # ════════════════════════════════════════════════════════════
    pdf.add_topic_header("20. C++ Keywords Quick Reference")

    pdf.add_table([
        ["Keyword", "Purpose"],
        ["auto", "Type deduction (C++11+)"],
        ["const", "Read-only variable"],
        ["constexpr", "Compile-time constant (C++11+)"],
        ["static", "Class-level / file-scope variable"],
        ["virtual", "Polymorphic function"],
        ["override", "Explicit override (C++11+)"],
        ["final", "Cannot be overridden / inherited"],
        ["explicit", "Prevent implicit conversion"],
        ["friend", "Grant access to private members"],
        ["inline", "Hint to inline function"],
        ["mutable", "Can be modified in const object"],
        ["volatile", "Don't optimize away"],
        ["typename", "Indicate type (templates)"],
        ["template", "Generic programming"],
        ["nullptr", "Null pointer (C++11+)"],
        ["sizeof", "Size of type/object"],
        ["typedef", "Type alias (use 'using' instead)"],
        ["using", "Type alias (preferred)"],
        ["namespace", "Group declarations"],
        ["enum / enum class", "Enumeration"],
        ["new / delete", "Dynamic memory"],
        ["this", "Pointer to current object"],
        ["throw / try / catch", "Exception handling"],
    ])

    pdf.add_subtopic_header("Type Aliases")
    pdf.add_text(code(
        "// using is preferred over typedef\n"
        "using ll = long long;\n"
        "using vi = vector&lt;int&gt;;\n"
        "using vvi = vector&lt;vector&lt;int&gt;&gt;;\n"
        "using pii = pair&lt;int, int&gt;;\n"
        "using vpii = vector&lt;pair&lt;int, int&gt;&gt;;"
    ))

    # ════════════════════════════════════════════════════════════
    # GENERATE
    # ════════════════════════════════════════════════════════════
    pdf.generate()
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
