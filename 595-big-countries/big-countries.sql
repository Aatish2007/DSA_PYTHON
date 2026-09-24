# Write your MySQL query statement below
select name,population,area from World
where area>=3000000 or population>=25000000
#we can use UNION but we have to write area and poulation in different block 
