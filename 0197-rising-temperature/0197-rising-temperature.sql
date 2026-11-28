# Write your MySQL query statement below
with final as (select 
*,
DATEDIFF(recordDate,lag(recordDate)over()) as rn1,
lag(temperature) over() as rn2
from Weather
order by recordDate )
select id
from final 
where rn1 = 1 and temperature > rn2