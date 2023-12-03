-- 取得不供應零件P2 的供應商的名字 (SQL減法)
select sname
from s
where s_no not in (select s_no
                   from sp
                   where p_no = 'P2')
