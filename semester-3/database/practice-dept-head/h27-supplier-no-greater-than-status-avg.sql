-- 找出狀態值在平均以上的供應商號碼

select s_no
from s
where status between
    (select avg(status) from s)
    and (select max(status) from s)
