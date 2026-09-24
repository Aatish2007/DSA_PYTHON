# Write your MySQL query statement below
SELECT name FROM customer
WHERE referee_id is NULL OR referee_id!=2
#where IFNULL (referee_id,0)<>2-----METHOD @2