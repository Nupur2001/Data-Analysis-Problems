import pandas as pd
df=pd.read_csv('data/generated_sales_data.csv') # Load the CSV file into a DataFrame
print("Data loaded successfully!")  # Confirmation message
print("--------------------------")
print("                          ")
print("First 5 rows of the DataFrame:")
print(df.head())  # Display the first few rows of the DataFrame

print("--------------------------")
print("                          ")

print("DataFrame Information:")
print(df.info())  # Display information about the DataFrame

print("--------------------------")
print("                          ")

print("Summary Statistics:")
print(df.describe())  # Display summary statistics of the DataFrame

print("--------------------------")
print("                          ")

print("Column Names and Data Types:")
print(df.columns)  # Display the column names of the DataFrame

print("--------------------------")
print("                          ")

print("DataFrame Shape:")
print(df.shape)  # Display the shape of the DataFrame (rows, columns)

print("--------------------------")
print("                          ")

print("Checking for missing values in the DataFrame:")
print(df.isnull().sum())  # Check for missing values in each column


#Output
'''
Summary Statistics:
             Sales       Profit    Discount    Quantity
count   100.000000   100.000000  100.000000  100.000000
mean   2739.928700  -329.635700    0.159600    5.880000
std    1445.675959   495.872529    0.091308    2.832995
min     113.410000 -1759.570000    0.000000    1.000000
25%    1485.017500  -581.210000    0.080000    3.000000
50%    3032.980000  -264.660000    0.170000    6.000000
75%    3958.667500   -33.707500    0.250000    8.000000
max    4965.620000   833.820000    0.290000   10.000000
--------------------------
                          
Column Names and Data Types:
Index(['Order ID', 'Order Date', 'Customer ID', 'City', 'Product Category',
       'Sales', 'Profit', 'Discount', 'Quantity', 'Segment'],
      dtype='object')
--------------------------
                          
DataFrame Shape:
(100, 10)
(venv) (base) nupursikka@Nupurs-MacBook-Pro Super Store Again % clear                        
(venv) (base) nupursikka@Nupurs-MacBook-Pro Super Store Again % python notebooks/data_load.py
Data loaded successfully!
--------------------------
                          
First 5 rows of the DataFrame:
   Order ID  Order Date Customer ID       City Product Category    Sales  Profit  Discount  Quantity      Segment
0  ORD-1001  18/11/2024    CUST-199     Mumbai       Technology  2704.94 -708.51      0.20         1    Corporate
1  ORD-1002  20/10/2024    CUST-653  Hyderabad  Office Supplies  1397.35  313.19      0.01         8     Consumer
2  ORD-1003  23/09/2024    CUST-712    Chennai  Office Supplies  2810.90  518.84      0.08         7  Home Office
3  ORD-1004  29/07/2024    CUST-148  Hyderabad  Office Supplies  4667.93  814.57      0.07         8  Home Office
4  ORD-1005  31/07/2024    CUST-539      Delhi       Technology  3830.57 -569.12      0.02         9    Corporate
--------------------------
                          
DataFrame Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 10 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Order ID          100 non-null    object 
 1   Order Date        100 non-null    object 
 2   Customer ID       100 non-null    object 
 3   City              100 non-null    object 
 4   Product Category  100 non-null    object 
 5   Sales             100 non-null    float64
 6   Profit            100 non-null    float64
 7   Discount          100 non-null    float64
 8   Quantity          100 non-null    int64  
 9   Segment           100 non-null    object 
dtypes: float64(3), int64(1), object(6)
memory usage: 7.9+ KB
None
--------------------------
                          
Summary Statistics:
             Sales       Profit    Discount    Quantity
count   100.000000   100.000000  100.000000  100.000000
mean   2739.928700  -329.635700    0.159600    5.880000
std    1445.675959   495.872529    0.091308    2.832995
min     113.410000 -1759.570000    0.000000    1.000000
25%    1485.017500  -581.210000    0.080000    3.000000
50%    3032.980000  -264.660000    0.170000    6.000000
75%    3958.667500   -33.707500    0.250000    8.000000
max    4965.620000   833.820000    0.290000   10.000000
--------------------------
                          
Column Names and Data Types:
Index(['Order ID', 'Order Date', 'Customer ID', 'City', 'Product Category',
       'Sales', 'Profit', 'Discount', 'Quantity', 'Segment'],
      dtype='object')
--------------------------
                          
DataFrame Shape:
(100, 10)
--------------------------
                          
Checking for missing values in the DataFrame:
Order ID            0
Order Date          0
Customer ID         0
City                0
Product Category    0
Sales               0
Profit              0
Discount            0
Quantity            0
Segment             0
dtype: int64
'''
