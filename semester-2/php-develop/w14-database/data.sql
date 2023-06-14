CREATE TABLE `student` (
                           `id` varchar(10) NOT NULL,
                           `name` varchar(10) NOT NULL,
                           `birth` date NOT NULL,
                           `addr` varchar(50) NOT NULL,
                           PRIMARY KEY (`id`)
);

PREPARE stmt FROM 'INSERT INTO `student` (`id`, `name`, `birth`, `addr`) VALUES (?, ?, ?, ?)';

SET @id1 = '1106137101';
SET @name1 = '王小明';
SET @birth1 = '2018-05-12';
SET @addr1 = '高雄市三民區建工路415號';
EXECUTE stmt USING @id1, @name1, @birth1, @addr1;

SET @id2 = '1106137102';
SET @name2 = '李小華';
SET @birth2 = '2018-01-10';
SET @addr2 = '台北市大安區';
EXECUTE stmt USING @id2, @name2, @birth2, @addr2;

SET @id3 = '1106137103';
SET @name3 = '陳大明';
SET @birth3 = '2017-10-19';
SET @addr3 = '高雄市三民區';
EXECUTE stmt USING @id3, @name3, @birth3, @addr3;

SET @id4 = '1106137104';
SET @name4 = '吳大華';
SET @birth4 = '2018-05-19';
SET @addr4 = '高雄市左營區';
EXECUTE stmt USING @id4, @name4, @birth4, @addr4;

DEALLOCATE PREPARE stmt;
