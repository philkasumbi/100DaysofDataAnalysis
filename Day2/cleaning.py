import pandas as pd
# load data 
df = pd.read_csv("/home/philip-kasumbi/Desktop/online retail/Online_Retail.csv")

pd.set_option("display.max_rows",5050)


# remove duplicates
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())


#Remove the InvoiceNo that starts with C(cancelled)
rows_to_remove = df[df["InvoiceNo"].str.startswith(('C','c'),na=False)]
df.drop(rows_to_remove.index,inplace=True)
# confirm if all are deleted
print(df[df["InvoiceNo"].str.startswith(('C','c'),na=False)]) # empty data frame

# remove rows where the unit price is 0
zero_unitprice = df[df['UnitPrice'] == 0.0]
df.drop(zero_unitprice.index,inplace=True)
print(df[df['UnitPrice'] == 0.0]) #empty data frame

# remove rows where Quantity is zero or negative
negated_quantity = df[df['Quantity'] <= 0]
df.drop(negated_quantity.index,inplace=True)

# convert columns to their preffered datatypes
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceNo'] = pd.to_numeric(df['InvoiceNo'])
print(df.dtypes)

# replace the null values to unknown
df['CustomerID'] = df['CustomerID'].replace(" ","Unknown")

# remove any trailing spaces in these columns
df['Country'] = df['Country'].str.strip()
df['Description'] = df['Description'].str.strip()

# create column for total price
df['Total Price'] = (df['UnitPrice'] * df['Quantity']).round(2)


print(df.info())
print(df.describe())
print(df.head(10))

df.to_csv("Cleaned_Online_Retail.csv",index=False)

# Analysis
print(df['Country'].nunique())
# get the top countries by total sales 
top_countries = df.groupby("Country")["Total Price"].sum().sort_values(ascending=False).head()

print(top_countries)

# top products by revenue
Top_products = df.groupby("Description")["Total Price"].sum().sort_values(ascending=False).head()
print(Top_products)

# top products by quantity
Top_products_by_quantity = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head()
print(Top_products_by_quantity)

# rarely products by quantity
low_products_by_quantity = df.groupby("Description")["Quantity"].sum().sort_values().head()
print(low_products_by_quantity)
