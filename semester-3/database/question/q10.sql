-- 統計 2018 年各月份利潤與業績統計表
-- 列出 交易月 利潤總額 營業總額 ，查詢結果 依月份遞增排序

select
    month(OrderDate) as '交易月',
    sum(Qty * (UnitPrice * Discount - Cost)) as '利潤總額',
    sum(Qty * UnitPrice * Discount) as '營業總額'
from
    product join orderdetail using (ProdID)
            join salesorder using (OrderID)
where
    OrderDate between '2018-01-01' and '2018-12-31'
group by month(OrderDate)
order by 交易月;
