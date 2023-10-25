-- 對於高於安全存量三倍以上的產品
-- 列出產品名稱 現存量 安全庫存 成本 庫存現值，
-- 依庫存現值遞減排序

SELECT
    p.ProdName AS 產品名稱,
    i.Stock AS 現存量,
    i.SafeStock AS 安全庫存,
    p.Cost AS 成本,
    p.Cost*i.Stock AS 庫存現值
FROM
    product as p,
    inv as i
WHERE p.ProdID = i.ProdId AND (i.Stock / i.SafeStock) > 3
ORDER BY 庫存現值 desc;
