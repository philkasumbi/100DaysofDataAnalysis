import pandas as pd
import numpy as np

# load data 
df = pd.read_csv("/home/philip-kasumbi/Desktop/cafe_sales/dirty_cafe_sales.csv")
print(df)

# duplicates and null values 
print(df.duplicated().sum())
# print(df.isnull().sum())

# delete rows where item is unknown/nan/error
df = df.dropna(subset=['Item'])
df = df[~df['Item'].isin(['UNKNOWN','ERROR'])]
print(df['Item'].unique())

# delete rows where Quantity is unknown/nan/error
df = df.dropna(subset=['Quantity'])
df = df[~df['Quantity'].isin(['UNKNOWN','ERROR'])]
df['Quantity'] = df['Quantity'].astype(int)

# price per unit column
df['Price Per Unit'] = df['Price Per Unit'].replace(['UNKNOWN','ERROR'],np.nan)
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'],errors='coerce') 
df['Price Per Unit'] = df.groupby('Item')['Price Per Unit'].transform(lambda x : x.fillna(x.median()))

# total spent column
df['Total Spent'] = df['Total Spent'].replace(['UNKNOWN','ERROR'],np.nan)
df['Total Spent'] = pd.to_numeric(df['Total Spent'],errors='coerce')
df['Total Spent'] = df['Total Spent'].fillna(df['Quantity']*df['Price Per Unit'])

# payment method column
df['Payment Method'] = df['Payment Method'].replace('ERROR','UNKNOWN')
df['Payment Method'] = df['Payment Method'].fillna('UNKNOWN')

# location column
df['Location'] = df['Location'].fillna('UNKNOWN')
df['Location'] = df['Location'].replace('ERROR','UNKNOWN')

# Transaction Date column
df['Transaction Date'] = df['Transaction Date'].replace(['UNKNOWN','ERROR'],np.nan)
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'],errors='coerce')
df = df.dropna(subset=['Transaction Date'])


# break the date columns
df['Day'] = df['Transaction Date'].dt.day_name()
df['Month'] = df['Transaction Date'].dt.month_name()



print(df.dtypes)
print(df.isnull().sum())

print(df.shape[1])
print(df.info())

df.to_csv('/home/philip-kasumbi/Desktop/cafe_sales/Cleaned_cafe_sales.csv')