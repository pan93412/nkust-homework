select DeptName                                 as 部門名稱
     , EmpName                                  as 業務姓名
     , JobTitle                                 as 現任職稱
     , sum(Qty * UnitPrice * Discount)          as 業績總額
     , sum(Qty * (UnitPrice * Discount - Cost)) as 利潤總額
from dept
         join (employee) using (DeptId)
         join (salesorder) using (EmpId)
         join (orderdetail) using (OrderId)
         join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by DeptName, EmpName, JobTitle
having count(EmpId) > 3
order by 利潤總額 desc;