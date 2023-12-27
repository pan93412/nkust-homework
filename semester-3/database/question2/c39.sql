select DeptName as 部門名稱, EmpName as 姓名, MonthSalary as 目前月薪資
from dept join (employee) using (DeptId)
where MonthSalary > (
    select max(MonthSalary)
    from dept join (employee) using (DeptId)
    where DeptName like '業務%'
    )
order by DeptName, MonthSalary desc;