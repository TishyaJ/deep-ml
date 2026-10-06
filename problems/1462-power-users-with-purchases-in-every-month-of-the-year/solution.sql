-- your query
with year as (
    select 
        user_id, 
        month(purchase_date) as pm
    from purchases
    where purchase_date>='2024-01-01' and purchase_date<'2025-01-01'
    group by 
        user_id,
        month(purchase_date)
    having count(purchase_id)>=2
)
select user_id
from year
group by user_id
having count(pm)=12
order by user_id;