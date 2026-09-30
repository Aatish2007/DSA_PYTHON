# Write your MySQL query statement below
select 
    product_id,
    year as first_year,
    quantity,
    price
FROM Sales
where(product_id,year)in (
    select product_id,min(year) as f_year
    from Sales
    group by product_id
)