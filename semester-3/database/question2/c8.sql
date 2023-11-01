SELECT DISTINCT product.ProdName AS 產品名稱
FROM product, salesorder, orderdetail, employee
WHERE salesorder.EmpId = employee.EmpId
    AND orderdetail.OrderId = salesorder.OrderId
    AND orderdetail.ProdId = product.ProdId
    AND employee.City = '台北市'
    AND YEAR(salesorder.OrderDate) = 2018
ORDER BY 產品名稱;
