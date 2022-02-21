import numpy as np
import pandas as pd


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
