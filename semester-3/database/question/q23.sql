-- 根據月份，統計 2018 年各月份加班費合計

select month(overdate) as 月份, ceil(sum(monthsalary / 224 * 1.5 * overhours)) as 加班費
from overtime join (employee) using (EmpId)
where overdate between '2018-01-01' and '2018-12-31'
group by month(overdate)
order by 加班費 desc;
