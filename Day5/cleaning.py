import pandas as pd

# load the data 
df= pd.read_csv("/home/philip-kasumbi/Desktop/Movie Industry/movies.csv")


# check and remove duplicates 
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

# check for null values and fix
print(df.isnull().sum())

df['rating'] = df['rating'].fillna("Not rated")
df['rating'] = df['rating'].replace({"Unrated":"Not rated","Not Rated":"Not rated","TV-PG":"PG"})
df['score'] = df['score'].fillna(df['score'].median())
df['votes'] = df['votes'].fillna(0)
df['writer'] = df['writer'].fillna("Unknown")
df['star'] = df['star'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
# budget and gross = find the median budget,gross for every genre
df['budget'] = df.groupby('genre')['budget'].transform(lambda x: x.fillna(x.median()))
df['gross'] = df.groupby('genre')['gross'].transform(lambda x: x.fillna(x.median()))
df.dropna(subset=['budget','gross'],inplace=True)
df['company'] = df['company'].fillna("Unkown")
df['runtime'] = df.groupby('genre')['runtime'].transform(lambda x:x.fillna(x.median())) 

# stardazing columns 
df[['released_date','released_country']] = df['released'].str.split(' (',expand=True,regex=False)
df['released_country'] = df['released_country'].str.replace(')','')
print(df['genre'].unique())


df['released_date'] = df['released_date'].fillna(df['year'].astype(str))
df['released_country'] = df['released_country'].fillna("Unknown")


# drop the released column
df.drop(columns='released',inplace=True)

# change datatype
df[['votes','budget','runtime','gross']] = df[['votes','budget','runtime','gross']].astype(int) 
df['released_date'] = pd.to_datetime(df['released_date'],errors='coerce')
df['released_date'] = df['released_date'].fillna("Unknown")


print(df.head())
print(df.dtypes)

# create profit column
df['Profit'] = df['gross'] - df['budget']


print(df.describe())
df.to_csv("/home/philip-kasumbi/Desktop/Movie Industry/cleaned_movies.csv")