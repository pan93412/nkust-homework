-- 列出 2018 年業務部門個別業務之業績總額
-- 列出其部門名稱 業務姓名 現任職稱 年薪 業績總額，將輸出結果
-- 以部門別遞增排序，同一部門者則 依年薪遞減排序

select
    DeptName    as 部門名稱,
    EmpName     as 業務姓名,
    JobTitle    as 現任職稱,
    MonthSalary * 16.5 as 年薪,
    sum(UnitPrice * Qty * Discount) as 業績總額
from dept   join employee using (DeptId)
            join salesorder using (EmpId)
            join orderdetail using (OrderId)
            join product using (ProdId)
where   DeptName like '業務%' and
        OrderDate between '2018-01-01' and '2018-12-31'
group by DeptName, EmpName, JobTitle, MonthSalary
order by DeptName, 年薪 desc;