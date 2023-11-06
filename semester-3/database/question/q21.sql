-- 將單價低於 5000 元的產品，計算其 2018 年的交易次數與
-- 交易總數 。
-- 列出產品名稱 單價 交易次數 交易總數，並依單價遞減排序

select ProdName, UnitPrice, count(*) as '交易次數', sum(Qty) as '交易總數'
from product join (orderdetail) using (ProdID)
             join (salesorder) using (OrderID)
where UnitPrice < 5000 and
        OrderDate between '2018-01-01' and '2018-12-31'
group by ProdName, UnitPrice
order by UnitPrice desc;