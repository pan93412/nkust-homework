-- 4. 計算公司的庫存成本，與超出安全存量之多餘成本
--
-- 計算公司的庫存成本，與超出安全存量之多餘成本 現有量 安全存量 成本
--
-- 列出產品名稱、庫存成本、冗餘成本，並依產品名稱排序

SELECT
    ProdName AS 產品名稱,
    Cost * Stock AS 庫存成本,
    (Stock - SafeStock) * Cost AS 冗餘成本
FROM product as p, inv as i
WHERE
    p.ProdID = i.ProdID
    AND Stock > SafeStock
ORDER BY
    ProdName;
