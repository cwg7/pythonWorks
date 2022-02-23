import numpy as np
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)


## Here we have a dataframe with missing data (fields with NaN values)

df = pd.read_csv('C:\\Users\\cwins\\Downloads\\UNZIP_FOR_NOTEBOOKS_FINAL (1)\\03-Pandas\\movie_scores.csv')
print(df)
print("\n")
# check for null values

# print(df.isnull())

# check for inverse (not null)

#print(df.notnull())

# boolean check for actors with 'pre movie score'

#print(df['pre_movie_score'].notnull())

# return rows where pre movie score is not null

#print(df[df['pre_movie_score'].notnull()])

#### 3 options w/ missing data
#### Keep the data  (do nothing)
#### Drop the data
#### Fill the data

# drop data

# drop any rows that have any missing values

print(df.dropna())

# drop rows that have all null values
# threshold = need at least one non null value
print(df.dropna(thresh = 1))

# drop rows with null values in a particular column (in this case 'last_name')

df.dropna(subset=['last_name'])

# fill data

print(df.fillna('NEW VALUE!'))

# fill data where pre_movie_score column values are null

print(df['pre_movie_score'].fillna(0))

# how to save changes

#df['pre_movie_score'] = df['pre_movie_score'].fillna(0)


#

airline_tix = {'first':100,'business':np.nan,'economy-plus':50,'economy':30}

ser = pd.Series(airline_tix)
print(ser)

# interpolate
# because 'business' == Nan, you can apply interpolate here

print(ser.interpolate())