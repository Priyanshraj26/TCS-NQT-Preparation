/*
 * Q002: Implement Stack using Array
 * Question: ../../../DSA-Questions/Other-Topics/Q002-implement-stack-array.md
 *
 * Approach Overview:
 * All operations are O(1) time, O(n) space for storage.
 */

#include <iostream>
#include <cassert>
using namespace std;

// ===========================================
// Stack Implementation using Array
// ===========================================
class Stack {
private:
    int* arr;
    int topIdx;
    int capacity;

public:
    Stack(int cap = 1000) {
        capacity = cap;
        arr = new int[capacity];
        topIdx = -1;
    }

    ~Stack() {
        delete[] arr;
    }

    void push(int x) {
        if (topIdx == capacity - 1) {
            cout << "Stack Overflow!" << endl;
            return;
        }
        arr[++topIdx] = x;
    }

    int pop() {
        if (isEmpty()) {
            return -1; // underflow
        }
        return arr[topIdx--];
    }

    int top() {
        if (isEmpty()) {
            return -1;
        }
        return arr[topIdx];
    }

    bool isEmpty() {
        return topIdx == -1;
    }

    int size() {
        return topIdx + 1;
    }
};

// ===========================================
// Dry Run
// ===========================================
/*
 * Stack s; topIdx = -1
 * push(10): topIdx=0, arr[0]=10     | stack: [10]
 * push(20): topIdx=1, arr[1]=20     | stack: [10, 20]
 * push(30): topIdx=2, arr[2]=30     | stack: [10, 20, 30]
 * top():    return arr[2] = 30      | stack: [10, 20, 30]
 * pop():    return arr[2]=30, topIdx=1 | stack: [10, 20]
 * size():   return 1+1 = 2
 * pop():    return 20, topIdx=0     | stack: [10]
 * pop():    return 10, topIdx=-1    | stack: []
 * isEmpty(): topIdx == -1 -> true
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    Stack s;

    assert(s.isEmpty() == true);
    assert(s.size() == 0);
    assert(s.pop() == -1); // empty pop

    s.push(10);
    s.push(20);
    s.push(30);

    assert(s.size() == 3);
    assert(s.isEmpty() == false);
    assert(s.top() == 30);
    assert(s.pop() == 30);
    assert(s.pop() == 20);
    assert(s.size() == 1);
    assert(s.top() == 10);
    assert(s.pop() == 10);
    assert(s.isEmpty() == true);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    Stack s;
    int q;
    cout << "Enter number of operations: ";
    cin >> q;
    while (q--) {
        string op;
        cin >> op;
        if (op == "push") {
            int x; cin >> x;
            s.push(x);
            cout << "Pushed " << x << endl;
        } else if (op == "pop") {
            cout << "Popped: " << s.pop() << endl;
        } else if (op == "top") {
            cout << "Top: " << s.top() << endl;
        } else if (op == "size") {
            cout << "Size: " << s.size() << endl;
        } else if (op == "empty") {
            cout << (s.isEmpty() ? "Yes" : "No") << endl;
        }
    }
    return 0;
}

/*
 * Complexity Analysis:
 *   push: O(1), pop: O(1), top: O(1), isEmpty: O(1), size: O(1)
 *   Space: O(n) where n is the capacity
 *
 * Common Mistakes:
 *   - Not checking for overflow/underflow
 *   - Off-by-one: topIdx starts at -1, not 0
 *   - Memory leak: forgetting to delete[] in destructor
 *
 * Interview Tips:
 *   - Know both array-based and linked-list-based implementations
 *   - Mention dynamic resizing for production code
 *   - LIFO principle: Last In, First Out
 *   - Applications: function calls, undo, expression evaluation
 */
