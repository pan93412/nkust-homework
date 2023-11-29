 

create database sp;
use sp;

CREATE TABLE `p` (
  `p_no` varchar(5) NOT NULL,
  `pname` varchar(10) NOT NULL,
  `color` varchar(10) NOT NULL,
  `weight` smallint(6) NOT NULL,
  `city` varchar(10) NOT NULL
);

-- 
-- 列出以下資料庫的數據： `p`
-- 

INSERT INTO `p` VALUES ('P1', 'Nut', 'Red', 12, 'London');
INSERT INTO `p` VALUES ('P2', 'Bolt', 'Green', 17, 'Paris');
INSERT INTO `p` VALUES ('P3', 'Screw', 'Blue', 17, 'Rome');
INSERT INTO `p` VALUES ('P4', 'Screw', 'Red', 14, 'London');
INSERT INTO `p` VALUES ('P5', 'Cam', 'Blue', 12, 'Paris');
INSERT INTO `p` VALUES ('P6', 'Cog', 'Red', 19, 'London');

-- --------------------------------------------------------

-- 
-- 資料表格式： `s`
-- 

CREATE TABLE `s` (
  `s_no` varchar(5) NOT NULL,
  `sname` varchar(10) NOT NULL,
  `status` smallint(6) NOT NULL,
  `city` varchar(10) NOT NULL
);

-- 
-- 列出以下資料庫的數據： `s`
-- 

INSERT INTO `s` VALUES ('S1', 'Smith ', 20, 'London ');
INSERT INTO `s` VALUES ('S2', 'Jones ', 10, 'Paris  ');
INSERT INTO `s` VALUES ('S3', 'Blake ', 30, 'Paris  ');
INSERT INTO `s` VALUES ('S4', 'Clark ', 20, 'London ');
INSERT INTO `s` VALUES ('S5', 'Adams ', 30, 'Athens ');

-- --------------------------------------------------------

-- 
-- 資料表格式： `sp`
-- 

CREATE TABLE `sp` (
  `s_no` varchar(5) NOT NULL,
  `p_no` varchar(5) NOT NULL,
  `qty` smallint(6) NOT NULL
);

-- 
-- 列出以下資料庫的數據： `sp`
-- 

INSERT INTO `sp` VALUES ('S1', 'P1', 300);
INSERT INTO `sp` VALUES ('S1', 'P2', 200);
INSERT INTO `sp` VALUES ('S1', 'P3', 400);
INSERT INTO `sp` VALUES ('S1', 'P4', 200);
INSERT INTO `sp` VALUES ('S1', 'P5', 100);
INSERT INTO `sp` VALUES ('S1', 'P6', 100);
INSERT INTO `sp` VALUES ('S2', 'P1', 300);
INSERT INTO `sp` VALUES ('S2', 'P2', 400);
INSERT INTO `sp` VALUES ('S3', 'P2', 200);
INSERT INTO `sp` VALUES ('S4', 'P2', 200);
INSERT INTO `sp` VALUES ('S4', 'P4', 300);
INSERT INTO `sp` VALUES ('S4', 'P5', 400);

