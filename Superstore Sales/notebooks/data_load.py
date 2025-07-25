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