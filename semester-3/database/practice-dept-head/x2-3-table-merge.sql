-- 取出所有城市的配對，其中供應商位於第一個城市，而他所供應的零件則儲存於第二個城市。

SELECT DISTINCT s.city AS 第一個城市, p.city AS 第二個城市
FROM sp JOIN (p, s)
    ON (sp.p_no = p.p_no AND sp.s_no = s.s_no)
