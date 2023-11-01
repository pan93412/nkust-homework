-- 取出所有由一個以上的供應商所供應的零件之零件號碼

select p_no
from sp
group by p_no
having count(*) > 1;

select distinct p_no, count(*) over (partition by p_no)
from sp;