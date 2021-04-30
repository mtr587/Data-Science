import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('covid_19_data.csv')

print('1. Find null value.')
a = df.isnull().sum()
print(a)

print('2. Draw heatmap.')
sns.heatmap(df.isnull())
# plt.show()

print('3. Show the number of Confirmed, Deaths and Recovered cases in each Region.')
b = df.groupby('Region').sum()
print('Confirmed case by Region.')
confirmed_case = df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)
print(b)
print(confirmed_case)

print('4. Remove all records where confirmed case less than 10.')
df = df[~(df['Confirmed'] < 10)]

print('5. In which Region, maximum number of Confirmed cases were recorded?')
maximum_num_confirmed = df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)
print(maximum_num_confirmed)

print('6. How many Confirmed, Deaths and Recovered cases were reported from India till 4/29/2020.')
india = df[df['Region'] == 'India']
print(india)

print('7. Sort the entire data with respect to number of Confirmed cases in ascending order.')
sort_by_confirmed = df.sort_values(by=['Confirmed'], ascending=True)
print(sort_by_confirmed)