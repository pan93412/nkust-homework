-- 列出2018 年中所有顧客與公司的交易統計，根據各客戶別，列出其客戶寶號,業績總額,利潤總額,交易次數，並根據利潤總額由大到小排序

SELECT CustName                                 as 客戶寶號,
       sum(Qty * UnitPrice * Discount)          as 業績總額,
       sum(Qty * (UnitPrice * Discount - Cost)) as 利潤總額,
       count(*)                                 as 交易次數
FROM customer
         join (salesorder) using (CustId)
         left join (orderdetail) using (OrderId)
         left join (product) using (ProdId)
where OrderDate between '2018-01-01' and '2018-12-31'
group by CustName
order by 利潤總額 desc;
