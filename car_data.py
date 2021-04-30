import pandas as pd

car = pd.read_csv('Cars Data1.csv')

print('1. Find all null value, if any, fill with the mean of that column.')
a = car.isnull().sum()
b= car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)
print(a)
print(b)

print('2. Check what are the different types of Make are there in dataset. And what is the count (occurrence) of each Make in data.')
number_of_make = car['Make'].unique()
number_of_each_make = car['Make'].value_counts()
print(number_of_make)
print(number_of_each_make)

print('3. Show all the record where Origin is Asia or Europe.')
'Way 1'
q = car[(car['Origin'] == 'Asia') | (car['Origin'] == 'Europe')]
'Way 2'
p = car[car['Origin'].isin(['Asia', 'Europe'])]
# print(q)
print(p)

print('4. Remove unwanted records. Remove all records (rows) where Weight is above 4000.')
car[~(car['Weight'] > 4000)]

print('5. Increase all values of "MPG_City" column by 3.')
car['MPG_City'] = car['MPG_City'].apply(lambda x: x+3)