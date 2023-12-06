create database jointest;
use jointest;

create table customers (
    c_id int primary key auto_increment,
    name varchar(64) not null,
    city varchar(64) not null,
    address varchar(64) not null,
    phone varchar(64) not null
);

create table orders (
    o_id int primary key auto_increment,
    orderno int,
    c_id int references customers(c_id)
);

insert customers (c_id, name, city, address, phone)
    values
        (1, '張一', '台北市', 'XX路100號', '02-12345678'),
        (2, '王二', '新竹縣', 'YY路200號', '03-12345678'),
        (3, '李三', '高雄縣', 'ZZ路300號', '07-12345678');

insert orders (o_id, orderno, c_id)
    values
        (1, 2572, 3),
        (2, 7375, 3),
        (3, 7520, 1),
        (4, 1054, 1),
        (5, 1257, 5)