# Solution: Implement Stack Using Array

[← Back to Question](../../DSA-Questions/Other-Topics/Q002-implement-stack-array.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Array-based Stack | O(1) per operation | O(n) | ✓✓ |

---

## Approach 1: Array-Based Stack Implementation

### Intuition
A stack follows LIFO (Last In, First Out). Use an array with a `top` pointer that tracks the index of the topmost element. Push increments `top` and places the element; pop returns the element at `top` and decrements it.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class Stack {
private:
    int* arr;
    int topIdx;
    int capacity;

public:
    // Constructor
    Stack(int size) {
        capacity = size;
        arr = new int[capacity];
        topIdx = -1; // empty stack
    }

    // Destructor
    ~Stack() {
        delete[] arr;
    }

    // Push element onto stack
    void push(int val) {
        if (isFull()) {
            cout << "Stack Overflow!" << endl;
            return;
        }
        arr[++topIdx] = val;
    }

    // Pop element from stack
    int pop() {
        if (isEmpty()) {
            cout << "Stack Underflow!" << endl;
            return -1;
        }
        return arr[topIdx--];
    }

    // Peek at top element
    int top() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return arr[topIdx];
    }

    // Check if stack is empty
    bool isEmpty() {
        return topIdx == -1;
    }

    // Check if stack is full
    bool isFull() {
        return topIdx == capacity - 1;
    }

    // Get current size
    int size() {
        return topIdx + 1;
    }
};

int main() {
    Stack st(5);

    // Test push
    st.push(10);
    st.push(20);
    st.push(30);
    cout << "Top: " << st.top() << endl;   // 30
    cout << "Size: " << st.size() << endl;  // 3

    // Test pop
    cout << "Popped: " << st.pop() << endl; // 30
    cout << "Popped: " << st.pop() << endl; // 20
    cout << "Top: " << st.top() << endl;    // 10
    cout << "Size: " << st.size() << endl;  // 1

    // Test empty
    cout << "Empty: " << boolalpha << st.isEmpty() << endl; // false
    st.pop(); // removes 10
    cout << "Empty: " << st.isEmpty() << endl; // true

    // Test underflow
    st.pop(); // Stack Underflow!

    // Test overflow
    st.push(1); st.push(2); st.push(3); st.push(4); st.push(5);
    st.push(6); // Stack Overflow!

    cout << "Size: " << st.size() << endl; // 5

    return 0;
}
```

### Dry Run

**Operations:** push(10), push(20), push(30), pop(), top(), pop()

| Operation | topIdx | Array State | Return |
|-----------|--------|-------------|--------|
| Initial | -1 | [ _, _, _, _, _ ] | -- |
| push(10) | 0 | [ 10, _, _, _, _ ] | -- |
| push(20) | 1 | [ 10, 20, _, _, _ ] | -- |
| push(30) | 2 | [ 10, 20, 30, _, _ ] | -- |
| pop() | 1 | [ 10, 20, _, _, _ ] | 30 |
| top() | 1 | [ 10, 20, _, _, _ ] | 20 |
| pop() | 0 | [ 10, _, _, _, _ ] | 20 |

### Complexity Analysis
- **push:** O(1)
- **pop:** O(1)
- **top:** O(1)
- **isEmpty/isFull:** O(1)
- **Space:** O(n) where n = capacity

---

## Common Mistakes
1. Not checking for overflow before push or underflow before pop
2. Initializing `topIdx = 0` instead of `-1` (off-by-one)
3. Forgetting to deallocate memory (memory leak without destructor)
4. Confusing `top` (peek) with `pop` (peek + remove)

## Interview Tips
- Know the difference between stack (LIFO) and queue (FIFO)
- The STL `stack<int>` uses a `deque` internally, but array-based is asked to test fundamentals
- Real-world uses: function call stack, undo operations, expression evaluation, backtracking
- Follow-up: implement a dynamic stack that resizes when full (double the capacity)
- Follow-up: implement stack using linked list (no size limit)
- For TCS NQT: this tests OOP basics along with data structure knowledge
