-- 計算2016年，各部門業務人員的業績總額(沒有業績的不需列出)。請列出部門名稱、
-- 業務姓名、與業績總額。結果請以部門名稱遞增排序，同部門者以業績總額遞減排序。


-- dept.DeptName
-- employee.JobTitle
-- employee.empName
-- salesorder.Empid Map orderdetails.OrderId [Qty * Discount] Map prod.UnitPrice

SELECT dept.DeptName                                                   AS 部門名稱,
       employee.EmpName                                                AS 業務姓名,
       SUM(orderdetail.Qty * orderdetail.Discount * product.UnitPrice) AS 業績總額
FROM employee
         INNER JOIN (dept, salesorder, orderdetail, product)
                    ON (
                                employee.DeptId = dept.DeptId
                            AND salesorder.EmpId = employee.EmpId
                            AND orderdetail.OrderId = salesorder.OrderId
                            AND product.ProdID = orderdetail.ProdId
                        )
WHERE salesorder.OrderDate BETWEEN '2016-01-01' AND '2016-12-31'
  AND (
            employee.JobTitle LIKE '%業務%'
        OR employee.JobTitle LIKE '%專員%'
    )
GROUP BY dept.DeptName, employee.EmpName
HAVING 業績總額 > 0
ORDER BY dept.DeptName, 業績總額 DESC;
