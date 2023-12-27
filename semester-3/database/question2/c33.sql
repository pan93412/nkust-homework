select
    CustName as 客戶寶號,
    sum(Qty * Discount * UnitPrice) as 交易額,
    EmpName as 業務姓名
from customer   join (salesorder) using (CustId)
                join (employee) using (EmpId)
                join (orderdetail) using (OrderId)
                join (product) using (ProdId)
where salesorder.OrderDate between '2018-01-01' and '2018-12-31'
group by CustName, EmpName
order by 交易額 desc
limit 15;
