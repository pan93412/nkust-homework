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
