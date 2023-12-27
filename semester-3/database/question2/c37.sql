select employee.EmpName as 姓名, employee.JobTitle as 現任職稱
from employee, employee as boss
where boss.JobTitle = '總經理'
    and employee.City = boss.City
    and employee.EmpId <> boss.EmpId
order by 姓名;
