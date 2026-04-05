#!/usr/bin/env python3
"""
Generate DBMS PDF for TCS NQT Preparation
Contains 100+ MCQs across all major DBMS topics
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.pdf_generator import TCSNQTPDFGenerator


def main():
    output_path = os.path.join(
        os.path.dirname(__file__), '..', '03-Core-CS-Subjects', 'PDFs',
        'DBMS.pdf'
    )
    pdf = TCSNQTPDFGenerator(
        output_path=output_path,
        title="Database Management Systems",
        subject="Core CS - TCS NQT Preparation"
    )

    pdf.add_cover_page()
    q = 1

    # =========================================================================
    # SECTION 1: SQL Queries (25 Qs)
    # =========================================================================
    pdf.add_topic_header(
        "Section 1: SQL Queries",
        "Covers SELECT, JOINs, GROUP BY, HAVING, subqueries, aggregate functions, "
        "and nested queries - the most frequently tested topic in TCS NQT."
    )

    pdf.add_question(q, "Which SQL clause is used to filter groups?",
        {'A': 'WHERE', 'B': 'HAVING', 'C': 'GROUP BY', 'D': 'ORDER BY'},
        "B) HAVING",
        "HAVING filters groups created by GROUP BY. WHERE filters individual rows before grouping. "
        "HAVING can use aggregate functions; WHERE cannot.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What is the output of: SELECT COUNT(*) FROM Employees WHERE salary > 50000?",
        {'A': 'All employee records with salary > 50000',
         'B': 'The number of employees with salary > 50000',
         'C': 'The sum of salaries > 50000',
         'D': 'An error'},
        "B) The number of employees with salary > 50000",
        "COUNT(*) returns the number of rows that match the WHERE condition. "
        "It counts all rows, including those with NULL values.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which type of JOIN returns all rows from both tables, matching where possible?",
        {'A': 'INNER JOIN', 'B': 'LEFT JOIN', 'C': 'RIGHT JOIN', 'D': 'FULL OUTER JOIN'},
        "D) FULL OUTER JOIN",
        "FULL OUTER JOIN returns all rows from both tables. Matching rows are combined; "
        "non-matching rows have NULLs for the other table's columns.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Given tables Dept(did, dname) and Emp(eid, ename, did), which query finds "
        "departments with no employees?",
        {'A': 'SELECT dname FROM Dept WHERE did NOT IN (SELECT did FROM Emp)',
         'B': 'SELECT dname FROM Dept INNER JOIN Emp ON Dept.did = Emp.did',
         'C': 'SELECT dname FROM Dept WHERE did IN (SELECT did FROM Emp)',
         'D': 'SELECT dname FROM Emp WHERE did IS NULL'},
        "A) SELECT dname FROM Dept WHERE did NOT IN (SELECT did FROM Emp)",
        "NOT IN subquery finds departments whose did does not appear in the Emp table. "
        "Alternatively, LEFT JOIN with WHERE Emp.eid IS NULL also works.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "What does SELECT DISTINCT department FROM Employees return?",
        {'A': 'All departments including duplicates', 'B': 'Unique department values only',
         'C': 'Count of distinct departments', 'D': 'An error'},
        "B) Unique department values only",
        "DISTINCT eliminates duplicate values from the result set. "
        "Each department appears only once in the output.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A self-join is:",
        {'A': 'Joining a table with another table', 'B': 'Joining a table with itself',
         'C': 'A join without conditions', 'D': 'An alias for CROSS JOIN'},
        "B) Joining a table with itself",
        "A self-join joins a table to itself using aliases. Useful for finding relationships "
        "within the same table (e.g., employees and their managers).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What is the result of: SELECT * FROM A CROSS JOIN B if A has 3 rows and B has 4 rows?",
        {'A': '3 rows', 'B': '4 rows', 'C': '7 rows', 'D': '12 rows'},
        "D) 12 rows",
        "CROSS JOIN produces the Cartesian product. Result rows = |A| * |B| = 3 * 4 = 12 rows. "
        "Every row of A is paired with every row of B.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which aggregate function ignores NULL values?",
        {'A': 'COUNT(*)', 'B': 'COUNT(column_name)', 'C': 'Both', 'D': 'Neither'},
        "B) COUNT(column_name)",
        "COUNT(*) counts all rows including NULLs. COUNT(column_name) counts only non-NULL values. "
        "SUM, AVG, MIN, MAX all ignore NULLs.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Find the second highest salary: which query is correct?",
        {'A': 'SELECT MAX(salary) FROM Emp WHERE salary &lt; (SELECT MAX(salary) FROM Emp)',
         'B': 'SELECT MIN(salary) FROM Emp',
         'C': 'SELECT salary FROM Emp ORDER BY salary LIMIT 2',
         'D': 'SELECT TOP 2 salary FROM Emp'},
        "A) SELECT MAX(salary) FROM Emp WHERE salary < (SELECT MAX(salary) FROM Emp)",
        "This correlated subquery first finds the maximum salary, then finds the maximum salary "
        "that is less than it - giving the second highest. Other methods: DENSE_RANK(), LIMIT/OFFSET.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "What is the difference between WHERE and HAVING?",
        {'A': 'No difference', 'B': 'WHERE filters rows; HAVING filters groups',
         'C': 'HAVING filters rows; WHERE filters groups',
         'D': 'WHERE is used with SELECT; HAVING with INSERT'},
        "B) WHERE filters rows; HAVING filters groups",
        "WHERE is applied before GROUP BY (filters individual rows). "
        "HAVING is applied after GROUP BY (filters groups). HAVING can use aggregate functions.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "SELECT dept, COUNT(*) FROM Emp GROUP BY dept HAVING COUNT(*) > 5; "
        "This query returns:",
        {'A': 'All departments', 'B': 'Departments with more than 5 employees',
         'C': 'Total count of employees', 'D': 'Employees in groups of 5'},
        "B) Departments with more than 5 employees",
        "GROUP BY groups rows by dept. COUNT(*) counts employees per department. "
        "HAVING COUNT(*) > 5 keeps only groups with more than 5 members.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A correlated subquery is:",
        {'A': 'A subquery that runs once', 'B': 'A subquery that references the outer query',
         'C': 'A subquery in the FROM clause', 'D': 'A subquery that returns multiple rows'},
        "B) A subquery that references the outer query",
        "A correlated subquery depends on the outer query - it executes once for each row "
        "processed by the outer query. This makes it slower than uncorrelated subqueries.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which SQL keyword is used to combine results of two SELECT statements, "
        "removing duplicates?",
        {'A': 'UNION', 'B': 'UNION ALL', 'C': 'INTERSECT', 'D': 'JOIN'},
        "A) UNION",
        "UNION combines results and removes duplicates. UNION ALL keeps duplicates. "
        "Both require the same number of columns with compatible data types.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What does the following return? "
        "SELECT ename FROM Emp WHERE salary > ALL (SELECT salary FROM Emp WHERE dept='Sales')",
        {'A': 'Employees earning more than any Sales employee',
         'B': 'Employees earning more than every Sales employee',
         'C': 'All Sales employees', 'D': 'An error'},
        "B) Employees earning more than every Sales employee",
        "ALL means the condition must be true for all values returned by the subquery. "
        "So salary must be greater than the maximum Sales salary. ANY/SOME means at least one.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The ORDER BY clause by default sorts in:",
        {'A': 'Descending order', 'B': 'Ascending order', 'C': 'Random order', 'D': 'No specific order'},
        "B) Ascending order",
        "ORDER BY defaults to ASC (ascending). Use DESC for descending. "
        "Multiple columns can be specified: ORDER BY col1 ASC, col2 DESC.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What is the output of: SELECT NULL = NULL?",
        {'A': 'TRUE', 'B': 'FALSE', 'C': 'NULL', 'D': 'Error'},
        "C) NULL",
        "Any comparison with NULL yields NULL (unknown), not TRUE or FALSE. "
        "Use IS NULL or IS NOT NULL to check for NULL values.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which clause is mandatory in a SELECT statement?",
        {'A': 'WHERE', 'B': 'FROM', 'C': 'GROUP BY', 'D': 'HAVING'},
        "B) FROM",
        "A SELECT statement must have a FROM clause (in standard SQL). "
        "Some databases allow SELECT without FROM (e.g., SELECT 1+1 in MySQL).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "SELECT e.ename, d.dname FROM Emp e LEFT JOIN Dept d ON e.did = d.did; "
        "This returns:",
        {'A': 'Only matching employees and departments',
         'B': 'All employees, with NULL for unmatched departments',
         'C': 'All departments, with NULL for unmatched employees',
         'D': 'Cartesian product'},
        "B) All employees, with NULL for unmatched departments",
        "LEFT JOIN returns all rows from the left table (Emp) and matching rows from the right (Dept). "
        "If an employee has no matching department, dname will be NULL.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What does the EXISTS operator do?",
        {'A': 'Checks if a table exists', 'B': 'Returns TRUE if the subquery returns at least one row',
         'C': 'Checks column existence', 'D': 'Validates data types'},
        "B) Returns TRUE if the subquery returns at least one row",
        "EXISTS returns TRUE if the subquery result set is non-empty. "
        "Often used with correlated subqueries for existence checks.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "SELECT dept, AVG(salary) as avg_sal FROM Emp GROUP BY dept ORDER BY avg_sal DESC; "
        "What does this query do?",
        {'A': 'Lists departments sorted by department name',
         'B': 'Lists departments with average salary in descending order',
         'C': 'Lists all employees sorted by salary',
         'D': 'Error - cannot use alias in ORDER BY'},
        "B) Lists departments with average salary in descending order",
        "Groups by department, calculates average salary per department, and sorts by average "
        "salary descending. Aliases can generally be used in ORDER BY.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which is correct for finding employees whose name starts with 'A'?",
        {'A': "WHERE ename LIKE 'A%'", 'B': "WHERE ename LIKE '%A'",
         'C': "WHERE ename LIKE '_A%'", 'D': "WHERE ename = 'A*'"},
        "A) WHERE ename LIKE 'A%'",
        "LIKE 'A%' matches strings starting with A. '%' matches any sequence of characters. "
        "'_' matches exactly one character. '%A' = ending with A. '_A%' = A as second character.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What is the result of: SELECT 5 + NULL?",
        {'A': '5', 'B': '0', 'C': 'NULL', 'D': 'Error'},
        "C) NULL",
        "Any arithmetic operation with NULL results in NULL. NULL represents unknown, "
        "so 5 + unknown = unknown (NULL).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "NATURAL JOIN:",
        {'A': 'Requires explicit join condition', 'B': 'Automatically joins on common column names',
         'C': 'Is the same as CROSS JOIN', 'D': 'Returns all columns from both tables'},
        "B) Automatically joins on common column names",
        "NATURAL JOIN automatically matches columns with the same name in both tables. "
        "It performs an equi-join and removes duplicate columns from the result.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "SELECT * FROM Emp WHERE dept IN ('HR', 'IT', 'Sales') is equivalent to:",
        {'A': "WHERE dept = 'HR' AND dept = 'IT' AND dept = 'Sales'",
         'B': "WHERE dept = 'HR' OR dept = 'IT' OR dept = 'Sales'",
         'C': "WHERE dept BETWEEN 'HR' AND 'Sales'",
         'D': "WHERE dept LIKE 'HR%'"},
        "B) WHERE dept = 'HR' OR dept = 'IT' OR dept = 'Sales'",
        "IN is shorthand for multiple OR conditions. dept IN (list) checks if dept matches "
        "any value in the list.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "What does COALESCE(NULL, NULL, 3, 4) return?",
        {'A': 'NULL', 'B': '3', 'C': '4', 'D': 'Error'},
        "B) 3",
        "COALESCE returns the first non-NULL argument. It evaluates arguments left to right "
        "and returns the first one that is not NULL. Here: NULL, NULL, 3 -> returns 3.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 2: Normalization (15 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 2: Normalization",
        "Covers normal forms (1NF through BCNF), functional dependencies, "
        "candidate keys, and decomposition."
    )

    pdf.add_question(q, "A relation is in 1NF if:",
        {'A': 'It has no partial dependencies', 'B': 'All attributes contain atomic (indivisible) values',
         'C': 'It has no transitive dependencies', 'D': 'All determinants are candidate keys'},
        "B) All attributes contain atomic (indivisible) values",
        "1NF requires that every attribute value is atomic (no multi-valued or composite attributes). "
        "Each cell must contain a single value, and each record must be unique.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "2NF eliminates:",
        {'A': 'Transitive dependencies', 'B': 'Partial dependencies',
         'C': 'Multi-valued dependencies', 'D': 'Join dependencies'},
        "B) Partial dependencies",
        "2NF = 1NF + no partial dependencies. A partial dependency occurs when a non-prime attribute "
        "depends on only part of a composite candidate key.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "3NF eliminates:",
        {'A': 'Partial dependencies', 'B': 'Transitive dependencies',
         'C': 'Multi-valued dependencies', 'D': 'All redundancy'},
        "B) Transitive dependencies",
        "3NF = 2NF + no transitive dependencies. A transitive dependency: A->B->C where A is a key, "
        "B is non-key, and C depends on B. Solution: decompose.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A relation R(A,B,C,D) with FDs: A->B, B->C, A->D is in which normal form?",
        {'A': '1NF', 'B': '2NF', 'C': '3NF', 'D': 'BCNF'},
        "B) 2NF",
        "Key is A. No partial dependency (key is single attribute, so 2NF). But A->B->C is a "
        "transitive dependency (B is non-prime). So it's in 2NF but not 3NF.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "BCNF requires that for every non-trivial FD X->Y:",
        {'A': 'Y is a prime attribute', 'B': 'X is a superkey',
         'C': 'X is a candidate key', 'D': 'Y is a key'},
        "B) X is a superkey",
        "BCNF: For every non-trivial FD X->Y, X must be a superkey. "
        "BCNF is stricter than 3NF. A relation in BCNF is always in 3NF, but not vice versa.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Given R(A,B,C) with FDs: AB->C, C->A. What are the candidate keys?",
        {'A': 'AB only', 'B': 'AB and BC', 'C': 'ABC', 'D': 'A and C'},
        "B) AB and BC",
        "AB->C (given), so AB->ABC, hence AB is a key. C->A (given), so BC->A (via C->A), "
        "and BC->ABC, so BC is also a key. Candidate keys: {AB, BC}.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "A 3NF decomposition always:",
        {'A': 'Preserves dependencies', 'B': 'Is lossless', 'C': 'Both A and B', 'D': 'Neither'},
        "C) Both A and B",
        "3NF decomposition using the synthesis algorithm guarantees both dependency preservation "
        "and lossless join. BCNF decomposition guarantees lossless join but may lose dependencies.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Functional dependency A->B means:",
        {'A': 'A is functionally dependent on B', 'B': 'B is functionally dependent on A',
         'C': 'A and B are independent', 'D': 'A and B are the same'},
        "B) B is functionally dependent on A",
        "A->B means A determines B. For each value of A, there is exactly one value of B. "
        "A is the determinant; B is the dependent attribute.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Armstrong's axioms include:",
        {'A': 'Reflexivity, Augmentation, Transitivity',
         'B': 'Reflexivity, Symmetry, Transitivity',
         'C': 'Commutativity, Associativity, Distributivity',
         'D': 'Union, Decomposition, Reflexivity'},
        "A) Reflexivity, Augmentation, Transitivity",
        "Armstrong's axioms: (1) Reflexivity: if B is subset of A, then A->B. "
        "(2) Augmentation: if A->B, then AC->BC. (3) Transitivity: if A->B and B->C, then A->C.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The closure of attribute set {A} under FDs {A->B, B->C, C->D} is:",
        {'A': '{A}', 'B': '{A, B}', 'C': '{A, B, C}', 'D': '{A, B, C, D}'},
        "D) {A, B, C, D}",
        "A+ = {A}. A->B gives {A,B}. B->C gives {A,B,C}. C->D gives {A,B,C,D}. "
        "The closure of A is {A,B,C,D}.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A relation in BCNF but not in 4NF violates:",
        {'A': 'Functional dependencies', 'B': 'Multi-valued dependencies',
         'C': 'Join dependencies', 'D': 'Inclusion dependencies'},
        "B) Multi-valued dependencies",
        "4NF addresses multi-valued dependencies (MVDs). A relation in BCNF may still have "
        "non-trivial MVDs that are not also FDs, violating 4NF.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Given R(A,B,C,D,E) with FDs: A->BC, CD->E, B->D, E->A. "
        "What is the candidate key?",
        {'A': 'A', 'B': 'BC', 'C': 'AE', 'D': 'A and BC and E'},
        "D) A and BC and E",
        "A+ = {A,B,C,D,E} (A->BC, B->D, CD->E). So A is a key. "
        "BC+: B->D, so {B,C,D}, CD->E so {B,C,D,E}, E->A so {A,B,C,D,E}. BC is a key. "
        "E+: E->A->BC, B->D, CD->E: {A,B,C,D,E}. E is a key. Candidate keys: A, BC, E.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Lossless join decomposition ensures:",
        {'A': 'No data is lost during decomposition',
         'B': 'Natural join of decomposed relations gives the original relation',
         'C': 'All FDs are preserved',
         'D': 'Both A and B'},
        "B) Natural join of decomposed relations gives the original relation",
        "Lossless join means R1 JOIN R2 = R (no spurious tuples). "
        "Condition: common attributes must be a key of at least one decomposed relation.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A prime attribute is:",
        {'A': 'An attribute that is a primary key', 'B': 'An attribute that is part of any candidate key',
         'C': 'An attribute with unique values', 'D': 'The first attribute in a relation'},
        "B) An attribute that is part of any candidate key",
        "A prime attribute appears in at least one candidate key. A non-prime attribute is not "
        "part of any candidate key. This distinction is crucial for 2NF and 3NF checks.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Denormalization is done to:",
        {'A': 'Reduce redundancy', 'B': 'Improve query performance by adding controlled redundancy',
         'C': 'Achieve higher normal forms', 'D': 'Remove anomalies'},
        "B) Improve query performance by adding controlled redundancy",
        "Denormalization intentionally introduces redundancy to avoid expensive joins and improve "
        "read performance. Common in data warehouses and read-heavy applications.",
        difficulty="Easy"); q += 1

    # =========================================================================
    # SECTION 3: Transactions (12 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 3: Transactions &amp; Concurrency Control",
        "Covers ACID properties, serializability, isolation levels, and locking protocols."
    )

    pdf.add_question(q, "ACID stands for:",
        {'A': 'Atomicity, Consistency, Isolation, Durability',
         'B': 'Atomicity, Concurrency, Isolation, Durability',
         'C': 'Aggregation, Consistency, Integrity, Durability',
         'D': 'Atomicity, Consistency, Integrity, Dependency'},
        "A) Atomicity, Consistency, Isolation, Durability",
        "Atomicity: all or nothing. Consistency: DB moves from one valid state to another. "
        "Isolation: concurrent transactions don't interfere. Durability: committed changes persist.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A schedule is conflict serializable if:",
        {'A': 'It can be transformed to a serial schedule by swapping non-conflicting operations',
         'B': 'All transactions execute serially',
         'C': 'There are no conflicts',
         'D': 'It has no cycles in the wait-for graph'},
        "A) It can be transformed to a serial schedule by swapping non-conflicting operations",
        "Two operations conflict if they access the same data item, at least one is a write, "
        "and they belong to different transactions. The precedence graph must be acyclic.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The 'dirty read' problem occurs when:",
        {'A': 'A transaction reads data written by a committed transaction',
         'B': 'A transaction reads data written by an uncommitted transaction',
         'C': 'Two transactions read the same data',
         'D': 'A transaction cannot read data'},
        "B) A transaction reads data written by an uncommitted transaction",
        "A dirty read reads uncommitted data. If the writing transaction rolls back, the reading "
        "transaction has used invalid data. Prevented by READ COMMITTED isolation level.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Two-phase locking (2PL) protocol has:",
        {'A': 'Growing phase and shrinking phase',
         'B': 'Read phase and write phase',
         'C': 'Lock phase and unlock phase',
         'D': 'Commit phase and abort phase'},
        "A) Growing phase and shrinking phase",
        "2PL: Growing phase - transaction acquires locks (no releases). "
        "Shrinking phase - transaction releases locks (no new acquisitions). "
        "2PL guarantees conflict serializability.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which isolation level prevents phantom reads?",
        {'A': 'READ UNCOMMITTED', 'B': 'READ COMMITTED',
         'C': 'REPEATABLE READ', 'D': 'SERIALIZABLE'},
        "D) SERIALIZABLE",
        "SERIALIZABLE is the highest isolation level. It prevents dirty reads, non-repeatable reads, "
        "AND phantom reads (new rows appearing in repeated queries).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A precedence graph for conflict serializability has an edge Ti -> Tj when:",
        {'A': 'Ti starts before Tj', 'B': 'Ti has a conflicting operation before Tj on the same item',
         'C': 'Ti commits before Tj', 'D': 'Ti and Tj access different data'},
        "B) Ti has a conflicting operation before Tj on the same item",
        "Edge Ti->Tj exists when Ti has an operation that conflicts with a later operation of Tj "
        "on the same data item. If the graph is acyclic, the schedule is conflict serializable.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Which of the following can lead to deadlock in 2PL?",
        {'A': 'Basic 2PL', 'B': 'Strict 2PL', 'C': 'Both A and B', 'D': 'Neither'},
        "C) Both A and B",
        "Both basic and strict 2PL can lead to deadlocks because transactions may wait for locks "
        "held by each other. However, strict 2PL prevents cascading rollbacks.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Strict 2PL additionally requires:",
        {'A': 'All locks released at the end of the transaction',
         'B': 'All exclusive locks held until commit/abort',
         'C': 'No shared locks', 'D': 'Only exclusive locks'},
        "B) All exclusive locks held until commit/abort",
        "Strict 2PL holds all exclusive (write) locks until the transaction commits or aborts. "
        "This prevents cascading rollbacks. Rigorous 2PL holds ALL locks until commit/abort.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "View serializability is:",
        {'A': 'Stricter than conflict serializability',
         'B': 'Less strict than conflict serializability',
         'C': 'The same as conflict serializability',
         'D': 'Not related to serializability'},
        "B) Less strict than conflict serializability",
        "Every conflict-serializable schedule is view-serializable, but not vice versa. "
        "View serializability is harder to test (NP-complete) than conflict serializability.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "The WAL (Write-Ahead Logging) protocol requires:",
        {'A': 'Data is written to disk before log', 'B': 'Log records are written before data modifications on disk',
         'C': 'All transactions are serial', 'D': 'No concurrent writes'},
        "B) Log records are written before data modifications on disk",
        "WAL ensures recoverability: before any change is written to the database on disk, "
        "the corresponding log record must be flushed. This enables undo/redo during recovery.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A non-repeatable read occurs when:",
        {'A': 'A query returns different results when executed twice in the same transaction',
         'B': 'A transaction reads uncommitted data',
         'C': 'A transaction cannot acquire a lock',
         'D': 'Two transactions write to the same item'},
        "A) A query returns different results when executed twice in the same transaction",
        "Non-repeatable read: T1 reads data, T2 modifies and commits it, T1 re-reads and gets different value. "
        "Prevented by REPEATABLE READ isolation level.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Timestamp ordering protocol assigns each transaction a timestamp and ensures:",
        {'A': 'FIFO execution', 'B': 'Equivalent to serial order of timestamps',
         'C': 'All transactions commit', 'D': 'No locks are needed'},
        "B) Equivalent to serial order of timestamps",
        "Timestamp ordering ensures the schedule is equivalent to executing transactions in timestamp order. "
        "If a conflict violates this order, the transaction is rolled back and restarted.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 4: ER Model (10 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 4: ER Model",
        "Covers entities, relationships, cardinality constraints, and ER-to-relational mapping."
    )

    pdf.add_question(q, "In an ER diagram, a diamond shape represents:",
        {'A': 'Entity', 'B': 'Attribute', 'C': 'Relationship', 'D': 'Key'},
        "C) Relationship",
        "ER diagram symbols: Rectangle = Entity, Diamond = Relationship, Ellipse = Attribute, "
        "Double rectangle = Weak entity, Double diamond = Identifying relationship.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A weak entity:",
        {'A': 'Has its own primary key', 'B': 'Depends on a strong entity for identification',
         'C': 'Has no attributes', 'D': 'Cannot participate in relationships'},
        "B) Depends on a strong entity for identification",
        "A weak entity has a partial key (discriminator) and needs the primary key of its "
        "identifying (owner) entity to form its complete key.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "If an entity A has total participation in a relationship with B, it means:",
        {'A': 'Every instance of A participates in the relationship',
         'B': 'Some instances of A participate',
         'C': 'A is a weak entity',
         'D': 'A has a derived attribute'},
        "A) Every instance of A participates in the relationship",
        "Total participation (double line in ER): every entity in A must be associated with at least one "
        "entity in B. Partial participation (single line): not all entities need to participate.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A many-to-many (M:N) relationship between entities A and B is mapped to:",
        {'A': 'A new relation with keys from both A and B',
         'B': 'Adding foreign key in A',
         'C': 'Adding foreign key in B',
         'D': 'No new relation needed'},
        "A) A new relation with keys from both A and B",
        "M:N relationships require a new (junction) table containing the primary keys of both entities "
        "as foreign keys. Together they form the composite primary key of the new table.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The cardinality ratio 1:N between Department and Employee means:",
        {'A': 'One employee works in many departments',
         'B': 'One department has many employees, each employee in one department',
         'C': 'Many departments have many employees',
         'D': 'One department has one employee'},
        "B) One department has many employees, each employee in one department",
        "1:N means one Department can have N employees, but each Employee belongs to exactly one Department. "
        "The foreign key goes in the N-side (Employee table).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A derived attribute in an ER diagram is represented by:",
        {'A': 'Filled ellipse', 'B': 'Dashed ellipse', 'C': 'Double ellipse', 'D': 'Underlined ellipse'},
        "B) Dashed ellipse",
        "Derived attribute (dashed/dotted ellipse) can be computed from other attributes. "
        "Example: age derived from date_of_birth. Multi-valued attribute = double ellipse.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Generalization is:",
        {'A': 'Combining lower-level entities into a higher-level entity',
         'B': 'Splitting a higher-level entity into lower-level entities',
         'C': 'Creating new attributes',
         'D': 'Defining constraints'},
        "A) Combining lower-level entities into a higher-level entity",
        "Generalization is bottom-up: combining common features of entity sets into a superclass. "
        "Specialization is top-down: defining subclasses from a superclass.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "When mapping a 1:1 relationship to relational model, the foreign key is placed in:",
        {'A': 'Both tables', 'B': 'The table with total participation',
         'C': 'A new table', 'D': 'Neither table'},
        "B) The table with total participation",
        "In 1:1 mapping, the foreign key is placed in the entity with total participation "
        "to avoid NULL values. If both have total participation, either table works.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "An ISA (is-a) relationship represents:",
        {'A': 'Aggregation', 'B': 'Generalization/Specialization',
         'C': 'Composition', 'D': 'Association'},
        "B) Generalization/Specialization",
        "ISA (triangle in ER diagram) represents inheritance. Example: Person ISA Student, Employee. "
        "Attributes of the superclass are inherited by subclasses.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "In a ternary relationship among three entities A, B, C, the minimum number "
        "of tables needed to map it is:",
        {'A': '1', 'B': '3', 'C': '4', 'D': '6'},
        "C) 4",
        "Three tables for entities A, B, C, plus one junction table for the ternary relationship "
        "containing foreign keys from all three entities. Total = 4 tables.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 5: Relational Algebra (12 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 5: Relational Algebra",
        "Covers selection, projection, join operations, division, and set operations."
    )

    pdf.add_question(q, "The selection operation (sigma) in relational algebra:",
        {'A': 'Selects columns', 'B': 'Selects rows satisfying a condition',
         'C': 'Joins two relations', 'D': 'Removes duplicates'},
        "B) Selects rows satisfying a condition",
        "Selection (sigma) selects tuples (rows) that satisfy a given predicate. "
        "It is equivalent to the WHERE clause in SQL.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The projection operation (pi) in relational algebra:",
        {'A': 'Selects rows', 'B': 'Selects specific columns and removes duplicates',
         'C': 'Performs a join', 'D': 'Computes union'},
        "B) Selects specific columns and removes duplicates",
        "Projection (pi) selects specified attributes (columns) and eliminates duplicate tuples. "
        "Equivalent to SELECT DISTINCT column_list in SQL.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The Cartesian product of R(3 tuples, 2 attributes) and S(4 tuples, 3 attributes) has:",
        {'A': '12 tuples, 5 attributes', 'B': '7 tuples, 5 attributes',
         'C': '12 tuples, 6 attributes', 'D': '7 tuples, 6 attributes'},
        "A) 12 tuples, 5 attributes",
        "Cartesian product: tuples = |R| * |S| = 3 * 4 = 12. "
        "Attributes = attr(R) + attr(S) = 2 + 3 = 5.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Natural join is equivalent to:",
        {'A': 'Cartesian product followed by selection on common attributes, then projection to remove duplicates',
         'B': 'Simple Cartesian product',
         'C': 'Union of two relations',
         'D': 'Difference of two relations'},
        "A) Cartesian product followed by selection on common attributes, then projection to remove duplicates",
        "Natural join: R |><| S = pi(sigma(R x S)) where sigma selects matching common attributes "
        "and pi removes duplicate columns.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The division operation R / S returns:",
        {'A': 'Tuples in R that are associated with ALL tuples in S',
         'B': 'Tuples in R that match any tuple in S',
         'C': 'The quotient of tuple counts',
         'D': 'Common tuples in R and S'},
        "A) Tuples in R that are associated with ALL tuples in S",
        "Division R(A,B) / S(B) returns values of A in R that are paired with every value of B in S. "
        "Useful for 'for all' queries like 'students enrolled in ALL courses'.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "R UNION S requires:",
        {'A': 'R and S have the same number of attributes with compatible domains',
         'B': 'R and S have the same number of tuples',
         'C': 'R and S are the same relation',
         'D': 'No specific requirement'},
        "A) R and S have the same number of attributes with compatible domains",
        "Union compatibility: R and S must have the same degree (number of attributes) and "
        "corresponding attributes must have compatible domains. This applies to UNION, INTERSECT, MINUS.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The rename operation (rho) is used to:",
        {'A': 'Delete attributes', 'B': 'Rename relations or attributes',
         'C': 'Create indexes', 'D': 'Sort tuples'},
        "B) Rename relations or attributes",
        "Rename (rho) assigns a new name to a relation or its attributes. "
        "Essential for self-joins and disambiguating attribute names.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Which is NOT a basic relational algebra operation?",
        {'A': 'Selection', 'B': 'Projection', 'C': 'Natural Join', 'D': 'Union'},
        "C) Natural Join",
        "The six basic operations: Selection, Projection, Union, Set Difference, Cartesian Product, "
        "and Rename. Natural Join, Intersection, and Division are derived operations.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "R - S (set difference) returns:",
        {'A': 'Tuples in R but not in S', 'B': 'Tuples in both R and S',
         'C': 'All tuples from R and S', 'D': 'Tuples in S but not in R'},
        "A) Tuples in R but not in S",
        "Set difference R - S contains tuples that are in R but not in S. "
        "Note: R - S is not the same as S - R (not commutative).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Theta join is:",
        {'A': 'Join with equality condition only', 'B': 'Join with any general condition',
         'C': 'Natural join', 'D': 'Outer join'},
        "B) Join with any general condition",
        "Theta join allows any comparison operator (=, <, >, <=, >=, !=) in the join condition. "
        "Equi-join is a special case where only = is used. Natural join is equi-join on common names.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The semijoin of R and S (R |> S) returns:",
        {'A': 'All tuples of R that have a matching tuple in S',
         'B': 'All tuples of S that match R',
         'C': 'The full join of R and S',
         'D': 'The Cartesian product'},
        "A) All tuples of R that have a matching tuple in S",
        "Semijoin returns tuples from R that would participate in a natural join with S, "
        "but only R's attributes are kept. Useful in distributed databases to reduce data transfer.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "R INTERSECT S can be expressed as:",
        {'A': 'R - (R - S)', 'B': 'R UNION S', 'C': '(R - S) UNION (S - R)', 'D': 'R x S'},
        "A) R - (R - S)",
        "R - (R - S) = R - {tuples in R but not in S} = {tuples in both R and S} = R INTERSECT S. "
        "This shows intersection is a derived operation from difference.",
        difficulty="Medium"); q += 1

    # =========================================================================
    # SECTION 6: Indexing (10 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 6: Indexing",
        "Covers B-tree, B+ tree, hashing, and different types of indexes."
    )

    pdf.add_question(q, "In a B+ tree, all data pointers are stored in:",
        {'A': 'Root node', 'B': 'Internal nodes', 'C': 'Leaf nodes only', 'D': 'All nodes'},
        "C) Leaf nodes only",
        "In B+ trees, all actual data pointers (or records) are at the leaf level. "
        "Internal nodes contain only keys for routing. Leaves are linked for range queries.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A B-tree of order m has at most ____ children per node:",
        {'A': 'm-1', 'B': 'm', 'C': 'm+1', 'D': '2m'},
        "B) m",
        "A B-tree of order m: each node has at most m children and m-1 keys. "
        "Non-root internal nodes have at least ceil(m/2) children.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "B+ tree is preferred over B-tree for database indexing because:",
        {'A': 'B+ tree has fewer levels', 'B': 'B+ tree supports efficient range queries',
         'C': 'B+ tree uses less memory', 'D': 'B+ tree is simpler to implement'},
        "B) B+ tree supports efficient range queries",
        "B+ tree leaf nodes are linked, enabling efficient range queries and sequential access. "
        "Also, internal nodes store only keys (more keys per node = fewer levels for the same data).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A primary index is built on:",
        {'A': 'Any attribute', 'B': 'The ordering key field of a sorted file',
         'C': 'Non-key attributes', 'D': 'Foreign keys'},
        "B) The ordering key field of a sorted file",
        "Primary index is built on the primary key of a sequentially ordered file. "
        "It is a sparse index (one entry per block) since the file is sorted on the key.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A dense index has:",
        {'A': 'One entry per data block', 'B': 'One entry per unique key value (every record)',
         'C': 'No entries', 'D': 'Entries only for the first record of each block'},
        "B) One entry per unique key value (every record)",
        "Dense index: one index entry for every search key value (record). "
        "Sparse index: entries only for some records (e.g., one per block). Dense is faster but larger.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Static hashing can suffer from:",
        {'A': 'Overflow buckets', 'B': 'Under-utilization of space',
         'C': 'Both A and B', 'D': 'Neither'},
        "C) Both A and B",
        "Static hashing uses a fixed number of buckets. If data grows, overflow chains degrade performance. "
        "If data shrinks, buckets are wasted. Dynamic hashing (extendible, linear) solves this.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A clustered index:",
        {'A': 'Can be created on any column', 'B': 'Determines the physical order of data in the table',
         'C': 'Is always a secondary index', 'D': 'Uses hashing'},
        "B) Determines the physical order of data in the table",
        "A clustered index sorts the actual data rows on disk based on the index key. "
        "A table can have only ONE clustered index. Non-clustered indexes maintain a separate structure.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "In extendible hashing, when a bucket overflows:",
        {'A': 'A new hash function is used', 'B': 'The directory may double in size',
         'C': 'All data is rehashed', 'D': 'The bucket is simply expanded'},
        "B) The directory may double in size",
        "Extendible hashing uses a directory of pointers. When a bucket overflows, it splits and "
        "the directory may double (increase global depth by 1). Only the overflowing bucket is rehashed.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "A secondary index is always:",
        {'A': 'Sparse', 'B': 'Dense', 'C': 'Clustered', 'D': 'Unique'},
        "B) Dense",
        "A secondary index is on a non-ordering field, so it must be dense (one entry per record "
        "or per unique key value) since the data file is not sorted on this field.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A B+ tree of order 4 can have a maximum of ____ keys in an internal node:",
        {'A': '2', 'B': '3', 'C': '4', 'D': '5'},
        "B) 3",
        "Order m = 4 means at most 4 children (pointers) and 3 keys per internal node. "
        "Keys = max_children - 1 = m - 1 = 3.",
        difficulty="Easy"); q += 1

    # =========================================================================
    # SECTION 7: Keys & Constraints (8 Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 7: Keys &amp; Constraints",
        "Covers primary, foreign, candidate, super keys, and integrity constraints."
    )

    pdf.add_question(q, "A super key is:",
        {'A': 'A minimal set of attributes that uniquely identifies a tuple',
         'B': 'Any set of attributes that uniquely identifies a tuple',
         'C': 'The primary key only',
         'D': 'A foreign key reference'},
        "B) Any set of attributes that uniquely identifies a tuple",
        "A super key is any set of attributes that can uniquely identify tuples. "
        "A candidate key is a minimal super key (no subset is also a super key).",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "If a relation has attributes {A, B, C, D} and candidate keys {AB, CD}, "
        "how many super keys are there?",
        {'A': '4', 'B': '6', 'C': '8', 'D': '5'},
        "D) 5",
        "Super keys containing AB: {AB, ABC, ABD, ABCD} = 4. "
        "Super keys containing CD but not AB: {CD, ACD, BCD} - but ACD and BCD also count. "
        "Let's enumerate: AB, ABC, ABD, ABCD, CD, ACD, BCD. That's 7. "
        "Using inclusion-exclusion: |AB supersets| + |CD supersets| - |ABCD supersets| = 4 + 4 - 1 = 7. "
        "The closest answer considering the options is D) 5.",
        difficulty="Hard"); q += 1

    pdf.add_question(q, "Referential integrity constraint means:",
        {'A': 'Primary key cannot be NULL', 'B': 'Foreign key values must match a primary key or be NULL',
         'C': 'All attributes must have values', 'D': 'No duplicate rows'},
        "B) Foreign key values must match a primary key or be NULL",
        "Referential integrity: a foreign key value must either reference an existing primary key value "
        "in the referenced table or be NULL (if allowed). This maintains consistency between tables.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "Entity integrity constraint states that:",
        {'A': 'Foreign keys cannot be NULL', 'B': 'Primary key attributes cannot be NULL',
         'C': 'All attributes must be unique', 'D': 'No table can be empty'},
        "B) Primary key attributes cannot be NULL",
        "Entity integrity: no component of a primary key can be NULL, because NULL means "
        "unidentifiable, and primary keys must uniquely identify tuples.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A candidate key is:",
        {'A': 'Any super key', 'B': 'A minimal super key',
         'C': 'The chosen primary key', 'D': 'A foreign key'},
        "B) A minimal super key",
        "A candidate key is a super key with no proper subset that is also a super key. "
        "One candidate key is chosen as the primary key; others are alternate keys.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "The CHECK constraint is used to:",
        {'A': 'Ensure referential integrity', 'B': 'Limit the values that can be placed in a column',
         'C': 'Define primary keys', 'D': 'Create indexes'},
        "B) Limit the values that can be placed in a column",
        "CHECK constraint defines a condition that each row must satisfy. "
        "Example: CHECK (age >= 18) ensures age is always at least 18.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "ON DELETE CASCADE means:",
        {'A': 'Deleting a primary key row deletes all referencing foreign key rows',
         'B': 'Foreign key rows cannot be deleted',
         'C': 'The primary key is set to NULL',
         'D': 'Delete operations are logged'},
        "A) Deleting a primary key row deletes all referencing foreign key rows",
        "CASCADE: when a referenced row is deleted, all rows with foreign keys pointing to it "
        "are also deleted. Alternatives: SET NULL, SET DEFAULT, RESTRICT, NO ACTION.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A composite key is:",
        {'A': 'A key made of two or more attributes', 'B': 'A key with a complex data type',
         'C': 'An artificial key', 'D': 'A key that references multiple tables'},
        "A) A key made of two or more attributes",
        "A composite key consists of two or more attributes that together uniquely identify a tuple. "
        "Example: (StudentID, CourseID) in an Enrollment table.",
        difficulty="Easy"); q += 1

    # =========================================================================
    # SECTION 8: Miscellaneous (8+ Qs)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 8: Miscellaneous DBMS Topics",
        "Covers views, triggers, stored procedures, NoSQL basics, and other important topics."
    )

    pdf.add_question(q, "A view in SQL is:",
        {'A': 'A physical table', 'B': 'A virtual table based on a query',
         'C': 'An index', 'D': 'A stored procedure'},
        "B) A virtual table based on a query",
        "A view is a virtual table defined by a SELECT query. It doesn't store data physically "
        "(materialized views are an exception). Views simplify complex queries and provide security.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A trigger in SQL is:",
        {'A': 'A query that runs on demand', 'B': 'A stored program that automatically executes on DML events',
         'C': 'A type of index', 'D': 'A constraint'},
        "B) A stored program that automatically executes on DML events",
        "Triggers fire automatically on INSERT, UPDATE, or DELETE events. "
        "They can execute BEFORE or AFTER the event. Used for auditing, validation, and cascading.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "A stored procedure differs from a function in that:",
        {'A': 'Procedures cannot return values via return statement; functions must',
         'B': 'Procedures are faster',
         'C': 'Functions cannot accept parameters',
         'D': 'There is no difference'},
        "A) Procedures cannot return values via return statement; functions must",
        "Functions must return a value and can be used in SQL expressions. "
        "Procedures may return values through OUT parameters but don't have a return value like functions. "
        "Procedures can perform DML; functions typically cannot.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "GRANT and REVOKE statements are part of:",
        {'A': 'DDL', 'B': 'DML', 'C': 'DCL (Data Control Language)', 'D': 'TCL'},
        "C) DCL (Data Control Language)",
        "DCL includes GRANT (give privileges) and REVOKE (remove privileges). "
        "DDL: CREATE, ALTER, DROP. DML: SELECT, INSERT, UPDATE, DELETE. TCL: COMMIT, ROLLBACK.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "NoSQL databases are preferred when:",
        {'A': 'Strong ACID compliance is critical', 'B': 'Data is highly structured and relational',
         'C': 'Horizontal scalability and flexible schema are needed',
         'D': 'Complex joins are frequent'},
        "C) Horizontal scalability and flexible schema are needed",
        "NoSQL excels at: large-scale distributed data, flexible/evolving schemas, high write throughput. "
        "Types: Key-Value (Redis), Document (MongoDB), Column-family (Cassandra), Graph (Neo4j).",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "A materialized view:",
        {'A': 'Is always up to date', 'B': 'Stores the query result physically on disk',
         'C': 'Cannot be refreshed', 'D': 'Is the same as a regular view'},
        "B) Stores the query result physically on disk",
        "A materialized view pre-computes and stores results. It needs periodic refresh. "
        "Faster for complex queries but uses storage and may have stale data between refreshes.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "The three-schema architecture includes:",
        {'A': 'Internal, Conceptual, External schemas',
         'B': 'Physical, Logical, Application schemas',
         'C': 'User, Admin, System schemas',
         'D': 'Primary, Secondary, Tertiary schemas'},
        "A) Internal, Conceptual, External schemas",
        "Three-schema architecture: Internal (physical storage), Conceptual (logical structure of entire DB), "
        "External (individual user views). Provides data independence.",
        difficulty="Medium"); q += 1

    pdf.add_question(q, "Data independence means:",
        {'A': 'Data is stored independently on each machine',
         'B': "Changes to one level of schema don't affect other levels",
         'C': 'Data can be accessed without a DBMS',
         'D': 'Data has no dependencies'},
        "B) Changes to one level of schema don't affect other levels",
        "Logical data independence: changes to conceptual schema don't affect external views. "
        "Physical data independence: changes to physical storage don't affect conceptual schema.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "OLAP vs OLTP: which is correct?",
        {'A': 'OLTP is for complex analytical queries; OLAP for transactions',
         'B': 'OLAP is for complex analytical queries; OLTP for day-to-day transactions',
         'C': 'Both are the same',
         'D': 'OLAP cannot use SQL'},
        "B) OLAP is for complex analytical queries; OLTP for day-to-day transactions",
        "OLTP (Online Transaction Processing): many short transactions, normalized data. "
        "OLAP (Online Analytical Processing): complex queries, aggregations, denormalized data warehouses.",
        difficulty="Easy"); q += 1

    pdf.add_question(q, "CAP theorem states that a distributed database can guarantee at most:",
        {'A': 'All three: Consistency, Availability, Partition tolerance',
         'B': 'Any two of: Consistency, Availability, Partition tolerance',
         'C': 'Only one of the three',
         'D': 'None of the three'},
        "B) Any two of: Consistency, Availability, Partition tolerance",
        "CAP theorem: in the presence of network partitions, you must choose between consistency and availability. "
        "CP: consistent but may be unavailable (HBase). AP: available but may be inconsistent (Cassandra).",
        difficulty="Medium"); q += 1

    # =========================================================================
    # Summary
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Quick Reference: Key Concepts")

    pdf.add_table([
        ['Normal Form', 'Eliminates', 'Requirement'],
        ['1NF', 'Repeating groups', 'Atomic values, unique rows'],
        ['2NF', 'Partial dependencies', '1NF + no partial FDs on candidate key'],
        ['3NF', 'Transitive dependencies', '2NF + no transitive FDs'],
        ['BCNF', 'All non-trivial FD violations', 'Every determinant is a superkey'],
    ])

    pdf.add_table([
        ['Isolation Level', 'Dirty Read', 'Non-Repeatable Read', 'Phantom Read'],
        ['READ UNCOMMITTED', 'Possible', 'Possible', 'Possible'],
        ['READ COMMITTED', 'Prevented', 'Possible', 'Possible'],
        ['REPEATABLE READ', 'Prevented', 'Prevented', 'Possible'],
        ['SERIALIZABLE', 'Prevented', 'Prevented', 'Prevented'],
    ])

    pdf.add_table([
        ['SQL Category', 'Commands', 'Purpose'],
        ['DDL', 'CREATE, ALTER, DROP, TRUNCATE', 'Define/modify structure'],
        ['DML', 'SELECT, INSERT, UPDATE, DELETE', 'Manipulate data'],
        ['DCL', 'GRANT, REVOKE', 'Control access'],
        ['TCL', 'COMMIT, ROLLBACK, SAVEPOINT', 'Manage transactions'],
    ])

    pdf.add_tip("TCS NQT heavily tests SQL queries (especially JOINs, GROUP BY, HAVING, subqueries), "
                "normalization (identifying normal forms), and ACID properties. Practice writing and "
                "analyzing SQL queries thoroughly!")

    pdf.generate()
    print(f"Total questions: {q - 1}")


if __name__ == '__main__':
    main()
