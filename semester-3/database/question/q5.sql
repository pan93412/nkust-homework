-- 5. 列出與總經理住在同一縣市的員工姓名與職稱
--
-- 列出與總經理住在同一縣市的員工姓名與職稱
-- 不可直接寫縣市 "台北市"，依姓名遞增排序

SELECT EmpName AS 姓名, JobTitle AS 現任職稱
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
ORDER BY
    EmpName DESC;
