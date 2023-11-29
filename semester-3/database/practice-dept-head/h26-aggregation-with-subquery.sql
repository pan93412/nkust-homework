-- 取得狀態值大於目前S表中平均狀態值的供應商之供應商號碼

select s_no
from s
where status < (select avg(status) from s)
