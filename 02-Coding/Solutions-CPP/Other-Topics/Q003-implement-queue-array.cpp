/*
 * Q003: Implement Queue using Array
 * Question: ../../../DSA-Questions/Other-Topics/Q003-implement-queue-array.md
 *
 * Approach: Circular array-based queue. All operations O(1).
 */

#include <iostream>
#include <cassert>
using namespace std;

// ===========================================
// Queue Implementation using Circular Array
// ===========================================
class Queue {
private:
    int* arr;
    int frontIdx, rearIdx, count, capacity;

public:
    Queue(int cap = 1000) {
        capacity = cap;
        arr = new int[capacity];
        frontIdx = 0;
        rearIdx = -1;
        count = 0;
    }

    ~Queue() {
        delete[] arr;
    }

    void enqueue(int x) {
        if (count == capacity) {
            cout << "Queue Overflow!" << endl;
            return;
        }
        rearIdx = (rearIdx + 1) % capacity;
        arr[rearIdx] = x;
        count++;
    }

    int dequeue() {
        if (isEmpty()) return -1;
        int val = arr[frontIdx];
        frontIdx = (frontIdx + 1) % capacity;
        count--;
        return val;
    }

    int front() {
        if (isEmpty()) return -1;
        return arr[frontIdx];
    }

    bool isEmpty() {
        return count == 0;
    }

    int size() {
        return count;
    }
};

// ===========================================
// Dry Run
// ===========================================
/*
 * Queue q; frontIdx=0, rearIdx=-1, count=0
 * enqueue(10): rearIdx=0, arr[0]=10, count=1   | queue: [10]
 * enqueue(20): rearIdx=1, arr[1]=20, count=2   | queue: [10, 20]
 * enqueue(30): rearIdx=2, arr[2]=30, count=3   | queue: [10, 20, 30]
 * front():     return arr[0] = 10
 * dequeue():   return 10, frontIdx=1, count=2  | queue: [20, 30]
 * dequeue():   return 20, frontIdx=2, count=1  | queue: [30]
 * size():      return 1
 * isEmpty():   count==0? No -> false
 */

// ===========================================
// Tests
// ===========================================
void runTests() {
    Queue q;

    assert(q.isEmpty() == true);
    assert(q.size() == 0);
    assert(q.dequeue() == -1);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    assert(q.size() == 3);
    assert(q.front() == 10);
    assert(q.dequeue() == 10);
    assert(q.dequeue() == 20);
    assert(q.size() == 1);
    assert(q.front() == 30);
    assert(q.dequeue() == 30);
    assert(q.isEmpty() == true);

    // Test circular behavior
    Queue q2(3);
    q2.enqueue(1); q2.enqueue(2); q2.enqueue(3);
    q2.dequeue(); // remove 1
    q2.enqueue(4); // should wrap around
    assert(q2.front() == 2);
    assert(q2.size() == 3);

    cout << "All tests passed!" << endl;
}

int main() {
    runTests();

    Queue q;
    int ops;
    cout << "Enter number of operations: ";
    cin >> ops;
    while (ops--) {
        string op;
        cin >> op;
        if (op == "enqueue") {
            int x; cin >> x;
            q.enqueue(x);
            cout << "Enqueued " << x << endl;
        } else if (op == "dequeue") {
            cout << "Dequeued: " << q.dequeue() << endl;
        } else if (op == "front") {
            cout << "Front: " << q.front() << endl;
        } else if (op == "size") {
            cout << "Size: " << q.size() << endl;
        } else if (op == "empty") {
            cout << (q.isEmpty() ? "Yes" : "No") << endl;
        }
    }
    return 0;
}

/*
 * Complexity Analysis:
 *   All operations: O(1) time
 *   Space: O(n) where n is the capacity
 *
 * Common Mistakes:
 *   - Not using circular indexing (wasting space with linear array)
 *   - Confusing front and rear pointers
 *   - Not handling empty queue before dequeue/front
 *
 * Interview Tips:
 *   - Know circular queue vs linear queue
 *   - FIFO principle: First In, First Out
 *   - Applications: BFS, scheduling, buffering
 *   - Can also implement queue using two stacks
 */
