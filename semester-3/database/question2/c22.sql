-- 列出 2018 年度各行業別(化學,機械…)的顧客與本公司交易的行業別與業績總額(總和)，並依業績總額遞減排序

select
    Industry as 行業別,
    sum(Qty * Discount * UnitPrice) as 營業額
from customer   join (salesorder) using (CustId)
                join (orderdetail) using (OrderId)
                join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by Industry
order by 營業額 desc;