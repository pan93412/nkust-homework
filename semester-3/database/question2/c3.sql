-- 列出部門主管年假天數統計表。列出部門名稱、主管姓名、現任職稱、年假天數。結果以部門名稱排序

SELECT dept.DeptName        AS 部門名稱,
       employee.EmpName     AS 業務姓名,
       employee.JobTitle    AS 現任職稱,
       employee.AnnualLeave AS 年假天數
FROM employee
         JOIN (dept)
              ON (
                  employee.EmpId = dept.ManagerEmpId
                  )
ORDER BY dept.DeptName
