-- 列出產品毛利率表
-- 列出其產品名稱,毛利率,單價,成本，依毛利率遞減排序。其中毛利率=(單價-成本)/成本

SELECT
    ProdName AS 產品名稱,
    (UnitPrice - Cost) / Cost AS 毛利率,
    UnitPrice AS 單價,
    Cost AS 成本
FROM product
ORDER BY 毛利率 DESC;