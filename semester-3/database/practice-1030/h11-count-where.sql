-- 取出零件 P2 出貨的次數，且 qty>200
select count(*) as 供應商數目 from sp where p_no = 'P2' and qty > 200;