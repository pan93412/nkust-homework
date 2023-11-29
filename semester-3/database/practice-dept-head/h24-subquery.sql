-- 取得有供應零件P2 的供應商的名字
select sname
from s
where s_no in (select s_no
               from sp
               where p_no = 'P2')
