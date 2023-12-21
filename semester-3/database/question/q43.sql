-- 列出2018 年中，每個個別業務銷售次數大於3 次者(至少成交過三筆訂單)
-- 列出其部門名稱,業務姓名,現任職稱,業績總額與利潤總額，並根據利潤總額由大到小排序

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
where JobTitle like '%業務%'
group by DeptName, EmpName, JobTitle
having count(EmpId) >= 3
order by 利潤總額 desc;
