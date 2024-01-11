select DeptName                  as 部門名稱,
       EmpName                   as 姓名,
       ifnull(sum(OverHours), 0) as 加班時數合計,
       ifnull(sum(distinct leav.Days), 0) as 請假天數合計
from dept
         join (employee e) on (dept.ManagerEmpId = e.EmpId)
         left join (overtime ot) on (e.EmpId = ot.EmpId and ot.OverDate between '2018-01-01' and '2018-12-31')
         left join (leav) on (e.EmpId = leav.EmpID and leav.Year = 2018)
group by DeptName, EmpName
order by 部門名稱
