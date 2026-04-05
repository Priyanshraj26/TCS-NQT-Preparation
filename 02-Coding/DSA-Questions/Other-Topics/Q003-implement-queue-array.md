# Q003: Implement Queue using Array

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Queue                        |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★                         |

---

## Problem Statement

Implement a **Queue** data structure using a circular array with the following operations:
- `enqueue(x)` -- Add element x to the rear.
- `dequeue()` -- Remove and return the front element. Return -1 if queue is empty.
- `front()` -- Return the front element without removing it. Return -1 if empty.
- `isEmpty()` -- Return true if the queue is empty.
- `size()` -- Return the number of elements.

---

## Input Format

- Series of operations on the queue.

## Output Format

- Output for each query operation.

---

## Constraints

- 1 <= number of operations <= 10^4
- 1 <= x <= 10^5

---

## Examples

```
Operations: enqueue(10), enqueue(20), front(), dequeue(), size(), isEmpty()
Output:     -, -, 10, 10, 1, false
```

---

## Hints

1. Use circular array to avoid wasting space.
2. Track front and rear indices.
3. Use modular arithmetic for wrapping around.

---

## Tags

`Queue` `Circular Array` `Data Structure Implementation` `TCS NQT` `Easy`
