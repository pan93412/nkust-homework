-- 在Select子句中有Distinct運算符號的聚合函數
-- 取出現在有供應零件的供應商數目

SELECT COUNT(DISTINCT s_no) AS 有供應零件的供應商數目
FROM sp;
