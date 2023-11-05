# import modules
import csv
import pandas as pd

# read the data from the file
data = pd.read_csv('MS-ASL/aggregated_data/aggregated_data.csv')

# let's see the head of the file
print(data.head())