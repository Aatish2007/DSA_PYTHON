# Write your MySQL query statement below
select round(count(DISTINCT player_id)/(select count(distinct player_id)from Activity),2) as fraction
FROM Activity
where(player_id,DATE_SUB(event_date,Interval 1 day)) in (
    select player_id,min(event_date)as first_login
    from Activity 
    group by player_id
)