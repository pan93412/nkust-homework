-- 列出所有全勤的學生 (2018 年無任何公假、事假、病假、曠課記錄
-- 的學生 ))，且為民國 2001 年以後 不含 出生的列出 班級座號 姓名 出生年
-- 月日 住址 電話 排序，依「出生年月日遞增 排序 相同者依「班級座號」
-- 遞增排序

select
    students.ClassNo as 班級座號,
    students.StName as 姓名,
    students.Birthday as 出生年月日,
    students.Address as 住址,
    students.Phone as 電話
from students
where
    Birthday > '2001-12-31' and
    ClassNo not in (
        select ClassNo
        from records
        where YMD between '2018-01-01' and '2018-12-31'
    )
order by Birthday, ClassNo;
