import pandas as pd

df = pd.read_csv('Police Data.csv')

print('1. Remove column that only contains missing values.')
a = df.isnull().sum()
print(a)
df.drop(columns='country_name', inplace=True)

print('2. For speeding, were men or women stop more often?')
b = df[df['violation'] == 'Speeding']['driver_gender'].value_counts()
print(b)
print('Men speeding more often')

print('3. Does gender affect who gets searched during a stop?')
c = df.groupby('driver_gender').search_conducted.sum()
print(c)
'total search conducted'
total_search_conducted = df['search_conducted'].value_counts()
print(total_search_conducted)           # match print c

print('Mapping + data-type casting')
print('4. What is the mean stop-duration?')
'calculate the mean of each column first.'
df['stop_duration'] = df['stop_duration'].map({'0-15 Min' : 7.5, '16-30 Min' : 22.5, '30+ Min' : 45})
d = df['stop_duration'].mean()
print(df)
print(d)

print('5. Compare the age distributions for each violation.')
e = df.groupby('violation')['driver_age'].describe()
print(e)