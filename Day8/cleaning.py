import pandas as pd 

df = pd.read_csv("/home/philip-kasumbi/Desktop/Health_risk_Data/Health_Risk_Dataset.csv")


df['Consciousness'] = df['Consciousness'].replace({"A":"Alert","P":" Pain response","C":"Confusion","V":"Verbal","U":"Unresponsive"})
df['On_Oxygen'] = df['On_Oxygen'].replace({0:"No",1:"Yes"})
print(df)

df.to_csv("/home/philip-kasumbi/Desktop/Health_risk_Data/Cleaned_Health_Risk_Dataset.csv")