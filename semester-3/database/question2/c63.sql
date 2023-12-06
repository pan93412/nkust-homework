-- 老闆想要知道哪些客人總是買便宜的東西。請列出每次都是購買便宜貨
-- (單價15,000以下)的客戶名稱。欄位顯示客戶名稱，並依據客戶名稱排序

select CustName
from customer
where CustId not in (select distinct CustId
                     from customer
                              join (salesorder) using (CustId)
                              join (orderdetail) using (OrderId)
                              join (product) using (ProdId)
                     where UnitPrice >= 15000);
