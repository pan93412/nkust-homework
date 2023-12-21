-- 在2018 年中，針對低於平均單價的各產品
-- 列出其產品名稱,銷售業績,利潤總和，結果依銷售業績遞減排序

select ProdName                                 as 產品名稱
     , sum(Qty * UnitPrice * Discount)          as 銷售業績
     , sum(Qty * (UnitPrice * Discount - Cost)) as 利潤總和
from product
         join (orderdetail) using (ProdID)
         join (salesorder) using (OrderId)
where OrderDate between '2018-01-01' and '2018-12-31'
    and UnitPrice < (select avg(UnitPrice) from product)
group by ProdName
order by 銷售業績 desc;
