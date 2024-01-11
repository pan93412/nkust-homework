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