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

print('\n############### delete column review from dataset##################')
# let's check missing info
print(data.columns)
del data['review']
print(data.columns)
data.to_csv('MS-ASL/aggregated_data/dataset.csv', index=False)

print('\n############### Check missing info ##################')
# let's check missing info
print(data.isnull().sum())

print('\n############### Number of rows with all null values ##################')
count_null_rows = data.isna().all(axis=1).sum()
print(count_null_rows)

print('\n############### Number of rows with 15 null values ##################')
# Count rows with two null values
count_rows_with_15_nulls = (data.isna().sum(axis=1) == 15).sum()
print(count_rows_with_15_nulls)

print('\n############### Number of rows with 1 null values ##################')
# Count rows with two null values
count_rows_with_1_null = (data.isna().sum(axis=1) == 1).sum()
print(count_rows_with_1_null)


print('\n############### Rows with 15 null values ##################')
rows_with_15_nulls = data[data.isna().sum(axis=1) == 15]
print(rows_with_15_nulls)

print('\n############### Delete rows with 15 null values ##################')
data = data[~(data.isna().sum(axis=1) == 15)]
print('\n############### Rows with 15 null values ##################')
count_rows_with_15_nulls = (data.isna().sum(axis=1) == 15).sum()
print(count_rows_with_15_nulls)

print('\n############### Rows with 1 null value ##################')
rows_with_1_null = data[data.isna().sum(axis=1) == 1]
print(rows_with_1_null)


