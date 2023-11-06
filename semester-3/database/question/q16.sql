-- 計算 2018 年個別產品銷售的產品名稱 出貨次數 與業績總額

select
    ProdName as '產品名稱',
    count(*) as '出貨次數',
    sum(Qty*UnitPrice*Discount) as '業績總額'
from product right join (orderdetail) using (ProdID)
             left join (salesorder) using (OrderID)
where OrderDate between '2018-01-01' and '2018-12-31'
group by ProdName
order by 產品名稱;
