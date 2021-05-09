import pandas as pd

df = pd.read_csv('Udemy Courses.csv')

print('1. What are all different subjects for which Udemy is offering courses?')
a = df['subject'].unique()
print(a)

print('2. Which subject has the maximum number of courses?')
b = df['subject'].value_counts()
print(b)

print('3. Show all the courses which are Free of cost.')
c = df[df['price'] == 'Free']
print(c)

print('4. Show all the courses which are Paid.')
d = df[df['is_paid'] == True]
print(d)

print('5. What are Top Selling Courses?')
e = df.sort_values('num_subscribers', ascending=False)
print(e)

print('6. Show all courses of Graphic Design where the price is below 100.')
f = df[df['price'] != 'Free']
f_price = f['price'].astype(int)
f_rsl = f[(f['subject'] == 'Graphic Design') & (f_price < 100)]
print(f_rsl)

print('7. List out all courses that are relate to Python.')
g = df[df['course_title'].str.contains('Python')]
print(g)
g_num = len(g)
print(g_num)

print('8. What are courses that published in year 2015?')
print(df.dtypes)
df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
print(df.dtypes)
df['Year'] = df['published_timestamp'].dt.year
print(df)
h = df[df['Year'] == 2015]
print(h)

print('9. What are the maximum of subscribers for each level of courses.')
i = df.groupby('level')['num_subscribers'].max()
print(i)
j = df.groupby('level').max()
print(j)