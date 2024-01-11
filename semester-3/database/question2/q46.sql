SELECT dept.DeptName as 部門名稱, employee.EmpName as 姓名, 加班費總計
FROM dept,
     employee
         left JOIN(SELECT employee.EmpId, monthsalary / 224 * 1.5 * overhours as 加班費總計
                   FROM employee,
                        overtime
                   WHERE employee.EmpId = overtime.EmpId
                     AND month(overdate) in (6, 7, 8)
                     AND year(overdate) = 2018) A1 on employee.EmpId = A1.empid
WHERE employee.DeptId = dept.DeptId
  AND employee.EmpId not in (SELECT leav.EmpID FROM leav WHERE month in (6, 7, 8) AND year = 2018)
ORDER BY dept.DeptName, employee.EmpName;
