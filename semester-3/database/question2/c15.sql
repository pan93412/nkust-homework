-- 統計 2018 年各月份利潤與業績統計表
-- 列出交易月,利潤總額,營業總額，查詢結果依月份遞增排序

select
    month(OrderDate) as 交易月,
    sum(Qty * (Discount * UnitPrice - Cost)) as 利潤總額,
    sum(Qty * Discount * UnitPrice) as 營業總額
from salesorder join (orderdetail) using (OrderId)
                join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by 交易月
order by 交易月;
