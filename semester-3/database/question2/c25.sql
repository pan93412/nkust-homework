-- 對於 2018年所有產品，列出其產品名稱,銷售次數,業績總額,利潤總額，並依產品名稱排序

select
    ProdName as 產品名稱,
    count(*) as 銷售次數,
    sum(Qty * Discount * UnitPrice) as 業績總額,
    sum(Qty * (Discount * UnitPrice - Cost)) as 利潤總額
from salesorder join (orderdetail) using (OrderId)
                join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by 產品名稱
order by 產品名稱;
