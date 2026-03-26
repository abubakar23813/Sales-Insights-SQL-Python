---DATA--
SELECT *
FROM Sales.[100_sales_Records];

--Total Sales--
SELECT 
	SUM(Total_Revenue)
FROM Sales.[100_sales_Records];

-- Top Items --
SELECT TOP 5
	Item_Type,
	SUM(Total_Revenue) AS Total
FROM Sales.[100_sales_Records]
GROUP BY Item_Type
ORDER BY Total DESC;

-- Region Wise Sales --
SELECT 
	Region,
	SUM(Total_Revenue) AS Total
FROM Sales.[100_sales_Records]
GROUP BY Region
ORDER BY Total DESC;


-- Highest Profit --
SELECT 
	Item_Type,
		SUM(Total_Profit) AS Total
FROM Sales.[100_sales_Records]
GROUP BY Item_Type
ORDER BY Total DESC;



-- Highest Profitable Region --
SELECT 
	Region,
		SUM(Total_Profit) AS Total
FROM Sales.[100_sales_Records]
GROUP BY Region
ORDER BY Total DESC;

--KEY INSIGHT --
/*
- Cosmetics is the highest selling product category, generating the most revenue. This suggests strong and consistent customer demand in the beauty segment.

- Office Supplies and Household items also contribute significantly, indicating that daily-use products have stable and high sales performance.

- Sub-Saharan Africa is the top-performing region, followed by Europe and also most profitable Region. This indicates that these markets have the highest customer base or demand and Protiable.

- Fruits category has the lowest revenue, which may suggest low pricing, low demand, or limited availability
*/