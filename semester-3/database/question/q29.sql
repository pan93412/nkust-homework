-- 列出 2018 年 105 班三月份曠課超過 7 節 含 的同學資料。列
-- 出其姓名 住址 家長 曠課節數。查詢結果依據姓名排序

select
    StName as 姓名,
    Address as 住址,
    Parent as 家長,
    sum(Absent) as 曠課節數
from students join (records) using (ClassNo)
where ClassNo like '105%'
        and YMD between '2018-01-01' and '2018-12-31'
group by StName, Address, Parent
having 曠課節數 >= 7
order by 姓名;