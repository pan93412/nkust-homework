-- 分析各年度商品的銷售頻次，及銷售數量。列出年度，產品名稱，銷售次數，
-- 以及總銷售數量，並依年度(遞增)，銷售次數(遞減)，產品名稱(遞增)排序。

select
    year(OrderDate) as 年度,
    ProdName as 產品名稱,
    count(*) as 銷售次數,
    sum(Qty) as 總銷售數量
from product    join (orderdetail) using (ProdID)
                join (salesorder) using (OrderId)
group by 年度, 產品名稱
order by 年度, 銷售次數 desc, 產品名稱;