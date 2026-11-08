-- Business SQL analysis
SELECT DATE_TRUNC('month', Order_Date) month, SUM(Sales) revenue, SUM(Profit) profit, COUNT(*) orders
FROM orders GROUP BY 1 ORDER BY 1;

SELECT Category, SUM(Sales) revenue, SUM(Profit) profit,
       ROUND(SUM(Profit)/NULLIF(SUM(Sales),0)*100,2) margin_pct
FROM orders GROUP BY Category ORDER BY revenue DESC;

SELECT State, SUM(Sales) revenue, SUM(Profit) profit, COUNT(*) orders,
       ROUND(AVG(Customer_Rating),2) avg_rating
FROM orders GROUP BY State ORDER BY revenue DESC;

SELECT Delivery_Status, COUNT(*) orders, ROUND(AVG(Customer_Rating),2) avg_rating,
       ROUND(AVG(Returned)*100,2) return_rate_pct, SUM(Profit) profit
FROM orders GROUP BY Delivery_Status;

SELECT CASE WHEN Discount_Pct < .10 THEN '<10%' WHEN Discount_Pct < .20 THEN '10-20%'
            WHEN Discount_Pct < .30 THEN '20-30%' ELSE '30%+' END discount_band,
       COUNT(*) orders, SUM(Sales) revenue, SUM(Profit) profit, AVG(Profit) avg_profit
FROM orders GROUP BY 1 ORDER BY 1;

WITH m AS (SELECT DATE_TRUNC('month',Order_Date) month,SUM(Sales) revenue FROM orders GROUP BY 1)
SELECT month,revenue,LAG(revenue) OVER(ORDER BY month) previous_month,
       ROUND((revenue-LAG(revenue) OVER(ORDER BY month))/NULLIF(LAG(revenue) OVER(ORDER BY month),0)*100,2) mom_growth_pct
FROM m ORDER BY month;
