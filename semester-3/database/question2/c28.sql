select month(overdate) as 月, sum(monthsalary / 224 * 1.5 * overhours) as 加班費合計
from overtime join (employee) using (EmpId)
where overdate between '2018-01-01' and '2018-12-31'
group by month(overdate);