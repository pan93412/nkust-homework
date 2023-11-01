-- 列出2016年供應商採購次數統計表。列出供應商名稱與採購次數，僅列出次數大於一次的廠商。
-- 結果請以採購次數做遞減排序。次數相同者請以廠商名稱遞增排序

SELECT
    supplier_name,
    COUNT(*) AS purchase_count