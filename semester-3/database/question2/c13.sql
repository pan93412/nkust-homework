-- 製作一份「 2018 年度產品銷售數量統計表」列出產品名稱
-- 件數 總數量 平均數量 最大量 最小量，依產品名稱排序

SELECT ProdName AS 產品名稱, Count(*) AS 件數, SUM(Qty) AS 總數量, AVG(Qty) AS 平均數量, MAX(Qty) AS 最大量, MIN(Qty) AS 最小量
FROM product
    JOIN orderdetail USING (ProdID)
    JOIN salesorder USING (OrderId)
WHERE OrderDate BETWEEN '2018-01-01' AND '2018-12-31'
GROUP BY ProdName
ORDER BY ProdName;
