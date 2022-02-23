import numpy as np
import pandas as pd
import timeit

# This block of code allows for the entire Dataframe to be viewed upon printing dataframe output
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

# read in csv file as dataframe
df = pd.read_csv('C:\\Users\\cwins\\Downloads\\UNZIP_FOR_NOTEBOOKS_FINAL (1)\\03-Pandas\\tips.csv')
#print(df)

# create a unique function to capture last 4 values of credit card number (from dataframe)

def last_four(num):
    return str(num)[-4:]


# use the Apply method to apply unique function to data
dfViewLastFour = df['CC Number'].apply(last_four)
#print(dfViewLastFour)

# Create a yelp-like function that returns a gauge for price in terms of meal cost (ie $ = cheap; $$ = more expensive; $$$ = most expensive)

def yelp(price):
    if price < 10:
        return '$'
    elif price >=10 and price < 30:
        return '$$'
    else:
        return '$$$'

df['yelp'] = df['total_bill'].apply(yelp)
print(df['yelp'])

#print(df)


# How to use apply_method on multiple columns

# Make a function that gauges how generous the tip was given the ratio tip/ total_bill
# for simplicity, generous is 25% and above

def quality(total_bill,tip):
    if tip/total_bill > .25:
        return "Generous"
    else:
        return "Other"

# Here's how to apply this function to multiple columns

tipQuality = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis = 1)
print(tipQuality)

# Assign function to its own column

df['tip_quality'] = tipQuality
print(df)

# Vectorize
# The purpose of np.vectorize is to transform functions which are not num-py aware

df['Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])

# Demonstration of timeit

# code snippet to be executed only once
# Notice an 'r' was necessary before csv file path in order for this to execute properly

import timeit
setup = '''
import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\\Users\\cwins\\Downloads\\UNZIP_FOR_NOTEBOOKS_FINAL (1)\\03-Pandas\\tips.csv')
def quality(total_bill,tip):
    if tip/total_bill  > 0.25:
        return "Generous"
    else:
        return "Other"
'''

# code snippet whose execution time is to be measured
stmt_one = ''' 
tipQuality = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis = 1)
'''

stmt_two = '''
df['Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''

#print("Lambda speed: " + str(timeit.timeit(setup = setup, stmt = stmt_one, number = 1000)))
#print("\n")
#print("Vectorize speed: " + str(timeit.timeit(setup = setup, stmt = stmt_two, number = 1000)))

# In this instance np.vectorize greatly outperformed the lambda



df = pd.read_csv('C:\\Users\\cwins\\Downloads\\UNZIP_FOR_NOTEBOOKS_FINAL (1)\\03-Pandas\\tips.csv')

# sorting methodologies

# How to sort by columns
# sort by tip ( low to high )

#print(df.sort_values(['tip']))

# tip by descending order

#print(df.sort_values(['tip'], ascending= False))

# sort by multiple columns

# print(df.sort_values(['tip', 'size']))

# How to get max value of bill column

print(df['total_bill'].max())

# How to get index of max value of bill column

maxTotalBillIndex = df['total_bill'].idxmax()

# How to return particular Series via passing in index
print(df.iloc[maxTotalBillIndex])


# values count method

df['sex'].value_counts()

# How to get different values of columns

df['day'].unique()

# How to count number of Different values in columns

df['day'].nunique()

# Replace method

# replace 'females' with 'f' in sex column

df['sex'].replace('Female', 'F')

# Mapping method

mymap = {'Female': 'F', 'Male': 'M'}

df['sex'].map(mymap)


# Duplicate rows

simple_df = pd.DataFrame([1,2,2], ['a','b','c'])
print(simple_df)
print(simple_df.duplicated())

# drop duplicates

simple_df = simple_df.drop_duplicates()
print(simple_df)

# Between method call

filterBetween = df[df['total_bill'].between(10,20,inclusive=True)]

# 10 rows that had the largest tip

df.nlargest(10,'tip')

# 2 rows that had smallest tip

df.nsmallest(2, 'tip')

# sample 5 random rows of dataframe

df.sample(5)

# sample 10% of dataframe

print(df.sample(frac = 0.1))
