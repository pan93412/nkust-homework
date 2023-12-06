-- 列出2016-2018的業績差異表，舉例來說，王玉治的業績差異2017為王玉治
-- 2017年的總業績減去他2016年的總業績。列出業務員姓名，
-- 業績差異2017，業績差異2018

with total as (select year(OrderDate) as OrderYear, EmpId, EmpName, sum(Qty * Discount * UnitPrice) as feat
               from employee
                        join (dept) using (DeptId)
                        left join salesorder using (EmpId)
                        left join orderdetail using (OrderId)
                        left join product using (ProdId)
               where DeptName like '業務%'
               group by OrderYear, EmpId, EmpName),
     pivot as (select EmpName                            as 姓名,
                      sum(IF(OrderYear = 2016, feat, 0)) as 2016業績,
                      sum(IF(OrderYear = 2017, feat, 0)) as 2017業績,
                      sum(IF(OrderYear = 2018, feat, 0)) as 2018業績
               from total
               group by EmpName)
select 姓名, 2017業績 - 2016業績 as 差異2017, 2018業績 - 2017業績 as 差異2018
from pivot
order by 姓名;