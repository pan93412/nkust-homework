SELECT EmpName AS 員工姓名, JobTitle AS 職稱
FROM
    employee AS empl,
    (
        SELECT EmpId, City
        FROM employee
        WHERE JobTitle = '總經理'
    ) AS manager
WHERE
    empl.City = manager.City AND
    empl.EmpId <> manager.EmpId
ORDER BY 員工姓名;
