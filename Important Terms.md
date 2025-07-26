# 📘 Important Terms in Data Analysis (with pandas)

## 📊 1. DataFrame
A two-dimensional, labeled data structure — like an Excel spreadsheet in memory.  
✅ Example: rows = records, columns = fields  
✅ Comes from the pandas library.  
```python
import pandas as pd
df = pd.read_csv("data.csv")  # df is a DataFrame
```

## 🔣 2. Series
A one-dimensional labeled array (like a column or row of a DataFrame).  
```python
df["Sales"]  # is a Series
```

## 📁 3. CSV (Comma-Separated Values)
A common file format used to store tabular data as plain text.  
```python
df = pd.read_csv("data.csv")
```

## 🔄 4. Index
The labels or row numbers that identify rows in a DataFrame.  
Can be default (0,1,2,...) or a custom column.

## 🧼 5. Missing Values
Empty or NaN (Not a Number) cells that need to be handled before analysis.  
```python
df.isnull().sum()
```

## 🔍 6. EDA (Exploratory Data Analysis)
The process of exploring data using statistics and visualizations.  
✅ Goal: Discover trends, outliers, patterns  
✅ Tools: describe(), value_counts(), plots, etc.

## 🧹 7. Data Cleaning
Removing or correcting invalid, missing, or inconsistent data.  
Examples:
- Filling NaNs
- Removing duplicates
- Converting data types

## 📏 8. Shape
Returns the number of rows and columns in a DataFrame.  
```python
df.shape  # (1000, 10)
```

## 🔢 9. dtypes (Data Types)
Data type of each column: int, float, object (string), datetime, etc.  
```python
df.dtypes
```

## 📈 10. Aggregation
Summarizing data using functions like sum, mean, count, etc.  
```python
df.groupby("City")["Sales"].sum()
```

## 🧱 11. Pivot Table
Restructures data for summarization, like Excel pivot tables.  
```python
df.pivot_table(values="Sales", index="City", columns="Category")
```

## 🧮 12. GroupBy
Groups rows by column(s) and allows aggregation within groups.  
```python
df.groupby("Product Category")["Profit"].mean()
```

## 🪣 13. Value Counts
Counts frequency of unique values in a column.  
```python
df["City"].value_counts()
```

## 🔎 14. Filtering / Querying
Selecting rows based on conditions.  
```python
df[df["Sales"] > 500]
```

## 🖇️ 15. Merging / Joining
Combining two DataFrames using a common key (like SQL JOINs).  
```python
pd.merge(df1, df2, on="Customer ID")
```

## 🧱 16. Concatenation
Stacking DataFrames vertically or horizontally.  
```python
pd.concat([df1, df2])
```

## 📅 17. Datetime Conversion
Converting columns to date/time format for time-based analysis.  
```python
df["Order Date"] = pd.to_datetime(df["Order Date"])
```

## 📉 18. Outlier
A data point that is significantly different from others.  
Often removed or flagged during EDA.

## 📐 19. Correlation
A measure of how strongly two variables are related.  
```python
df.corr()
```

## 📊 20. Visualization
Plotting data to gain insights.  
Popular libraries:
- matplotlib
- seaborn
- plotly
