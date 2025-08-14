import pandas as pd

# load data 
df = pd.read_csv("/home/philip-kasumbi/Desktop/student education/Student_performance_data _.csv")

print(df.columns)
# check for duplicates
print(df.duplicated().sum())

# check for null values 
print(df.isnull().sum())



# change columns values and their data types
df['Gender'] = df['Gender'].replace({0:"Male",1:"Female"})
df['Gender'] = df['Gender'].astype(object)
df['Ethnicity'] = df['Ethnicity'].replace({0:'Caucasian',1:'African American',2:'Asian',3:'Other'})
df['Ethnicity'] = df['Ethnicity'].astype(object)
df['ParentalEducation'] = df['ParentalEducation'].replace({0:'None',1:'High School',2:'Some College',3:"Bachelor's",4:'Higher'})
df['ParentalEducation'] = df['ParentalEducation'].astype(object)

df['StudyTimeWeekly'] = df['StudyTimeWeekly'].round(1) 
df['Tutoring'] = df['Tutoring'].replace({1:"Yes",0:"No"})
df['Tutoring'] = df['Tutoring'].astype(object)

df['ParentalSupport'] = df['ParentalSupport'].replace({0:'None',1:'Low',2:'Moderate',3:"High",4:'Very High'})
df['ParentalSupport'] = df['ParentalSupport'].astype(object)

df['Extracurricular'] = df['Extracurricular'].replace({1:"Yes",0:"No"})
df['Extracurricular'] = df['Extracurricular'].astype(object)

df['Sports'] = df['Sports'].replace({1:"Yes",0:"No"})
df['Sports'] = df['Sports'].astype(object)

df['Music'] = df['Music'].replace({1:"Yes",0:"No"})
df['Music'] = df['Music'].astype(object)

df['Volunteering'] = df['Volunteering'].replace({1:"Yes",0:"No"})
df['Volunteering'] = df['Volunteering'].astype(object)
df['GPA'] = df['GPA'].round(1) 

def grade_mapping(x):
    if x >= 3.5:
        return "A"
    elif x >= 3.0:
        return "B"
    elif x >= 2.5:
        return "C"
    elif x >= 2.0:
        return "D"
    else:
        return "F"

df['Grade_Class'] = df['GradeClass'].apply(grade_mapping)

# check datatypes
print(df.dtypes)
print(df.head())

df.to_csv("/home/philip-kasumbi/Desktop/student education/cleaned.csv")