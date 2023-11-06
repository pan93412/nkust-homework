SELECT dept.DeptName AS '部門名稱',
       employee.EmpName AS '姓名',
       employee.JobTitle AS '現任職稱',
       employee.MonthSalary AS '目前月薪資',
       sum(overtime.OverHours) AS '加班時數總計',
       sum(MonthSalary / 224 * 1.5 * overtime.OverHours) AS '加班費'
FROM dept
         INNER JOIN (employee, overtime)
                    ON (
                                dept.DeptId = employee.DeptId AND
                                employee.EmpId = overtime.EmpId
                    )
WHERE overtime.OverDate BETWEEN '2018-01-01' AND '2018-12-31'
  AND dept.DeptName LIKE '%研發%'
GROUP BY dept.DeptName, employee.EmpName, employee.JobTitle, employee.MonthSalary
ORDER BY DeptName,
         MonthSalary DESC;
