-- 統計 2018 年各班各種假別的總數，產出缺曠課統計表

select
    left(students.ClassNo, 3) as 班級,
    sum(records.Leave) as 事假總計,
    sum(records.SickLeave) as 病假總計,
    sum(records.PublicLeave) as 公假總計,
    sum(records.Absent) as 曠課總計
from students join (records) using (ClassNo)
where records.YMD between '2018-01-01' and '2018-12-31'
group by 班級;
