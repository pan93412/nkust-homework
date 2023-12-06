-- 列出所有客戶的訂單編號資料 (inner join)

select *
from customers inner join (orders) using (c_id);