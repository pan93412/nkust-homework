select s.*, p.*
	from s, p
	where s.city = p.city;

-- another solution…
select s.*, p.*
	from s join p
    on s.city = p.city;
