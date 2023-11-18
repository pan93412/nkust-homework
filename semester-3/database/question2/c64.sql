-- 誰賣過所有SCSI相關產品?請列出賣過所有SCSI相關產品的業務員名稱，並列出其員工所有資料。欄位顯示姓名, 現任職稱,縣市,月薪資，並依據業務姓名排序

select EmpName as 姓名, JobTitle as 現任職稱, City as 縣市, MonthSalary as 月薪資, *
from employee   join (salesorder) using (EmpId)
                join (orderdetail) using (OrderId)
                right join (
                    select ProdID, count(*) as c
                    from product
                    where ProdName like '%SCSI%'
                    group by ProdID
                ) as `p` using (ProdId)
# having count(distinct EmpName) = p.c
order by 姓名;

with scsi_product as
    (
        select ProdID, ProdName, count(*) over (partition by ProdName like '%SCSI%') as ProdCount
        from product
        where ProdName like '%SCSI%'
    )
select EmpName as 姓名, JobTitle as 現任職稱, City as 縣市, MonthSalary as 月薪資, ProdCount
from employee   right join (salesorder) using (EmpId)
                right join (orderdetail) using (OrderId)
                right join scsi_product using (ProdId);

# any
select * from product
    join (orderdetail) using (ProdID)
    join (salesorder) using (OrderId)
where product.ProdName like '%SCSI%'
    and salesorder.EmpId = 00005;

# all
select ProdID from product
    join (orderdetail) using (ProdID)
    join (salesorder) using (OrderId)
where product.ProdName like '%SCSI%'
    and salesorder.EmpId = 00005
intersect
select ProdID from product
    join (orderdetail) using (ProdID)
    join (salesorder) using (OrderId)
where product.ProdName like '%SCSI%';

#all
select ProdID from product
    join (orderdetail) using (ProdID)
    join (salesorder) using (OrderId)
where product.ProdName like '%SCSI%'
group by ProdID
except
select ProdID from product
    join (orderdetail) using (ProdID)
    join (salesorder) using (OrderId)
where product.ProdName like '%SCSI%'
    and salesorder.EmpId = 00054
group by ProdID;

# all
select EmpName as 姓名, JobTitle as 現任職稱, City as 縣市, MonthSalary as 月薪資
from employee
where not exists (
    select ProdID from product
        join (orderdetail) using (ProdID)
        join (salesorder) using (OrderId)
    where product.ProdName like '%SCSI%'
    group by ProdID
    except
    select ProdID from product
        join (orderdetail) using (ProdID)
        join (salesorder) using (OrderId)
    where product.ProdName like '%SCSI%'
        and salesorder.EmpId = employee.EmpId
    group by ProdID
)
order by 姓名;
