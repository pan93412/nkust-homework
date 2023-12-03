-- 取得和供應商S1在同一個城市之供應商的供應商號碼

select s_no
from s
where city = (select city from s where s_no = 'S1');