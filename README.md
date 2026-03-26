# Global Sales Data Analysis: From Raw Data to Real Insights

I recently completed a project that I'm really excited about—a full data analysis of over 100 global sales records. As a B.Com student diving into Data Science, this was my chance to bring together everything I’ve been learning: cleaning messy data, spotting trends, and building a complete pipeline from Python to a professional SQL Server database.

It was more than just running code—it was about uncovering what the numbers were really saying about the business.

---

# What I Used

· Python (Pandas for cleaning, Matplotlib for visuals, and SQLAlchemy to connect everything)
· SQL Server (where I organized the data under a custom Sales schema, just like in a real enterprise setup)

---

# How I Structured the Project

· 100 Sales Records.csv – The raw data with global sales, regions, and product categories.
· main.py – The Python script that does the heavy lifting: cleaning, exploring the data, and connecting securely to the database.
· SQLPROJECT FILE.sql – A set of SQL queries that calculate totals, rank regions, and break down performance by product.

---

# What I Discovered

Once the data was clean and organized, a few really interesting insights emerged:

1. Cosmetics are the clear winner – They’re the top revenue driver, which makes sense given strong margins and consistent demand.
2. Africa (Sub-Saharan) and Europe lead in profit – Two very different markets, both showing major growth potential.
3. Office Supplies and Household items are the steady performers – These categories might not be flashy, but they’re reliable and essential.
4. February is the busiest month – Sales peak here, likely due to post-holiday restocking or early-year planning.

---

# How to Run It (If You Want to Try)

If someone wants to test this out, here’s the simple version:

1. Set up a schema called Sales in SQL Server and run the provided SQL script to build the tables.
2. In the Python script (main.py), update the server name to your local setup:
   ```python
   server = r"YOUR_SERVER_NAME\SQLEXPRESS"
   ```
3. Install the needed libraries:
   ```bash
   pip install pandas sqlalchemy pyodbc matplotlib
   ```
4. Run main.py and watch the analysis come to life.

---

# A Little About Me

I’m a B.Com student with a growing passion for data science. For me, this project wasn’t just about technical skills—it was about proving that I can take real-world data, clean it up, analyze it, and turn it into insights that actually matter. I love bridging the gap between business knowledge and technical tools like Python and SQL.# Sales-Insights-SQL-Python
A comprehensive data analysis project using Python (Pandas) and SQL Server to extract business insights from global sales records, featuring a custom Sales schema for better data organization
