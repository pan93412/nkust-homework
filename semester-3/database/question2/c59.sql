-- 列出2016-2018三年中，銷售業績持續成長的產品, 列出產品名稱，2018業績，2017業績，2016業績

WITH sales_2016 AS (SELECT product.ProdName,
                           IFNULL(SUM(orderdetail.Discount * orderdetail.Qty * product.UnitPrice), 0) AS feat
                    FROM product
                             LEFT JOIN (orderdetail, salesorder) ON (
                                product.ProdID = orderdetail.ProdId
                            AND orderdetail.OrderID = salesorder.OrderID
                            AND salesorder.OrderDate BETWEEN '2016-01-01' AND '2016-12-31'
                        )
                    GROUP BY product.ProdName
                    ORDER BY feat)
   , sales_2017 AS (SELECT product.ProdName,
                           IFNULL(SUM(orderdetail.Discount * orderdetail.Qty * product.UnitPrice), 0) AS feat
                    FROM product
                             LEFT JOIN (orderdetail, salesorder) ON (
                                product.ProdID = orderdetail.ProdId
                            AND orderdetail.OrderID = salesorder.OrderID
                            AND salesorder.OrderDate BETWEEN '2017-01-01' AND '2017-12-31'
                        )
                    GROUP BY product.ProdName
                    ORDER BY feat)
   , sales_2018 AS (SELECT product.ProdName,
                           IFNULL(SUM(orderdetail.Discount * orderdetail.Qty * product.UnitPrice), 0) AS feat
                    FROM product
                             LEFT JOIN (orderdetail, salesorder) ON (
                                product.ProdID = orderdetail.ProdId
                            AND orderdetail.OrderID = salesorder.OrderID
                            AND salesorder.OrderDate BETWEEN '2018-01-01' AND '2018-12-31'
                        )
                    GROUP BY product.ProdName
                    ORDER BY feat)
SELECT sales_2018.ProdName AS '產品名稱',
       sales_2018.feat     AS '業績2018',
       sales_2017.feat     AS '業績2017',
       sales_2016.feat     AS '業績2016'
FROM sales_2016
     CROSS JOIN sales_2017 ON (sales_2016.ProdName = sales_2017.ProdName)
     CROSS JOIN sales_2018 ON (sales_2016.ProdName = sales_2018.ProdName)
WHERE
    sales_2018.feat > sales_2017.feat
AND sales_2017.feat > sales_2016.feat
ORDER BY sales_2016.ProdName;
