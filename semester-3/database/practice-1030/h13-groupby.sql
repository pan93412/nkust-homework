select s_no, p_no, sum(qty)
from sp
group by s_no, p_no
