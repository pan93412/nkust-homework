SELECT
    EmpName AS 姓名,
    employee.JobTitle AS 現任職稱,
    DeptName AS 部門名稱,
    2020 - year(person.Birth) AS 年齡,
    2020 - person.WorkYear AS 年資
FROM employee INNER JOIN (dept, person, exp)
ON (
    employee.DeptId = dept.DeptId
    AND employee.EmpId = person.EmpId
    AND employee.EmpId = exp.EmpId
)
WHERE
    (  -- 有研發經驗
            exp.CompJob1 LIKE '研發%'
        OR exp.CompJob2 LIKE '研發%'
        OR exp.OutsideJob1 LIKE '研發%'
        OR exp.OutsideJob2 LIKE '研發%'
    )
    AND ( -- 專長
        person.Expertise1 IN ('電子電路', '數位電路')
        OR person.Expertise2 IN ('電子電路', '數位電路')
    )
HAVING
    年齡 BETWEEN 25 AND 40
    AND 年資 >= 3
ORDER BY 年齡 desc;
