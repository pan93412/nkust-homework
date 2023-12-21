-- 對於2018年6,7,8月沒有請假的員工，列出部門名稱、姓名與其6,7,8月加班費總計(無加班紀錄者以空白顯示)
-- 欄位名稱顯示為: 部門名稱,姓名,加班費總計，並依部門名稱、姓名排序

select DeptName as 部門名稱, EmpName as 姓名, ifnull(sum(MonthSalary / 224 * 1.5 * OverHours), 0) as 加班費統計
from dept
         join employee using (DeptId)
         left join overtime using (EmpId)
where EmpId in (select e.EmpId
                from employee e
                         left join (leav) on (e.EmpId = leav.EmpID and Year = 2018 and Month in (6, 7, 8))
                group by EmpId
                having sum(Days) IS NULL)
group by DeptName, EmpName
order by 部門名稱, 姓名;
