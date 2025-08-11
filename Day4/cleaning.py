import pandas as pd

df = pd.read_csv("/home/philip-kasumbi/Desktop/Olympic_history/athlete_events.csv")
pd.set_option("display.max_columns",15)

# check the null values and duplicates
print(df.isnull().sum())
print(df.duplicated().sum())


# remove duplicates
df.drop_duplicates(inplace=True)

# sorting the null values and changing data types
print(df['Age'].unique())
df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
df['Height'] = df['Height'].fillna(df["Height"].median()).astype(float)
df['Weight'] = df['Weight'].fillna(df["Weight"].median()).astype(float)
df['Medal'] = df['Medal'].fillna("No Medal")

# column conversion
df['Sex'] = df['Sex'].replace({'M':'Male','F':'Female'})
 
# stardadizing events 
event_mapping = {
    # Athletics / Track
    "Athletics": "Track & Field",
    "Athletics Men's": "Men's Track & Field",
    "Athletics Women's": "Women's Track & Field",
    "Track And Field": "Track & Field",

    # Football / Soccer
    "Football": "Soccer",
    "Football Men's": "Men's Soccer",
    "Football Women's": "Women's Soccer",
    "Soccer Men's": "Men's Soccer",
    "Soccer Women's": "Women's Soccer",

    # Basketball
    "Basketball Men's": "Men's Basketball",
    "Basketball Women's": "Women's Basketball",
    "Men’s Basketball": "Men's Basketball",  # Fix curly apostrophe
    "Women’s Basketball": "Women's Basketball",

    # Hockey
    "Field Hockey": "Hockey",
    "Ice Hockey": "Hockey (Ice)",
    "Hockey Men's": "Men's Hockey",
    "Hockey Women's": "Women's Hockey",

    # Swimming
    "Swimming Men's": "Men's Swimming",
    "Swimming Women's": "Women's Swimming",
    "Men’s Swimming": "Men's Swimming",
    "Women’s Swimming": "Women's Swimming",

    # Rowing
    "Rowing Men's": "Men's Rowing",
    "Rowing Women's": "Women's Rowing",

    # Volleyball
    "Volleyball Men's": "Men's Volleyball",
    "Volleyball Women's": "Women's Volleyball",
    "Beach Volleyball Men's": "Men's Beach Volleyball",
    "Beach Volleyball Women's": "Women's Beach Volleyball",

    # Tennis
    "Tennis Men's": "Men's Tennis",
    "Tennis Women's": "Women's Tennis",
    "Table Tennis Men's": "Men's Table Tennis",
    "Table Tennis Women's": "Women's Table Tennis"
}
df['Event'] = df['Event'].replace(event_mapping)
df['Event'] = df['Event'].str.strip().str.title()
print(df['Event'].unique())

# drop columns
df.drop(columns="Games",inplace= True)
print(df.head(20))

# create important columns 
df['Medal_Binary'] = df["Medal"].apply(lambda m: 0 if m =="No Medal" else 1)
df['Age_bracket'] = df["Age"].apply(
    lambda x: "Under 20" if x < 20
     else "20-29" if x <30
     else "30+"
     )
df['BMI'] = df['Weight'] / ( (df['Height'] / 100) ** 2 )
df['BMI'] = df['BMI'].round(2)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

df['BMI_Category'] = df['BMI'].apply(bmi_category)


print(df.dtypes)


df.to_csv("/home/philip-kasumbi/Desktop/Olympic_history/cleaned_athlete_events.csv")