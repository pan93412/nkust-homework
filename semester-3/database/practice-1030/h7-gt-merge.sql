-- 取出所有供應商及零件的詳細組合，其中供應商城市的字母順序在零件的城市之後

select s.*, p.*
from s, p
where s.city > p.city
