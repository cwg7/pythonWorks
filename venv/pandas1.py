import numpy as np
import pandas as pd

# This block of code allows for the entire Dataframe to be viewed upon printing dataframe output
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

## Example

myIndex = ['USA', 'Canada', 'Mexico']
myData = [1776, 1867, 1821]

mySer = pd.Series(data = myData, index = myIndex)
#print(mySer)




# TASK: Use pandas to grab the expenses paid by Bob.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
#  Link to Solution: https://gist.github.com/Pierian-Data/3d7f7cb3528f015d9584d04a7168b97f

expenses = pd.Series({'Andrew':200,'Bob':150,'Claire':450})
print(expenses)

# bob_expense = # Use pandas, don't just manually write in the number here.

bob_expense = expenses['Bob']

#print(bob_expense)

# Set Dataframe as csv file (example)

df = pd.read_csv('C:\\Users\\cwins\\Downloads\\UNZIP_FOR_NOTEBOOKS_FINAL (1)\\03-Pandas\\tips.csv')
#print(df)

# Set 'Payment ID' Column title as Dataframe Index

df = df.set_index('Payment ID')
#print(df)

#refresh original dataframe

df = pd.read_csv('C:\\Users\\cwins\\Downloads\\UNZIP_FOR_NOTEBOOKS_FINAL (1)\\03-Pandas\\tips.csv')
#print(df)

#Perform operations on data. Let's find instances of where 'total_bill' > 40

bool_series = df['total_bill'] > 40
#print(df[bool_series])

#simplified code
#print(df[df['total_bill'] > 40])

# Filter all males

filterAllMales = df[df['sex'] == "Male"]
#print(filterAllMales)

# combining conditions

combinedFilter = df[(df['total_bill'] > 30) & (df['sex'] == "Male")]
#print(combinedFilter)

weekendOnly = df[(df['day'] == 'Sun') | (df['day'] == 'Sat')]
#print(weekendOnly)

# Cleaner method to filter weekend values (isin method)
options = ['Sun','Sat']
#print(df[df['day'].isin(options)])



