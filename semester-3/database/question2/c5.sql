-- 列出2018年所有員工的加班時數統計表。沒有加班的員工則以0表示
-- 列出員工姓名，加班時數。並以加班時數遞減排序，同樣加班時數者請以員工姓名遞增排序

select employee.EmpName AS 員工名稱, coalesce(sum(overtime.OverHours), 0) as 加班時數
from employee left join (overtime) on (employee.EmpId = overtime.EmpId)
where overtime.OverDate between '2018-01-01' and '2018-12-31' OR overtime.OverDate is null
group by employee.EmpName
order by 加班時數 desc, employee.EmpName;
