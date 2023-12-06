-- 列出 2018 年度台北市的銷售員沒賣過的產品名稱
-- 注意 同一個產品名稱只要顯示一次 ) ，並依產品名稱排序。

select ProdName as 產品名稱
from product
where ProdID not in (
    select distinct ProdId
    from salesorder join (orderdetail) using (OrderId)
                    join (employee) using (EmpId)
    where City = '台北市'
        and OrderDate between '2018-01-01' and '2018-12-31'
    )
order by ProdName