# import mysql.connector as mysql
# import pandas as pd

# conn=mysql.connect(
#     host='localhost',
#     user='root',
#     password='Coffee&Code#2024',
#     database='superstore_sales_data'
# )
# print("MyAQL Database connected successfully!")  # Confirmation message

# query="SELECT * FROM superstore_sales_data" # SQL query to fetch all data from the table
# df=pd.read_sql(query,conn)  # Load the SQL query result into a DataFrame

# print("Data loaded successfully from MySQL database!")  # Confirmation message

# print("--------------------------")
# print("                          ")
# print("First 5 rows of the DataFrame:")
# print(df.head())  # Display the first few rows of the DataFrame
# print("--------------------------")
# print("                          ") 


# conn.close()  # Close the database connection
# print("MySQL Database connection closed.")  # Confirmation message



import pandas as pd
from sqlalchemy import create_engine
import mysql.connector as mysql

# Step 1: Load CSV into a DataFrame
csv_path = 'data/generated_sales_data.csv'
df = pd.read_csv(csv_path)
print("✅ CSV loaded successfully!")

# Step 2: Create SQLAlchemy engine for MySQL connection
user = "root"
password = "Coffee&Code#2024"
host = "localhost"
database = "superstore_sales_data"

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# Step 3: Insert DataFrame into MySQL (creates 'sales_table' table)
df.to_sql(name='sales_table', con=engine, if_exists='replace', index=False)
print("✅ Data inserted into MySQL as 'sales_table'")

# Step 4 (Optional): Verify by querying first 5 rows
conn = mysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
query = "SELECT * FROM sales_table LIMIT 5"
verify_df = pd.read_sql(query, conn)
print("✅ Preview of inserted data:")
print(verify_df)

conn.close()
print("🔒 MySQL connection closed.")