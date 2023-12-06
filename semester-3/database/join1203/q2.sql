-- 列出所有客戶的訂單編號資料 (left join)

select *
from customers left join (orders) using (c_id);