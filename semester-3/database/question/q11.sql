-- 列出 2018 年中，公司各產品的利潤統計表，
-- 列出產品名稱 單價 成本 總數量 利潤總額
-- 查詢結果依總利潤遞減排序

select
    ProdName as 產品名稱,
    UnitPrice as 單價,
    Cost as 成本,
    sum(Qty) as 總數量,
    sum(Qty * (UnitPrice * Discount - Cost)) as 利潤總額
from product join orderdetail using (ProdID)
             join salesorder using (OrderID)
where OrderDate between '2018-01-01' and '2018-12-31'
group by ProdName, UnitPrice, Cost
order by 利潤總額 desc;
