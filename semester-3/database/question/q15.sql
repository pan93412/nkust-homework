-- 列出 2018 年度每個業務部門為公司帶來的銷售利潤總和。
-- 列出部門名稱與 利潤總額，並依部門名稱排序

select  DeptName, sum(Qty * (UnitPrice * Discount - Cost)) as TotalProfit
from    dept    join (employee) using (DeptID)
                join (salesorder) using (EmpID)
                join (orderdetail) using (OrderID)
                join (product) using (ProdId)
where   DeptID in (select DeptID from employee) and
        DeptName like '業務%' and
        OrderDate between '2018-01-01' and '2018-12-31'
group by
        DeptName
order by
        DeptName;
