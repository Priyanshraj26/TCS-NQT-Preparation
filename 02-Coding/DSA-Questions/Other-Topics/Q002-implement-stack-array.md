# Q002: Implement Stack using Array

| Field       | Detail                          |
|-------------|---------------------------------|
| **Difficulty** | Easy                         |
| **Topic**      | Stack                        |
| **Source**     | TCS NQT                       |
| **Frequency**  | ★★★★★                       |

---

## Problem Statement

Implement a **Stack** data structure using an array with the following operations:
- `push(x)` -- Push element x onto the stack.
- `pop()` -- Remove and return the top element. Return -1 if stack is empty.
- `top()` / `peek()` -- Return the top element without removing it. Return -1 if empty.
- `isEmpty()` -- Return true if the stack is empty.
- `size()` -- Return the number of elements.

---

## Input Format

- Series of operations on the stack.

## Output Format

- Output for each query operation.

---

## Constraints

- 1 <= number of operations <= 10^4
- 1 <= x <= 10^5

---

## Examples

```
Operations: push(10), push(20), top(), pop(), size(), isEmpty()
Output:     -,  -, 20, 20, 1, false
```

---

## Hints

1. Use a `top` pointer (index) to track the current top of the stack.
2. Push increments top, pop decrements top.
3. Handle overflow/underflow conditions.

---

## Tags

`Stack` `Array` `Data Structure Implementation` `TCS NQT` `Easy`
