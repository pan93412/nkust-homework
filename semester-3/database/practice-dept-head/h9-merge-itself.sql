select first.s_no AS 供應商1, second.s_no AS 供應商2
from s first,
     s second
where first.city = second.city
  and first.s_no <> second.s_no
