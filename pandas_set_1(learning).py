# -*- coding: utf-8 -*-
"""Pandas - Set 1(LEARNING).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KUogv5pYQkmSfxuMj38063J2STWQqlU-
"""

import pandas as pd

"""**Creadting a data Frame and reading the csv**"""

df = pd.read_csv('salaries_by_college_major.csv')
pd.options.display.float_format = '{:,.2f}'.format

"""**Printing the top 5 elements of a file**"""

df.head()

"""**Getting number of rows and columns**"""

df.shape

"""**Printing the name of all columns**"""

df.columns

"""**Checking if Nan(Not a number) is present or not or just a blank space**"""

df.isna()

df.tail()

"""**Dropping all the Nan Values**"""

df = df.dropna()

df.tail()

"""**Find College Major with Highest Starting Salaries**"""

df['Starting Median Salary'].max() #Getting the max value from columns Starting Median Salary
df['Starting Median Salary'].idxmax() #Getting the ID of max value from columns Starting Median Salary i.e. 43
print(df.loc[43]) #Printing all the details of row 43
df['Undergraduate Major'][43] #Printing the name of the Degree with Highest Starting Median Salary

"""**College major having the highest mid-career salary**"""

max_value = df['Mid-Career Median Salary'].idxmax()
print(df.loc[max_value])
df['Undergraduate Major'][max_value]

"""**Difference between mid carrer 10th and 90th salary and adding this difference row in our data-frams(df)**"""

diff = df['Mid-Career 90th Percentile Salary']-df['Mid-Career 10th Percentile Salary']
df.insert(5,'Difference',diff)
df.head()

"""**Sorting DF on the basis of diffecence and it creates a copy of df.Original df is unchanged**"""

sorted = df.sort_values('Difference')
sorted[['Undergraduate Major','Difference']].head()

"""**Using GroupBy Function to group the common elements and in the next cell finding the mean of it**"""

df.groupby('Group').count()

df.groupby('Group').mean()

"""**Here I have calculated mean of a column named Starting Median Salary and : in it represents to select all the rows and after column represnts the group name**"""

df.loc[:,['Starting Median Salary','Mid-Career Median Salary']].mean()