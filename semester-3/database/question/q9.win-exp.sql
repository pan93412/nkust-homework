-- 列出 2018 年經理級以上員工的加班時數統計表
-- 列出其部門名稱 姓名 現任職稱 總加班時數，
-- 依部門名稱排序，同部門依總加班時數遞減排序 idx

SELECT
    DeptName,
    EmpName,
    JobTitle,
    OverHours,
    SUM(OverHours) OVER (ORDER BY DeptName) AS TotalHours
FROM
    dept JOIN (employee, overtime)
    ON (dept.DeptId = employee.DeptId AND employee.EmpId = overtime.EmpId)
WHERE
    OverDate BETWEEN '2018-01-01' AND '2018-12-31'
    AND JobTitle LIKE '%經理'
ORDER BY
    DeptName;
#     OverHours,
#     TotalHours DESC,
#     EmpName
