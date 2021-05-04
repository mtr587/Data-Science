import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('London Housing Data.csv')

print('1. Count and find null.')
a = df.count()
b = df.isnull().sum()
print(a)
print(b)

print('2. Draw heatmap for null of houses_sold and no_of_crimes.')
sns.heatmap(df.isnull())
# plt.show()

print('3. Convert the datetype of "Date" column to Date-Time format.')
df['date'] = pd.to_datetime(df.date)
print(df['date'])

print('4. Add a new column "year" in the dataframe, which contains years only.')
df['year'] = df.date.dt.year        # dt means only include year in data
# df['month'] = df.date.dt.month
print(df['year'])

print('5. Add a new column "month" as 2nd column in the dataframe, which contain month only.')
df.insert(1, 'month', df.date.dt.month)         # dt.insert(index, 'new column name', new column value)
print(df.head())

print('6. Remove column "year" and "month" from the dataframe.')
#df.drop(['month', 'year'], axis=1, inplace=True)        # axis=1 means column, =0 means index
print(df.head())

print('7. Show all the record where "no_of_crimes" is 0, and, how many such records are there.')
c = df[df['no_of_crimes'] == 0]
print(c)
d = len(df[df['no_of_crimes'] == 0])
print(d)

print('8. What is the maximum and minimum of "average_price" per year in england?')
eg = df[df['area'] == 'england']
print(eg)
eg_max = eg.groupby('year')['average_price'].max()
eg_min = eg.groupby('year')['average_price'].min()
print(eg_max)
print(eg_min)

print('9. Show the total count of records of each area, where average_price is less than 100000.')
f= df[df['average_price'] < 100000]['area'].value_counts()
print(f)