-- 將單價低於 5000 元的產品，計算其 2018 年的交易次數與交易總數
-- 列出產品名稱,單價,交易次數,交易總數，並依單價遞減排序

SELECT product.ProdName as 產品名稱, product.unitprice as 單價, count(*) as 交易次數, sum(orderdetail.qty) as 交易總數
FROM product,
     salesorder,
     orderdetail
WHERE salesorder.OrderId = orderdetail.OrderId
  AND orderdetail.ProdId = product.ProdID
  AND product.unitprice <= 5000
  AND salesorder.orderdate BETWEEN '2018-01-01' AND '2018-12-31'
GROUP BY product.ProdName, product.UnitPrice
ORDER BY 單價 DESC;