import numpy as np
import pandas as pd

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