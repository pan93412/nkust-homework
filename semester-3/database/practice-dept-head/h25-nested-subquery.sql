-- 列出有產品來源是 Paris 的供應商

select s.sname
from s
where s_no in (select s_no
               from sp
               where p_no in (select p_no
                              from p
                              where p.city = 'Paris'))
