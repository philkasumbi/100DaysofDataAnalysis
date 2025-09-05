import pandas as pd
import re

df = pd.read_csv("C:/Users/KMTC KITUI CYBER/Desktop/data analysis/Perfumes_dataset.csv")
# pd.set_option('display.max_rows',1010)
# pd.set_option('display.max_columns',20)

# capitalize the brand column
df['brand'] = df['brand'].str.capitalize()
print(df['brand'].nunique())
df['brand'] = df['brand'].str.strip()

# perfume 
print(df['perfume'].nunique())
df['perfume'] = df['perfume'].str.capitalize().str.strip()

# type 
df['type'] = df['type'].replace({"edp":"EDP","edt":"EDT","parfum":"Parfum"})
print(df['type'].unique())
result = df['type'] == "Extrait de Parfum"
print(result.sum())

# drop rows where the type is Type
# df.drop(df[df['type'] == "Type"].index)
df = df[df['type']!= 'Type']
type = df['type'] =="Type"
print(type.sum())
# style the headers
# df.columns = df.columns.str.upper()

# category
print(df['category'].nunique())
df['category'] = df['category'].str.strip() 

# target
# delete where target audience is gourmand 
df = df[df['target_audience'] != 'Gourmand']
Gourmand = df['target_audience'] == 'Gourmand'
print(Gourmand.sum())

df['target_audience'] = df['target_audience'].replace({"Men":"Male","Women":"Female"}).str.strip()
print(df['target_audience'].unique())

# longevity
df['longevity'] = df['longevity'].replace(r':contentReference\[.*?\]\{.*?\}',"",regex=True).str.strip()
df['longevity'] = df['longevity'].replace({"Medium–Strong":"Strong","Light–Medium":"Medium","Very Strong":"Strong","6–8 hours":"Strong"})

df['longevity'] = df['longevity'].str.strip()
print(df['longevity'].unique()) 

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print(df.isnull().sum())

print(df.info())
print(df.dtypes)
print(df.shape)
print(df.head(10))

df.to_csv("C:/Users/KMTC KITUI CYBER/Desktop/data analysis/cleaned_perfume_dataset.csv",index=False)
