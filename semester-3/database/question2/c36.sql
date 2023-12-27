SELECT
    DeptName AS 部門名稱,
    EmpName AS 姓名,
    JobTitle AS 現任職稱,
    MonthSalary AS 目前月薪資,
    SUM(leav.Days) AS 請假天數
FROM employee JOIN (dept, leav)
ON employee.DeptID = dept.DeptID AND employee.EmpID = leav.EmpID
WHERE Year = 2018 AND DeptName LIKE '業務%'
GROUP BY DeptName, EmpName, JobTitle, MonthSalary
ORDER BY 請假天數 DESC
LIMIT 1;