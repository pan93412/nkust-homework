-- 對於 2018 年所有產品，列出其產品名稱 銷售次數 業績總額
-- 利潤總額，並依產品名稱排序

select
    ProdName,
    count(*) as '銷售次數',
    sum(Qty * UnitPrice * Discount) as '業績總額',
    sum(Qty * (UnitPrice * Discount - Cost)) as '利潤總額'
from product    join (orderdetail) using (ProdID)
                right join (salesorder) using (OrderID)
where OrderDate between '2018-01-01' and '2018-12-31'
group by ProdName
order by ProdName;