-- 那些業務員三年業績都達標?
-- 請列出三年業績都超出銷售配額的業務員，列出其姓名。並依據姓名排序

WITH rec2016 AS (
    SELECT employee.EmpName
    FROM employee JOIN (salesorder, orderdetail, product, quota) ON (
        employee.EmpId = salesorder.EmpId
        AND employee.EmpId = quota.EmpId
        AND salesorder.OrderId = orderdetail.OrderId
        AND orderdetail.ProdId = product.ProdId
    )
    WHERE salesorder.OrderDate between '2016-01-01' and '2016-12-31'
    GROUP BY employee.EmpName, quota.Quota2016
    HAVING SUM(product.UnitPrice * orderdetail.Qty * orderdetail.Discount) > quota.Quota2016
), rec2017 AS (
    SELECT employee.EmpName
    FROM employee JOIN (salesorder, orderdetail, product, quota) ON (
        employee.EmpId = salesorder.EmpId
        AND employee.EmpId = quota.EmpId
        AND salesorder.OrderId = orderdetail.OrderId
        AND orderdetail.ProdId = product.ProdId
    )
    WHERE salesorder.OrderDate between '2017-01-01' and '2017-12-31'
    GROUP BY employee.EmpName, quota.Quota2017
    HAVING SUM(product.UnitPrice * orderdetail.Qty * orderdetail.Discount) > quota.Quota2017
), rec2018 AS (
    SELECT employee.EmpName
    FROM employee JOIN (salesorder, orderdetail, product, quota) ON (
        employee.EmpId = salesorder.EmpId
        AND employee.EmpId = quota.EmpId
        AND salesorder.OrderId = orderdetail.OrderId
        AND orderdetail.ProdId = product.ProdId
    )
    WHERE salesorder.OrderDate between '2018-01-01' and '2018-12-31'
    GROUP BY employee.EmpName, quota.Quota2018
    HAVING SUM(product.UnitPrice * orderdetail.Qty * orderdetail.Discount) > quota.Quota2018
), result AS (
    (SELECT * FROM rec2016)
    INTERSECT
    (SELECT * FROM rec2017)
    INTERSECT
    (SELECT * FROM rec2018)
)
    SELECT EmpName AS 姓名 FROM result ORDER BY EmpName;