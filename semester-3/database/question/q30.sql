-- 對於 2018 年總加班時數 5 小時以上 含五小時 的員工
-- 列出其部門名稱 姓名 現任職稱 目前月薪資 總加班時數，
-- 依部門名稱遞增排序，同部門則依總加班時數遞減排序

select
    DeptName as 部門名稱,
    EmpName as 姓名,
    JobTitle as 現任職稱,
    MonthSalary as 目前月薪資,
    sum(OverHours) as 總加班時數
from dept   join (employee) using (DeptId)
            join (overtime) using (EmpId)
where OverDate between '2018-01-01' and '2018-12-31'
group by DeptName, EmpName, JobTitle, MonthSalary
having 總加班時數 >= 5
order by DeptName, 總加班時數 desc;
