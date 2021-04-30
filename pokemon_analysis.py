import pandas as pd

df = pd.read_csv('pokemon_data.csv')

'first 5 line of data'
df.head(5)

'Total numbers of rows and columns of data'
df.shape

'Index of dataframe'
#df.index()

'Name of each column'
# df.columns()

'date-type of each column'
# df.dtypes()

'In a columns, it shows all the unique values. It can be applied on a single column only, not on the whole dataframe'
# df['Type 1'].unique()

'It shows the total number of unique values in each column. Ir can be applied on a single column as well as on whole dataframe'
# df.nunique()

'Shows the total number of non-null values in each column. It can be applied on a single column as well as on whole dataframe'
# df.count()

'In a column, it shows all the unique values with their count. It can be applied on a single column only.'
# df['Type 1'].value_counts()

'Provide basic information about the dataframe.'
# df.info()

print('1. Find all the unique "Type 1" values and specific values in "Type 1" in data.')
ut1 = df['Type 1'].nunique()
specific_type = df['Type 1'].unique()
print(ut1)
print(specific_type)

print('2. Find numbers of Grass type pokemon in "Type 1".')
'Way 1'
number_in_each_type = df['Type 1'].value_counts()
print(number_in_each_type)
grass_data = df[df['Type 1'] == 'Grass']
print(grass_data)
'Way 2'
grass_p_data = df.groupby('Type 1').get_group('Grass')
print(grass_p_data)

print('3. Find number of times when the "HP" was exactly 80.')
hp_is_80 = df[df['HP'] == 80]
print(hp_is_80)

print('4. Find out all the null value in the data.')
number_of_null = df.isnull().sum()
number_of_not_null = df.notnull().sum()
print(number_of_null)
print(number_of_not_null)

print('5. Rename the column "HP" to "Blood".')
df.rename(columns={'HP' : 'Blood'}, inplace=True)       # inplace=True use to change premantly

print('6. What is the mean, standard deviation, variance of "Blood" in this data.')
blood_describe = df['Blood'].describe()
blood_variance = df['Blood'].var()
print(blood_describe)
print(blood_variance)

print('7. Find all instances when "True" is record.')
'value_counts'
legendary = df['Legendary'].value_counts()
'filtering'
a = df[df['Legendary'] == True]
'str contain, not apply in this data. Example: normal True, super True, it use to find all data include but not only include True.'
# df[df['Legendary'].str.contains(True)]      # in this case, not '', but mostly need ''.
print(legendary)
print(a)

print('8. Find all instances when "Attack" >=100 and "Sp. Atk" >= 120')
high_both_atk = df[(df['Attack'] >= 100) & (df['Sp. Atk'] >= 120)]
print(high_both_atk)

print('9. Find all instances when "Attack" >=100 or "Sp. Atk" >= 120')
high_either_atk = df[(df['Attack'] >= 100) | (df['Sp. Atk'] >= 120)]
print(high_either_atk)

print('10. Find all instances when A: "Attack" >=100 and "Sp. Atk" >= 120 or B: "Speed" > 130.')
z = df[(df['Attack'] >= 100) & (df['Sp. Atk'] >= 120) | (df['Speed'] > 130)]
print(z)

print('11. What is the mean value of each column against each "Legendary".')     # also apply for describe(), std()... ...
b = df.groupby('Legendary').mean()
print(b)

print('12. Show all the record where Legendary is True.')
c = df[df['Legendary'] == True]
print(c)
