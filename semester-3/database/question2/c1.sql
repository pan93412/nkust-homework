-- 列出公司內所有現任職稱為工程師的員工中，薪資最高的前6名。列出部門名稱、姓名、職稱、縣市與薪資。查詢結果依據薪資做遞減排序。

SELECT dept.DeptName AS 部門名稱, employee.EmpName AS 姓名, employee.JobTitle As 職稱, employee.City As 縣市, employee.MonthSalary AS 薪資
FROM employee JOIN (dept) ON (employee.DeptId = dept.DeptId)
WHERE employee.JobTitle like '%工程師%'
ORDER BY employee.MonthSalary DESC
LIMIT 6;