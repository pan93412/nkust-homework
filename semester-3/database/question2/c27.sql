select
	dept.DeptName as 部門名稱,
    employee.EmpName as 姓名,
    sum(orderdetail.Qty * orderdetail.Discount * product.UnitPrice) as 業績總額
from dept 	join (employee) using (DeptId)
            join (salesorder) using (EmpId)
            join (orderdetail) using (OrderId)
            join (product) using (ProdID)
where employee.MonthSalary between 30000 and 50000
		and salesorder.OrderDate between '2018-01-01' and '2018-12-31'
        and DeptName like '%業務%'
group by dept.DeptName, employee.EmpName
order by 業績總額 desc;
