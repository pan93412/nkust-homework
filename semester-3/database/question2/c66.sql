-- 以2016年的採購成本為基礎，分析產品的名目成本(列於product表中的成本)與實際採購的平均成本的差異。
-- 列出產品名稱，名目成本，實際成本，成本差異。若2016年沒有採購該產品，實際成本以0顯示，差異則已減號
-- (-)顯示。結果成本差異遞減排序。(if() 函數的用法，例如 select if(actualcost is null, 0,
-- cost-actualcost)。 或上網google mysql if()函數用法 )

with product as (
    select
        product.ProdName as name,
        product.Cost as expected_cost,
        ifnull(sum(purchasedetail.PurchasePrice * purchasedetail.Qty) / sum(purchasedetail.Qty), 0) as actual_cost
    from
        product left join (purchaseorder, purchasedetail)
        on (
            purchasedetail.ProdId = product.ProdID
                and purchaseorder.PurchaseID = purchasedetail.PurchaseID
                and purchaseorder.PurchaseDate between '2016-01-01' and '2016-12-31')
    group by name, expected_cost
)
select
    name as prodname,
    expected_cost as cost,
    actual_cost as 實際成本,
    if(actual_cost > 0,
       expected_cost - actual_cost,
       '-') as 成本差異
from product
order by 成本差異 desc, (cast(cost as char(114514)));
