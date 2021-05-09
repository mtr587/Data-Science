import pandas as pd

df = pd.read_csv('India Census 2011.csv')



print('1. Hide the index of dataframe.')
a = df.style.hide_index()
print(df.head())


print('2. Set caption/heading on the dataframe.')
b = df.style.set_caption('India Census Dataset, 2011')
print(df.head())

print('3. Show the records related with the districts - New Delhi, Lucknow, Jaipur.')
c = df[df['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])]
print(c)

print('4. Calculate state-wise.')
print('A: Total number of population.')
d = df.groupby('State_name')['Population'].sum().sort_values(ascending=False)
print(d)
print('B: Total number of population with different religions.')
e = df.columns
print(e)
f = df.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum()
print(f)

print('5. How many male workers were there in Maharashtra state?')
g = df[df['State_name'] == 'MAHARASHTRA']['Male_Workers'].sum()
print(g)

print('6. How to set a column as index of the dataframe')
h = df.set_index('District_name')
print(h)

print('7a. Add a suffix to the column names.')
i = df.add_suffix('_check')
print(i)
j = df.add_prefix('correct_')
print(j)