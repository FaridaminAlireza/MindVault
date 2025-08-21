
-- Employees with salary records
SELECT e.name, s.salary
FROM employees e
INNER JOIN salaries s
ON e.id = s.emp_id;


-- left join 
SELECT a.id, a.name, b.salary
FROM employees a
LEFT JOIN salaries b
ON a.id = b.emp_id;


-- Even though LEFT JOIN should return all left table rows,
-- the WHERE clause filtered out the NULLs.
SELECT e.name, s.salary
FROM employees e
LEFT JOIN salaries s
ON e.id = s.emp_id
WHERE s.salary > 60000;

-- Now LEFT JOIN behavior is preserved — 
-- all employees are included, even if the salary condition fails.
SELECT e.name, s.salary
FROM employees e
LEFT JOIN salaries s
ON e.id = s.emp_id AND s.salary > 60000;



-- Employees with no salary record
SELECT e.name
FROM employees e
LEFT JOIN salaries s
ON e.id = s.emp_id
WHERE s.salary IS NULL;


-- GROUP BY and having
SELECT dept, COUNT(*) as num_employees, AVG(salary) as avg_salary
FROM employees e
LEFT JOIN salaries s
ON e.id = s.emp_id
GROUP BY dept
HAVING AVG(salary) > 60000;

SELECT DISTINCT dept FROM employees;


SELECT name, salary
FROM employees e
LEFT JOIN salaries s ON e.id = s.emp_id
ORDER BY salary DESC;

SELECT * FROM employees ORDER BY id LIMIT 5 OFFSET 10;


-- Subquery
-- Employees with salary above company average
SELECT name
FROM employees e
JOIN salaries s ON e.id = s.emp_id
WHERE s.salary > (SELECT AVG(salary) FROM salaries);

-- COALESCE Handle NULLs
SELECT name, COALESCE(salary, 0) as salary
FROM employees e
LEFT JOIN salaries s ON e.id = s.emp_id;

-- Conditional logic in SELECT
SELECT name, salary,
       CASE 
         WHEN salary >= 70000 THEN 'High'
         WHEN salary >= 50000 THEN 'Medium'
         ELSE 'Low'
       END as salary_level
FROM employees e
LEFT JOIN salaries s ON e.id = s.emp_id;


-- What is a WITH Statement / CTE?
-- CTE = Common Table Expression
CTE = Common Table Expression
WITH avg_salary AS (
    SELECT AVG(salary) AS avg_sal
    FROM salaries
)
SELECT e.name, s.salary
FROM employees e
JOIN salaries s ON e.id = s.emp_id
JOIN avg_salary a ON 1=1
WHERE s.salary > a.avg_sal;

--Many think the first reference to cte is materialized and reused.
-- Reality: In most SQL engines, a CTE is not materialized by default 
-- — it’s inlined into each query.
-- Each reference is re-evaluated separately, so the query inside the CTE runs
-- each time it’s referenced.


--If the CTE query is expensive, referencing it multiple times can be inefficient.
-- Use temporary tables if you want to compute once and reuse:
-- Temp table = materialized once, reused efficiently.

CREATE TEMP TABLE temp_salaries AS
SELECT * FROM salaries;

SELECT COUNT(*) FROM temp_salaries;
SELECT AVG(salary) FROM temp_salaries;

-- Seq Scan on employees  (cost=0.00..12.50 rows=5 width=50)
--   Filter: (salary > 50000)
-- Seq Scan → full table scan
-- cost=0.00..12.50 → estimated startup cost..total cost
-- rows=5 → estimated number of rows returned



-- EXPLAIN shows how PostgreSQL plans to execute a query.

-- It does not execute the query by default (unless you use EXPLAIN ANALYZE).
--Provides information like:
--Which scan type is used (Seq Scan, Index Scan, etc.)
--Estimated cost
--Estimated rows
--Join algorithms (Nested Loop, Hash Join, Merge Join)
--EXPLAIN SELECT * FROM employees WHERE salary > 50000;

-- If you want real execution statistics, use:
EXPLAIN ANALYZE SELECT * FROM employees WHERE salary > 50000;


-- EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
-- SELECT * FROM employees WHERE salary > 50000;

