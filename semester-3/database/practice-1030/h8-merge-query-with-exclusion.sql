-- 取出所有供應商及零件資料的組合，其中供應商及零件在同一城市，但略去狀態是20的供應商

select s.*, p.*
	from s join p on s.city = p.city -- or from s, p where s.city = p.city
    and not status = 20; -- or status <> 20