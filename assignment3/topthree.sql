SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    Department d
    JOIN Employee e ON d.id = e.departmentId
WHERE
    e.salary IN (
        SELECT DISTINCT salary
        FROM Employee e2
        WHERE e2.departmentId = d.id
        ORDER BY salary DESC
        LIMIT 3
    )
ORDER BY
    Department, Salary DESC;


-- postgres