# Write your MySQL query statement below
WITH DailySum AS (
    SELECT 
        visited_on, 
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
RollingMetrics AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(AVG(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount,
        -- Generate a row number based on date to easily filter out the first 6 incomplete days
        ROW_NUMBER() OVER (ORDER BY visited_on) AS day_num
    FROM DailySum
)
SELECT 
    visited_on, 
    amount, 
    average_amount
FROM RollingMetrics
WHERE day_num >= 7
ORDER BY visited_on ASC;
