# Write your MySQL query statement below
select prod.product_name, sal.year, sal.price
from Product prod 
join Sales sal 
on sal.product_id=prod.product_id;