-- 計算 2018 年個別產品銷售的產品名稱,出貨次數與業績總額，並依產品名稱排序

select
    ProdName as 產品名稱,
    count(*) as 出貨次數,
    sum(Qty * Discount * UnitPrice) as 業績總額
from salesorder join (orderdetail) using (OrderId)
                join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by 產品名稱
order by 產品名稱;
