-- 清掉 s 後面的空白
update s set city = trim(city);
update s set sname = trim(sname);

select s_no from s where city = 'Paris' and status > 20;
