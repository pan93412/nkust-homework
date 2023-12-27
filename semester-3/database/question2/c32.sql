select DeptName as 部門名稱, sum(Quota2018) as '部門業績目標'
from dept   join (employee) using (DeptId)
            join (quota) using (EmpId)
group by DeptName
order by DeptName;
