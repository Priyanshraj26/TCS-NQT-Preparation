# Solution: Implement Queue Using Array (Circular Queue)

[← Back to Question](../../DSA-Questions/Other-Topics/Q003-implement-queue-array.md)

## Approach Overview

| Approach | Time Complexity | Space Complexity | Recommended |
|----------|----------------|------------------|-------------|
| Simple Array (wasteful) | O(1) enqueue, O(n) dequeue | O(n) | ✗ |
| Circular Queue | O(1) per operation | O(n) | ✓✓ |

---

## Approach 1: Simple Array (Naive)

### Intuition
Use `front` and `rear` pointers. Enqueue at `rear`, dequeue at `front`. Problem: after many dequeue operations, front moves forward and space at the beginning is wasted.

### C++ Code
```cpp
#include <iostream>
using namespace std;

class SimpleQueue {
    int* arr;
    int front, rear, capacity;

public:
    SimpleQueue(int size) {
        capacity = size;
        arr = new int[capacity];
        front = 0;
        rear = -1;
    }
    ~SimpleQueue() { delete[] arr; }

    void enqueue(int val) {
        if (rear == capacity - 1) {
            cout << "Queue Overflow!" << endl;
            return;
        }
        arr[++rear] = val;
    }

    int dequeue() {
        if (front > rear) {
            cout << "Queue Underflow!" << endl;
            return -1;
        }
        return arr[front++]; // wastes space!
    }

    int peek() {
        if (front > rear) return -1;
        return arr[front];
    }

    bool isEmpty() { return front > rear; }
};

int main() {
    SimpleQueue q(5);
    q.enqueue(10);
    q.enqueue(20);
    cout << q.dequeue() << endl; // 10
    cout << q.peek() << endl;    // 20
    return 0;
}
```

### Complexity Analysis
- **Enqueue:** O(1)
- **Dequeue:** O(1) but wastes space (front spaces are never reused)

---

## Approach 2: Circular Queue (Optimal)

### Intuition
Use modular arithmetic to wrap around the array. When `rear` reaches the end, it wraps to index 0 if space is available. This reuses space freed by dequeue operations.

Key formula: `next index = (current + 1) % capacity`

### C++ Code
```cpp
#include <iostream>
using namespace std;

class CircularQueue {
private:
    int* arr;
    int front, rear;
    int capacity;
    int count; // current number of elements

public:
    CircularQueue(int size) {
        capacity = size;
        arr = new int[capacity];
        front = 0;
        rear = -1;
        count = 0;
    }

    ~CircularQueue() {
        delete[] arr;
    }

    // Add element to the rear
    void enqueue(int val) {
        if (isFull()) {
            cout << "Queue Overflow!" << endl;
            return;
        }
        rear = (rear + 1) % capacity; // wrap around
        arr[rear] = val;
        count++;
    }

    // Remove element from the front
    int dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow!" << endl;
            return -1;
        }
        int val = arr[front];
        front = (front + 1) % capacity; // wrap around
        count--;
        return val;
    }

    // Peek at front element
    int peek() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return arr[front];
    }

    bool isEmpty() {
        return count == 0;
    }

    bool isFull() {
        return count == capacity;
    }

    int size() {
        return count;
    }

    // Display the queue
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }
        int idx = front;
        for (int i = 0; i < count; i++) {
            cout << arr[idx] << " ";
            idx = (idx + 1) % capacity;
        }
        cout << endl;
    }
};

int main() {
    CircularQueue q(5);

    // Basic operations
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);
    q.enqueue(50);
    cout << "Queue: "; q.display(); // 10 20 30 40 50

    // Overflow test
    q.enqueue(60); // Queue Overflow!

    // Dequeue and wrap-around
    cout << "Dequeued: " << q.dequeue() << endl; // 10
    cout << "Dequeued: " << q.dequeue() << endl; // 20

    // Now front=2, rear=4. Enqueue wraps around.
    q.enqueue(60); // goes to index 0
    q.enqueue(70); // goes to index 1
    cout << "Queue: "; q.display(); // 30 40 50 60 70

    cout << "Front: " << q.peek() << endl;  // 30
    cout << "Size: " << q.size() << endl;    // 5
    cout << "Full: " << boolalpha << q.isFull() << endl; // true

    // Dequeue all
    while (!q.isEmpty()) {
        cout << q.dequeue() << " ";
    }
    cout << endl; // 30 40 50 60 70

    cout << "Empty: " << q.isEmpty() << endl; // true

    return 0;
}
```

### Dry Run
**Capacity = 5**

| Operation | front | rear | count | Array (indices 0-4) | Notes |
|-----------|-------|------|-------|---------------------|-------|
| Initial | 0 | -1 | 0 | [ _, _, _, _, _ ] | |
| enqueue(10) | 0 | 0 | 1 | [ 10, _, _, _, _ ] | |
| enqueue(20) | 0 | 1 | 2 | [ 10, 20, _, _, _ ] | |
| enqueue(30) | 0 | 2 | 3 | [ 10, 20, 30, _, _ ] | |
| dequeue() -> 10 | 1 | 2 | 2 | [ _, 20, 30, _, _ ] | front moves |
| dequeue() -> 20 | 2 | 2 | 1 | [ _, _, 30, _, _ ] | |
| enqueue(40) | 2 | 3 | 2 | [ _, _, 30, 40, _ ] | |
| enqueue(50) | 2 | 4 | 3 | [ _, _, 30, 40, 50 ] | |
| enqueue(60) | 2 | 0 | 4 | [ 60, _, 30, 40, 50 ] | **wraps!** |
| enqueue(70) | 2 | 1 | 5 | [ 60, 70, 30, 40, 50 ] | full |
| dequeue() -> 30 | 3 | 1 | 4 | [ 60, 70, _, 40, 50 ] | |

### Complexity Analysis
- **Enqueue:** O(1)
- **Dequeue:** O(1)
- **Peek:** O(1)
- **isEmpty/isFull:** O(1)
- **Space:** O(n) where n = capacity

---

## Common Mistakes
1. Not using modular arithmetic -- linear queue wastes space
2. Using only `front == rear` to check full/empty (ambiguous without count variable)
3. Forgetting to wrap `front` when it reaches the end of the array
4. Off-by-one in capacity calculation

## Interview Tips
- The circular queue is the standard way to implement a fixed-size queue efficiently
- Alternative to `count`: use `(rear - front + capacity) % capacity` for size, but waste one slot to distinguish full from empty
- Real-world uses: CPU scheduling, BFS, print spooler, buffering
- The STL `queue<int>` uses a `deque` internally
- Follow-up: implement using linked list (dynamic size), implement deque (double-ended queue)
- For TCS NQT: know the wrap-around logic with modular arithmetic
