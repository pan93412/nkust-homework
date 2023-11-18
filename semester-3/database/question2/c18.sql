-- 列出2018年研發部門之部門名稱,姓名,現任職稱,目前月薪資,加班合計與加班費合計
-- ，將輸出結果以部門別遞增排序，同一部門者則依月薪遞減排序

select
    DeptName as 部門名稱,
    EmpName as 姓名,
    JobTitle as 現任職稱,
    MonthSalary as 目前月薪資,
    sum(OverHours) as 加班合計,
    sum(MonthSalary/224*1.5*OverHours) as 加班費合計
from dept   join employee using (DeptId)
            join overtime using (EmpId)
where OverDate between '2018-01-01' and '2018-12-31'
        and DeptName like '研發%'
group by 部門名稱, 姓名, 現任職稱, 目前月薪資
order by 部門名稱, 目前月薪資 desc;