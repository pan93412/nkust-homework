select
	customer.CustName as 客戶名稱,
	sum(orderdetail.Qty * orderdetail.Discount * product.UnitPrice) as 業績總和,
	sum(orderdetail.Qty * (orderdetail.Discount * product.UnitPrice - product.Cost)) as 利潤總和
from customer 	join (salesorder) using (custid)
                join (orderdetail) using (OrderId)
                join (product) using (ProdID)
where salesorder.OrderDate between '2018-01-01' and '2018-12-31'
        and customer.City = '台北市'
group by customer.CustName
order by customer.CustName;
