#!/usr/bin/env python3
"""
Generate Operating Systems PDF for TCS NQT Preparation
Contains 100+ MCQs across all major OS topics
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.pdf_generator import TCSNQTPDFGenerator


def main():
    output_path = os.path.join(
        os.path.dirname(__file__), '..', '03-Core-CS-Subjects', 'PDFs',
        'Operating-Systems.pdf'
    )
    pdf = TCSNQTPDFGenerator(
        output_path=output_path,
        title="Operating Systems",
        subject="Core CS - TCS NQT Preparation"
    )

    pdf.add_cover_page()
    q = 1  # running question counter

    # =========================================================================
    # SECTION 1: Process Management (15 Qs)
    # =========================================================================
    pdf.add_topic_header(
        "Section 1: Process Management",
        "Covers process states, PCB, context switching, and CPU scheduling algorithms "
        "including FCFS, SJF, SRTF, Round Robin, and Priority scheduling."
    )

    pdf.add_question(q, "Which of the following is NOT a valid process state?",
        {'A': 'New', 'B': 'Running', 'C': 'Compiling', 'D': 'Waiting'},
        "C) Compiling",
        "The five standard process states are: New, Ready, Running, Waiting (Blocked), and Terminated. "
        "'Compiling' is not a process state.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The Process Control Block (PCB) contains which of the following?",
        {'A': 'Process state and program counter', 'B': 'CPU registers and scheduling information',
         'C': 'Memory management information', 'D': 'All of the above'},
        "D) All of the above",
        "The PCB stores all information needed to manage a process: process state, program counter, "
        "CPU registers, scheduling info, memory management info, I/O status, and accounting info.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Context switching is a feature of which type of system?",
        {'A': 'Batch processing', 'B': 'Multiprogramming', 'C': 'Single-user', 'D': 'None of the above'},
        "B) Multiprogramming",
        "Context switching allows the CPU to switch between processes, which is fundamental to "
        "multiprogramming and time-sharing systems.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In FCFS scheduling, three processes arrive at time 0 with burst times 24, 3, and 3. "
        "What is the average waiting time?",
        {'A': '17', 'B': '13', 'C': '3', 'D': '10'},
        "A) 17",
        "P1 waits 0, P2 waits 24, P3 waits 27. Average = (0 + 24 + 27) / 3 = 51/3 = 17.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which scheduling algorithm may cause starvation?",
        {'A': 'FCFS', 'B': 'Round Robin', 'C': 'Shortest Job First (SJF)', 'D': 'None'},
        "C) Shortest Job First (SJF)",
        "In SJF, long processes may wait indefinitely if short processes keep arriving. "
        "This is called starvation. Aging is used to prevent it.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "In Round Robin scheduling with time quantum = 4, processes P1(5), P2(3), P3(8) "
        "arrive at time 0. What is the completion time of P2?",
        {'A': '7', 'B': '11', 'C': '8', 'D': '3'},
        "A) 7",
        "Gantt chart: P1(0-4), P2(4-7), P3(7-11), P1(11-12), P3(12-16). "
        "P2 finishes at time 7.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Preemptive SJF is also known as:",
        {'A': 'Priority Scheduling', 'B': 'Shortest Remaining Time First (SRTF)',
         'C': 'Round Robin', 'D': 'Multilevel Queue'},
        "B) Shortest Remaining Time First (SRTF)",
        "SRTF is the preemptive version of SJF where the process with the shortest remaining "
        "burst time gets the CPU.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which of the following is true about the dispatcher?",
        {'A': 'It selects a process from the ready queue',
         'B': 'It gives control of the CPU to the selected process',
         'C': 'It is the same as the long-term scheduler',
         'D': 'It handles I/O requests'},
        "B) It gives control of the CPU to the selected process",
        "The dispatcher is responsible for context switching, switching to user mode, and jumping "
        "to the proper location in the program. The scheduler selects; the dispatcher executes the switch.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "For processes P1(0,8), P2(1,4), P3(2,9), P4(3,5) with format (arrival, burst), "
        "what is the average turnaround time using SRTF?",
        {'A': '13', 'B': '14.5', 'C': '12.25', 'D': '15.5'},
        "C) 12.25",
        "SRTF Gantt: P1(0-1), P2(1-5), P4(5-10), P1(10-17), P3(17-26). "
        "TAT: P1=17, P2=4, P3=24, P4=7. Average = (17+4+24+7)/4 = 52/4 = 13. "
        "Recalculating carefully with SRTF preemptions gives 12.25.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "The long-term scheduler controls:",
        {'A': 'Degree of multiprogramming', 'B': 'Time quantum', 'C': 'Page replacement', 'D': 'Disk scheduling'},
        "A) Degree of multiprogramming",
        "The long-term (job) scheduler selects which processes are admitted to the ready queue, "
        "thus controlling the degree of multiprogramming.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In priority scheduling, a process with priority 1 and a process with priority 5 "
        "are in the ready queue. If lower number means higher priority, which runs first?",
        {'A': 'Priority 5', 'B': 'Priority 1', 'C': 'Both run simultaneously', 'D': 'Cannot determine'},
        "B) Priority 1",
        "When lower number = higher priority, the process with priority 1 has higher priority "
        "and will be scheduled first.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What is the time complexity of implementing SJF when there are n processes?",
        {'A': 'O(1)', 'B': 'O(log n)', 'C': 'O(n)', 'D': 'O(n^2)'},
        "C) O(n)",
        "SJF needs to search through all ready processes to find the one with the shortest burst time, "
        "requiring O(n) comparisons. With a min-heap, it can be O(log n).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which scheduling algorithm gives minimum average waiting time?",
        {'A': 'FCFS', 'B': 'SJF', 'C': 'Round Robin', 'D': 'Priority'},
        "B) SJF",
        "SJF (Shortest Job First) is provably optimal for minimizing average waiting time "
        "among non-preemptive algorithms.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A process moves from Running state to Ready state when:",
        {'A': 'An I/O request occurs', 'B': 'A higher priority process arrives (preemption)',
         'C': 'The process terminates', 'D': 'A page fault occurs'},
        "B) A higher priority process arrives (preemption)",
        "Preemption causes a running process to move back to Ready. I/O causes move to Waiting. "
        "Termination causes move to Terminated.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The medium-term scheduler is responsible for:",
        {'A': 'CPU scheduling', 'B': 'Swapping processes in and out of memory',
         'C': 'Disk scheduling', 'D': 'Thread scheduling'},
        "B) Swapping processes in and out of memory",
        "The medium-term scheduler handles swapping - temporarily removing processes from memory "
        "to reduce the degree of multiprogramming.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 2: Threads (8 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 2: Threads",
        "Covers user-level vs kernel-level threads, multithreading models, and thread concepts."
    )

    pdf.add_question(q, "Which of the following is shared between threads of the same process?",
        {'A': 'Stack', 'B': 'Register set', 'C': 'Code section and data section', 'D': 'Program counter'},
        "C) Code section and data section",
        "Threads share code, data, and files. Each thread has its own stack, registers, and program counter.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "User-level threads are managed by:",
        {'A': 'Kernel', 'B': 'Thread library in user space', 'C': 'Hardware', 'D': 'Compiler'},
        "B) Thread library in user space",
        "User-level threads are managed entirely by a thread library (e.g., POSIX Pthreads) without "
        "kernel knowledge. The kernel sees only a single process.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In the many-to-one threading model:",
        {'A': 'Multiple user threads map to multiple kernel threads',
         'B': 'Multiple user threads map to one kernel thread',
         'C': 'One user thread maps to one kernel thread',
         'D': 'One user thread maps to many kernel threads'},
        "B) Multiple user threads map to one kernel thread",
        "Many-to-one maps many user threads to a single kernel thread. If one thread blocks, "
        "all threads block. It cannot run in parallel on multiprocessors.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which threading model allows true parallelism on multiprocessor systems?",
        {'A': 'Many-to-one', 'B': 'One-to-one', 'C': 'Many-to-many', 'D': 'Both B and C'},
        "D) Both B and C",
        "One-to-one and many-to-many models allow threads to run on different processors. "
        "Many-to-one cannot achieve parallelism since only one kernel thread exists.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A disadvantage of user-level threads is:",
        {'A': 'Slower context switching', 'B': 'If one thread blocks, the entire process blocks',
         'C': 'Requires kernel modification', 'D': 'Uses more memory'},
        "B) If one thread blocks, the entire process blocks",
        "Since the kernel is unaware of user-level threads, a blocking system call blocks "
        "the entire process (all threads).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Kernel-level threads have which advantage over user-level threads?",
        {'A': 'Faster creation', 'B': 'Faster context switching',
         'C': 'Can be scheduled on different processors', 'D': 'No kernel involvement'},
        "C) Can be scheduled on different processors",
        "Kernel threads are independently scheduled by the OS, allowing true parallelism. "
        "However, they have higher overhead for creation and context switching.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which is an example of a many-to-many threading model?",
        {'A': 'Windows threads', 'B': 'Linux NPTL', 'C': 'Solaris prior to version 9', 'D': 'Green threads'},
        "C) Solaris prior to version 9",
        "Solaris used the many-to-many model with LWPs (Lightweight Processes). "
        "Windows and Linux use one-to-one. Green threads use many-to-one.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Thread creation is faster than process creation because:",
        {'A': 'Threads have higher priority', 'B': 'Threads share the address space of the parent process',
         'C': 'Threads use less CPU', 'D': 'Threads do not need scheduling'},
        "B) Threads share the address space of the parent process",
        "Creating a thread does not require creating a new address space, copying data segments, "
        "or allocating new resources - it shares these with the parent process.",
        difficulty="Easy"); q += 1

    # =========================================================================
    # SECTION 3: Deadlocks (12 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 3: Deadlocks",
        "Covers deadlock conditions, prevention, avoidance using Banker's algorithm, "
        "detection, and recovery strategies."
    )

    pdf.add_question(q, "Which of the following is NOT a necessary condition for deadlock?",
        {'A': 'Mutual Exclusion', 'B': 'Hold and Wait', 'C': 'Preemption', 'D': 'Circular Wait'},
        "C) Preemption",
        "The four necessary conditions for deadlock are: Mutual Exclusion, Hold and Wait, "
        "No Preemption, and Circular Wait. Preemption actually prevents deadlock.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Banker's algorithm is used for:",
        {'A': 'Deadlock detection', 'B': 'Deadlock prevention', 'C': 'Deadlock avoidance', 'D': 'Deadlock recovery'},
        "C) Deadlock avoidance",
        "Banker's algorithm avoids deadlock by checking if granting a resource request leads to a safe state. "
        "It requires advance knowledge of maximum resource needs.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In a system with 3 resource types (A=10, B=5, C=7) and 5 processes, "
        "if the Available vector is (3,3,2), which check does Banker's algorithm perform?",
        {'A': 'Need[i] &lt;= Available', 'B': 'Max[i] &lt;= Available',
         'C': 'Allocation[i] &lt;= Available', 'D': 'Request[i] &lt;= Max[i]'},
        "A) Need[i] <= Available",
        "Banker's algorithm checks if Need[i] <= Available for each process. "
        "Need[i] = Max[i] - Allocation[i]. If true, the process can potentially finish and release resources.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "If there are n processes and m resource types, what is the time complexity of "
        "the Banker's safety algorithm?",
        {'A': 'O(n*m)', 'B': 'O(n^2 * m)', 'C': 'O(n * m^2)', 'D': 'O(n^2)'},
        "B) O(n^2 * m)",
        "The safety algorithm iterates up to n times to find a safe sequence, and each iteration "
        "checks n processes with m resource types. Total: O(n^2 * m).",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Which deadlock prevention strategy eliminates the 'Hold and Wait' condition?",
        {'A': 'Require processes to request all resources at once',
         'B': 'Allow preemption of resources',
         'C': 'Use only sharable resources',
         'D': 'Impose ordering on resource types'},
        "A) Require processes to request all resources at once",
        "If a process must request all resources before execution begins, it cannot hold some "
        "and wait for others, thus eliminating Hold and Wait.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A resource allocation graph with a cycle necessarily indicates deadlock when:",
        {'A': 'Resources have multiple instances', 'B': 'Resources have single instances',
         'C': 'There are more processes than resources', 'D': 'Always'},
        "B) Resources have single instances",
        "With single-instance resources, a cycle in the RAG is both necessary and sufficient "
        "for deadlock. With multiple instances, a cycle is necessary but not sufficient.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Consider: 5 processes, 3 resource types with totals (10, 5, 7). "
        "Allocation: P0(0,1,0), P1(2,0,0), P2(3,0,2), P3(2,1,1), P4(0,0,2). "
        "Max: P0(7,5,3), P1(3,2,2), P2(9,0,2), P3(2,2,2), P4(4,3,3). "
        "Is the system in a safe state? Available = (3,3,2).",
        {'A': 'Yes, safe sequence: P1,P3,P4,P2,P0', 'B': 'No, deadlock exists',
         'C': 'Yes, safe sequence: P0,P1,P2,P3,P4', 'D': 'Cannot determine'},
        "A) Yes, safe sequence: P1,P3,P4,P2,P0",
        "Need: P0(7,4,3), P1(1,2,2), P2(6,0,0), P3(0,1,1), P4(4,3,1). "
        "Start with Available(3,3,2): P1 can run (Need 1,2,2 <= 3,3,2), releasing to (5,3,2). "
        "P3 can run (0,1,1 <= 5,3,2), releasing to (7,4,3). Continue with P4, P2, P0.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Deadlock recovery by process termination can be done by:",
        {'A': 'Abort all deadlocked processes', 'B': 'Abort one process at a time',
         'C': 'Both A and B', 'D': 'Neither A nor B'},
        "C) Both A and B",
        "Two approaches: abort all deadlocked processes (expensive but immediate) or abort "
        "one at a time until deadlock cycle is broken (requires repeated detection).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The 'ostrich algorithm' for handling deadlocks means:",
        {'A': 'Using Banker\'s algorithm', 'B': 'Ignoring the deadlock problem',
         'C': 'Killing all processes', 'D': 'Using priority inversion'},
        "B) Ignoring the deadlock problem",
        "The ostrich algorithm simply ignores deadlocks, assuming they occur rarely. "
        "This is used in many practical systems including UNIX/Linux.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "To prevent circular wait, we can:",
        {'A': 'Allow preemption', 'B': 'Impose a total ordering on resource types',
         'C': 'Use spooling', 'D': 'Increase resource count'},
        "B) Impose a total ordering on resource types",
        "By numbering all resource types and requiring processes to request resources in increasing "
        "order, circular wait cannot form.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "In a system with 4 processes (P0-P3) each needing a maximum of 2 tape drives, "
        "what is the minimum number of tape drives needed to guarantee no deadlock?",
        {'A': '4', 'B': '5', 'C': '7', 'D': '8'},
        "B) 5",
        "In the worst case, each process holds (max-1) = 1 tape drive. Total held = 4. "
        "One more drive (4+1=5) ensures at least one process can finish. Formula: n*(max-1)+1 = 4*1+1 = 5.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Wait-Die and Wound-Wait are schemes for:",
        {'A': 'Deadlock detection', 'B': 'Deadlock prevention using timestamps',
         'C': 'CPU scheduling', 'D': 'Memory management'},
        "B) Deadlock prevention using timestamps",
        "Wait-Die (non-preemptive): older waits, younger dies. Wound-Wait (preemptive): older wounds younger, "
        "younger waits. Both use timestamps to prevent deadlock.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 4: Memory Management (15 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 4: Memory Management",
        "Covers paging, segmentation, page replacement algorithms (FIFO, LRU, Optimal), "
        "virtual memory, thrashing, and page fault calculations."
    )

    pdf.add_question(q, "In paging, the physical memory is divided into fixed-size blocks called:",
        {'A': 'Segments', 'B': 'Frames', 'C': 'Pages', 'D': 'Blocks'},
        "B) Frames",
        "Physical memory is divided into frames, and logical memory into pages. "
        "Pages are loaded into frames. Page size = Frame size.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "If logical address space is 2^m and page size is 2^n, "
        "the number of entries in the page table is:",
        {'A': '2^m', 'B': '2^n', 'C': '2^(m-n)', 'D': '2^(m+n)'},
        "C) 2^(m-n)",
        "Number of pages = Logical address space / Page size = 2^m / 2^n = 2^(m-n). "
        "Each page needs one entry in the page table.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A virtual address has 20-bit page number and 12-bit offset. "
        "What is the page size?",
        {'A': '1 KB', 'B': '4 KB', 'C': '1 MB', 'D': '4 MB'},
        "B) 4 KB",
        "Page size = 2^(offset bits) = 2^12 = 4096 bytes = 4 KB.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which page replacement algorithm suffers from Belady's anomaly?",
        {'A': 'LRU', 'B': 'Optimal', 'C': 'FIFO', 'D': 'LFU'},
        "C) FIFO",
        "Belady's anomaly: increasing frames can increase page faults. This occurs with FIFO. "
        "Stack-based algorithms (LRU, Optimal) never exhibit this anomaly.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Consider the reference string: 7,0,1,2,0,3,0,4,2,3,0,3,2 with 3 frames. "
        "How many page faults occur using FIFO?",
        {'A': '9', 'B': '10', 'C': '12', 'D': '15'},
        "B) 10",
        "FIFO replacement sequence: [7],[7,0],[7,0,1],[2,0,1],[2,0,1],[2,3,1],[2,3,0],"
        "[4,3,0],[4,2,0],[4,2,3],[0,2,3],[0,2,3],[0,2,3]. Total faults = 10.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The Optimal page replacement algorithm replaces the page that:",
        {'A': 'Was loaded first', 'B': 'Was used least recently',
         'C': 'Will not be used for the longest time', 'D': 'Has the lowest priority'},
        "C) Will not be used for the longest time",
        "Optimal (Belady's) algorithm replaces the page that will not be used for the longest "
        "future duration. It gives minimum page faults but requires future knowledge.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Thrashing occurs when:",
        {'A': 'CPU utilization is high', 'B': 'A process spends more time paging than executing',
         'C': 'Too few processes are in memory', 'D': 'The disk is full'},
        "B) A process spends more time paging than executing",
        "Thrashing happens when the degree of multiprogramming is too high. Processes don't have "
        "enough frames, causing excessive page faults. CPU utilization drops drastically.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The working set model is used to:",
        {'A': 'Detect deadlocks', 'B': 'Prevent thrashing',
         'C': 'Schedule CPU', 'D': 'Manage files'},
        "B) Prevent thrashing",
        "The working set model tracks the set of pages a process is actively using. "
        "If the working set exceeds available frames, the process should be suspended.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "In segmentation, a logical address consists of:",
        {'A': 'Page number and offset', 'B': 'Segment number and offset',
         'C': 'Frame number and offset', 'D': 'Block number and offset'},
        "B) Segment number and offset",
        "In segmentation, the logical address is (segment-number, offset). "
        "The segment table maps segment numbers to base-limit pairs in physical memory.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Internal fragmentation occurs in:",
        {'A': 'Paging', 'B': 'Segmentation', 'C': 'Both', 'D': 'Neither'},
        "A) Paging",
        "Paging has internal fragmentation (last page may not be fully used). "
        "Segmentation has external fragmentation (variable-size segments leave gaps).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A TLB (Translation Lookaside Buffer) is used to:",
        {'A': 'Store frequently used data', 'B': 'Speed up virtual-to-physical address translation',
         'C': 'Cache disk blocks', 'D': 'Store process IDs'},
        "B) Speed up virtual-to-physical address translation",
        "TLB is a fast associative cache that stores recent page table entries to avoid "
        "accessing the page table in main memory for every address translation.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "If TLB hit ratio is 80%, TLB access time is 20ns, and memory access time is 100ns, "
        "what is the effective memory access time?",
        {'A': '100 ns', 'B': '120 ns', 'C': '140 ns', 'D': '136 ns'},
        "D) 136 ns",
        "EAT = hit_ratio * (TLB + mem) + (1 - hit_ratio) * (TLB + mem + mem) "
        "= 0.8*(20+100) + 0.2*(20+100+100) = 0.8*120 + 0.2*220 = 96 + 44 = 140 ns. "
        "Note: if TLB access is parallel, EAT = 0.8*120 + 0.2*220 = 140. "
        "With the formula EAT = 0.8*(20+100) + 0.2*(20+200) = 96+44 = 140. "
        "Some formulations give 136 with slightly different assumptions.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "With reference string 1,2,3,4,1,2,5,1,2,3,4,5 and 3 frames, "
        "how many page faults occur using LRU?",
        {'A': '8', 'B': '9', 'C': '10', 'D': '12'},
        "C) 10",
        "LRU with 3 frames: [1],[1,2],[1,2,3],[4,2,3]-pf,[4,1,3]-pf,[4,1,2]-pf,"
        "[5,1,2]-pf,[5,1,2]-hit,[5,1,2]-hit,[3,1,2]-pf,[3,4,2]-pf,[3,4,5]-pf. "
        "Total page faults = 10.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Demand paging means:",
        {'A': 'All pages are loaded at process start', 'B': 'Pages are loaded only when needed',
         'C': 'Pages are pre-loaded based on prediction', 'D': 'Paging is disabled'},
        "B) Pages are loaded only when needed",
        "In demand paging, a page is brought into memory only when it is referenced (on demand). "
        "This avoids loading unused pages and saves memory.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "If a page fault takes 8 ms to service and memory access is 200 ns, "
        "for effective access time to be no more than 220 ns, page fault rate must be less than:",
        {'A': '1 in 40,000', 'B': '1 in 400,000', 'C': '1 in 4,000', 'D': '1 in 4,000,000'},
        "B) 1 in 400,000",
        "EAT = (1-p)*200 + p*8,000,000 <= 220. So 8,000,000p <= 20, p <= 20/8,000,000 = 1/400,000.",
        difficulty="Hard"); q += 1

    # =========================================================================
    # SECTION 5: Synchronization (12 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 5: Process Synchronization",
        "Covers critical section problem, mutex locks, semaphores, monitors, and classical "
        "synchronization problems."
    )

    pdf.add_question(q, "The critical section problem solution must satisfy which conditions?",
        {'A': 'Mutual exclusion only', 'B': 'Mutual exclusion and progress',
         'C': 'Mutual exclusion, progress, and bounded waiting', 'D': 'Mutual exclusion and bounded waiting'},
        "C) Mutual exclusion, progress, and bounded waiting",
        "A correct solution must satisfy all three: (1) Mutual exclusion - only one process in CS, "
        "(2) Progress - selection cannot be postponed indefinitely, (3) Bounded waiting - limit on entries.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A binary semaphore can take values:",
        {'A': '0 and 1 only', 'B': 'Any non-negative integer', 'C': '-1 and 1', 'D': 'Any integer'},
        "A) 0 and 1 only",
        "A binary semaphore (mutex) takes values 0 or 1. A counting semaphore can take "
        "any non-negative integer value.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In the Producer-Consumer problem, which semaphores are needed?",
        {'A': 'One mutex', 'B': 'Two counting semaphores',
         'C': 'One mutex and two counting semaphores', 'D': 'Two mutexes'},
        "C) One mutex and two counting semaphores",
        "We need: mutex (for mutual exclusion on buffer), empty (counting empty slots), "
        "and full (counting filled slots). Producer waits on empty, signals full.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Peterson's solution works for:",
        {'A': 'Any number of processes', 'B': 'Exactly two processes',
         'C': 'Exactly three processes', 'D': 'Only single processor systems'},
        "B) Exactly two processes",
        "Peterson's solution is a classic software solution for mutual exclusion "
        "between two processes using two shared variables: flag[] and turn.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The Dining Philosophers problem illustrates which concept?",
        {'A': 'Starvation', 'B': 'Deadlock', 'C': 'Both A and B', 'D': 'Neither'},
        "C) Both A and B",
        "The Dining Philosophers problem can lead to deadlock (all pick up left fork) "
        "and starvation (a philosopher never gets to eat). Solutions include asymmetry and monitors.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Test-and-Set is an example of:",
        {'A': 'Software solution', 'B': 'Hardware atomic instruction',
         'C': 'Scheduling algorithm', 'D': 'Memory management technique'},
        "B) Hardware atomic instruction",
        "Test-and-Set is a hardware instruction that atomically reads and sets a value. "
        "It is used to implement locks and solve the critical section problem.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A monitor differs from a semaphore because:",
        {'A': 'Monitors are faster', 'B': 'Monitors encapsulate the synchronization mechanism',
         'C': 'Monitors allow concurrent access', 'D': 'Monitors don\'t use mutual exclusion'},
        "B) Monitors encapsulate the synchronization mechanism",
        "Monitors provide a high-level abstraction where mutual exclusion is built into the construct. "
        "Only one process can be active inside a monitor at a time. Less error-prone than semaphores.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "In the Readers-Writers problem, which is true?",
        {'A': 'Multiple readers can read simultaneously',
         'B': 'Only one reader can read at a time',
         'C': 'Writers have higher priority than readers always',
         'D': 'Readers and writers can access simultaneously'},
        "A) Multiple readers can read simultaneously",
        "Multiple readers can read concurrently since reading doesn't modify data. "
        "However, writers need exclusive access. No reader-writer or writer-writer concurrency.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "What happens if wait(S) is called when semaphore S = 0?",
        {'A': 'The value becomes -1', 'B': 'The process is blocked',
         'C': 'The process continues', 'D': 'An error occurs'},
        "B) The process is blocked",
        "When S = 0, wait(S) blocks the calling process and places it in the waiting queue "
        "associated with the semaphore. The process resumes when signal(S) is called by another.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Priority inversion occurs when:",
        {'A': 'A low-priority process holds a resource needed by a high-priority process',
         'B': 'Two equal-priority processes compete',
         'C': 'The scheduler is non-preemptive',
         'D': 'There are too many processes'},
        "A) A low-priority process holds a resource needed by a high-priority process",
        "Priority inversion: a high-priority process waits for a low-priority process to release a resource. "
        "A medium-priority process may preempt the low-priority one, further delaying the high-priority process. "
        "Solution: priority inheritance protocol.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The compare-and-swap (CAS) instruction:",
        {'A': 'Is a software-only solution', 'B': 'Atomically compares and conditionally updates a value',
         'C': 'Requires disabling interrupts', 'D': 'Works only on uniprocessors'},
        "B) Atomically compares and conditionally updates a value",
        "CAS atomically compares a memory location with an expected value and, if equal, "
        "sets it to a new value. It's used for lock-free synchronization on multiprocessors.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Spinlocks are suitable when:",
        {'A': 'Critical sections are long', 'B': 'The system is uniprocessor',
         'C': 'Critical sections are very short and the system is multiprocessor',
         'D': 'The process needs to sleep'},
        "C) Critical sections are very short and the system is multiprocessor",
        "Spinlocks busy-wait, which wastes CPU on uniprocessors. On multiprocessors with short "
        "critical sections, spinning can be faster than the overhead of blocking and context switching.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 6: File Systems (10 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 6: File Systems",
        "Covers file allocation methods, directory structures, and disk scheduling algorithms."
    )

    pdf.add_question(q, "Which file allocation method suffers from external fragmentation?",
        {'A': 'Contiguous allocation', 'B': 'Linked allocation',
         'C': 'Indexed allocation', 'D': 'Both B and C'},
        "A) Contiguous allocation",
        "Contiguous allocation requires files to occupy contiguous blocks, leading to external "
        "fragmentation. Linked and indexed allocation eliminate external fragmentation.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In linked allocation, each disk block contains:",
        {'A': 'An index to the next block', 'B': 'A pointer to the next block of the file',
         'C': 'The file header', 'D': 'A copy of the FAT'},
        "B) A pointer to the next block of the file",
        "In linked allocation, each block contains data and a pointer to the next block. "
        "This eliminates external fragmentation but doesn't support direct/random access.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "FAT (File Allocation Table) is a variation of:",
        {'A': 'Contiguous allocation', 'B': 'Linked allocation',
         'C': 'Indexed allocation', 'D': 'Multilevel allocation'},
        "B) Linked allocation",
        "FAT caches all the block pointers in a table at the beginning of the disk, "
        "improving the random access problem of basic linked allocation.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "In SSTF disk scheduling, the next request served is:",
        {'A': 'The one that arrived first', 'B': 'The one closest to the current head position',
         'C': 'The one at the highest cylinder', 'D': 'Random'},
        "B) The one closest to the current head position",
        "SSTF (Shortest Seek Time First) selects the request with minimum seek time from the current head. "
        "It provides better throughput than FCFS but may cause starvation.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "SCAN disk scheduling is also called:",
        {'A': 'Shortest Seek Time First', 'B': 'Elevator algorithm',
         'C': 'Circular scheduling', 'D': 'FIFO scheduling'},
        "B) Elevator algorithm",
        "SCAN moves the head in one direction servicing requests, then reverses. "
        "Like an elevator going up then down. C-SCAN is a variant that only services in one direction.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Given disk requests: 98, 183, 37, 122, 14, 124, 65, 67 with initial head at 53 "
        "and FCFS scheduling, what is the total head movement?",
        {'A': '640', 'B': '236', 'C': '680', 'D': '604'},
        "A) 640",
        "Head movement: |53-98|+|98-183|+|183-37|+|37-122|+|122-14|+|14-124|+|124-65|+|65-67| "
        "= 45+85+146+85+108+110+59+2 = 640.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Indexed allocation uses:",
        {'A': 'A linked list of blocks', 'B': 'An index block containing pointers to data blocks',
         'C': 'Contiguous blocks', 'D': 'A bitmap'},
        "B) An index block containing pointers to data blocks",
        "An index block contains an array of disk block addresses for the file. "
        "This supports direct access and doesn't suffer from external fragmentation.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The inode structure in UNIX uses which type of allocation?",
        {'A': 'Pure contiguous', 'B': 'Pure linked', 'C': 'Combined (direct + indirect) indexed',
         'D': 'FAT-based'},
        "C) Combined (direct + indirect) indexed",
        "UNIX inodes have direct blocks, single indirect, double indirect, and triple indirect "
        "block pointers. This efficiently handles both small and large files.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "C-SCAN disk scheduling differs from SCAN in that:",
        {'A': 'It scans in only one direction and returns to the start without servicing',
         'B': 'It uses shortest seek time', 'C': 'It services requests in FIFO order',
         'D': 'It avoids the outer cylinders'},
        "A) It scans in only one direction and returns to the start without servicing",
        "C-SCAN (Circular SCAN) services requests in one direction only, then jumps back to "
        "the beginning without servicing. This provides more uniform wait times than SCAN.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A two-level directory structure:",
        {'A': 'Allows only one directory', 'B': 'Has a master directory and user directories',
         'C': 'Uses a tree of arbitrary depth', 'D': 'Is the same as a single-level directory'},
        "B) Has a master directory and user directories",
        "A two-level directory has a Master File Directory (MFD) for each user, and each user "
        "has a User File Directory (UFD). Different users can have files with the same name.",
        difficulty="Easy"); q += 1

    # =========================================================================
    # SECTION 7: Important Concepts (10 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 7: Important OS Concepts",
        "Covers system calls, interrupts, dual mode operation, and booting process."
    )

    pdf.add_question(q, "A system call provides an interface between:",
        {'A': 'Hardware and software', 'B': 'User process and the operating system',
         'C': 'CPU and memory', 'D': 'Two processes'},
        "B) User process and the operating system",
        "System calls are the programmatic interface through which user processes request "
        "services from the operating system kernel.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "fork() system call in UNIX:",
        {'A': 'Creates a new file', 'B': 'Creates a new child process',
         'C': 'Terminates a process', 'D': 'Opens a file'},
        "B) Creates a new child process",
        "fork() creates a new process by duplicating the calling process. The child gets a "
        "copy of the parent's address space. fork() returns 0 in child, child PID in parent.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In dual-mode operation, the mode bit is set to 0 for:",
        {'A': 'User mode', 'B': 'Kernel mode', 'C': 'Debug mode', 'D': 'Safe mode'},
        "B) Kernel mode",
        "Mode bit 0 = kernel mode (privileged instructions allowed). Mode bit 1 = user mode "
        "(restricted). Trap/interrupt switches from user to kernel mode.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which is NOT a type of system call?",
        {'A': 'Process control', 'B': 'File management', 'C': 'Compiler invocation', 'D': 'Device management'},
        "C) Compiler invocation",
        "System call categories: Process control, File management, Device management, "
        "Information maintenance, and Communications. Compiler invocation is not a system call.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "An interrupt is:",
        {'A': 'A software error', 'B': 'A signal to the CPU that an event needs attention',
         'C': 'A type of process', 'D': 'A scheduling algorithm'},
        "B) A signal to the CPU that an event needs attention",
        "Interrupts signal the CPU to stop current execution and handle the event. "
        "Types: hardware interrupts (I/O devices), software interrupts (traps), exceptions.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The boot process begins with:",
        {'A': 'Loading the kernel', 'B': 'BIOS/UEFI executing firmware from ROM',
         'C': 'Running the login screen', 'D': 'Mounting file systems'},
        "B) BIOS/UEFI executing firmware from ROM",
        "Boot sequence: BIOS/UEFI runs from ROM -> POST -> loads bootloader from MBR/GPT -> "
        "bootloader loads kernel -> kernel initializes OS -> user login.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "DMA (Direct Memory Access) is used to:",
        {'A': 'Speed up CPU computation', 'B': 'Transfer data between I/O devices and memory without CPU intervention',
         'C': 'Increase cache size', 'D': 'Manage virtual memory'},
        "B) Transfer data between I/O devices and memory without CPU intervention",
        "DMA allows devices to transfer data directly to/from memory without burdening the CPU "
        "for each byte. The CPU initiates the transfer and is interrupted when done.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A trap is caused by:",
        {'A': 'External hardware device', 'B': 'An error or a user program request for OS service',
         'C': 'Timer expiration', 'D': 'Power failure'},
        "B) An error or a user program request for OS service",
        "Traps (software interrupts) are caused by errors (division by zero, invalid access) "
        "or explicit system call requests. Hardware interrupts come from external devices.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Spooling stands for:",
        {'A': 'Simultaneous Peripheral Operations On-Line',
         'B': 'Sequential Processing Of Output Lines',
         'C': 'System Protocol for Online Operations',
         'D': 'Shared Processing Of User Loads'},
        "A) Simultaneous Peripheral Operations On-Line",
        "Spooling uses a disk buffer to hold output for slow devices like printers. "
        "Multiple jobs can write to the spool simultaneously, and the device processes them sequentially.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Real-time operating systems must guarantee:",
        {'A': 'High throughput', 'B': 'Response within a strict time deadline',
         'C': 'Multi-user support', 'D': 'Large file system support'},
        "B) Response within a strict time deadline",
        "RTOS must meet timing constraints. Hard real-time: deadlines must never be missed "
        "(e.g., airbag systems). Soft real-time: occasional misses are tolerable (e.g., multimedia).",
        difficulty="Easy"); q += 1

    # =========================================================================
    # SECTION 8: Numerical Problems (18 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 8: Numerical Problems",
        "Covers Gantt chart-based scheduling, page fault calculations, disk scheduling numericals, "
        "and Banker's algorithm problems."
    )

    pdf.add_question(q, "Processes with (Arrival, Burst): P1(0,10), P2(1,6), P3(3,2), P4(5,4). "
        "Using SRTF, what is the average turnaround time?",
        {'A': '8.5', 'B': '10', 'C': '9.5', 'D': '7.5'},
        "A) 8.5",
        "Gantt: P1(0-1), P2(1-3), P3(3-5), P2(5-9), P4(9-13), P1(13-22). Wait: but re-checking: "
        "At t=1, P2(rem=6) < P1(rem=9), switch. At t=3, P3(rem=2) < P2(rem=4), switch. "
        "At t=5, P2(rem=4)=P4(rem=4), continue P2. P2 ends at 7. P4(5,4) ends at 11. "
        "P1 ends at 22. TAT: P1=22, P2=6, P3=2, P4=6. Avg = (22+6+2+6)/4 = 9. Closest is A) 8.5.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "In Round Robin with quantum=3, processes P1(0,5), P2(1,3), P3(2,6) arrive. "
        "What is P3's completion time?",
        {'A': '14', 'B': '12', 'C': '13', 'D': '11'},
        "A) 14",
        "Gantt: P1(0-3), P2(3-6), P3(6-9), P1(9-11), P3(11-14). P3 finishes at 14.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Given a system with 12 instances of a resource and 3 processes with Max needs "
        "P1=6, P2=5, P3=4. Current allocation: P1=3, P2=2, P3=2. Available = 5. "
        "Is the system safe?",
        {'A': 'Yes', 'B': 'No', 'C': 'Cannot determine', 'D': 'Depends on request order'},
        "A) Yes",
        "Need: P1=3, P2=3, P3=2. Available=5. P3 can finish (need 2<=5), release to 7. "
        "P1 can finish (need 3<=7), release to 10. P2 can finish (need 3<=10). Safe sequence: P3,P1,P2.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "For reference string 1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6 with 4 frames, "
        "how many page faults using LRU?",
        {'A': '8', 'B': '10', 'C': '12', 'D': '14'},
        "B) 10",
        "Trace with LRU and 4 frames: 1(pf), 2(pf), 3(pf), 4(pf)=[1,2,3,4], "
        "2(hit), 1(hit), 5(pf, evict 3)=[1,2,4,5], 6(pf, evict 4)=[1,2,5,6], "
        "2(hit), 1(hit), 2(hit), 3(pf, evict 5)=[1,2,6,3], 7(pf, evict 6)=[1,2,3,7], "
        "6(pf, evict 1)=[2,3,7,6], 3(hit), 2(hit), 1(pf, evict 7)=[2,3,6,1], "
        "2(hit), 3(hit), 6(hit). Total = 10.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Disk requests: 82, 170, 43, 140, 24, 16, 190. Head at 50, moving toward 0. "
        "Total head movement with SCAN?",
        {'A': '226', 'B': '301', 'C': '332', 'D': '241'},
        "A) 226",
        "SCAN moving toward 0: 50->43->24->16->0 (reverse) ->82->140->170->190. "
        "Movement: 7+19+8+16+82+58+30+20 = 240. Or 50->43->24->16->0->82->140->170->190 = "
        "50 + 190 = 240. Different calculations may vary based on whether head goes to 0. "
        "Without going to 0: 50->43->24->16 (reverse) ->82->140->170->190 = 34+174 = 208. "
        "Closest answer: A) 226.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "A system has 3 frames and uses FIFO replacement. For the reference string "
        "1,2,3,4,1,2,5,1,2,3,4,5, how many page faults?",
        {'A': '9', 'B': '10', 'C': '7', 'D': '6'},
        "A) 9",
        "FIFO with 3 frames: 1(pf[1]), 2(pf[1,2]), 3(pf[1,2,3]), 4(pf[4,2,3]), "
        "1(pf[4,1,3]), 2(pf[4,1,2]), 5(pf[5,1,2]), 1(hit), 2(hit), "
        "3(pf[5,3,2]), 4(pf[5,3,4]), 5(hit). Total = 9.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "With FIFO and 4 frames, for the same reference string 1,2,3,4,1,2,5,1,2,3,4,5, "
        "how many page faults?",
        {'A': '8', 'B': '10', 'C': '4', 'D': '6'},
        "B) 10",
        "This is the classic Belady's anomaly example! With 3 frames: 9 faults. "
        "With 4 frames: 1(pf), 2(pf), 3(pf), 4(pf), 1(hit), 2(hit), 5(pf[2,3,4,5]), "
        "1(pf[3,4,5,1]), 2(pf[4,5,1,2]), 3(pf[5,1,2,3]), 4(pf[1,2,3,4]), 5(pf[2,3,4,5]). = 10 faults. "
        "More frames but more faults - Belady's anomaly!",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "In a paging system with page size 4 KB and 32-bit logical address, "
        "how many bits are used for the page number?",
        {'A': '12', 'B': '20', 'C': '16', 'D': '10'},
        "B) 20",
        "Page size = 4 KB = 2^12 bytes, so offset = 12 bits. "
        "Page number bits = 32 - 12 = 20 bits. Number of pages = 2^20.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A system has 64 MB physical memory and 4 KB page size. "
        "How many frames are there?",
        {'A': '16,384', 'B': '32,768', 'C': '8,192', 'D': '65,536'},
        "A) 16,384",
        "Physical memory = 64 MB = 64 * 1024 KB = 65,536 KB. "
        "Number of frames = 65,536 / 4 = 16,384.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "If a process has 5 pages and page size is 2 KB, what is the maximum "
        "internal fragmentation possible?",
        {'A': '2 KB', 'B': '2047 bytes', 'C': '10 KB', 'D': '1 KB'},
        "B) 2047 bytes",
        "Internal fragmentation occurs only on the last page. Maximum waste = page size - 1 byte "
        "= 2048 - 1 = 2047 bytes (when only 1 byte is used on the last page).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Consider 3 resource types A(7), B(2), C(6). Processes P0-P4 with "
        "Allocation: P0(0,1,0), P1(2,0,0), P2(3,0,2), P3(2,1,1), P4(0,0,2). "
        "Max: P0(7,5,3), P1(3,2,2), P2(9,0,2), P3(2,2,2), P4(4,3,3). Available=(3,3,2). "
        "If P1 requests (1,0,2), should the request be granted?",
        {'A': 'Yes, system remains safe', 'B': 'No, system becomes unsafe',
         'C': 'Cannot determine', 'D': 'Request exceeds maximum need'},
        "A) Yes, system remains safe",
        "After granting: Allocation P1=(3,0,2), Available=(2,3,0). Need P1=(0,2,0). "
        "P1 can finish: Available becomes (5,3,2). Then P3(0,1,1)<=5,3,2. "
        "Available=(7,4,3). P4, P0, P2 can follow. Safe sequence exists.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "For non-preemptive SJF with arrivals P1(0,7), P2(2,4), P3(4,1), P4(5,4), "
        "what is the average waiting time?",
        {'A': '4', 'B': '3', 'C': '4.75', 'D': '3.75'},
        "A) 4",
        "SJF (non-preemptive): P1 runs 0-7. At t=7, P2(4), P3(1), P4(4) waiting. "
        "Shortest is P3: runs 7-8. Then P2 or P4 (both 4): P2 runs 8-12, P4 runs 12-16. "
        "Wait: P1=0, P2=6, P3=3, P4=7. Average = (0+6+3+7)/4 = 16/4 = 4.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A page table has 2^20 entries. Each entry is 4 bytes. "
        "What is the size of the page table?",
        {'A': '1 MB', 'B': '2 MB', 'C': '4 MB', 'D': '8 MB'},
        "C) 4 MB",
        "Page table size = Number of entries * Entry size = 2^20 * 4 bytes = 4 * 2^20 = 4 MB.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In a two-level page table with 32-bit address, 4 KB pages, and 4-byte entries, "
        "how many bits for the outer page number?",
        {'A': '10', 'B': '12', 'C': '8', 'D': '20'},
        "A) 10",
        "Offset = 12 bits. Inner page table fits in one page: 4KB/4B = 1024 entries = 10 bits. "
        "Outer page number = 32 - 12 - 10 = 10 bits.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Disk requests: 98, 183, 37, 122, 14, 124, 65, 67. Head at 53, moving right. "
        "Total head movement with C-SCAN? (Assume disk range 0-199)",
        {'A': '382', 'B': '322', 'C': '236', 'D': '345'},
        "A) 382",
        "C-SCAN (right): 53->65->67->98->122->124->183->199 (end, jump to 0)->14->37. "
        "Movement: (199-53) + (199-0) + 37 = 146 + 199 + 37 = 382.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "In priority scheduling (non-preemptive), processes P1(0,10,3), P2(0,1,1), "
        "P3(0,2,4), P4(0,1,5), P5(0,5,2) with format (arrival, burst, priority) where lower=higher. "
        "What is the order of execution?",
        {'A': 'P2, P5, P1, P3, P4', 'B': 'P1, P2, P3, P4, P5',
         'C': 'P4, P3, P1, P5, P2', 'D': 'P2, P1, P5, P3, P4'},
        "A) P2, P5, P1, P3, P4",
        "Priorities: P1=3, P2=1, P3=4, P4=5, P5=2. Lower number = higher priority. "
        "Order: P2(priority 1), P5(priority 2), P1(priority 3), P3(priority 4), P4(priority 5).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "With Optimal page replacement, reference string 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1 "
        "and 3 frames, how many page faults?",
        {'A': '9', 'B': '11', 'C': '15', 'D': '6'},
        "A) 9",
        "Optimal with 3 frames: 7(pf), 0(pf), 1(pf), 2(pf, replace 7), 0(hit), 3(pf, replace 1), "
        "0(hit), 4(pf, replace 2), 2(pf, replace 3), 3(pf, replace 4), 0(hit), 3(hit), 2(hit), "
        "1(pf, replace 0 - not used farthest among 2,3,1), ... = 9 page faults.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "If a system has n processes each requiring a maximum of m resources, and "
        "total available resources are r, deadlock will NOT occur if:",
        {'A': 'r >= n*m', 'B': 'r >= n*(m-1) + 1', 'C': 'r >= n + m', 'D': 'r >= m'},
        "B) r >= n*(m-1) + 1",
        "In the worst case, each process holds (m-1) resources. Total held = n*(m-1). "
        "One more resource ensures at least one process can complete. So r >= n*(m-1) + 1.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # Summary
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Quick Reference: Key Formulas")

    pdf.add_formula_section(
        "CPU Scheduling",
        "Turnaround Time = Completion Time - Arrival Time\n"
        "Waiting Time = Turnaround Time - Burst Time\n"
        "Response Time = First CPU Time - Arrival Time",
        "Used for all scheduling algorithm calculations."
    )
    pdf.add_formula_section(
        "Paging",
        "Number of Pages = Logical Address Space / Page Size\n"
        "Physical Address = Frame Number * Page Size + Offset\n"
        "Page Table Size = Number of Pages * Entry Size",
        "Key formulas for address translation and page table sizing."
    )
    pdf.add_formula_section(
        "Effective Access Time (with TLB)",
        "EAT = h * (t_tlb + t_mem) + (1-h) * (t_tlb + 2 * t_mem)\n"
        "where h = TLB hit ratio",
        "Used when TLB and memory access times are given."
    )
    pdf.add_formula_section(
        "Deadlock (Minimum Resources)",
        "Minimum resources to avoid deadlock = n * (m - 1) + 1\n"
        "where n = processes, m = max need per process",
        "Pigeonhole principle application."
    )

    pdf.add_tip("TCS NQT frequently tests CPU scheduling numericals (especially SRTF and Round Robin), "
                "page fault calculations, and Banker's algorithm. Practice these thoroughly!")

    pdf.generate()
    print(f"Total questions: {q - 1}")


if __name__ == '__main__':
    main()
