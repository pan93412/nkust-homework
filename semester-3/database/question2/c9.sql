SELECT
    ProdName AS 產品名稱,
    Cost * Stock AS 庫存成本,
    (Stock - SafeStock) * Cost AS 冗餘成本
FROM product as p, inv as i
WHERE
    p.ProdID = i.ProdID
    AND Stock > SafeStock
ORDER BY
    冗餘成本 DESC;
