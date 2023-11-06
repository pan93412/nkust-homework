-- 列出 2018 年各縣市員工加班時數的個別總和 例如 台北市 30)
-- 列出縣市、 加班時數總計 ，將結果以縣市排序

select city, sum(OverHours) as total
from employee join overtime using (EmpId)
where OverDate between '2018-01-01' and '2018-12-31'
group by city
order by city;
