import pandas as pd

# load data
df = pd.read_csv("/home/philip-kasumbi/Desktop/Hotel booking/hotel_bookings.csv")
pd.set_option("display.max_columns",35)

# drop duplicates
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print(df.shape)

# sorting the null values 
print(df.isnull().sum())
df['company'] = df['company'].fillna("None")
df['agent'] = df['agent'].fillna("None")
df['country'] = df['country'].fillna("Unknown")

# converting columns to their preffered data types
df['children'] = df['children'].fillna(0).astype(int)
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
print(df.dtypes)

# changing some columns to readable data 
df['is_canceled'] = df['is_canceled'].replace({1:"Y",0:"N"})  
df['is_repeated_guest'] = df['is_repeated_guest'].replace({1:"Y",0:"N"}) 

# remove rows with negative adr
negative_adr = df[df["adr"]<0]
df.drop(negative_adr.index,inplace=True)

# add useful columns
df['Total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
df['Total_Guests'] = df['adults'] + df['children'] + df['babies']
print(df.columns)

# remove the rows where no quest visited
no_guests = df[df['Total_Guests']==0]
df.drop(no_guests.index,inplace=True)

# replace the undefined to other and remove trailing spaces
df['distribution_channel'] = df['distribution_channel'].replace('Undefined','Other')
df['distribution_channel'] = df['distribution_channel'].str.strip()
df['meal'] = df['meal'].replace('Undefined','Other')
df['meal'] = df['meal'].str.strip()

# empty the rows with NaN values
df = df.fillna("")

# Export to csv
df.to_csv("cleaned_hotel_bookings.csv",index=False)
