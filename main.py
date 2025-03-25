import pandas as pd
df = pd.read_csv('Students_Grading_Dataset.csv')
df.info() #info about columns and number of values there 
print(df.head()) #first 5 rows
print(df.tail()) #last 5 rows

print(df.describe())   # basic statistics (mean, std, etc.) - using count we understood that there 516 missing values (10%), so we need to replace it. it is to many to delete 
print(df['Attendance (%)'].skew()) #because it is -0.03859979161769357 which is nearly 0 (<0.5 and >-0.5), we assume the data to be balanced; so we will fill missing values with mean
df['Attendance (%)'] = df['Attendance (%)'].fillna(df['Attendance (%)'].mean()) #now there are no missing values 

print(df['Assignments_Avg'].skew()) #it is also inside the balanced range
df['Assignments_Avg'] = df['Assignments_Avg'].fillna(df['Assignments_Avg'].mean())

print(df['Stress_Level (1-10)'].value_counts())
df.info() #info about columns and number of values there 

#because we have only 3206 values about Parent_Education_Level, it is the best way to just fill missing values with "Unknown". Filling mith the most common one will introduce bias and dropping 30% or the whole column is too much
df['Parent_Education_Level'] = df['Parent_Education_Level'].fillna('Unknown')
df.info()

print(df.groupby('Parent_Education_Level')['Total_Score'].mean()) #because each of final score has mean of 69 points, it is not connected to parents' education level

print(df.groupby('Gender')['Total_Score'].mean()) #they also have approximately same score, so it doesn't matter 

print(df.groupby('Attendance (%)')['Total_Score'].mean()) #it is inconvenient to use this type, because there are 5000 values of attendance and 5000 values of final score
print(df[['Attendance (%)', 'Total_Score']].corr()) #it is better to search correlation in this case; however, here correlation is slightly negative. it might be thought that as attendance increases, the final score descreases, but it is too small and insignificant, so we assume that there is no correlation between attendance and final score. +0.3 to +0.5 is Weak correlation Positive; 0 to ±0.3 Very weak positive or no correlation; -0.3 to -0.5	Weak negative correlation

print(df[['Age', 'Total_Score']].corr()) #very very small positive correlation, we assume there is no correlation

print(df.groupby('Department')['Total_Score'].mean()) #again very small difference, so no real correlation 

print(df[['Midterm_Score', 'Total_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df[['Assignments_Avg', 'Total_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Quizzes_Avg', 'Total_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Participation_Score', 'Total_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df[['Projects_Score', 'Total_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df[['Projects_Score', 'Total_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df.groupby('Parent_Education_Level')['Final_Score'].mean()) #because each of final score has mean of 69 points, it is not connected to parents' education level

print(df[['Final_Score', 'Total_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Study_Hours_per_Week', 'Total_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df[['Stress_Level (1-10)', 'Total_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Sleep_Hours_per_Night', 'Total_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df.groupby('Extracurricular_Activities')['Total_Score'].mean()) #there is no real difference between attending or not attending

print(df.groupby('Internet_Access_at_Home')['Total_Score'].mean()) #there is no real difference between attending or not attending

print(df.groupby('Family_Income_Level')['Total_Score'].mean()) #there is no real difference between attending or not attending

print(df.groupby('Gender')['Final_Score'].mean()) #they also have approximately same score, so it doesn't matter 

print(df.groupby('Attendance (%)')['Final_Score'].mean()) #it is inconvenient to use this type, because there are 5000 values of attendance and 5000 values of final score
print(df[['Attendance (%)', 'Final_Score']].corr()) #it is better to search correlation in this case; however, here correlation is slightly negative. it might be thought that as attendance increases, the final score descreases, but it is too small and insignificant, so we assume that there is no correlation between attendance and final score. +0.3 to +0.5 is Weak correlation Positive; 0 to ±0.3 Very weak positive or no correlation; -0.3 to -0.5	Weak negative correlation

print(df[['Age', 'Final_Score']].corr()) #very very small negative correlation, we assume there is no correlation

print(df.groupby('Department')['Final_Score'].mean()) #again very small difference, so no real correlation 

print(df[['Midterm_Score', 'Final_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Assignments_Avg', 'Final_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Quizzes_Avg', 'Final_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Participation_Score', 'Final_Score']].corr()) #very very very small positive correlation, so we assume there is no correlation

print(df[['Projects_Score', 'Final_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df[['Projects_Score', 'Final_Score']].corr()) #very very very small negative correlation, so we assume there is no correlation

print(df['Grade'].value_counts())

print(df.groupby('Grade')['Attendance (%)'].mean()) #there is a positive relationship between attendance and getting A or B, however it is not as straigthforward in C, D and F cases

print(df['Extracurricular_Activities'].value_counts())
print(df['Internet_Access_at_Home'].value_counts())
print(df['Family_Income_Level'].value_counts())

print(df.groupby('Grade')['Midterm_Score'].mean()) #there is a small relationship
print(df.groupby('Grade')['Assignments_Avg'].mean()) #there is a small relationship
print(df.groupby('Grade')['Quizzes_Avg'].mean()) #there is a small relationship
print(df.groupby('Grade')['Participation_Score'].mean()) #there is a small relationship
print(df.groupby('Grade')['Projects_Score'].mean()) #there is a small relationship
print(df.groupby('Grade')['Study_Hours_per_Week'].mean()) #there is a small relationship
print(df.groupby('Grade')['Stress_Level (1-10)'].mean()) #there is a small relationship
print(df.groupby('Grade')['Sleep_Hours_per_Night'].mean()) #there is a small relationship

print(df.groupby('Grade')['Total_Score'].mean()) #there is a small relationship
print(df.groupby('Grade')['Final_Score'].mean()) #there is a small relationship

print(df.groupby('Parent_Education_Level')['Grade'].value_counts(normalize=True).unstack().round(2)) #students with parents who have PhD have a slightly more chanche of getting an A, however it is very small (2-4%)
print(df.groupby('Department')['Grade'].value_counts(normalize=True).unstack().round(2)) #those who chose engineering have bigger chance of getting A rather than other departments (3-5%), however it is not as vivid in other grade categories
print(df.groupby('Extracurricular_Activities')['Grade'].value_counts(normalize=True).unstack().round(2)) #those who has no extras are more likely to get A and F, but in other grades they are less likely, although the relationship is small (2-4%)
print(df.groupby('Internet_Access_at_Home')['Grade'].value_counts(normalize=True).unstack().round(2)) #no real relationship
print(df.groupby('Family_Income_Level')['Grade'].value_counts(normalize=True).unstack().round(2)) #no real relationship
print(df.groupby('Gender')['Grade'].value_counts(normalize=True).unstack().round(2)) #no real relationship


