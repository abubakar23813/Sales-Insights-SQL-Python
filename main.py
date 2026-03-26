import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import urllib



df = pd.read_csv("100 Sales Records.csv")
print(df.head())
print(df.columns)

#Checking Missing Values
print(df.isnull().sum())

#Handling Missing Values
df = df.dropna()

# Basic analysis
print(df.info())
print(df.describe())

# Total Sales
Total_sales = df["Total Revenue"].sum()
print("Total Sales:",Total_sales)

# Top Products
Top_Products = df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False)
print("Top Sold Products:",Top_Products)

#Top Regions
Top_Regions = df.groupby("Region")["Total Revenue"].sum().sort_values(ascending=False)
print("Top Sold Regions:",Top_Regions)

#Top Sales Channel
Top_Sales_Channel = df.groupby("Sales Channel")["Total Revenue"].sum().sort_values(ascending=False)
print("Top Sold Channel Revenue:",Top_Sales_Channel)

# Monthly Sales
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
Monthly_Sales = df.groupby("Month")["Total Revenue"].sum()
print("Monthly Sales:",Monthly_Sales)
#Feb record highest sale of the year : 24740517.77

#Graph
Monthly_Sales.plot(kind="bar")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
# ===  KEY INSIGHT===

# Cosmetics is the highest selling product category, generating the most revenue. This suggests strong and consistent customer demand in the beauty segment.

#Office Supplies and Household items also contribute significantly, indicating that daily-use products have stable and high sales performance.

#Sub-Saharan Africa is the top-performing region, followed by Europe. This indicates that these markets have the highest customer base or demand.

#Offline sales are higher than online sales, showing that traditional sales channels are still dominant in this dataset.

#Sales peak in February and November, suggesting possible seasonal trends such as bulk purchasing or festive demand during these months.

#Very low sales in August and March may indicate off-season periods or reduced customer activity.

#Fruits category has the lowest revenue, which may suggest low pricing, low demand, or limited availability.


#connection details
server = r"DESKTOP-MDHNOTM\SQLEXPRESS"
database = "SalesDB"
driver = "{ODBC Driver 17 for SQL Server}"

# connecting server
connection_string = f"DRIVER={driver};"f"SERVER={server};"f"DATABASE={database};"f"Trusted_Connection=yes"
params = urllib.parse.quote_plus(connection_string)


#SQLAlchemy Engine
engine = create_engine(f"mssql+pyodbc://?odbc_connect={params}")

try:
    query = "SELECT * FROM Sales.[100_sales_Records]"
    df = pd.read_sql(query, engine)
    print("connection successful")
    print(df.head())
except Exception as e:
    print("ERROR:",e)

# Top Items
query_1 = """SELECT TOP 5 *
FROM(
    SELECT
        Item_Type,
        SUM(Total_Revenue) as total
    FROM Sales.[100_sales_Records]
    GROUP BY Item_Type
) AS sub
ORDER BY total DESC"""
df_top = pd.read_sql(query_1, engine)
print(df_top)

#Region analysis
query_2 = """SELECT *
FROM(
    SELECT
        Region,
        SUM(Total_Revenue) as total
    FROM Sales.[100_sales_Records]
    GROUP BY Region
) AS sub
ORDER BY total DESC"""
df_region = pd.read_sql(query_2, engine)
print(df_region)


# Visualisation
df_top.plot(x="Item_Type",y="total",kind="bar")
plt.title("Top Items")
plt.xlabel("Item Type")
plt.ylabel("Total Revenue")
plt.show()











