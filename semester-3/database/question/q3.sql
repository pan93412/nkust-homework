-- 列出 2018 年度台北市的銷售員曾賣過的產品名稱
-- 注意 同一個產品名稱只要顯示一次 ))，並依產品名稱排序。

SELECT DISTINCT product.ProdName AS 產品名稱
FROM product, salesorder, orderdetail, employee
WHERE salesorder.EmpId = employee.EmpId
    AND orderdetail.OrderId = salesorder.OrderId
    AND orderdetail.ProdId = product.ProdId
    AND employee.City = '台北市'
    AND YEAR(salesorder.OrderDate) = 2018
ORDER BY 產品名稱;
