-- 列出 2018 年度中，哪一個商品女生銷售業績的比男生好，請列出商品名稱，並依商品名稱排序。

with
    male_sales as (
        select
            ProdName as name, sum(Qty * Discount * UnitPrice) as feat
        from
            product join (orderdetail) using (ProdID)
                    join (salesorder) using (OrderID)
                    join (person) using (EmpId)
        where
            person.Gender = '男' and
            OrderDate between '2018-01-01' and '2018-12-31'
        group by name
        order by name
    ),
    female_sales as (
        select
            ProdName as name, sum(Qty * Discount * UnitPrice) as feat
        from
            product join (orderdetail) using (ProdID)
                    join (salesorder) using (OrderID)
                    join (person) using (EmpId)
        where
            person.Gender = '女' and
            OrderDate between '2018-01-01' and '2018-12-31'
        group by name
        order by name
    )
select female_sales.name, female_sales.feat
from male_sales cross join female_sales using (name)
where female_sales.feat > male_sales.feat
group by name;
