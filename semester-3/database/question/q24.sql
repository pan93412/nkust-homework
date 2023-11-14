-- 欲計算客戶的利潤貢獻度，對於 2018 年台北市的客戶，
-- 列出客戶名稱 業績總和 利潤總和，結果依客戶名稱排序

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
