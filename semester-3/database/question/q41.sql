-- 對於2018年6,7,8月沒有請假的員工，列出部門名稱、姓名與其6,7,8月加班費總計(無加班紀錄者以空白顯示)
-- 欄位名稱顯示為: 部門名稱,姓名,加班費總計，並依部門名稱、姓名排序

select DeptName as 部門名稱, EmpName as 姓名, sum(MonthSalary / 224 * 1.5 * OverHours) as 加班費統計
from dept
         join employee using (DeptId)
         left join overtime on (employee.EmpId = overtime.EmpId and
                                OverDate between '2018-06-01' and '2018-08-31')
where employee.EmpId not in
      (select e.EmpId
       from employee e
                join (leav) on (e.EmpId = leav.EmpID and Year = 2018 and Month in (6, 7, 8))
       group by EmpId)
group by DeptName, EmpName
order by 部門名稱, 姓名;

SELECT dept.DeptName as 部門名稱, employee.EmpName as 姓名, 加班費總計
FROM dept,
     employee
         left JOIN(SELECT employee.EmpId, monthsalary / 224 * 1.5 * overhours as 加班費總計
                   FROM employee,
                        overtime
                   WHERE employee.EmpId = overtime.EmpId
                     AND month(overdate) in (6, 7, 8)
                     AND year(overdate) = 2018) A1 on employee.EmpId = A1.empid
WHERE employee.EmpId not in (SELECT leav.EmpID FROM leav WHERE month in (6, 7, 8) AND year = 2018)
ORDER BY dept.DeptName, employee.EmpName;