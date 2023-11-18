-- 統計 2018 年各班各種假別的總數，產出缺曠課統計表

select
    students.ClassNo as 班別,
    sum(records.Absent) as 曠課,
    sum(records.Leave) as 事假,
    sum(records.PublicLeave) as 公假,
    sum(records.SickLeave) as 病假
from students join (records) using (ClassNo)
where records.YMD between '2018-01-01' and '2018-12-31'
group by students.ClassNo;
