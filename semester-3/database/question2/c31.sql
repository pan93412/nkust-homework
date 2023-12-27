-- 統計 2018 年度，不同行業別對公司的利潤貢獻度統計表。
-- 列出行業別 業績總額 利潤總額，將結果依行業別排序

select
    Industry as 行業別,
    sum(Qty * Discount * UnitPrice) as 業績總額,
    sum(Qty * (Discount * UnitPrice - Cost)) as 利潤總額
from customer   join (salesorder) using (CustId)
                join (orderdetail) using (OrderId)
                join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by 行業別
order by 行業別;
