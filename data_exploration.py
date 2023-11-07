# import modules
import csv
import pandas as pd

# read the data from the file
data = pd.read_csv('MS-ASL/aggregated_data/aggregated_data.csv')
pd.set_option('display.max_columns', None)


print('\n############### Data  shape ##################')
# let's see the head of the file
print(data.shape)
'''(25522, 17)'''

print('\n############### Data first rows ##################')
# let's see the head of the file
print(data.head())
'''column review is empty'''

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

print('\n############### Check missing info ##################')
# let's check missing info
print(data.isnull().sum())
'''
org_text         16
clean_text        9
start_time        9
signer_id         9
signer            9
start             9
end               9
file              9
label             9
height            9
fps               9
end_time          9
url               9
text              9
box               0
width             9
review        18371
dtype: int64
'''

print('\n############### Check non null value of column review ##################')
# let's check missing info
non_empty_values = data['review'].dropna()
print(non_empty_values)
