-- 計算各年份年度的交易年、業績總額與利潤，並依交易年排序

select
    year(OrderDate) as 交易年,
    sum(Qty * Discount * UnitPrice) as 營業額,
    sum(Qty * (Discount * UnitPrice - Cost)) as 利潤
from salesorder join (orderdetail) using (OrderId)
                join (product) using (ProdId)
group by 交易年
order by 交易年;