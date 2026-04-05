/*
 * Q002: Detect Cycle in Linked List (Floyd's Algorithm)
 * Question: DSA-Questions/Linked-Lists/Q002-detect-cycle.md
 *
 * Approach Overview:
 * +---------------------+----------+---------+
 * | Approach            | Time     | Space   |
 * +---------------------+----------+---------+
 * | Hash Set            | O(n)     | O(n)    |
 * | Floyd's Algorithm   | O(n)     | O(1)    |
 * +---------------------+----------+---------+
 */

#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

// ==================== ListNode Definition ====================
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// ==================== Approach 1: Hash Set (Brute Force) ====================
/*
 * Idea: Store each visited node in a hash set.
 * If we encounter a node already in the set, a cycle exists.
 */
bool hasCycleBruteForce(ListNode* head) {
    unordered_set<ListNode*> visited;
    ListNode* curr = head;

    while (curr != nullptr) {
        if (visited.count(curr)) {
            return true;  // Node already visited => cycle
        }
        visited.insert(curr);
        curr = curr->next;
    }

    return false;  // Reached NULL => no cycle
}

// ==================== Approach 2: Floyd's Cycle Detection (Optimal) ====================
/*
 * Idea: Use two pointers -- slow (1 step) and fast (2 steps).
 * If there's a cycle, fast will eventually catch up to slow.
 * If fast reaches NULL, there's no cycle.
 *
 * Dry Run (cycle: 3->2->0->-4->back to 2):
 *   Start: slow=3, fast=3
 *   Step 1: slow=2, fast=0
 *   Step 2: slow=0, fast=2  (fast wrapped around)
 *   Step 3: slow=-4, fast=-4  => MATCH! Cycle detected.
 *
 * Why it works: In a cycle of length L, the relative speed
 * difference is 1 step per iteration, so they must meet within L steps.
 */
bool hasCycleFloyd(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;         // Move 1 step
        fast = fast->next->next;   // Move 2 steps

        if (slow == fast) {
            return true;  // Cycle detected
        }
    }

    return false;  // No cycle
}

// ==================== Follow-up: Find Cycle Start Node ====================
/*
 * After slow and fast meet inside the cycle:
 * 1. Reset one pointer to head
 * 2. Move both one step at a time
 * 3. They meet at the cycle start
 *
 * Math proof: Let distance from head to cycle start = a,
 * cycle length = c, and distance from cycle start to meeting point = b.
 * slow traveled: a + b
 * fast traveled: a + b + k*c (for some k >= 1)
 * Since fast = 2 * slow: a + b + k*c = 2(a + b) => a = k*c - b
 * So moving 'a' steps from head and 'a' steps from meeting point
 * both end up at cycle start.
 */
ListNode* detectCycleStart(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    // Phase 1: Detect cycle
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            // Phase 2: Find cycle start
            ListNode* entry = head;
            while (entry != slow) {
                entry = entry->next;
                slow = slow->next;
            }
            return entry;  // Cycle start node
        }
    }

    return nullptr;  // No cycle
}

// ==================== Main with Test Cases ====================
int main() {
    // Test Case 1: List with cycle (3 -> 2 -> 0 -> -4 -> back to 2)
    cout << "=== Test Case 1: List with cycle ===" << endl;
    ListNode* n1 = new ListNode(3);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(0);
    ListNode* n4 = new ListNode(-4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n2;  // Cycle back to n2

    cout << "Has cycle (Hash Set): " << (hasCycleBruteForce(n1) ? "true" : "false") << endl;
    cout << "Has cycle (Floyd's):  " << (hasCycleFloyd(n1) ? "true" : "false") << endl;
    ListNode* cycleStart = detectCycleStart(n1);
    cout << "Cycle starts at node: " << (cycleStart ? to_string(cycleStart->val) : "NULL") << endl;

    // Break cycle for cleanup
    n4->next = nullptr;
    delete n1; delete n2; delete n3; delete n4;

    // Test Case 2: No cycle
    cout << "\n=== Test Case 2: No cycle ===" << endl;
    ListNode* a1 = new ListNode(1);
    ListNode* a2 = new ListNode(2);
    ListNode* a3 = new ListNode(3);
    a1->next = a2;
    a2->next = a3;

    cout << "Has cycle (Hash Set): " << (hasCycleBruteForce(a1) ? "true" : "false") << endl;
    cout << "Has cycle (Floyd's):  " << (hasCycleFloyd(a1) ? "true" : "false") << endl;
    cycleStart = detectCycleStart(a1);
    cout << "Cycle starts at node: " << (cycleStart ? to_string(cycleStart->val) : "NULL") << endl;

    delete a1; delete a2; delete a3;

    // Test Case 3: Single node, no cycle
    cout << "\n=== Test Case 3: Single node ===" << endl;
    ListNode* b1 = new ListNode(1);
    cout << "Has cycle: " << (hasCycleFloyd(b1) ? "true" : "false") << endl;
    delete b1;

    // Test Case 4: Single node with self-loop
    cout << "\n=== Test Case 4: Self-loop ===" << endl;
    ListNode* c1 = new ListNode(1);
    c1->next = c1;
    cout << "Has cycle: " << (hasCycleFloyd(c1) ? "true" : "false") << endl;
    c1->next = nullptr;
    delete c1;

    return 0;
}

/*
 * Complexity Analysis:
 * - Hash Set: Time O(n), Space O(n)
 * - Floyd's: Time O(n), Space O(1) -- preferred in interviews
 *
 * Common Mistakes:
 * 1. Not checking fast->next before accessing fast->next->next
 * 2. Confusing node equality (pointer comparison) with value comparison
 * 3. Forgetting the follow-up: finding the cycle START node
 *
 * Interview Tips:
 * - Always mention Floyd's algorithm by name -- shows you know the concept
 * - Be ready to explain WHY fast and slow meet (math proof)
 * - The follow-up (find cycle start) is frequently asked as Part 2
 * - Practice drawing the cycle on paper
 */
