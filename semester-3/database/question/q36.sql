-- 列出 2018 年不曾請過假且不曾加過班的員工，
-- 列出其部門名稱 姓名 目前月薪資，將輸出結果以部門別遞增排序，
-- 同一部門者則依月薪遞減排序

select DeptName as 部門名稱, EmpName as 姓名, MonthSalary as 目前月薪資
from dept
         join (employee) using (DeptId)
where EmpId not in (select distinct EmpId
                    from leav
                    where leav.Year = 2018)
   or EmpId not in (select distinct EmpId
                    from overtime
                    where OverDate between '2018-01-01' and '2018-12-31')
