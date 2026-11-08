# Power BI Model

Tables: Orders (fact), Customers, Products, Date (calendar).

Relationships:
- Customers[Customer_ID] 1 -> * Orders[Customer_ID]
- Products[Subcategory] 1 -> * Orders[Subcategory]
- Date[Date] 1 -> * Orders[Order_Date]

Date table:
Date = ADDCOLUMNS(CALENDAR(MIN(Orders[Order_Date]),MAX(Orders[Order_Date])),
"Year",YEAR([Date]),"Month",FORMAT([Date],"MMM"),
"Month Number",MONTH([Date]),"Year Month",FORMAT([Date],"YYYY-MM"),
"Quarter","Q"&FORMAT([Date],"Q"))

Dashboard pages:
1. Executive Overview — Sales, Profit, Margin, Orders, AOV, Return Rate, trend, category/state.
2. Customer & Channel — customer segments, channels, AOV.
3. Operations — on-time %, late orders, ratings, returns.
4. Profitability — discount bands, category margin, regional profitability.

Recommended slicers: Year, Month, State, Category, Channel, Customer Segment, Payment Method.
