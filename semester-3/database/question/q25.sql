-- 統計 2018 年各班各種假別的總數，產出缺曠課統計表

select
    students.ClassNo,
    sum(records.Absent),
    sum(records.Leave),
    sum(records.PublicLeave),
    sum(records.SickLeave)
from students join (records) using (ClassNo)
where records.YMD between '2018-01-01' and '2018-12-31'
group by students.ClassNo;