SELECT
    ProdName AS 產品名稱,
    (UnitPrice - Cost) / Cost AS 毛利率,
    UnitPrice AS 單價,
    Cost AS 成本
FROM product
ORDER BY 毛利率 DESC;