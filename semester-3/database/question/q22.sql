-- 將目前月薪介於 30000 與 50000 的業務員，
-- 列出其部門名稱 姓名 ,2018 年的業績總額，結果依業績總額遞減排序

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
