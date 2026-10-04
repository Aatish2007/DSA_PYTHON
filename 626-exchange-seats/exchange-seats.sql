# Write your MySQL query statement below
SELECT 
    id,
    CASE 
        -- If ID is odd and there is a next student, take the next student
        WHEN id % 2 != 0 AND LEAD(student) OVER (ORDER BY id) IS NOT NULL 
            THEN LEAD(student) OVER (ORDER BY id)
        -- If ID is odd and it's the last student (no next student), keep the current student
        WHEN id % 2 != 0 AND LEAD(student) OVER (ORDER BY id) IS NULL 
            THEN student
        -- If ID is even, take the previous student
        ELSE LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat;
