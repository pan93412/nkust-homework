-- 列出與總經理住在同一縣市的員工姓名與職稱
-- 不可直接寫縣市 台北市，依姓名遞增排序

select employee.EmpName as 員工姓名, employee.JobTitle as 職稱
from employee, employee as boss
where boss.JobTitle = '總經理'
    and employee.City = boss.City
order by 員工姓名;


