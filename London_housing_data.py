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
plt.show()