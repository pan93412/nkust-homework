-- 列出 2018 年度每個業務部門為公司帶來的銷售利潤總和。列出部門名稱與 利潤總額，並依部門名稱排序

select
    DeptName as 部門名稱,
    sum(Qty * (Discount * UnitPrice - Cost)) as 利潤總額
from dept   join (employee) using (DeptId)
            join (salesorder) using (EmpId)
            join (orderdetail) using (OrderId)
            join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by DeptName
order by DeptName;