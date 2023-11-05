# import modules
import csv
import pandas as pd

# read the data from the file
data = pd.read_csv('MS-ASL/aggregated_data/aggregated_data.csv')
pd.set_option('display.max_columns', None)

print('\n############### Data first rows ##################')
# let's see the head of the file
print(data.head())
#column review is empty

print('\n############### Data last rows ##################')
# let's see the tail of the file
print(data.tail())
# Last three rows are empty

print('\n############### Data info ##################')
# let's see the tail of the file
print(data.info())
''' 0   org_text    25506 non-null  object
 1   clean_text  25513 non-null  object
 2   start_time  25513 non-null  float64
 3   signer_id   25513 non-null  float64
 4   signer      25513 non-null  float64
 5   start       25513 non-null  float64
 6   end         25513 non-null  float64
 7   file        25513 non-null  object
 8   label       25513 non-null  float64
 9   height      25513 non-null  float64
 10  fps         25513 non-null  float64
 11  end_time    25513 non-null  float64
 12  url         25513 non-null  object
 13  text        25513 non-null  object
 14  box         25522 non-null  float64
 15  width       25513 non-null  float64
 16  review      7151 non-null   float64'''

