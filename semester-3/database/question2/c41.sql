select DeptName as 部門名稱, EmpName as 姓名, MonthSalary as 月薪
from dept
         join (employee) using (DeptId)
where EmpId not in (select distinct EmpId
                    from leav
                    where leav.Year = 2018)
   or EmpId not in (select distinct EmpId
                    from overtime
                    where OverDate between '2018-01-01' and '2018-12-31')
order by 部門名稱, 月薪 desc, 姓名