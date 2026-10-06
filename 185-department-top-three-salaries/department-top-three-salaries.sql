# Write your MySQL query statement below
SELECT 
    Department, 
    Employee, 
    Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM Employee e
    INNER JOIN Department d ON e.departmentId = d.id
) AS ranked_table
WHERE salary_rank <= 3;
