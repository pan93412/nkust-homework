-- 列出月薪高於業務部門最高月薪的員工，列出其部門名稱
-- 姓名 目前月薪資。將輸出結果以部門別遞增排序，同一部門者
-- 則依月薪遞減排序

select DeptName as 部門名稱, EmpName as 姓名, MonthSalary as 目前月薪資
from dept join (employee) using (DeptId)
where MonthSalary > (
    select max(MonthSalary)
    from dept join (employee) using (DeptId)
    where DeptName like '業務%'
    )
order by DeptName, MonthSalary desc;