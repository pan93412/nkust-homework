-- 列出2016年供應商採購次數統計表。列出供應商名稱與採購次數，
-- 僅列出次數大於一次的廠商。結果請以採購次數做遞減排序。次數相同者請以廠商名稱遞增排序

-- 供應商 suppiler/id, purchaseorder/pid

select supplier.SupplierName as 供應商名稱, COUNT(*) as 採購次數
from supplier join (purchaseorder) on (supplier.SupplierId = purchaseorder.SupplierId)
where purchaseorder.PurchaseDate between '2016-01-01' and '2016-12-31'
group by supplier.SupplierName
order by 採購次數 desc, SupplierName;
