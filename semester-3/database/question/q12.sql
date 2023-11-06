-- 列出 2019 年業務部門員工請假天數的總和
-- 依請假天數遞減排序，請假天數相同者，請以員工姓名遞增排序

select
    DeptName        as 部門名稱,
    EmpName         as 姓名,
    sum(leav.Days)  as 請假天數的總和
from dept   join (employee) using (DeptId)
            join (leav) using (EmpId)
where       leav.Year = 2019 and
            DeptName like '業務%'
group by    DeptName, EmpName
order by    請假天數的總和 desc, 姓名;