-- (難)列出2018年，各縣市銷售業績最佳的產品名稱。
-- 列出縣市，商品名稱，銷售業績，並依銷售業績排序

select 縣市, 商品名稱, 銷售業績
from (select City                                                                            as 縣市,
             ProdName                                                                        as 商品名稱,
             sum(Qty * Discount * UnitPrice)                                                 as 銷售業績,
             (rank() over (partition by City order by sum(Qty * Discount * UnitPrice) desc)) as 排序
      from product
               join (orderdetail) using (ProdID)
               join (salesorder) using (OrderId)
               join (employee) using (EmpId)
      where OrderDate between '2018-01-01' and '2018-12-31'
      group by City, ProdName) as t
where 排序 = 1
order by 縣市;
