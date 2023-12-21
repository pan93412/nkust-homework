-- 列出2018年度每個部門的加班時數總計與請假天數總計(無請假或加班紀錄者以空白或NULL顯示)
-- 列出部門名稱、請假天數與加班時數。並依部門名稱排序

select DeptName                  as 部門名稱,
       ifnull(sum(OverHours), 0) as 加班時數總計,
       ifnull(sum(leav.Days), 0) as 請假天數合計
from dept
         join (employee e) on (dept.ManagerEmpId = e.EmpId)
         left join (overtime ot) on (e.EmpId = ot.EmpId and ot.OverDate between '2018-01-01' and '2018-12-31')
         left join (leav) on (e.EmpId = leav.EmpID and leav.Year = 2018)
group by DeptName
order by 部門名稱
