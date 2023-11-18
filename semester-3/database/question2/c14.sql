-- 列出 2018 年經理級以上員工的加班時數統計表列出其部門名稱,姓名,
-- 現任職稱,總加班時數，依部門名稱排序，同部門依總加班時數遞減排序

select
    DeptName as 部門名稱,
    EmpName as 姓名,
    JobTitle as 現任職稱,
    sum(OverHours) as 總加班時數
from
    dept join (employee) using (DeptId)
         join (overtime) using (EmpId)
where
    OverDate between '2018-01-01' and '2018-12-31'
        and JobTitle like '%經理'
group by
    部門名稱, 姓名, 現任職稱
order by 部門名稱, 總加班時數 desc;
