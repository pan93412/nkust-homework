select DeptName                  as 部門名稱,
       ifnull(sum(TotalDays), 0) as 請假天數,
       ifnull(sum(TotalOverHours), 0) as 加班時數
from dept
         join (employee e) on (dept.DeptId = e.DeptId)
         left join (
             SELECT EmpId, SUM(OverHours) as TotalOverHours
             FROM overtime
             WHERE OverDate between '2018-01-01' and '2018-12-31'
             GROUP BY EmpId
        ) ot using (EmpId)
       left join (
             SELECT EmpId, SUM(leav.Days) as TotalDays
             FROM leav
             WHERE Year = 2018
             GROUP BY EmpId
        ) leav using (EmpId)
group by DeptName
order by 部門名稱
