-- 統計 2018 年各業務部門的年度業績目標。
-- 其中部門業績目標為該部門業務員的業績目標 (Quota) 中，
-- 業績目標 85) 總和。查詢結果依部門名稱排序

select DeptName as 部門名稱, sum(Quota2018) as '業績目標'
from dept   join (employee) using (DeptId)
            join (quota) using (EmpId)
group by DeptName
order by DeptName;
